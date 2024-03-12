import csv
import pathlib
import requests
import os


# Change this before running the script
CLASS_YEAR = 2024
PATH_TO_CSV = f"./data/{CLASS_YEAR}.csv"

def download_image_attempt(image_url, class_name, slug):
    """
    This function attempts to download the images specified in the image url

    Most people use google drive, for which there's a tiny hack below
    to make the images accessible via requests

    Others don't use any sensible format whatsoever, and this script will tell you
    who it failed on. You'll need to manually download their images and copy it over to the
    target directory :)
    """
    if "drive.google" in image_url:
        image_url = image_url.replace("file/d/", "uc?id=")
        image_url = image_url[:image_url.rfind("/")]

    directory = f"../static/img/{class_name}"
    if not os.path.exists(directory):
        os.makedirs(directory)


    if pathlib.Path(f"{directory}/{slug}.jpg").exists():
        print(f"Skipping {slug}")
        return

    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(f"{directory}/{slug}.jpg", "wb") as f:
                f.write(response.content)
        else:
            print(f"Failed to download image for slug: {slug}")
    except Exception:
        print(f"Failed to download image for slug: {slug}")



"""
Export your year's excel sheet as a .csv file and run this script on it
"""
with open(PATH_TO_CSV) as file_in:
    next(file_in, None)
    csv_reader = csv.reader(file_in, delimiter=',')
    for row in csv_reader:
        code = "-".join(row[0].split(" ")).lower()
        with open(f"../content/{CLASS_YEAR}/{code}.md", "w") as file_out:
            file_out.write("---\n")
            file_out.write(f"name: \"{row[0]}\"\n")
            file_out.write(f"class: \"2024\"\n")
            file_out.write(f"slug: \"{code}\"\n")
            image_url = row[-2]
            download_image_attempt(image_url, CLASS_YEAR, code)
            file_out.write(f"image: \"{image_url}\"\n")
            file_out.write(f"email: \"mailto:{row[4]}\"\n")
            if row[7] != "":
                file_out.write(f"github: \"{row[7]}\"\n")
            if row[5]  !="":
                file_out.write(f"twitter: \"{row[5]}\"\n")
            if row[9]  != "":
                file_out.write(f"linkedin: \"{row[-3]}\"\n")
            if row[6]  != "":
                file_out.write(f"facebook: \"{row[6]}\"\n")
            file_out.write("---\n")
            file_out.write(row[2])
