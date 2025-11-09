import pandas as pd

# Path to your combined file
combined_path = '/Users/jackferrence/Desktop/CombineNFLData/nfl_pbp_2009_2019_combined.csv'

# Load the dataset
df = pd.read_csv(combined_path)

# Filter for only punt plays (case-insensitive to avoid issues)
punts = df[df['play_type'].str.lower() == 'punt']

# Save to a new CSV, or overwrite the old one if you prefer
punts.to_csv('/Users/jackferrence/Desktop/CombineNFLData/nfl_pbp_2009_2019_punts_only.csv', index=False)

print(f"Filtered dataset: {len(punts)} punt plays saved to nfl_pbp_2009_2019_punts_only.csv")
