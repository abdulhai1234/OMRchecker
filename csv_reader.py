import pandas as pd
import glob
import os

csv_files = glob.glob(r"D:\Projects\Sir Mansoor\OMRChecker\outputs\**\**\*.csv")
print(glob.glob(r"D:\Projects\Sir Mansoor\OMRChecker\outputs\**\**\*.csv"))

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through all files in the directory
for file_path in csv_files:
    filename = file_path.split("\\")[-1]
    if filename.startswith("Results") and filename.endswith(".csv"):
        # Load each CSV file into a DataFrame
        # file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)
        
        # Append the data to the combined DataFrame
        combined_data = combined_data.append(df, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_data.to_csv(os.path.join("outputs","Results.csv"), index=False)