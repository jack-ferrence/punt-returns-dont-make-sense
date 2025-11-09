import pandas as pd
import os

# Set the path to your folder on Desktop
folder_path = '/Users/jackferrence/Desktop/CombineNFLData'

# Create lists to store DataFrames in the correct order
all_dfs = []

# Loop through years from 2009 to 2019
for year in range(2009, 2020):
    # First add regular season file
    reg_file = os.path.join(folder_path, f'reg_pbp_{year}.csv')
    try:
        reg_df = pd.read_csv(reg_file)
        all_dfs.append(reg_df)
        print(f"✓ Loaded reg_pbp_{year}.csv - {len(reg_df)} rows")
    except FileNotFoundError:
        print(f"✗ reg_pbp_{year}.csv not found")
    
    # Then add postseason file
    post_file = os.path.join(folder_path, f'post_pbp_{year}.csv')
    try:
        post_df = pd.read_csv(post_file)
        all_dfs.append(post_df)
        print(f"✓ Loaded post_pbp_{year}.csv - {len(post_df)} rows")
    except FileNotFoundError:
        print(f"✗ post_pbp_{year}.csv not found")

# Combine all DataFrames vertically
if all_dfs:
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save to the same folder
    output_file = os.path.join(folder_path, 'nfl_pbp_2009_2019_combined.csv')
    combined_df.to_csv(output_file, index=False)
    
    print(f"\n{'='*50}")
    print(f"✓ Successfully combined all files!")
    print(f"Total rows in combined dataset: {len(combined_df)}")
    print(f"Total columns: {len(combined_df.columns)}")
    print(f"Saved as: nfl_pbp_2009_2019_combined.csv")
    print(f"Location: {folder_path}")
    print(f"{'='*50}")
else:
    print("No files were loaded. Please check your file names and location.")
