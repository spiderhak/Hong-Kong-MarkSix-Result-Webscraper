# Hong Kong Mark Six Lottery Historical Data Scraper

A comprehensive Python project for scraping and analyzing historical Hong Kong Mark Six lottery data from 1993 to 2025.

## 🎯 Project Overview

This project provides tools to scrape, clean, and analyze 33 years of Hong Kong Mark Six lottery data. It includes both educational Jupyter notebooks and production-ready Python scripts for data collection and processing.

## 📁 Project Structure

```
webScrap/
├── Mark6_Historical_Scraper.ipynb    # Educational Jupyter notebook (1993-2025)
├── Mark6_table.ipynb                 # Educational Jupyter notebook (2025 only)
├── historical_lottery_scraper.py     # Standalone Python script (1993-2025)
├── lottery_scraper.py                # Standalone Python script (2025 only)
├── all.csv                          # Complete historical dataset (4,250 records)
├── lottery_results_2025_final.csv   # 2025 dataset (96 records)
├── requirements.txt                  # Python dependencies
├── README.md                        # This file
└── .gitignore                       # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install -r requirements.txt
```

### Option 1: Educational Approach (Recommended)

```bash
# Open Jupyter notebook for step-by-step learning
jupyter notebook Mark6_Historical_Scraper.ipynb
```

### Option 2: Quick Execution

```bash
# Scrape all historical data (1993-2025)
python historical_lottery_scraper.py

# Scrape 2025 data only
python lottery_scraper.py
```

## 📊 Data Structure

The output CSV files contain the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `Draw Date` | Date of the lottery draw | "02/09/2025" |
| `num1` | First lottery number | 5 |
| `num2` | Second lottery number | 18 |
| `num3` | Third lottery number | 23 |
| `num4` | Fourth lottery number | 24 |
| `num5` | Fifth lottery number | 29 |
| `num6` | Sixth lottery number | 49 |
| `num7` | Seventh lottery number (bonus) | 11 |

## 🔧 Key Features

### Data Processing Pipeline
1. **Web Scraping**: Fetches data from `https://lottery.hk/en/mark-six/results/{year}`
2. **Data Cleaning**: Automatically removes monthly header rows
3. **Column Management**: Drops unnecessary columns (Draw Number, Details)
4. **Number Separation**: Splits lottery numbers into individual columns
5. **Data Validation**: Includes comprehensive quality checks
6. **Output Generation**: Saves clean data to CSV files

### Educational Benefits
- **Step-by-Step Learning**: Each notebook cell builds upon the previous one
- **Comprehensive Comments**: Every function and critical line is explained
- **Visual Progress**: Emojis and clear output help track progress
- **Real-World Application**: Shows complete data science pipeline

### Error Handling
- **Graceful Failures**: Continues processing even if some years fail
- **Progress Tracking**: Shows successful vs failed years
- **Retry Logic**: Built-in delays between requests to be server-friendly
- **Data Validation**: Checks for missing values and data quality

## 📈 Dataset Statistics

- **Total Years**: 33 years (1993-2025)
- **Total Records**: 4,250 lottery draws
- **Date Range**: 1993 to 2025
- **Data Quality**: Clean, analysis-ready format
- **File Size**: ~150KB (all.csv)

## 🛠️ Technical Details

### Dependencies
- `pandas` - Data manipulation and analysis
- `lxml` - XML/HTML processing
- `html5lib` - HTML parsing
- `requests` - HTTP requests
- `beautifulsoup4` - Web scraping
- `jupyter` - Interactive notebooks

### Web Scraping
- Uses `pandas.read_html()` for reliable table extraction
- Implements respectful scraping with 1-second delays
- Handles SSL certificate issues automatically
- Includes comprehensive error handling

### Data Cleaning
- Removes monthly header rows automatically
- Validates lottery number formats
- Handles missing values gracefully
- Ensures data integrity throughout processing

## 📚 Use Cases

The scraped data can be used for:
- **Statistical Analysis**: Number frequency analysis
- **Machine Learning**: Pattern recognition and prediction models
- **Data Visualization**: Charts and graphs of lottery trends
- **Research**: Academic studies on lottery patterns
- **Personal Projects**: Lottery analysis tools

## 🔍 Data Quality

The project includes comprehensive data quality checks:
- Missing value analysis
- Duplicate detection
- Number range validation (1-49 for Mark Six)
- Date range verification
- Data type validation

## ⚠️ Important Notes

1. **Respectful Scraping**: Includes 1-second delays between requests
2. **Error Handling**: Some years may fail due to website changes
3. **Data Quality**: Includes validation to ensure data integrity
4. **Educational Focus**: Designed for learning data science concepts

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hong-kong-lottery-scraper.git
   cd hong-kong-lottery-scraper
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**:
   ```bash
   python historical_lottery_scraper.py
   ```

4. **Explore the data**:
   ```bash
   jupyter notebook Mark6_Historical_Scraper.ipynb
   ```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

## 🎉 Acknowledgments

- Hong Kong Jockey Club for providing the lottery data
- Python community for excellent data science libraries
- Jupyter project for interactive computing environment

---

**Happy Data Scraping! 🎲📊**
