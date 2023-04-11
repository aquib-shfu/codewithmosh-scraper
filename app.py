# Author: Shaikh Aquib
# Year: 2023

from bs4 import BeautifulSoup
from bot import BotMaker
import config
import json


class SandPirate:
    def __init__(self):
        self.paths = json.load(open("paths.json", "r"))
        self.browser = BotMaker(browser="Chrome", remote=True)

    def capture_links(self) -> dict:
        course_details = {"title": [], "url": []}
        self.browser.move(config.HOMEPAGE)
        soup = BeautifulSoup(self.browser.get_source(), "lxml")
        elems = soup.find_all("div", {"class": "course-listing"})
        for elem in elems:
            title = elem.find("div", {"class": "course-listing-title"}).text.strip()
            course_details["title"].append(title)
            course_details["url"].append(config.BASE_URL + elem["data-course-url"])
        return course_details

    def cruise(self):
        print(self.capture_links())


if __name__ == "__main__":
    SandPirate().cruise()
