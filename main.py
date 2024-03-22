import os
import shutil
import time

def copy_ppt_from_pendrive(src_pendrive_path, dest_folder):
    # Check if the source pendrive path exists
    if os.path.exists(src_pendrive_path):
        # List all files in the pendrive
        pendrive_files = os.listdir(src_pendrive_path)
        # Look for .ppt files
        ppt_files = [file for file in pendrive_files if file.endswith('.ppt')]
        # Copy .ppt files to destination folder
        for ppt_file in ppt_files:
            src_file = os.path.join(src_pendrive_path, ppt_file)
            dest_file = os.path.join(dest_folder, ppt_file)
            shutil.copy(src_file, dest_file)
            print(f"File '{ppt_file}' copied to '{dest_folder}'")

# Example usage
src_pendrive_path = "H:\\"
dest_folder = "D:\\"  # Change this to your desired destination folder
    
while True:
    # Check for pendrive insertion
    drives = [drive for drive in os.listdir('H:\\') if os.path.isdir(os.path.join('H:\\', drive))]
    if len(drives) > 0:
        print("Pendrive detected.")
        copy_ppt_from_pendrive(src_pendrive_path, dest_folder)
        break
    else:
        print("Waiting for pendrive insertion...")
        time.sleep(5)  # Check every 5 seconds
