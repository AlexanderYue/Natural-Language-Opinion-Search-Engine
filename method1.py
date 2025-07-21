# run_method1.py
import pandas as pd
import os
import time
from utils import load_reviews, match_review, is_opinion_positive, DATA_PATH, OUTPUT_DIR, QUERIES

def method1_rating_filter(df, aspect, opinion):
    results = []
    opinion_positive = is_opinion_positive(opinion)

    for _, row in df.iterrows():
        try:
            rating = float(row['customer_review_rating'])
        except (ValueError, TypeError):
            continue
        if match_review(row['review_text'], aspect, opinion):
            if opinion_positive and rating > 3:
                results.append(row['review_id'])
            elif not opinion_positive and rating <= 3:
                results.append(row['review_id'])
    return results

def run_method1():
    start_time = time.time()
    print("Running Method 1 (Boolean + Rating Filter)...")
    df = load_reviews(DATA_PATH)
    for fname, (aspect, opinion) in QUERIES.items():
        matched_ids = method1_rating_filter(df, aspect, opinion)
        out_path = os.path.join(OUTPUT_DIR, f"{fname}_test2.txt")
        with open(out_path, 'w') as f:
            for rid in matched_ids:
                f.write(str(rid).strip("'\"") + "\n")
        print(f"[+] Method1: Wrote {len(matched_ids)} matches to {out_path}")
    elapsed = time.time() - start_time
    print(f"\n Finished baseline queries in {elapsed:.2f} seconds.")
if __name__ == "__main__":
    run_method1()
