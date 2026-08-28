"""Print and save a workflow diagram without requiring LangGraph."""

from __future__ import annotations

import io
import re
import uuid
from pathlib import Path
from typing import Any, Iterable

from PIL import Image, ImageDraw, ImageFont


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _node_names(app: Any) -> tuple[str, ...]:
    names = getattr(app, "node_names", None)
    if not names:
        raise TypeError(
            "draw_mermaid_png requires an object with a non-empty node_names sequence "
            "or a LangGraph-compatible get_graph() method."
        )
    return tuple(str(name) for name in names)


def _ascii_graph(names: Iterable[str]) -> str:
    return "\n".join(
        line
        for index, name in enumerate(names)
        for line in (("    |" if index else ""), f"[{name}]")
        if line
    )


def _mermaid_graph(names: tuple[str, ...]) -> str:
    lines = ["flowchart TD"]
    identifiers: list[str] = []
    for index, name in enumerate(names):
        identifier = re.sub(r"[^A-Za-z0-9_]", "_", name).strip("_")
        identifier = f"node_{index}_{identifier or 'step'}"
        identifiers.append(identifier)
        escaped_name = name.replace('"', "&quot;")
        shape = f'(["{escaped_name}"])' if name in {"__start__", "__end__"} else f'["{escaped_name}"]'
        lines.append(f"    {identifier}{shape}")
    lines.extend(
        f"    {source} --> {target}"
        for source, target in zip(identifiers, identifiers[1:])
    )
    return "\n".join(lines)


def _render_linear_png(names: tuple[str, ...]) -> bytes:
    """Render the linear graph locally as PNG using Pillow."""
    width = 720
    box_width = 430
    box_height = 54
    vertical_gap = 42
    margin = 36
    height = margin * 2 + len(names) * box_height + (len(names) - 1) * vertical_gap
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    left = (width - box_width) // 2
    right = left + box_width

    for index, name in enumerate(names):
        top = margin + index * (box_height + vertical_gap)
        bottom = top + box_height
        terminal = name in {"__start__", "__end__"}
        fill = "#e8f1ff" if terminal else "#f7f7f7"
        outline = "#3676c5" if terminal else "#555555"
        draw.rounded_rectangle(
            (left, top, right, bottom),
            radius=box_height // 2 if terminal else 8,
            fill=fill,
            outline=outline,
            width=2,
        )
        text_box = draw.textbbox((0, 0), name, font=font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]
        draw.text(
            ((width - text_width) / 2, top + (box_height - text_height) / 2),
            name,
            fill="#111111",
            font=font,
        )
        if index < len(names) - 1:
            line_top = bottom
            line_bottom = top + box_height + vertical_gap - 8
            center = width // 2
            draw.line((center, line_top, center, line_bottom), fill="#555555", width=2)
            draw.polygon(
                ((center - 5, line_bottom - 7), (center + 5, line_bottom - 7), (center, line_bottom)),
                fill="#555555",
            )

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def draw_mermaid_png(
    app: Any,
    save_file_name: str = "main_graph",
    output_dir: str | Path | None = None,
) -> Path:
    """Print ASCII/Mermaid definitions and save a PNG workflow diagram.

    Lightweight workflows are rendered locally. A compiled LangGraph remains
    supported through its ``get_graph`` drawing interface.
    """
    safe_file_name = re.sub(r"[^A-Za-z0-9._-]+", "_", save_file_name).strip("._-")
    safe_file_name = safe_file_name or "main_graph"
    destination = Path(output_dir) if output_dir else Path(PROJECT_ROOT) / "output"
    destination.mkdir(parents=True, exist_ok=True)

    graph_getter = getattr(app, "get_graph", None)
    if callable(graph_getter):
        graph = graph_getter()
        ascii_graph = graph.print_ascii()
        mermaid_graph = graph.draw_mermaid()
        png_bytes = graph.draw_mermaid_png()
    else:
        names = _node_names(app)
        ascii_graph = _ascii_graph(names)
        mermaid_graph = _mermaid_graph(names)
        png_bytes = _render_linear_png(names)

    print("ODRL correction agent graph:")
    if ascii_graph:
        print(ascii_graph)
    print("=" * 50)
    print(mermaid_graph)

    output_path = destination / f"{safe_file_name}_{str(uuid.uuid4())[:8]}.png"
    output_path.write_bytes(png_bytes)
    print(f"\nGraph generated: {output_path}")
    return output_path
