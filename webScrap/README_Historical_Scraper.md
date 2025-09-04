# Historical Mark Six Lottery Data Scraper (1993-2025)

This project provides comprehensive tools to scrape historical Hong Kong Mark Six lottery data from 1993 to 2025, based on the structure of `Mark6_table.ipynb`.

## 📁 Files Created

### 1. **Mark6_Historical_Scraper.ipynb**
- **Purpose**: Educational Jupyter notebook for step-by-step learning
- **Features**: 
  - 8 well-documented cells with detailed comments
  - Step-by-step data processing pipeline
  - Visual progress indicators with emojis
  - Comprehensive error handling
  - Data quality checks

### 2. **historical_lottery_scraper.py**
- **Purpose**: Standalone Python script for easy execution
- **Features**:
  - Same functionality as the notebook
  - Command-line executable
  - Progress tracking
  - Error handling and logging

### 3. **all.csv** (Output File)
- **Purpose**: Complete historical dataset
- **Content**: All lottery draws from 1993-2025
- **Format**: Clean, analysis-ready data with separated number columns

## 🚀 How to Use

### Option 1: Jupyter Notebook (Recommended for Learning)
```bash
# Open the notebook
jupyter notebook Mark6_Historical_Scraper.ipynb

# Run each cell step by step to understand the process
```

### Option 2: Python Script (Quick Execution)
```bash
# Run the complete scraper
python historical_lottery_scraper.py

# This will scrape all years from 1993-2025 and save to all.csv
```

## 📊 Data Structure

The output CSV file (`all.csv`) contains the following columns:

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
2. **Data Cleaning**: Removes monthly header rows automatically
3. **Column Management**: Drops unnecessary columns (Draw Number, Details)
4. **Number Separation**: Splits lottery numbers into individual columns
5. **Data Validation**: Includes quality checks and error handling
6. **Output Generation**: Saves clean data to `all.csv`

### Error Handling
- **Graceful Failures**: Continues processing even if some years fail
- **Progress Tracking**: Shows successful vs failed years
- **Retry Logic**: Built-in delays between requests to be server-friendly
- **Data Validation**: Checks for missing values and data quality

### Educational Benefits
- **Step-by-Step Learning**: Each cell builds upon the previous one
- **Comprehensive Comments**: Every function and critical line is explained
- **Visual Progress**: Emojis and clear output help track progress
- **Real-World Application**: Shows complete data science pipeline

## 📈 Expected Results

- **Total Years**: 33 years (1993-2025)
- **Estimated Records**: 4,000+ lottery draws
- **Processing Time**: 5-10 minutes (due to 1-second delays between requests)
- **Output File**: `all.csv` with clean, analysis-ready data

## 🛠️ Requirements

```bash
pip install pandas lxml html5lib
```

## 📚 Educational Value

This project demonstrates:
- **Web Scraping**: Using pandas.read_html() for table extraction
- **Data Cleaning**: Removing invalid rows and columns
- **Data Transformation**: Splitting and formatting data
- **Error Handling**: Robust error management
- **Data Validation**: Quality checks and statistics
- **File I/O**: Saving processed data to CSV

## 🎯 Use Cases

The scraped data can be used for:
- **Statistical Analysis**: Number frequency analysis
- **Machine Learning**: Pattern recognition and prediction models
- **Data Visualization**: Charts and graphs of lottery trends
- **Research**: Academic studies on lottery patterns
- **Personal Projects**: Lottery analysis tools

## ⚠️ Important Notes

1. **Respectful Scraping**: Includes 1-second delays between requests
2. **Error Handling**: Some years may fail due to website changes
3. **Data Quality**: Includes validation to ensure data integrity
4. **Educational Focus**: Designed for learning data science concepts

## 🔍 Troubleshooting

If you encounter issues:
1. **Check Internet Connection**: Ensure stable internet access
2. **Verify Dependencies**: Make sure all required packages are installed
3. **Check Website Availability**: Verify the lottery website is accessible
4. **Review Error Messages**: Check the console output for specific errors

## 📞 Support

This project is based on the educational structure of `Mark6_table.ipynb` and provides a comprehensive example of historical data scraping for educational purposes.
