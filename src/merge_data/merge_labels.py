import argparse
import logging
import os
import pandas as pd

LOGGING_FORMAT = "[%(asctime)-15s] %(message)s"


def load_labels() -> pd.DataFrame:
    """
    load_labels is the function used to load and join labels from data directory

    :return: pd.DataFrame
    """
    s1_data = pd.read_csv(f'{DATA_DIR}/s1.csv')
    s5_data = pd.read_csv(f'{DATA_DIR}/s5.csv')

    s1_data = s1_data.drop(s1_data.columns.difference([
        'Email_ID',
        'Keyword_1',
        'Keyword_2',
        'Keyword_3',
        'Keyword_4',
        'Keyword_5'
    ]), 1)

    s5_data = s5_data.drop(s5_data.columns.difference([
        'Email_ID',
        'Trace_ID',
        'Action',
        'Date'
    ]), 1)

    return s5_data.join(s1_data.set_index('Email_ID'), on='Email_ID')


def save_labels(data: pd.DataFrame, path: str) -> None:
    """
    save_labels is the function to save data labels to data directory

    :param data: pd.DataFrame, data from load_labels()
    :param path: str, is the path to save data
    :return: None
    """
    try:
        pd.DataFrame(data).to_csv(path)
        logging.info(f"Successfully saved records to {path}")
    except:
        logging.info(f'Save error')


def update_dates(df: pd.DataFrame) -> None:
    df['Date'] = df['Date'].str.replace(r' UTC$', '')
    df['Date'] = df['Date'].dt.floor('T')


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

    data = load_labels()

    filename = '/merged_labels.csv'
    path = args.path + filename if args.path else DATA_DIR + filename

    update_dates(data)
    save_labels(data, path)
