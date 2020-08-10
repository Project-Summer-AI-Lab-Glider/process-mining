import argparse
import logging
import os
import time
from typing import List

import pandas as pd
import numpy as np

LOGGING_FORMAT = "[%(asctime)-15s] %(message)s"


def load_data(urls: List[str]) -> List[pd.DataFrame]:
    """
    load_data is the function used to load data from data directory

    :param: urls List[str], it is list of path to files
    :return: List[pd.DataFrame], is the data structure with mail data
    """
    data_list = []

    for name in urls:
        filename = f'{DATA_DIR}/{name}.csv'
        data_list.append(pd.read_csv(filename))
        logging.info(f"Successfully read element from {name}.")

    return data_list


def concat_data(data: List[pd.DataFrame]) -> pd.DataFrame:
    """
    concat_data is the function used to concat a list of dataframes to one dataframe

    :param data: List[pd.DataFrame], it is a list of dataframes
    :return: pd.DataFrame
    """
    df = pd.concat(data)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    logging.info(f"Successfully concated data")

    return df


def save_data(data: pd.DataFrame, path: str) -> None:
    """
    save_labels is the function to save data labels to data directory

    :param data: pd.DataFrame, is the concated data
    :param path: str, is the path to save data
    :return: None
    """
    try:
        pd.DataFrame(data).to_csv(path)
        logging.info(f"Successfully saved records to {path}")
    except:
        logging.info(f'Save error')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="""
                            Script used to download data and save in data/ directory.\n
                            You can specify path to save data.
                            """)

    parser.add_argument("-v", "--verbose", help="Setting verbose debug information.", action="store_true")
    parser.add_argument("-p", "--path", help="Path used to save data.")
    args = parser.parse_args()

    CURRENT_DIR = os.path.abspath(os.curdir)
    SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    ROOT_PATH = os.path.abspath(os.path.join(SRC_PATH, os.pardir))

    DATA_DIR = os.path.join(ROOT_PATH, 'data')

    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
        logging.info(f"{DATA_DIR} was created successfully.")

    DATA_URLS = [
        'commits_databeef6be9-ea89-4955-ab43-c644eb39b419',
        'issues_data5ccef963-6b66-4871-8959-66abf8b8c498',
        'mails_data833c3053-e431-40c6-bb6a-24c4d19e9b67',
        'users_data94b2e7c2-f2f3-40ba-a8cb-fc1f287feafa',
    ]

    filename = '/merged_data.csv'
    path = args.path + filename if args.path else DATA_DIR + filename

    DATA_LIST = load_data(DATA_URLS)
    DATA = concat_data(DATA_LIST)

    save_data(DATA, path)
