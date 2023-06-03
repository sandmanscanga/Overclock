"""Module used for running unit tests against the example module."""
from typing import Any
from enum import Enum
import pytest

import requests

from src.example import add, subtract, divide, get_anchors


class ExpectedAddResult(Enum):
    """Expected result for 'add' unit test case."""

    RESULT_1 = 5
    RESULT_2 = 0


class ExpectedSubtractResult(Enum):
    """Expected result for 'subtract' unit test case."""

    RESULT_1 = 2
    RESULT_2 = 3


def test_add() -> None:
    """Test the 'add' function from the example module."""

    assert add(2, 3) == ExpectedAddResult.RESULT_1.value
    assert add(-1, 1) == ExpectedAddResult.RESULT_2.value


def test_subtract() -> None:
    """Test the 'subtract' function from the example module."""

    assert subtract(5, 3) == ExpectedSubtractResult.RESULT_1.value
    assert subtract(10, 7) == ExpectedSubtractResult.RESULT_2.value


def test_divide() -> None:
    """Test the 'divide' function from the example module."""

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(num1: int, num2: int, expected: int) -> None:
    """Test the 'add' function from the example module again."""

    assert add(num1, num2) == expected


def test_get_anchors() -> None:
    """Test the 'get_anchors' function from the example module."""

    class MockResponse:  # pylint: disable=too-few-public-methods
        """Mock the requests module's response text."""

        def __init__(self, text: str) -> None:
            """Create a new instance."""

            self.text = text

    def mock_get(*_: tuple[Any, ...]) -> MockResponse:
        """Mock the requests library 'requests.get' method response."""

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

    requests.get = mock_get  # type: ignore

    url = "https://example.com"
    expected_anchors = [
        "https://example.com",
        "https://example.com/page",
        "https://example.com/another-page"
    ]

    assert get_anchors(url) == expected_anchors


def main() -> None:
    """Execute the main process."""

    test_add()
    test_subtract()
    test_divide()
    test_add_parametrized(2, 3, 5)
    test_get_anchors()


if __name__ == "__main__":
    main()
