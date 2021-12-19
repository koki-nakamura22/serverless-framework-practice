import json
import requests
from bs4 import BeautifulSoup


def func2(event, context):
    url = "https://www.python.org/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    elm = soup.find("div", class_="introduction").find("p")

    body = {
        "url": url,
        "introductionText": elm.text
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
