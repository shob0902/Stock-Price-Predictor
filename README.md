# Stock Price Predictor with Real Market Data

This application uses LSTM neural networks to predict stock prices using real market data from Yahoo Finance.

## 🚀 Quick Start

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Fetch Real Stock Data
```bash
python fetch_stock_data.py
```

This will create a `real_stock_data.json` file with 3 years of historical data for:
- AAPL (Apple)
- GOOGL (Alphabet/Google)
- MSFT (Microsoft)
- AMZN (Amazon)
- TSLA (Tesla)
- META (Meta Platforms)
- NVDA (NVIDIA)

### Step 3: Open the Application
Open `stock_predictor.html` in your web browser.

## 📊 Data Sources

### Real Market Data (Recommended)
- **Source**: Yahoo Finance via yfinance library
- **Coverage**: 3 years of daily closing prices
- **Update Frequency**: Run `fetch_stock_data.py` weekly/monthly
- **Format**: JSON file with date and closing price data

### Synthetic Data (Fallback)
- **Used when**: Real data file is not found
- **Purpose**: Demonstration and testing
- **Patterns**: Realistic price movements with seasonality and noise

## 🔧 Features

### Real-Time Predictions
- LSTM neural network trained on historical data
- Sequence-based predictions (10-30 days lookback)
- Future price forecasting
- Accuracy metrics (RMSE, percentage accuracy)

### Interactive UI
- Stock symbol selection
- Adjustable sequence length
- Real-time training progress
- Interactive charts with Chart.js
- Performance metrics display

### Data Visualization
- Actual vs Predicted price comparison
- Price change percentage
- Training loss visualization
- Responsive design with animations

## 📈 How It Works

1. **Data Loading**: Fetches real stock data from JSON file
2. **Preprocessing**: Normalizes data to [0,1] range
3. **Sequence Creation**: Creates time-series sequences for LSTM
4. **Model Training**: Trains LSTM network on historical data
5. **Prediction**: Makes predictions on test data and future values
6. **Visualization**: Displays results with interactive charts

## 🎯 Model Architecture

- **LSTM Layers**: 2 layers with 16 units each
- **Dense Layers**: 8 units + 1 output unit
- **Dropout**: 10% to prevent overfitting
- **Optimizer**: Adam with learning rate 0.001
- **Loss Function**: Mean Squared Error

## 📋 Usage Instructions

1. **Select Stock**: Choose from available stock symbols
2. **Set Parameters**: 
   - Sequence Length: 10-30 days (how much history to consider)
   - Prediction Days: 1-100 days (how far to predict)
3. **Click Predict**: Start the training and prediction process
4. **View Results**: Check the chart and metrics

## ⚠️ Important Notes

- **Educational Purpose**: This is for learning and demonstration
- **Not Financial Advice**: Do not use for actual trading decisions
- **Data Accuracy**: Real data provides more realistic predictions
- **Model Limitations**: LSTM models have inherent prediction limitations

## 🔄 Updating Data

To get fresh stock data:
```bash
python fetch_stock_data.py
```

The script will:
- Fetch latest 3 years of data
- Update the JSON file
- Show summary statistics
- Display price changes over the period

## 🛠️ Technical Details

### File Structure
```
├── stock_predictor.html      # Main application
├── fetch_stock_data.py       # Data fetching script
├── requirements.txt          # Python dependencies
├── real_stock_data.json     # Real stock data (generated)
└── README.md               # This file
```

### Browser Requirements
- Modern browser with ES6 support
- Internet connection for TensorFlow.js and Chart.js CDN
- Local file access for JSON data file

### Performance
- CPU-optimized TensorFlow.js backend
- Reduced model size for browser compatibility
- Efficient data processing and visualization
- Responsive design for mobile devices

## 🎨 UI Features

- **Glassmorphism Design**: Modern glass-like interface
- **Smooth Animations**: CSS transitions and keyframes
- **Real-time Updates**: Live training progress
- **Responsive Layout**: Works on desktop and mobile
- **Data Source Indicator**: Shows whether real or synthetic data is used

## 📊 Metrics Explained

- **Accuracy**: Percentage accuracy based on RMSE relative to mean price
- **RMSE**: Root Mean Square Error (lower is better)
- **Predicted Price**: Next predicted stock price
- **Price Change**: Percentage change from current to predicted price

## 🔍 Troubleshooting

### Common Issues

1. **"Real stock data file not found"**
   - Run `python fetch_stock_data.py` first
   - Ensure `real_stock_data.json` is in the same directory

2. **"TensorFlow initialization failed"**
   - Refresh the page
   - Check internet connection for CDN resources

3. **"Not enough training data"**
   - Reduce sequence length
   - Try a different stock symbol

4. **Slow performance**
   - The app uses CPU backend for compatibility
   - Training takes 10-30 seconds depending on data size

### Data Quality
- Real data provides more accurate predictions
- Synthetic data is used as fallback
- Check the data source indicator in the UI 