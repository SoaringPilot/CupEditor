# Scrape the website data on the airports listed in the CUP file. Create text files with the information
# 2/2/2024

import time
import os

import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL1 = "https://www.airnav.com/airport/"


def read_cup_file(filename):
    file = open(filename)
    entries = file.readlines()
    return entries


def get_text_from_airport_website(airport_id):
    try:
        page = urlopen(URL1 + airport_id, timeout=2)
        html = page.read().decode("cp1252")
        soup = BeautifulSoup(html, "html.parser")
        text_string = ""
        # Filter out all the non-ascii characters
        for i in soup.getText():
            if i.isascii():
                text_string += i
    except:
        input("Error Getting Website Data for: " + airport_id)
        time.sleep(2)
        page = urlopen(URL1 + airport_id, timeout=2)
        html = page.read().decode("cp1252")
        soup = BeautifulSoup(html, "html.parser")
        text_string = ""
        # Filter out all the non-ascii characters
        for i in soup.getText():
            if i.isascii():
                text_string += i
        return text_string

    return text_string


def create_airport_data_file(input_text: str, airport_name: str):
    file = open("./Airports/" + airport_name + ".txt", 'w')
    file.write(input_text)
    file.close()


if __name__ == '__main__':
    # Get data from cup file as a list
    cup_data = read_cup_file("Old_Data/BALLr2.cup")

    for i in range(len(cup_data)):
        active_airport_id = cup_data[i].split(",")[1]
        # active_cup_runway = cup_data[i].split(",")[7]

        # Check if airport data file exists
        if not os.path.isfile("./Airports/" + active_airport_id + ".txt"):
            print("Working on Airport: ", active_airport_id, " ", round((i / len(cup_data)) * 100, 1), "%")
            # Get data from website about airport information
            webpage_text = get_text_from_airport_website(active_airport_id)
            create_airport_data_file(webpage_text, active_airport_id)
            time.sleep(10)
