import requests
import time
from PIL import Image, ImageFile
import os
import colourmap
from bs4 import BeautifulSoup
import classify

# to compensate for "truncated" file
ImageFile.LOAD_TRUNCATED_IMAGES = True


def weather():
    """Add weather data to csv file"""
    # get page and datasets
    html_page = requests.get('http://www.weather.gov.sg/weather-forecast-2hrnowcast-2/')
    soup = BeautifulSoup(html_page.content, 'html.parser')
    fileappend = open("data.csv", "a")
    for i in range(1, 49):
        # index 0 and 25 are titles, so skip them
        if i == 25:
            continue
        else:
            cls = soup.findAll('tr')[i]
            # something to do with encoding where \xa0 appears
            weather = cls.text.strip(" ").replace("\xa0", "")
            fileappend.write(", {}".format(classify.weather(weather.lower())))
    fileappend.close()


def download_file(url):
    # From https://stackoverflow.com/users/12641442/jenia
    # Much Thanks
    local_filename = "serisdata{}".format(time.strftime("%y, %m, %d, %H, %M, %S", time.localtime()).replace(", ", "") +
                                          ".png")
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


def extremevalues(targetlist, maximum=True):
    # max value True by default, min value is False
    # takes list of tuples, compares them to colourmap
    indexedlist = []
    illegal = [(0, 239, 1), (0, 21, 90), (0, 0, 0), (255, 255, 255)]
    for i in targetlist:
        if i not in illegal:
            indexedlist.append(colourmap.colourmap.index(i))

    if maximum:
        return colourmap.colourmap[max(indexedlist)]
    elif not maximum:
        return colourmap.colourmap[min(indexedlist)]


def wheredata(deletefile=False):
    # Same 30 points separated into districts
    points = [(727, 506), (634, 564), (585, 518), (584, 562), (460, 491), (659, 533), (685, 498), (687, 440),
              (634, 461),
              (560, 440), (597, 390), (683, 384), (737, 378), (795, 413), (817, 467), (925, 403), (1065, 329),
              (910, 306),
              (789, 277), (638, 287), (469, 351), (215, 376), (403, 277), (252, 217), (456, 116), (584, 232), (617, 89),
              (712, 196), (161, 578), (607, 626)]
    clr = []

    # updated every 10 seconds
    html = requests.get('https://www.solar-repository.sg/_irr_pic.cfm')
    # short html file so bs4 not needed, able to find with split easily
    imglink = html.text.split("\"")[1]
    filename = download_file(imglink)
    # CHANGE filename for testing
    im = Image.open(filename)

    for i in points:
        # get pixel colour from each district
        pixel = im.getpixel((i[0], i[1]))
        clr.append((pixel[0], pixel[1], pixel[2]))

    for colour in clr:
        if colour == (0, 239, 1):
            print("green detected")
            targetpoint = points[clr.index((0, 239, 1))]
            colourarray = []
            # generate 400 pixels surrounding the image
            for i in range(20):
                for j in range(20):
                    colourarray.append(im.getpixel((targetpoint[0] - 10 + i, targetpoint[1] - 10 + j)))

            if (0, 0, 0) in colourarray:
                # in the case of black dot close
                clr[clr.index(colour)] = extremevalues(colourarray, False)

            elif (255, 255, 255) in colourarray:
                # in the case of white dot close
                clr[clr.index(colour)] = extremevalues(colourarray, True)

        elif colour == (0, 0, 0):
            print("black")
            # in the case of on black dot
            clr[clr.index((0, 0, 0))] = extremevalues(clr, False)

        elif colour == (255, 255, 255):
            print("white")
            # in the case of on white dot
            clr[clr.index((255, 255, 255))] = extremevalues(clr, True)

    pixels = []
    # add the relative intensity of each pixel on a scale of 100
    for i in clr:
        index = colourmap.colourmap.index(i)
        pixels.append(index * 100 / 256)

    # add data to csv file
    fileappend = open("data.csv", "a")
    # add datetime
    fileappend.write("\n{}".format(time.time()))
    for i in pixels:
        fileappend.write(", {}".format(i))
    fileappend.close()


    # delete files/not and wait 5 seconds to ensure all editing is done and file is closed properly
    if deletefile:
        time.sleep(5)
        os.remove(filename)

    elif not deletefile:
        time.sleep(5)
