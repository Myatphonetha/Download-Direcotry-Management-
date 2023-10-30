
import os  # library for handling operation system environment
import shutil  # library for file handling

download_folder = 'C:\\Users\\Myat\\Desktop\\Download'# directory of user choice 

# Directory for file types where key represents file type and value represents file directory
folders = {
    'Images': 'C:\\Users\\Myat\\Desktop\\Download\\Images',
    'Documents': 'C:\\Users\\Myat\\Desktop\\Download\\Documents',
    'Code': 'C:\\Users\\Myat\\Desktop\\Download\\Code',
    'Music': 'C:\\Users\\Myat\\Desktop\\Download\\Music',
    'Videos': 'C:\\Users\\Myat\\Desktop\\Download\\Videos',
    'Archives': 'C:\\Users\\Myat\\Desktop\\Download\\Archives',
    'Executables': 'C:\\Users\\Myat\\Desktop\\Download\\Executables',
    'Others': 'C:\\Users\\Myat\\Desktop\\Download\\Others',
}

# Create the destination folders if they don't exist
for folder in folders.values():
    os.makedirs(folder, exist_ok=True)  # error handling if the folder exists

# List files in the download folder
for filename in os.listdir(download_folder):
    src_path = os.path.join(download_folder, filename)  #

    if os.path.isfile(src_path):  # checking if the file is a file not directory

        # Base name is ignored  -, and get the file extension such as .py , .jpg, .png
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Determine the destination folder
        if ext in ('.jpg', '.jpeg', '.png', '.gif'):
            dest_folder = folders['Images']
        elif ext in ('.pdf', '.doc', '.docx', '.txt'):
            dest_folder = folders['Documents']
        elif ext in ('.py', '.java', '.c', '.cpp', '.h', '.hpp', '.html', '.css', '.js', '.php'):
            dest_folder = folders['Code']
        elif ext in ('.mp3', '.wav', '.flac'):
            dest_folder = folders['Music']
        elif ext in ('.mp4', '.mov', '.avi', '.mkv'):
            dest_folder = folders['Videos']
        elif ext in ('.zip', '.rar', '.7z'):
            dest_folder = folders['Archives']
        elif ext in ('.exe', '.msi'):
            dest_folder = folders['Executables']
        elif os.path.isdir(src_path):  # check if it is a directory
            dest_folder = folders['Files']
        else:
            dest_folder = folders['Others']

        dest_path = os.path.join(dest_folder, filename)

        # Move the file to the appropriate folder
        shutil.move(src_path, dest_path)
        print(f"Moved {filename} to {dest_folder}")

print("Organizing complete.")

