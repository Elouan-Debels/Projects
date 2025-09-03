import os
import time

# Function to create folders
def create_folders():
    for i in range(20):
        folder_name = f'saved_stories-{int(time.time()) + i * 60}'  # Incrementing by 60 seconds (1 minute)
        folder_path = os.path.join("C:/Users/eloua/Desktop/advanced business amalytics and big data platforms/groepswerk/assignment 3/data", 'output', folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f'Created folder: {folder_name}')

# Create 20 folders in the "output" directory
create_folders()
