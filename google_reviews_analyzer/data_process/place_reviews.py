from typing import List

import pandas as pd


def get_reviews_by_place(file_path: str, place_name: str) -> List[str]:
    df = pd.read_csv(file_path)
    reviews = df[df["place_name"] == place_name]["review_text"].tolist()
    reviews = [review for review in reviews if isinstance(review, str)]
    return reviews
