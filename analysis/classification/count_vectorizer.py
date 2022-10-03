from pydoc import doc
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def get_cv_stats(df, attribute):
    vectorizer = CountVectorizer()
    df_cv = vectorizer.fit_transform(df[attribute])

    doc_freq = np.array(df_cv.astype(bool).sum(axis=0)).flatten()
    print("DOC_FREQ")
    print(doc_freq)

    return vectorizer.vocabulary_, len(vectorizer.vocabulary_), vectorizer.get_feature_names_out(), doc_freq, doc_freq.sum()
