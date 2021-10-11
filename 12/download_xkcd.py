"""
Downloads every single XKCD comic.
"""
from os import makedirs
from os.path import join, basename, dirname
from requests import get
from bs4 import BeautifulSoup


def wrapper():
    """
    starting url > store comics in ./xkcd
    Download the page. > Find the URL of the comic image.
    Download the image. > Save the image to ./xkcd
    Get the Prev button's url.
    """
    path = dirname(__file__) + "\\"
    url = "http://xkcd.com"
    makedirs(f"{path}xkcd", exist_ok=True)
    while not url.endswith("#"):
        print(f"Downloading page {url}...")
        res = get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text)
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("Could not find comic image.")
        else:
            comic_url = comic_elem[0].get("src")
            print(f"Downloading image {comic_url}...")
            res = get("http:"+comic_url)
            res.raise_for_status()
            with open(join(f"{path}xkcd", basename(comic_url)), "wb") as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)
        prev_link = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com" + prev_link.get("href")
    print("Done.")


if __name__ == "__main__":
    wrapper()
