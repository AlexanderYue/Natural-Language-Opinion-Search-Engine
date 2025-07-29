import ast

def extract_reviews_by_ids(id_file, sql_file, output_file):
    # Load review IDs
    with open(id_file, 'r', encoding='utf-8') as f:
        target_ids = set(line.strip().strip("'\"") for line in f if line.strip())

    matched = 0
    with open(sql_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
            line = line.strip().rstrip(',')  # remove trailing comma if present
            if not line:
                continue

            try:
                row = ast.literal_eval(line)  # safely parse the SQL tuple
                review_id = row[0]
                review_text = row[10]

                if review_id in target_ids:
                    matched += 1
                    outfile.write(f"[{review_id}]\n{review_text}\n\n")
            except Exception as e:
                print(f"Skipping line due to error: {e}")

    print(f"[+] Matched and wrote {matched} reviews to {output_file}")

if __name__ == "__main__":
    extract_reviews_by_ids(
        id_file="Outputs/image_quality_test3.txt",
        sql_file="reviews_segment.sql",
        output_file="matched_reviews.txt"
    )
