"""Module containing some random utilities."""
import requests
from bs4 import BeautifulSoup


def add(num1: int, num2: int) -> int:
    """Add one number to another."""

    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    """Subtract a number from another."""

    return num1 - num2


def divide(num1: int, num2: int) -> float:
    """Divide one number by the other."""

    return num1 / num2


def get_anchors(url: str) -> list[str]:
    """Get HTML anchor tag HREFs from remote URL."""

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    anchors = []
    for anchor in soup.findAll("a"):
        anchors.append(anchor.attrs["href"])

    return anchors


def main() -> None:
    """Execute the main process."""

    num1, num2 = 25, 5
    add_result = add(num1, num2)
    subtract_result = subtract(num1, num2)
    divide_result = divide(num1, num2)
    print(add_result, subtract_result, divide_result)

    anchors = get_anchors("https://www.google.com/")
    print(anchors)


if __name__ == "__main__":
    main()
