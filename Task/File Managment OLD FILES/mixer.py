import json

def convert_tsv_to_json(input_filepath, output_filepath):
    bist_data = []
    with open(input_filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if '\t' in line:
                ticker, name = line.strip().split('\t', 1)
                bist_data.append({"ticker": ticker.strip(), "companyName": name.strip(), "_source":"[cite: 4]"})

    with open(output_filepath, 'w', encoding='utf-8') as out_file:
        json.dump(bist_data, out_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    convert_tsv_to_json('Merges.txt', 'bist_data.json')