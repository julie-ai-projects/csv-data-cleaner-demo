import pandas as pd

def clean_csv(input_file, output_file):
    # Load data
    df = pd.read_csv(input_file)
    print("Original data loaded. Rows:", len(df))

    # Drop duplicates
    df = df.drop_duplicates()
    print("Removed duplicates. Rows left:", len(df))

    # Drop empty rows
    df = df.dropna(how='all')
    print("Removed empty rows. Rows left:", len(df))

    # Strip whitespace from string columns
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Convert columns with 'date' in name to datetime
    for col in df.columns:
        if 'date' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col])
                print(f"Formatted date column: {col}")
            except Exception:
                pass

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")


if __name__ == "__main__":
    clean_csv('dirty_data.csv', 'clean_data.csv')
