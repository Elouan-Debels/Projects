import os
import time
import glob
import requests

# Function to find the most recent folder
def find_most_recent_folder():
    folders = glob.glob('saved_stories-*')
    if folders:
        most_recent_folder = max(folders, key=os.path.getctime)
        return most_recent_folder
    else:
        return None

# Function to fetch new stories IDs
def fetch_new_stories():
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch new stories. Status code:', response.status_code)
        return []

# Function to save new stories IDs to a file
def save_stories_to_file(folder_path, stories):
    filename = os.path.join(folder_path, 'stories.txt')
    with open(filename, 'w') as file:
        for story_id in stories:
            file.write(str(story_id) + '\n')
    print(f'Saved {len(stories)} new stories to {filename}')

# Main loop
def main():
    while True:
        # Find the most recent folder
        recent_folder = find_most_recent_folder()
        
        if recent_folder is not None:
            folder_path = os.path.join(os.getcwd(), recent_folder)
        else:
            folder_name = f'saved_stories-{int(time.time())}'
            folder_path = os.path.join(os.getcwd(), folder_name)
            os.makedirs(folder_path, exist_ok=True)
        
        # Fetch new stories
        new_stories = fetch_new_stories()
        
        # Save new stories to file
        save_stories_to_file(folder_path, new_stories)
        
        # Wait for 2 minutes before fetching again
        time.sleep(120)

if __name__ == '__main__':
    main()
