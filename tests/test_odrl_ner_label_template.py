import unittest
from types import SimpleNamespace

from jinja2 import Environment, FileSystemLoader, select_autoescape


class OdrlNerLabelTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        environment = Environment(
            loader=FileSystemLoader("templates"),
            autoescape=select_autoescape(("html",)),
        )
        cls.template = environment.get_template("odrl-ner-label.html")

    def test_assignee_and_specific_rule_types_receive_colours(self):
        result = SimpleNamespace(
            text=["recipient", "may", "must", "not"],
            labels=[
                "S-ASSIGNEE",
                "B-RULE_TYPE-PERMISSION",
                "B-RULE_TYPE-OBLIGATION",
                "E-RULE_TYPE-PROHIBITION",
            ],
        )

        html = self.template.render(question="test", result=result)

        self.assertIn('class="lab e-ASSIGNEE">S-ASSIGNEE</div>', html)
        self.assertEqual(html.count('class="lab e-RULE_TYPE">'), 3)
        self.assertNotIn('class="lab e-O">S-ASSIGNEE</div>', html)
        self.assertNotIn('class="lab e-O">B-RULE_TYPE-PERMISSION</div>', html)


if __name__ == "__main__":
    unittest.main()
