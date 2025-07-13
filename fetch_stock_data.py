import yfinance as yf
import json
import pandas as pd
from datetime import datetime, timedelta

def fetch_stock_data():
    """Fetch real stock market data for all supported stocks"""
    
    # Stock symbols used in the application
    stocks = {
        'AAPL': 'Apple Inc.',
        'GOOGL': 'Alphabet Inc.',
        'MSFT': 'Microsoft Corporation',
        'AMZN': 'Amazon.com Inc.',
        'TSLA': 'Tesla Inc.',
        'META': 'Meta Platforms Inc.',
        'NVDA': 'NVIDIA Corporation'
    }
    
    # Calculate date range (3 years of data)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=3*365)
    
    all_stock_data = {}
    
    print("🔄 Fetching real stock market data from Yahoo Finance...")
    
    for symbol, company_name in stocks.items():
        try:
            print(f"📊 Fetching data for {symbol} ({company_name})...")
            
            # Download stock data
            ticker = yf.Ticker(symbol)
            data = ticker.history(start=start_date, end=end_date)
            
            if data.empty:
                print(f"❌ No data found for {symbol}")
                continue
            
            # Extract closing prices and dates
            stock_data = []
            for date, row in data.iterrows():
                stock_data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'close': float(row['Close'])
                })
            
            all_stock_data[symbol] = {
                'company': company_name,
                'data': stock_data,
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'data_points': len(stock_data)
            }
            
            print(f"✅ {symbol}: {len(stock_data)} data points fetched")
            
        except Exception as e:
            print(f"❌ Error fetching data for {symbol}: {str(e)}")
    
    # Save to JSON file
    with open('real_stock_data.json', 'w') as f:
        json.dump(all_stock_data, f, indent=2)
    
    print(f"\n🎉 Successfully saved data for {len(all_stock_data)} stocks to 'real_stock_data.json'")
    
    # Print summary
    for symbol, data in all_stock_data.items():
        if data['data']:
            first_price = data['data'][0]['close']
            last_price = data['data'][-1]['close']
            change_pct = ((last_price - first_price) / first_price) * 100
            print(f"📈 {symbol}: ${first_price:.2f} → ${last_price:.2f} ({change_pct:+.2f}%)")
    
    return all_stock_data

if __name__ == "__main__":
    fetch_stock_data() 