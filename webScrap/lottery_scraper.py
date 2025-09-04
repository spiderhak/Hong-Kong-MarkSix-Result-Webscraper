import pandas as pd
import ssl
import warnings

warnings.filterwarnings('ignore')

# Handle SSL certificate issues
ssl._create_default_https_context = ssl._create_unverified_context

def clean_lottery_data(df):
    """
    Clean the lottery data by removing monthly header rows and invalid data
    """
    print(f"Original data shape: {df.shape}")
    
    # Create a copy to avoid modifying original
    df_clean = df.copy()
    
    # Remove rows where all columns contain the same month name (monthly headers)
    monthly_rows = []
    for idx, row in df_clean.iterrows():
        # Check if all non-null values in the row are the same and contain month names
        non_null_values = [str(val) for val in row if pd.notna(val)]
        if len(non_null_values) > 0:
            # Check if all values are the same and contain month names
            if len(set(non_null_values)) == 1 and any(month in non_null_values[0] for month in 
                ['January', 'February', 'March', 'April', 'May', 'June', 
                 'July', 'August', 'September', 'October', 'November', 'December']):
                monthly_rows.append(idx)
    
    # Remove monthly header rows
    df_clean = df_clean.drop(monthly_rows)
    
    # Remove rows where Draw Number doesn't contain a slash (invalid lottery numbers)
    df_clean = df_clean[df_clean['Draw Number'].str.contains('/', na=False)]
    
    # Reset index after dropping rows
    df_clean = df_clean.reset_index(drop=True)
    
    print(f"Removed {len(monthly_rows)} monthly header rows")
    print(f"Cleaned data shape: {df_clean.shape}")
    
    return df_clean

def split_balls_drawn(balls_str):
    """Split balls drawn string into individual numbers"""
    if pd.isna(balls_str):
        return [None] * 7
    
    # Remove commas and split by spaces, then filter out empty strings
    numbers = [num.strip() for num in str(balls_str).replace(',', '').split() if num.strip()]
    
    # Ensure we have exactly 7 numbers, pad with None if less
    while len(numbers) < 7:
        numbers.append(None)
    
    # Return only first 7 numbers
    return numbers[:7]

def scrape_lottery_results():
    """
    Scrape lottery results from Hong Kong Mark Six lottery website and process to final clean format
    """
    url = "https://lottery.hk/en/mark-six/results/2025"
    
    try:
        # Scrape the lottery results table
        print("Fetching data from:", url)
        scraped = pd.read_html(url)
        
        print(f"Successfully scraped {len(scraped)} tables")
        
        # Process the first table (main results table)
        if scraped:
            df = scraped[0]
            print(f"\nOriginal table shape: {df.shape}")
            print("First few rows before cleaning:")
            print(df.head(10))
            
            # Clean the data (remove monthly headers)
            df_clean = clean_lottery_data(df)
            
            print(f"\nCleaned table shape: {df_clean.shape}")
            print("First few rows after cleaning:")
            print(df_clean.head(10))
            
            # Drop the 'Draw Number' column
            df_clean = df_clean.drop(columns=['Draw Number'])
            print(f"\nAfter dropping 'Draw Number' column:")
            print(df_clean.head())
            print(f"New shape: {df_clean.shape}")
            
            # Process 'Balls Drawn' column to add commas between numbers
            def format_balls_drawn(balls_str):
                """Format balls drawn string to have commas between numbers"""
                if pd.isna(balls_str):
                    return balls_str
                
                # Split by spaces and filter out empty strings
                numbers = [num.strip() for num in str(balls_str).split() if num.strip()]
                
                # Join with commas
                return ', '.join(numbers)
            
            df_clean['Balls Drawn'] = df_clean['Balls Drawn'].apply(format_balls_drawn)
            
            print(f"\nAfter formatting 'Balls Drawn' with commas:")
            print(df_clean.head())
            
            # Split 'Balls Drawn' column into 7 separate columns
            balls_data = df_clean['Balls Drawn'].apply(split_balls_drawn)
            
            # Create new columns for each number
            for i in range(7):
                df_clean[f'num{i+1}'] = balls_data.apply(lambda x: x[i])
            
            # Drop the original 'Balls Drawn' column
            df_clean = df_clean.drop(columns=['Balls Drawn'])
            
            print(f"\nAfter splitting 'Balls Drawn' into 7 columns:")
            print(df_clean.head())
            print(f"New shape: {df_clean.shape}")
            print(f"New columns: {list(df_clean.columns)}")
            
            # Drop the 'Details' column
            df_clean = df_clean.drop(columns=['Details'])
            
            print(f"\nAfter dropping 'Details' column:")
            print(df_clean.head())
            print(f"New shape: {df_clean.shape}")
            print(f"New columns: {list(df_clean.columns)}")
            
            # Save the final clean data
            output_file = 'lottery_results_2025_final.csv'
            df_clean.to_csv(output_file, index=False)
            print(f"\n✅ Final clean data saved to '{output_file}'")
            
            # Show data types
            print(f"\nData types:")
            print(df_clean.dtypes)
            
            # Show sample of final data
            print(f"\nSample of final clean data:")
            print(df_clean.head(10))
            
            # Show summary statistics
            print(f"\nSummary:")
            print(f"- Total lottery draws: {len(df_clean)}")
            print(f"- Date range: {df_clean['Draw Date'].min()} to {df_clean['Draw Date'].max()}")
            print(f"- Number columns: {[col for col in df_clean.columns if col.startswith('num')]}")
            print(f"- Total columns: {len(df_clean.columns)}")
            
        else:
            print("No tables found in the scraped data")
            
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Make sure you have the required dependencies installed:")
        print("pip install pandas lxml html5lib")

if __name__ == "__main__":
    scrape_lottery_results()
