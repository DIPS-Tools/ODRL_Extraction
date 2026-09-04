import unittest

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
        html = self.template.render()

        self.assertIn("if (base.startsWith('RULE_TYPE')) return 'RULE_TYPE';", html)
        self.assertIn("'ASSET', 'ACTION', 'ASSIGNEE', 'CONSTRAINT'", html)
        self.assertIn("tag.className = `lab e-${labelClass(labels[index])}`;", html)

    def test_result_page_downloads_raw_and_standard_odrl_json(self):
        html = self.template.render()

        self.assertIn("Download ODRL JSON", html)
        self.assertIn("fetch('/odrl_extraction_stds'", html)
        self.assertIn("link.download = 'ordl-generation.json'", html)

    def test_label_button_uses_generation_api_not_form_post(self):
        html = self.template.render()

        self.assertIn("fetch('/odrl_generation'", html)
        self.assertIn('form.addEventListener(\'submit\'', html)
        self.assertNotIn('action="/odrl-ner-label"', html)


if __name__ == "__main__":
    unittest.main()
