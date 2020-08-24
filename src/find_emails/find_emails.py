import argparse
import os
import logging
import pandas as pd

LOGGING_FORMAT = "[%(asctime)-15s] %(message)s"





def find_emails() -> pd.DataFrame:
    data = pd.read_csv(f'{DATA_DIR}/merged_data.csv')
    s5 = pd.read_csv(f'{DATA_DIR}/s5_without_utc.csv')
    final = pd.DataFrame()


    for s5_idx, s5_row in s5.iterrows():

        for email_index, email_row in data.iterrows():
            if s5_row.Date == email_row.date:

                    email_with_id = email_row.append(pd.Series([s5_row.Email_ID], index=['Email_ID']))
                    final = final.append(email_with_id, ignore_index=True)

    return final

def remove_duplicates(path: str):
    data = pd.read_csv(f'{DATA_DIR}{path}')

    to_delete = []
    sorted_data = data.sort_values(by=['Email_ID'])
    for idx, row in sorted_data.iterrows():
        if idx > 0:
            if row.Email_ID == before_row.Email_ID:
                to_delete.append(idx)
                to_delete.append(before_idx)
        before_row = row
        before_idx = idx
    data.drop(to_delete, inplace=True)
    print("Table of indexes, which ws deleted\n", to_delete)

    return data







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
    data_for_preprocesing = remove_duplicates(filename)
    save_final_emails(data_for_preprocesing, path)



