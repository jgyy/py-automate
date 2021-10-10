"""
Web Scraping
"""
from os import makedirs
from os.path import dirname, basename, join
from sys import argv
from random import choice
import webbrowser as wb
from pyperclip import paste
from requests import get
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

PATH = dirname(__file__) + "\\"


def wrapper1():
    """
    wrapper function part 1
    """
    wb.open("http://inventwithpython.com/")
    if len(argv) > 1:
        address = " ".join(argv[1:])
    else:
        address = paste()
        wb.open("https://www.google.com/maps/place/" + address)
    res = get("https://automatetheboringstuff.com/files/rj.txt")

    print(type(res))
    print(len(res.text))
    print(res.text[:250])
    try:
        res = get("http://inventwithpython.com/#bigbookpython")
        res.raise_for_status()
    except KeyError as exc:
        print(f"There was a problem: {exc}")

    res = get("https://automatetheboringstuff.com/files/rj.txt")
    print(res.raise_for_status())
    with open(f"{PATH}romeo_and_juliet.txt", "wb") as play_file:
        for chunk in res.iter_content(100000):
            play_file.write(chunk)
    res = get("http://nostarch.com")
    print(res.raise_for_status())
    no_starch_soup = BeautifulSoup(res.text)
    print(type(no_starch_soup))
    with open(f"{PATH}example.html", encoding="utf-8") as example_file:
        example_soup = BeautifulSoup(example_file)

    print(type(example_soup))
    elems = example_soup.select("#author")
    print(type(elems))
    print(len(elems))
    print(type(elems[0]))
    print(elems[0].getText())
    print(str(elems[0]))
    print(elems[0].attrs)
    p_elems = example_soup.select("p")
    print(str(p_elems[0]))
    print(p_elems[0].getText())
    print(str(p_elems[1]))
    print(p_elems[1].getText())
    print(str(p_elems[2]))
    print(p_elems[2].getText())

    with open(f"{PATH}example.html", encoding="utf-8") as soup:
        span_elem = BeautifulSoup(soup).select("span")[0]
    print(str(span_elem))
    print(span_elem.get("id"))
    print(span_elem.get("some_nonexistent_addr") is None)
    print(span_elem.attrs)
    print("Googling...")


def wrapper2():
    """
    wrapper function part 2
    """
    res = get("http://google.com/search?q=" + " ".join(argv[1:]))
    print(res.raise_for_status())
    soup = BeautifulSoup(res.text)
    link_elems = soup.select(".r a")
    num_open = min(5, len(link_elems))
    for i in range(num_open):
        wb.open("http://google.com" + link_elems[i].get("href"))
    url = "http://xkcd.com"
    makedirs(f"{PATH}xkcd", exist_ok=True)

    while choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) != 0:
        print(f"Downloading page {url}...")
        res = get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text)
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("Could not find comic image.")
        else:
            try:
                comic_url = "http:" + comic_elem[0].get("src")
                print(f"Downloading image {comic_url}...")
                res = get(comic_url)
                res.raise_for_status()
            except MissingSchema:
                prev_link = soup.select('a[rel="prev"]')[0]
                url = "http://xkcd.com" + prev_link.get("href")
                continue
            with open(join(f"{PATH}xkcd", basename(comic_url)), "wb") as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
        prev_link = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com" + prev_link.get("href")
    print("Done.")


def wrapper3():
    """
    wrapper function part 3
    """
    browser = Firefox()
    type(browser)
    browser.get("http://inventwithpython.com")
    try:
        elem = browser.find_element_by_class_name("navbar")
        print(f"Found <{elem.tag_name}> element with that class name!")
    except TypeError():
        print("Was not able to find an element with that name.")

    browser.get("http://inventwithpython.com")
    link_elem = browser.find_element_by_link_text(
        "Automate the Boring Stuff with Python"
    )
    type(link_elem)
    link_elem.click()

    browser.get("https://login.yahoo.com/")
    email_elem = browser.find_element_by_id("login-username")
    email_elem.send_keys("not_my_real_email")
    email_elem.submit()

    browser.get("http://nostarch.com")
    html_elem = browser.find_element_by_tag_name("html")
    html_elem.send_keys(Keys.END)
    html_elem.send_keys(Keys.HOME)


if __name__ == "__main__":
    wrapper1()
    wrapper2()
    wrapper3()
