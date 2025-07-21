import pandas as pd
import os

# Ensure output folder exists
os.makedirs("dataset", exist_ok=True)

# Sample review data (5 mock rows)
data = {
    'review_id': ['r1', 'r2', 'r3', 'r4', 'r5'],
    'product_id': ['p1', 'p2', 'p3', 'p4', 'p5'],
    'customer_id': ['c1', 'c2', 'c3', 'c4', 'c5'],
    'review_title': ['Great sound', 'Terrible audio', 'Okay mouse', 'GPS is useful', 'Blurry image'],
    'review_written_date': ['2023-01-01'] * 5,
    'customer_name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'review_from_title': ['title1', 'title2', 'title3', 'title4', 'title5'],
    'review_text': [
        "The audio quality of this speaker is amazing.",
        "Very poor audio quality, wouldn't recommend.",
        "Mouse button has a click problem sometimes.",
        "The GPS map feature is super useful on trips.",
        "I expected sharp image quality but it's blurry."
    ],
    'helpful_count': [2, 1, 0, 3, 1],
    'out_of_helpful_count': [2, 2, 1, 4, 2],
    'customer_review_rating': [5, 1, 3, 4, 2],
    'number_of_comments': [0, 0, 1, 2, 1],
    'amazon_verified_purchase': ['Y', 'Y', 'N', 'Y', 'N'],
    'amazon_vine_program_review': ['N', 'N', 'N', 'N', 'Y'],
    'review_with_metadata': ['', '', '', '', '']
}

df = pd.DataFrame(data)
df.to_pickle("dataset/reviews_segment.pkl")
print("[+] Created test dataset at dataset/reviews_segment.pkl")
