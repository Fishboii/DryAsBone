import scrape
import time
import logging
import traceback
import os
logging.basicConfig(filename='uhoh.log', filemode='w')

while True:
    # noinspection PyBroadException <= pycharm making fun of me catching all errors
    try:
        # Not good practice but i dont know how to catch a connection error so ill limit the file size
        if os.stat('uhoh.log').st_size > 2000000:
            break
        scrape.wheredata(True)
        scrape.weather()
        print("\nPing at {}".format(time.strftime("%H, %M, %S", time.localtime())))
        time.sleep(25)
    except Exception as e:
        # frankenstein'ed from past project
        print("error appeared, error and time logged, data for {} not logged".format(time.strftime("%y, %m, %d, %H, %M, %S", time.gmtime())))
        logging.error(time.strftime("%y, %m, %d, %H, %M", time.gmtime()) + traceback.format_exc())

# TODO: make YAML file
