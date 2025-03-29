import os
import shutil
import tempfile
import platform
import subprocess

def delete_temp_files():
    """Delete temporary files from the system's temp directories."""
    temp_dirs = [tempfile.gettempdir()]

    # Add more temp directories based on the OS
    if platform.system() == "Windows":
        temp_dirs.append(os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp'))
    elif platform.system() == "Linux":
        temp_dirs.append('/tmp')
    elif platform.system() == "Darwin":  # macOS
        temp_dirs.append('/tmp')

    for temp_dir in temp_dirs:
        try:
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print(f"Deleted file: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted directory: {file_path}")
        except Exception as e:
            print(f"Error deleting files in {temp_dir}: {e}")

def clear_recycle_bin():
    """Clear the recycle bin or trash based on the OS."""
    if platform.system() == "Windows":
        try:
            subprocess.run(['PowerShell', '-Command', 'Clear-RecycleBin -Confirm:$false'], check=True)
            print("Recycle bin cleared.")
        except Exception as e:
            print(f"Error clearing recycle bin: {e}")
    elif platform.system() == "Linux":
        try:
            # Clear trash for Linux (using xdg-trash)
            subprocess.run(['gio', 'trash', '--empty'], check=True)
            print("Trash cleared on Linux.")
        except Exception as e:
            print(f"Error clearing trash on Linux: {e}")
    elif platform.system() == "Darwin":  # macOS
        try:
            subprocess.run(['osascript', '-e', 'tell application "Finder" to empty trash'], check=True)
            print("Trash cleared on macOS.")
        except Exception as e:
            print(f"Error clearing trash on macOS: {e}")

def optimize_storage():
    """Placeholder for storage optimization tasks."""
    if platform.system() == "Windows":
        try:
            subprocess.run(['defrag', '/C', '/O'], check=True)
            print("Storage optimized on Windows.")
        except Exception as e:
            print(f"Error optimizing storage on Windows: {e}")
    elif platform.system() == "Linux":
        print("Consider using 'fstrim' for SSDs or 'e4defrag' for ext4 filesystems.")
    elif platform.system() == "Darwin":  # macOS
        print("macOS automatically manages storage optimization.")

def main():
    print("Starting maintenance tasks...")
    delete_temp_files()
    clear_recycle_bin()
    optimize_storage()
    print("Maintenance tasks completed.")

if __name__ == "__main__":
    main()
