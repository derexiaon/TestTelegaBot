import requests
from bs4 import BeautifulSoup


def get_weather():
    page = requests.get("https://world-weather.ru/pogoda/russia/kazan/")
    soup = BeautifulSoup(page.text, "html.parser")
    weather = soup.findAll(class_="weather-now-info")

    for data in weather:
        return data.find(id="weather-now-number").text
