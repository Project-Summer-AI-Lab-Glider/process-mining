from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from typing import List

# jesli pierwszy raz uzywasz nltk musisz pobrać tzw. słowniki
import nltk
nltk.download()


def clean_record(record: str) -> List[str]:
    ps = PorterStemmer()
    
    # pobieranie tekstu ze strony HTML wywala niektóre błędy np. znak ">" interpretowany jest w html jako &gt
    # a np. "\n" to ";" wstępnie możemy oczyścić zawartość maila pozbywając się tych znaków
    record = record.replace("&#010", "").replace("&gt", ">").replace("&lt", "<").replace(";", " ").replace("-", "")
    words = word_tokenize(record)
    
    # usuwanie tzw. stop_words, w języku ang. np. and, or, what, about
    # https://en.wikipedia.org/wiki/Stop_words
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    # stemming - usuwanie z wyrazów końcówki fleksyjnej wg algorytmu Portera
    # https://pl.wikipedia.org/wiki/Stemming
    words = [ps.stem(word) for word in words]
    return words


if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    df = pd.read_csv("../../data/merged_data.csv")
    example_mail = df.content[0]

    
    processed_mail = clean_record(example_mail)
    print(processed_mail)
