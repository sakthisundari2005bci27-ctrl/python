import os
import shutil

def organize_folder(path):
    # Dictionary to map file extensions to directory names
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.mov'],
        'Archives': ['.zip', '.rar', '.tar']
    }

    for filename in os.listdir(path):
        # Skip directories
        if os.path.isdir(os.path.join(path, filename)):
            continue
            
        file_ext = os.path.splitext(filename)[1].lower()
        
        for folder, exts in extensions.items():
            if file_ext in exts:
                folder_path = os.path.join(path, folder)
                
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Move the file
                shutil.move(os.path.join(path, filename), os.path.join(folder_path, filename))
                print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    # Change '.' to the directory you want to clean up
    target_dir = input("Enter the full path of the folder to organize: ")
    organize_folder(target_dir)
