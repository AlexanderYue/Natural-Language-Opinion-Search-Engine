import pandas as pd
import os
import time
from utils import load_reviews, match_review, DATA_PATH, OUTPUT_DIR, QUERIES

def run_baseline():
    start_time = time.time()
    print("Loading data...")
    df = load_reviews(DATA_PATH)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Running Boolean baseline queries...")
    for fname, (aspect, opinion) in QUERIES.items():
        matched_ids = []
        for _, row in df.iterrows():
            if match_review(row['review_text'], aspect, opinion):
                matched_ids.append(row['review_id'])
        out_path = os.path.join(OUTPUT_DIR, f"{fname}_test1.txt")
        with open(out_path, 'w') as f:
            for rid in matched_ids:
                f.write(str(rid).strip("'\"") + "\n")
        print(f"[+] Baseline: Wrote {len(matched_ids)} matches to {out_path}")

    elapsed = time.time() - start_time
    print(f"\n Finished baseline queries in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    run_baseline()
