import os
import shutil

# Define the path to the media folder
media_path = r"D:\Media\Music"

# Function to get the band name from the file or folder name
def extract_band_name(name):
    if " - " in name:
        return name.split(" - ")[0].strip()
    return None

# Iterate over each item in the directory
for item in os.listdir(media_path):
    item_path = os.path.join(media_path, item)
    
    # Only process files or directories that have the " - " pattern
    if " - " in item:
        # Extract band name
        band_name = extract_band_name(item)
        
        # Create new directory for the band if it doesn't exist
        band_folder = os.path.join(media_path, band_name)
        if not os.path.exists(band_folder):
            os.makedirs(band_folder)
        
        # Move the item into the respective band folder
        shutil.move(item_path, os.path.join(band_folder, item))

print("Media organisation complete.")
