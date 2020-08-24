import pandas as pd
import argparse
import os
import logging

def sort_s5_by_date() -> pd.DataFrame:
    data = pd.read_csv(f'{DATA_DIR}/s5_without_utc.csv')
    sorted_data = data.sort_values(by=['Date'])

    return sorted_data

def check_unique_date_in_s5(sorted_data: pd.DataFrame):
    repeated_email_ID = []
    for idx, row in sorted_data.iterrows():
        if idx > 0:
            if row.Date == before_row.Date:
                repeated_email_ID.append(row.Email_ID)
                repeated_email_ID.append(before_row.Email_ID)
        before_row = row
    print("Email_ID's with repeated date")
    print(repeated_email_ID)
    print(f'Number of email with_repeated_date:\t{len(repeated_email_ID)}')


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

    filename = '/s5_sorted_by_date.csv'
    path = args.path + filename if args.path else DATA_DIR + filename

    sorted_data = sort_s5_by_date()
    save_final_emails(sorted_data, path)
    check_unique_date_in_s5(sorted_data)


