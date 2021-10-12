"""
Resizes all images in current working directory to fit
in a 300x300 square, and adds catlogo.png to the lower-right corner.
"""
from os import makedirs, listdir
from os.path import join, dirname
from PIL import Image


def wrapper():
    """
    Loop over all files in the working directory.
    skip non-image files and the logo file itself
    Check if image needs to be resized.
    Calculate the new width and height to resize to.
    Resize the image. > Add logo. > Save changes.
    """
    path = dirname(__file__) + "\\"
    square_fit_size = 300
    logo_filename = "burmese-cat-love.jpg"
    logo_im = Image.open(path + logo_filename)
    logo_width, logo_height = logo_im.size
    makedirs(f"{path}withLogo", exist_ok=True)
    for filename in listdir(path):
        print(filename.endswith(".jpg"))
        if not (filename.endswith(".png") or filename.endswith(".jpg")):
            continue
        img = Image.open(path + filename)
        width, height = img.size
        if width > square_fit_size and height > square_fit_size:
            if width > height:
                height = int((square_fit_size / width) * height)
                width = square_fit_size
            else:
                width = int((square_fit_size / height) * width)
                height = square_fit_size
            print(f"Resizing {filename}...")
            img = img.resize((width, height))
        print(f"Adding logo to {filename}...")
        img.paste(logo_im, (width - logo_width, height - logo_height), logo_im)
        img.save(join(f"{path}withLogo", filename))


if __name__ == "__main__":
    wrapper()
