import os
import shutil

# Define your desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print(desktop_path)

# Define the subfolder categories and their associated file extensions
file_categories = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["pdf", "doc", "docx", "txt"],
    "Archives": ["zip", "tar", "gz"]
}

# Create the subfolders if they don't already exist
for category in file_categories:
    category_path = os.path.join(desktop_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Function to move files to the appropriate subfolder
def organize_files():
    for filename in os.listdir(desktop_path):
        # Skip directories
        if os.path.isdir(os.path.join(desktop_path, filename)):
            continue
        
        # Get the file extension
        file_extension = filename.split(".")[-1].lower()
        
        # Determine the category based on file extension
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                # Move the file to the corresponding category folder
                source = os.path.join(desktop_path, filename)
                destination = os.path.join(desktop_path, category, filename)
                shutil.move(source, destination)
                print(f"Moved: {filename} to {category} folder")
                break

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully.")
