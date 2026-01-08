#data transform code in pandas
import pandas as pd
def transform_data(input_file, output_file):
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Example transformation: Remove rows with any missing values
    df_cleaned = df.dropna()
    
    # Example transformation: Convert all column names to lowercase
    df_cleaned.columns = [col.lower() for col in df_cleaned.columns]
    
    # Example transformation: Add a new column that is the sum of two existing columns (if they exist)
    if 'column1' in df_cleaned.columns and 'column2' in df_cleaned.columns:
        df_cleaned['sum_column'] = df_cleaned['column1'] + df_cleaned['column2']
    
    # Write the transformed data to the output CSV file
    df_cleaned.to_csv(output_file, index=False)