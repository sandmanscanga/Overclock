import requests
from bs4 import BeautifulSoup
from example import add, subtract, divide, get_anchors
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 7) == 3

def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


def test_get_anchors():
    class MockResponse:
        def __init__(self, text):
            self.text = text

    def mock_get(url):
        html = """
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Sample HTML</title>
          </head>
          <body>
            <a href="https://example.com">Link 1</a>
            <a href="https://example.com/page">Link 2</a>
            <a href="https://example.com/another-page">Link 3</a>
          </body>
        </html>
        """
        return MockResponse(html)

    requests.get = mock_get

    url = "https://example.com"
    expected_anchors = [
        "https://example.com",
        "https://example.com/page",
        "https://example.com/another-page"
    ]

    assert get_anchors(url) == expected_anchors
