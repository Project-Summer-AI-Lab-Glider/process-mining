import logging
import os
import re

import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

from merge_data.merge_data import save_data


def remove_non_alphanumeric(text):
    words = [word for word in text if not re.match(r'[\W\d]*$', word)]
    return words


def remove_html(text):
    soup = BeautifulSoup(text, 'lxml')
    html_free = soup.get_text()
    return html_free


def remove_stopwords(text):
    words = [word for word in text if word not in stopwords.words('english')]
    return words


def clean_text(content: pd.Series) -> pd.Series:
    """
    Remove unnecessary words and items from text e.g numbers,
    capitalization, punctuation, stop words
    :param content: pd.Series which we want to clean
    :return:
    """
    cleaned_content = content.apply(lambda text: remove_html(text))
    print(cleaned_content[0])
    # Remove links from content
    cleaned_content = cleaned_content.apply(lambda elem: re.sub(r"https?://\S+", "", elem))
    # Tokenize content
    tokenizer = RegexpTokenizer('\\w+|\\$[\\d\\.]+|\\S+')
    cleaned_content = cleaned_content.apply(lambda elem: tokenizer.tokenize(elem.lower()))
    # Remove non alphanumeric tokens
    cleaned_content = cleaned_content.apply(lambda elem: remove_non_alphanumeric(elem))
    # Remove stopwords
    cleaned_content = cleaned_content.apply(lambda word: remove_stopwords(word))
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    cleaned_content = cleaned_content.apply(lambda elem: " ".join([lemmatizer.lemmatize(word) for word in elem]))

    return cleaned_content


if __name__ == "__main__":

    CURRENT_DIR = os.path.abspath(os.curdir)
    SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    ROOT_PATH = os.path.abspath(os.path.join(SRC_PATH, os.pardir))
    DATA_DIR = os.path.join(ROOT_PATH, 'data')

    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
        logging.info(f"{DATA_DIR} was created successfully.")

    data = pd.read_csv(f'{DATA_DIR}/found_emails.csv')
    s1 = pd.read_csv(f'{DATA_DIR}/s1.csv')
    data['content'] = clean_text(data['content'])
    data['subject'] = clean_text(data['subject'])
    filename = '/cleaned_emails.csv'
    path = DATA_DIR + filename

    save_data(data, path)
