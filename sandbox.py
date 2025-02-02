import csv
import pandas as pd
import os

input_file_path = r'C:\Users\singh\Desktop\AI\hospitality_content_generation\snapscrape\Snapscrape2\venue_instagram_profiles.csv'
output_file_path = r'C:\Users\singh\Desktop\AI\hospitality_content_generation\snapscrape\Snapscrape2\users_to_scrape'

with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    input_df = pd.read_csv(input_file_path)
    
    # Iterate over every row in the dataframe
    for index, row in input_df.iterrows():
        # If the Instagram column is not 'none', create a new CSV file with the Instagram username as the filename
        if row['Instagram'] != 'none':
            new_df = pd.DataFrame([row], columns=fieldnames)
            new_df.rename(columns={'Instagram': 'account'}, inplace=True)
            current_output_file_path = os.path.join(output_file_path, f'{row["Instagram"]}.csv')
            new_df.to_csv(current_output_file_path, index=False)

"""    # Users that will get requested 
    users_toscrape = [row['Instagram'] for index, row in input_df.iterrows() if row['Instagram'] != 'none']

    for user in users_toscrape:
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'account': user})

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if row['Instagram']:
                row['account'] = row.pop('Instagram')
                writer.writerow(row)"""