import pandas as pd

def convert_json_to_csv(json_file, csv_file):
    try:
        df = pd.read_json(json_file)
        df.to_csv(csv_file, index=False)
        print(f"Success! Saved as {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

# Example: convert_json_to_csv('data.json', 'data.csv')
