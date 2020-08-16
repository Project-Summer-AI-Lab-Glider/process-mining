import argparse
import logging
import os
import pandas as pd

LOGGING_FORMAT = "[%(asctime)-15s] %(message)s"





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



def save_final_emails(data: pd.DataFrame, path: str) -> None:
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

    s5_data = pd.read_csv(f'{DATA_DIR}/s5.csv')

    filename = '/s5_without_utc.csv'
    path = args.path + filename if args.path else DATA_DIR + filename

    update_dates(s5_data)
    save_labels(s5_data, path)

    # s5_with_row = add_row_for_idx(path)
    # save_labels(s5_with_row, path)

# def add_row_for_idx(path: str) -> None:
#     s5 = pd.read_csv(path)
#     result = pd.DataFrame()
#     for s5_idx, s5_row in s5.iterrows():
#         email_with_idx = s5_row.append(pd.Series([''], index=['idx_from_merged_data']))
#         result = result.append(email_with_idx, ignore_index=True)
#
#     return result