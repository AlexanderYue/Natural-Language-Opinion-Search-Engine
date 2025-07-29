#used to read queries from output file and write the whole review to file in order to double check precision
def write_ids_to_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        ids = [line.strip().strip("'\"") for line in infile if line.strip()]

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for rid in ids:
            outfile.write(rid + '\n')

    print(f"[+] Wrote {len(ids)} IDs to {output_path}")

if __name__ == "__main__":
    input_file = "input_ids.txt"    # Change to your actual input filename
    output_file = "cleaned_ids.txt" # Desired output file name
    write_ids_to_file(input_file, output_file)
