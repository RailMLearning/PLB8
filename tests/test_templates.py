import unittest
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader("myapp"), autoescape=select_autoescape())

class TestTemplates(unittest.TestCase):
    def test_index_template(self):
        template = env.get_template("index.html")
        html = template.render(myapp="TestApp", author_name="Rail", group="P3121", navigation=[])
        self.assertIn("TestApp", html)
        self.assertIn("Rail", html)
        self.assertIn("P3121", html)

    def test_users_template(self):
        template = env.get_template("users.html")
        html = template.render(users=[{"name": "Jane Doe", "id": "1"}])
        self.assertIn("Jane Doe", html)

    def test_user_template(self):
        template = env.get_template("user.html")
        html = template.render(user={"name": "Jane Doe", "id": "1"}, currencies=[])
        self.assertIn("Jane Doe", html)
        self.assertIn("Нет подписок", html)  # проверка условия
