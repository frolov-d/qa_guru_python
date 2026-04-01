import json

import allure
from allure import attachment_type


def test_attachment():
    # Текст
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)

    # HTML
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)

    # JSON
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)