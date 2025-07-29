from sentence_transformers import SentenceTransformer, util # type: ignore
import torch
import pandas as pd
import os
import time
from utils import load_reviews, DATA_PATH, OUTPUT_DIR, QUERIES, positive_words

# Load BERT model
device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

def is_opinion_positive(opinion):
    return any(word in positive_words for word in opinion.lower().split())

def method2_semantic_similarity(df, aspect, opinion, threshold=0.6): #--------Change threshold here------
    results = []
    query = f"{aspect} {opinion}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    reviews = df['review_text'].astype(str).tolist()
    review_ids = df['review_id'].tolist()

    review_embeddings = model.encode(
        reviews,
        batch_size=128, #--------Change batch size here------
        convert_to_tensor=True,
        show_progress_bar=True
    )

    similarities = util.cos_sim(query_embedding, review_embeddings)[0]
    opinion_positive = is_opinion_positive(opinion)

    for idx, score in enumerate(similarities):
        if score.item() >= threshold:

            rating = float(df.iloc[idx]['customer_review_rating'])

            if opinion_positive and rating > 3:
                results.append((review_ids[idx], score.item()))
            elif not opinion_positive and rating <= 3:
                results.append((review_ids[idx], score.item()))


    results.sort(key=lambda x: -x[1])
    return [rid for rid, _ in results]



def run_method2():
    start_time = time.time()
    print("Running Method 2 (Semantic Matching using BERT)...")
    df = load_reviews(DATA_PATH)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for fname, (aspect, opinion) in QUERIES.items():
        matched_ids = method2_semantic_similarity(df, aspect, opinion, threshold=0.6)
        out_path = os.path.join(OUTPUT_DIR, f"{fname}_test3.txt")
        with open(out_path, 'w') as f:
            for rid in matched_ids:
                f.write(str(rid).strip("'\"") + "\n")
        print(f"[+] Method2: Wrote {len(matched_ids)} matches to {out_path}")
    elapsed = time.time() - start_time
    print(f"\n Finished method2 queries in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    run_method2()