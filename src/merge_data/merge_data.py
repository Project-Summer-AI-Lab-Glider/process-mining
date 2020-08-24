import argparse
import logging
import os

import datetime
import time

from typing import List

import pandas as pd

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


def update_dates(df: pd.DataFrame) -> None:
    df['date'] = df['date'].astype(str).str[:-4]
    df['date'] = pd.to_datetime(df['date'], format="%a, %d %b %Y %H:%M:%S")



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
        'commits_data738a1791-db22-405f-a9f9-2207820dd591',
        'issues_dataa758a624-b518-4b21-98ea-b8de45734bd1',
        'mail_data5afb008d-62a5-4e14-a0fb-095977a91eeb',
        'users_datac5fc8ea1-4840-415b-a057-e06546b8e19f',
    ]

    filename = '/merged_data.csv'
    path = args.path + filename if args.path else DATA_DIR + filename

    DATA_LIST = load_data(DATA_URLS)
    DATA = concat_data(DATA_LIST)

    update_dates(DATA)
    save_data(DATA, path)
