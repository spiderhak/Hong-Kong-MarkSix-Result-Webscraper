#!/usr/bin/env python3
"""
Historical Mark Six Lottery Data Scraper (1993-2025)
Based on Mark6_table.ipynb structure

This script scrapes lottery data from 1993 to 2025 and saves it to all.csv
"""

import pandas as pd
import ssl
import warnings
import time
from datetime import datetime

# Suppress warnings
warnings.filterwarnings('ignore')

# Handle SSL certificate issues
ssl._create_default_https_context = ssl._create_unverified_context

def clean_lottery_data(df, year):
    """Clean lottery data by removing monthly headers and invalid data"""
    print(f"📊 {year} - Original data shape: {df.shape}")
    
    df_clean = df.copy()
    monthly_rows = []
    
    for idx, row in df_clean.iterrows():
        non_null_values = [str(val) for val in row if pd.notna(val)]
        if len(non_null_values) > 0:
            if len(set(non_null_values)) == 1 and any(month in non_null_values[0] for month in 
                ['January', 'February', 'March', 'April', 'May', 'June', 
                 'July', 'August', 'September', 'October', 'November', 'December']):
                monthly_rows.append(idx)
    
    df_clean = df_clean.drop(monthly_rows)
    
    if 'Draw Number' in df_clean.columns:
        df_clean = df_clean[df_clean['Draw Number'].str.contains('/', na=False)]
    
    df_clean = df_clean.reset_index(drop=True)
    
    print(f"🗑️  {year} - Removed {len(monthly_rows)} monthly header rows")
    print(f"📊 {year} - Cleaned data shape: {df_clean.shape}")
    
    return df_clean

def split_balls_drawn(balls_str):
    """Split balls drawn string into individual numbers"""
    if pd.isna(balls_str):
        return [None] * 7
    
    numbers = [num.strip() for num in str(balls_str).replace(',', '').split() if num.strip()]
    while len(numbers) < 7:
        numbers.append(None)
    
    return numbers[:7]

def process_lottery_data(df, year):
    """Process lottery data for a specific year"""
    if df is None or df.empty:
        print(f"❌ {year} - No data available")
        return None
    
    df_clean = clean_lottery_data(df, year)
    
    if df_clean.empty:
        print(f"❌ {year} - No valid data after cleaning")
        return None
    
    # Drop unnecessary columns
    columns_to_drop = ['Draw Number', 'Details']
    existing_columns_to_drop = [col for col in columns_to_drop if col in df_clean.columns]
    if existing_columns_to_drop:
        df_clean = df_clean.drop(columns=existing_columns_to_drop)
        print(f"🗑️  {year} - Removed columns: {existing_columns_to_drop}")
    
    # Format and split balls drawn
    if 'Balls Drawn' in df_clean.columns:
        def format_balls_drawn(balls_str):
            if pd.isna(balls_str):
                return balls_str
            numbers = [num.strip() for num in str(balls_str).split() if num.strip()]
            return ', '.join(numbers)
        
        df_clean['Balls Drawn'] = df_clean['Balls Drawn'].apply(format_balls_drawn)
        
        balls_data = df_clean['Balls Drawn'].apply(split_balls_drawn)
        for i in range(7):
            df_clean[f'num{i+1}'] = balls_data.apply(lambda x: x[i])
        
        df_clean = df_clean.drop(columns=['Balls Drawn'])
        print(f"🔢 {year} - Separated numbers into 7 columns")
    
    # Note: Year column removed as requested - data will be identified by Draw Date only
    print(f"✅ {year} - Processing completed. Final shape: {df_clean.shape}")
    
    return df_clean

def main():
    """Main function to scrape historical lottery data"""
    print("✅ Libraries imported successfully!")
    print("📚 Ready to start historical web scraping (1993-2025)...")
    print(f"🕐 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Define years to scrape
    start_year = 1993
    end_year = 2025
    years_to_scrape = list(range(start_year, end_year + 1))
    
    print(f"📅 Years to scrape: {start_year} to {end_year}")
    print(f"🔢 Total years: {len(years_to_scrape)}")
    
    # Initialize data collection
    all_data = []
    successful_years = []
    failed_years = []
    
    print("\n🌐 Starting historical data scraping...")
    print("⏳ This may take several minutes due to the large amount of data...")
    print("=" * 80)
    
    for i, year in enumerate(years_to_scrape, 1):
        print(f"\n📅 Processing year {year} ({i}/{len(years_to_scrape)})...")
        
        try:
            url = f"https://lottery.hk/en/mark-six/results/{year}"
            print(f"🌐 Fetching: {url}")
            
            scraped = pd.read_html(url)
            
            if scraped and len(scraped) > 0:
                df_year = scraped[0]
                processed_data = process_lottery_data(df_year, year)
                
                if processed_data is not None and not processed_data.empty:
                    all_data.append(processed_data)
                    successful_years.append(year)
                    print(f"✅ {year} - Successfully processed {len(processed_data)} records")
                else:
                    failed_years.append(year)
                    print(f"❌ {year} - No valid data after processing")
            else:
                failed_years.append(year)
                print(f"❌ {year} - No tables found on webpage")
                
        except Exception as e:
            failed_years.append(year)
            print(f"❌ {year} - Error occurred: {str(e)[:100]}...")
        
        # Add delay between requests
        if i < len(years_to_scrape):
            time.sleep(1)
    
    print("\n" + "=" * 80)
    print(f"🎉 Scraping completed!")
    print(f"✅ Successful years: {len(successful_years)}")
    print(f"❌ Failed years: {len(failed_years)}")
    print(f"📊 Total dataframes collected: {len(all_data)}")
    
    # Combine all data
    if all_data:
        print("\n🔗 Combining all historical data...")
        combined_df = pd.concat(all_data, ignore_index=True)
        
        print(f"✅ Successfully combined {len(all_data)} dataframes")
        print(f"📊 Combined data shape: {combined_df.shape} (rows × columns)")
        print(f"📋 Columns: {list(combined_df.columns)}")
        
        # Save to CSV
        output_file = 'all.csv'
        print(f"\n💾 Saving data to '{output_file}'...")
        
        try:
            combined_df.to_csv(output_file, index=False)
            print(f"✅ Successfully saved data to '{output_file}'")
            print(f"📁 File size: {len(combined_df):,} rows × {len(combined_df.columns)} columns")
            
            # Display summary
            print(f"\n📈 FINAL SUMMARY:")
            print(f"   🎯 Total lottery draws: {len(combined_df):,}")
            if 'Draw Date' in combined_df.columns:
                print(f"   📅 Date range: {combined_df['Draw Date'].min()} to {combined_df['Draw Date'].max()}")
                print(f"   📊 Data spans multiple years (1993-2025) as indicated by date range")
            
            print(f"\n🎉 HISTORICAL DATA SCRAPING COMPLETED SUCCESSFULLY!")
            print(f"📚 The complete dataset ({len(combined_df):,} records) is now ready for analysis!")
            print(f"🕐 Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    else:
        print("❌ No data to save!")

if __name__ == "__main__":
    main()
