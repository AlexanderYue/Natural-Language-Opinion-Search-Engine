# utils.py
import pandas as pd
import re

DATA_PATH = "dataset/reviews_segment.pkl"
OUTPUT_DIR = "Outputs"
QUERIES = {
    "audio_quality": ("audio quality", "poor"),
    "wifi_signal": ("wifi signal", "strong"),
    "mouse_button": ("mouse button", "click problem"),
    "gps_map": ("gps map", "useful"),
    "image_quality": ("image quality", "sharp")
}

positive_words = set(["good", "great", "excellent", "strong", "useful", "amazing", "fantastic", "sharp"])
negative_words = set(["bad", "poor", "terrible", "awful", "useless", "weak", "problem", "issue"])

stopwords = set("""
i me my myself we our ours ourselves you your yours yourself yourselves he him his himself
she her hers herself it its itself they them their theirs themselves what which who whom this
that these those am is are was were be been being have has had having do does did doing a an
the and but if or because as until while of at by for with about against between into through
during before after above below to from up down in out on off over under again further then once
here there when where why how all any both each few more most other some such no nor not only own
same so than too very s t can will just don should now
""".split())

def load_reviews(path):
    return pd.read_pickle(path)

def remove_stopwords(text):
    return ' '.join([word for word in text.lower().split() if word not in stopwords])

def match_review(text, aspect, opinion):
    cleaned_text = remove_stopwords(text)
    cleaned_aspect = remove_stopwords(aspect)
    cleaned_opinion = remove_stopwords(opinion)
    return cleaned_aspect in cleaned_text and cleaned_opinion in cleaned_text

def is_opinion_positive(opinion):
    return any(word in positive_words for word in opinion.lower().split())
