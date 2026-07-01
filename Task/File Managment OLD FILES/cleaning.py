import json

def filter_multiple_tickers(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    filtered_data = [company for company in data if "," not in company.get("ticker", "")]
    
    with open(output_filepath, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)

    print(f"Orijinal listedeki şirket sayısı: {len(data)}")
    print(f"Virgüllü olanlar silindikten sonraki şirket sayısı: {len(filtered_data)}")
    print(f"Filtrelenmiş veri '{output_filepath}' dosyasına kaydedildi.")

if __name__ == "__main__":
    input_file = "bist_data.json"
    output_file = "filtered_bist_data.json"
    filter_multiple_tickers(input_file, output_file)