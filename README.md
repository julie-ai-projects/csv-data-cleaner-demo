![CSV Data Cleaner Banner](https://raw.githubusercontent.com/julie-ai-projects/csv-data-cleaner-demo/main/banner.png)

# CSV Data Cleaner (Demo)

A Python automation script that cleans messy CSV files by removing duplicates, empty rows, and formatting inconsistent data.

## Features
- Removes duplicate rows
- Deletes completely empty rows
- Strips extra spaces
- Converts date columns to standard datetime format
- Saves cleaned data as `clean_data.csv`

## How to Run
```bash
python main.py
```

## Example Output
```
Original data loaded. Rows: 6
Removed duplicates. Rows left: 5
Removed empty rows. Rows left: 4
Formatted date column: join_date
✅ Cleaned data saved to clean_data.csv
```
