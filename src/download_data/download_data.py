import os
import sys
import time
import logging
import argparse 

from xml.etree import ElementTree as tree
from typing import List, Dict
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from consts import DATA_DOWNLOAD_BASE_URL, LOGGING_FORMAT


parser = argparse.ArgumentParser(description="Script used to download data.")

parser.add_argument("-v", "--verbose", help="Setting verbose debug informations.", action="store_true")
args = parser.parse_args()


logging.basicConfig(
    level=logging.DEBUG if args.verbose else logging.WARNING, 
    format=LOGGING_FORMAT
    )


def download_data():
    driver = webdriver.Chrome()
    driver.get(DATA_DOWNLOAD_BASE_URL)

    rows: List[Dict[str,str]] = []

    logging.info(f"Running {DATA_DOWNLOAD_BASE_URL} at Chrome driver.")
    logging.info(f"Waiting for page setting up.")
    time.sleep(3)

    page_count = len(driver.find_element_by_class_name("pages").find_elements_by_tag_name("a"))
    
    for i in range(page_count-1):
        num_of_records = len(driver.find_element_by_id("msglist").find_elements_by_tag_name("tr")) - 1
        for i in range(num_of_records):
            try:
                row_msg = driver.find_element_by_id(f"msg-{i}")
                author = row_msg.find_element_by_class_name("author")
                subject = row_msg.find_element_by_class_name("subject")
                date = row_msg.find_element_by_class_name("date")
                link = None
                try:
                    link = subject.find_element_by_tag_name("a")
                except NoSuchElementException:
                    continue
                finally:
                    rows.append({
                        "id": i,
                        "author": author,
                        "subject": subject,
                        "date": date,
                        "link": link or None
                    })
            except Exception:
                continue

        next_btn = driver.find_element_by_class_name("pages").find_elements_by_tag_name("a")[-1]
        next_btn.click()
        time.sleep(1)
    print(len(rows))


download_data()
