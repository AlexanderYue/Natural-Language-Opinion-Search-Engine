from sentence_transformers import SentenceTransformer, util  # type: ignore
import torch
import pandas as pd
import os
import time
from utils import load_reviews, DATA_PATH, QUERIES, positive_words

# Load BERT model on correct device
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"[INFO] Using device: {device}")
model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

def is_opinion_positive(opinion):
    return any(word in positive_words for word in opinion.lower().split())

def method2_semantic_similarity(df, aspect, opinion, threshold):  # ← change threshold here
    print(f"\n[PROCESSING] Aspect: '{aspect}' | Opinion: '{opinion}' | Threshold: {threshold}")
    results = []
    query = f"{aspect} {opinion}"

    print("[ENCODING] Embedding query...")
    query_embedding = model.encode(query, convert_to_tensor=True)

    print("[ENCODING] Embedding reviews...")
    reviews = df['review_text'].astype(str).tolist()
    review_ids = df['review_id'].tolist()

    review_embeddings = model.encode(
        reviews,
        batch_size=128,  # ← change batch size here
        convert_to_tensor=True,
        show_progress_bar=True
    )

    print("[COMPUTING] Calculating cosine similarities...")
    similarities = util.cos_sim(query_embedding, review_embeddings)[0]
    opinion_positive = is_opinion_positive(opinion)

    print("[FILTERING] Applying threshold and sentiment check...")
    for idx, score in enumerate(similarities):
        if score.item() >= threshold:
            rating = float(df.iloc[idx]['customer_review_rating'])
            if opinion_positive and rating > 3:
                results.append((review_ids[idx], score.item()))
            elif not opinion_positive and rating <= 3:
                results.append((review_ids[idx], score.item()))

    results.sort(key=lambda x: -x[1])
    print(f"[RESULT] Matched {len(results)} reviews for '{aspect}: {opinion}'")
    return [rid for rid, _ in results]

def run_method2():
    start_time = time.time()
    print("=== Running Method 2 (Semantic Matching using BERT) ===")
    df = load_reviews(DATA_PATH)

    output_folder = os.path.join("..", "m2_outputs")
    os.makedirs(output_folder, exist_ok=True)

    for fname, (aspect, opinion) in QUERIES.items():
        matched_ids = method2_semantic_similarity(df, aspect, opinion, threshold=0.6)
        out_path = os.path.join(output_folder, f"{fname}_test.txt")

        print(f"[WRITING] Saving matched IDs to: {out_path}")
        with open(out_path, 'w', encoding='utf-8') as f:
            for rid in matched_ids:
                f.write(str(rid).strip("'\"") + "\n")

        print(f"[+] Method2: Wrote {len(matched_ids)} matches for {fname}")

    elapsed = time.time() - start_time
    print(f"\nFinished Method 2 in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    run_method2()
