import argparse
import logging
import os
import pandas as pd

LOGGING_FORMAT = "[%(asctime)-15s] %(message)s"


def find_emails() -> pd.DataFrame:
    data = pd.read_csv(f'{DATA_DIR}/merged_data.csv')
    labels = pd.read_csv(f'{DATA_DIR}/merged_labels.csv')
    final = pd.DataFrame()

    for label_index, label_row in labels.iterrows():
        for email_index, email_row in data.iterrows():
            if label_row.Date == email_row.date:
                email_with_id = email_row.append(pd.Series([label_row.Email_ID], index=['email_ID_from_label']))
                final = final.append(email_with_id, ignore_index=True)

    return final


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

    data = find_emails()

    filename = '/found_emails.csv'
    path = args.path + filename if args.path else DATA_DIR + filename

    save_final_emails(data, path)
