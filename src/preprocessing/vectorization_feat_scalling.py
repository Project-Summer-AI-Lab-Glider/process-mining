import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from src.merge_data.merge_data import save_data


def count_words(clean_data):
    """this function creates a matrix of token counts"""
    cv = CountVectorizer()
    cv_fit = cv.fit(clean_data)
    cv_counts = cv.transform(clean_data)
    cv_counts_pd= pd.DataFrame(cv_counts.toarray())
    cv_counts_pd.columns = cv_fit.get_feature_names()
    print(cv_counts_pd)

    return cv_counts_pd


def tfidf_scalling(clean_data):
    """this function creates matrix of tf-idf values
    the higher the value - the more unique token
    """
    tfidf_vectorizer = TfidfVectorizer(use_idf=True)
    fitted_vectorizer = tfidf_vectorizer.fit(clean_data)
    tfidf_vectors = fitted_vectorizer.transform(clean_data)
    tfidf_vectors_pd = pd.DataFrame(tfidf_vectors.toarray())
    tfidf_vectors_pd.columns=tfidf_vectorizer.get_feature_names()

    return tfidf_vectors_pd


if __name__ == "__main__":

    CURRENT_DIR = os.path.abspath(os.curdir)
    SRC_PATH = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
    ROOT_PATH = os.path.abspath(os.path.join(SRC_PATH, os.pardir))
    DATA_DIR = os.path.join(ROOT_PATH, 'data')

    data = pd.read_csv(f'{DATA_DIR}/cleaned_emails.csv').content + pd.read_csv(f'{DATA_DIR}/cleaned_emails.csv').subject

    cv = count_words(data)
    filename1 = '/counted_words.csv'
    save_data(cv, DATA_DIR + filename1)

    tfidf = tfidf_scalling(data)
    filename2 = '/tfidf.csv'
    save_data(tfidf, DATA_DIR+filename2)