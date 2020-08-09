import argparse
import logging
import os
import time
import uuid
from typing import Dict, List
from xml.etree import ElementTree as ET

import pandas as pd
import requests
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException)

DATA_MAIL_DOWNLOAD_URL = 'http://mail-archives.apache.org/mod_mbox/camel-dev/201704.mbox/browser'
DATA_USERS_DOWNLOAD_URL = 'http://mail-archives.apache.org/mod_mbox/camel-users/201704.mbox/browser'
DATA_COMMITS_DOWNLOAD_URL = 'http://mail-archives.apache.org/mod_mbox/camel-commits/201704.mbox/browser'
DATA_ISSUES_DOWNLOAD_URL = 'http://mail-archives.apache.org/mod_mbox/camel-issues/201704.mbox/browser'

LOGGING_FORMAT = "[%(asctime)-15s] %(message)s"


def __download_data(data_download_url: str, dtype: str) -> List[Dict[str, str]]:
    """
    __download_data is the helper function used to download_data from data_download_url

    :param data_download_url: str, is the url to Apache mail database
    :return: List[Dict[str, str]], is the data structure with raw mails data
    """
    driver = webdriver.Chrome()
    driver.get(data_download_url)

    raw_data: List[Dict[str, str]] = []

    logging.info(f"Running {data_download_url} at Chrome driver.")
    logging.info("Waiting for page setting up.")
    time.sleep(5)

    page_count: int = len(driver.find_element_by_class_name("pages").find_elements_by_tag_name("a"))

    record_id = 0

    for page_num in range(page_count):
        logging.info(f"Scrapping data from page {page_num} of {page_count} pages.")

        num_of_records: int = len(driver.find_element_by_id("msglist").find_elements_by_tag_name("tr")) - 1
        logging.info(f"There is {num_of_records} at page number {page_num + 1}.")
        try:
            next_btn = driver.find_element_by_class_name("pages").find_elements_by_tag_name("a")[-1]
        except StaleElementReferenceException:
            continue

        for i in range(num_of_records):
            logging.info(f"Getting record: {record_id} from page {page_num + 1}.")
            try:
                row_msg = driver.find_element_by_id(f"msg-{i}")
                author = row_msg.find_element_by_class_name("author")
                subject = row_msg.find_element_by_class_name("subject")
                date = row_msg.find_element_by_class_name("date")
                try:
                    content_url = subject.find_element_by_tag_name("a")
                except NoSuchElementException:
                    logging.warning("Error during getting link to mail content.")
                finally:
                    raw_data.append({
                        "id": record_id,
                        "author": author.text,
                        "subject": subject.text,
                        "date": date.text,
                        "content_url": content_url.get_attribute("href") or None,
                        "dtype": dtype
                    })
            except Exception:
                logging.warning(f"Error during getting {record_id} from page {page_num + 1}.")
            record_id += 1

        try:
            next_btn.click()
        except StaleElementReferenceException:
            return raw_data
        time.sleep(3)
    return raw_data


def __get_xml_data(content_url: str, element: str) -> str:
    """
    __get_xml_data is the helper function used to get specified element from xml url

    :param content_url: str, is the url to the XML content
    :param element: str, is the element identifier in XML content url
    :return: str, is the content of element in content_url
    """
    try:
        raw_data = requests.get(content_url).text
        root = ET.fromstring(raw_data)
        logging.info(f"Successfully read {element} from {content_url}.")
        return root.find(element).text
    except (requests.exceptions.ConnectionError, AttributeError):
        logging.warning(f"Unable to read {element} from {content_url}.")
        return ""


def __save_data_to_path(raw_data: List[Dict[str, str]], path: str) -> bool:
    """
    __save_data_to_path is the helper function used to save raw_data from __download_data into path

    :param raw_data: List[Dict[str, str]], is data structure from __download_data
    :param path: str, is the path to save data
    :return: bool, returns True if the save was successful, otherwise False
    """
    data_to_save: List[Dict[str, str]] = []
    for record in raw_data:
        record["content"] = __get_xml_data(record.get("content_url"), "contents")
        data_to_save.append(record)
    try:
        pd.DataFrame(data_to_save).to_csv(path)
        logging.info(f"Successfully saved {len(data_to_save)} records to {path}.")
    except FileNotFoundError:
        logging.warning(f"Unable to save data to {path}.")
        return False
    return True


def load_data(url: str, path: str, dtype: str) -> None:
    """
    load_data is the main function used to download data, basic preprocess and save it in specified path

    :param path: str, is the path to save data
    :return: None
    """
    raw_data = __download_data(data_download_url=url, dtype=dtype)
    if __save_data_to_path(raw_data, path):
        logging.warning(f"Successfully saved data to {path}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
                            Script used to download data and save in data/ directory.\n
                            You can specify path to save data.
                            """)

    parser.add_argument("-v", "--verbose", help="Setting verbose debug information.", action="store_true")
    parser.add_argument("-p", "--path", help="Path used to save data.")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format=LOGGING_FORMAT
        )

    CURRENT_DIR = os.path.abspath(os.curdir)
    SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    ROOT_PATH = os.path.abspath(os.path.join(SRC_PATH, os.pardir))

    OUTPUT_DIR = os.path.join(ROOT_PATH, 'data')

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        logging.info(f"{OUTPUT_DIR} was created successfully.")

    urls = [DATA_USERS_DOWNLOAD_URL, DATA_COMMITS_DOWNLOAD_URL, DATA_ISSUES_DOWNLOAD_URL, DATA_MAIL_DOWNLOAD_URL]

    for url, name in zip(urls, ["users", "commits", "issues", "mails"]):
        filename = f"/{name}_data{uuid.uuid4()}.csv"
        load_data(url, path=args.path + filename if args.path else OUTPUT_DIR + filename, dtype=name)
