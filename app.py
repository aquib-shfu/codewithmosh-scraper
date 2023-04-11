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

    def find_links(self) -> dict:
        """Extracts the course title and url

        Returns
        -------
        course_details: dict
            key value pair for {course_title : course_url} of all courses
        """
        course_details = {"title": [], "url": []}
        self.browser.move(config.HOMEPAGE)
        soup = BeautifulSoup(self.browser.get_source(), "lxml")
        elems = soup.find_all("div", {"class": "course-listing"})
        for elem in elems:
            title = elem.find("div", {"class": "course-listing-title"}).text.strip()
            course_details["title"].append(title)
            course_details["url"].append(config.BASE_URL + elem["data-course-url"])
        return course_details

    def capture_slaves(self, course_url: str) -> dict:
        """ "Extracts all video title and urls from a course

        Parameters
        ----------
        course_url: str
            URL of the course

        Returns
        -------
        video_links: dict
            A dict with video_title : video_url key value pairs
        """
        video_links = {"title": [], "url": []}
        self.browser.move(course_url)
        # TODO: extract all cdn urls from a specific course page
        # and put them in video_links with respective order.

        return video_links

    # main
    def cruise(self):
        courses = self.find_links()
        for _, url in courses.items():
            course_videos = self.capture_slaves(url)


if __name__ == "__main__":
    SandPirate().cruise()
