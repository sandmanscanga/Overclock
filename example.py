def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b


from bs4 import BeautifulSoup

import requests
def get_anchors(url):


    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    stuff = []

    anchors = []
    for anchor in soup.findAll("a"):
        anchors.append(anchor.attrs["href"])


    string = "hi"
    return anchors
if __name__ == "__main__":
    anchors = get_anchors("https://www.google.com/")
    print(anchors)

# This file is purposely cringe, I want to test the workflows.
