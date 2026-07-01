import json
import time
import pandas as pd
from isyatirimhisse import fetch_financials

def fetch_bist_financials(json_filepath, output_filepath):
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    tickers = [company.get("ticker") for company in data if company.get("ticker")]
    total_tickers = len(tickers)
    
    print(f"Found {total_tickers} tickers in total. Initiating requests for 2025 data...\n")
    print("-" * 50)
    
    all_financials = []
    
    for idx, ticker in enumerate(tickers, start=1):
        print(f"[{idx}/{total_tickers}] Fetching -> {ticker}")
        
        try:
            df = fetch_financials(
                symbols=ticker,
                start_year=2025,
                end_year=2025,
                exchange='TRY',
                financial_group='1' # 1: XI_29, 2: IFRS (Change to 2 if needed)
            )
            
            if df is not None and not df.empty:
                df['Ticker'] = ticker 
                all_financials.append(df)
                
        except Exception as e:
            print(f"    [!] ERROR - Failed to fetch {ticker}: {e}")
            
        time.sleep(0.6)
        
    print("-" * 50)
    
    if all_financials:
        print("Concatenating balance sheet data...")
        master_df = pd.concat(all_financials, ignore_index=True)
        master_df.to_excel(output_filepath, index=False)
        print(f"Process completed! Data written to '{output_filepath}'.")
    else:
        print("Warning: No data was fetched. The 2025 reports for the companies might not be processed yet.")

if __name__ == "__main__":
    INPUT_FILE = "filtered_bist_data.json"
    OUTPUT_FILE = "BIST_2025_All_Financials.xlsx"
    
    fetch_bist_financials(INPUT_FILE, OUTPUT_FILE)