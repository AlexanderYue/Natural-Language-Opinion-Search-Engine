import os
import time
import pandas as pd
from utils import load_reviews, match_review, DATA_PATH, OUTPUT_DIR, QUERIES

def match_aspect_only(text, aspect):
    aspect_words = aspect.lower().split()
    text = text.lower()
    return any(word in text for word in aspect_words)

def match_aspect_and_opinion(text, aspect, opinion):
    return match_review(text, aspect, opinion)

def match_aspect_or_opinion(text, aspect, opinion):
    text = text.lower()
    aspect_words = aspect.lower().split()
    opinion_words = opinion.lower().split()

    aspect_found = any(word in text for word in aspect_words)
    opinion_found = all(word in text for word in opinion_words)

    return aspect_found or opinion_found

def run_baseline():
    start_time = time.time()
    print("Loading reviews...")
    df = load_reviews(DATA_PATH)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Running Boolean baseline tests...")

    for test_name in ["test1", "test2", "test3"]:
        for fname, (aspect, opinion) in QUERIES.items():
            test_start_time = time.time()
            matched_ids = []

            for _, row in df.iterrows():
                text = row['review_text']

                if test_name == "test1":
                    if match_aspect_only(text, aspect):
                        matched_ids.append(row['review_id'])

                elif test_name == "test2":
                    if match_aspect_and_opinion(text, aspect, opinion):
                        matched_ids.append(row['review_id'])

                elif test_name == "test3":
                    if match_aspect_or_opinion(text, aspect, opinion):
                        matched_ids.append(row['review_id'])

            out_path = os.path.join(OUTPUT_DIR, f"{fname}_{test_name}.txt")
            with open(out_path, 'w', encoding='utf-8') as f:
                for rid in matched_ids:
                    f.write(str(rid).strip("'\"") + "\n")

            test_elapsed = time.time() - test_start_time
            print(f"[+] {test_name} ({fname}): Wrote {len(matched_ids)} matches in {test_elapsed:.2f}s to {out_path}")

    total_elapsed = time.time() - start_time
    print(f"\nFinished all baseline tests in {total_elapsed:.2f} seconds.")

if __name__ == "__main__":
    run_baseline()
