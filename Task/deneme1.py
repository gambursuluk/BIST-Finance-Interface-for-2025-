import json
import time
import pandas as pd
from isyatirimhisse import fetch_financials

def fetch_bist_financials(json_filepath, output_filepath):
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    tickers = [company.get("ticker") for company in data if company.get("ticker")]
    total_tickers = len(tickers)
    
    print(f"Toplam {total_tickers} hisse bulundu. İstekler başlıyor...\n")
    print("-" * 50)
    
    all_financials = []
    
    for idx, ticker in enumerate(tickers, start=1):
        print(f"[{idx}/{total_tickers}] Çekiliyor -> {ticker}")
        
        try:
            # v5.0+ API'sine göre güncellenmiş parametreler
            df = fetch_financials(
                symbols=ticker,
                start_year=2025,
                end_year=2025,
                exchange='TRY',
                financial_group='1' # 1: XI_29, 2: UFRS (Gerekirse 2 olarak değiştirebilirsin)
            )
            
            if df is not None and not df.empty:
                df['Ticker'] = ticker 
                all_financials.append(df)
                
        except Exception as e:
            # Sunucu kaynaklı kopmalarda scriptin patlamaması için
            print(f"    [!] HATA - {ticker} alınamadı: {e}")
            
        # İş Yatırım sunucularını darlayıp ban yememek için thread'i uyutuyoruz
        time.sleep(0.6)
        
    print("-" * 50)
    
    if all_financials:
        print("Bilanço verileri birleştiriliyor...")
        master_df = pd.concat(all_financials, ignore_index=True)
        master_df.to_excel(output_filepath, index=False)
        print(f"İşlem tamam! Veriler '{output_filepath}' dosyasına yazıldı.")
    else:
        print("Uyarı: Hiçbir veri çekilemedi. Şirketlerin 2025 verileri henüz işlenmemiş olabilir.")

if __name__ == "__main__":
    INPUT_FILE = "filtered_bist_data.json"
    OUTPUT_FILE = "BIST_2025_Tüm_Mali_Tablolar.xlsx"
    
    fetch_bist_financials(INPUT_FILE, OUTPUT_FILE)