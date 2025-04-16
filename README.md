# Workshop Mods Content Copier

This Python script is designed to copy the contents of the `mods` folder from various Steam Workshop content subdirectories **and potentially local mod directories** to a specified destination folder. This can be useful for consolidating mods from different sources into a single location for easier management and use with your game.

## Prerequisites

* **Python 3** installed on your system.

## Usage

1.  **Save the script:** Save the provided Python code as a `.py` file (e.g., `copy_workshop_mods.py`).

2.  **Modify the paths:** Open the script in a text editor and locate the following lines at the end of the file:

    ```python
    workshop_path = r"G:\SteamLibrary\steamapps\workshop\content\108600"  # Replace with the actual path to the folder containing 'mods'
    target_destination = r"C:\Users\louiz\source\repos\PZ py\mods"  # Replace with your desired destination
    ```

    * Replace the value of `workshop_path` with the actual path to your Steam Workshop content folder. The example path `G:\SteamLibrary\steamapps\workshop\content\108600` is a common location for Project Zomboid mods, but you should adjust it based on the game you are working with. The script will look for subdirectories within this path, assuming each subdirectory represents a workshop item ID.
    * Replace the value of `target_destination` with the path to the folder where you want to copy the contents of the `mods` folders. This is typically your game's local mods directory.

3.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the Python script, and run it using the command:

    ```bash
    python copy_workshop_mods.py
    ```

4.  **Monitor the output:** The script will print messages to the console indicating which workshop IDs are being processed and which files or folders are being copied. It will also report any errors encountered during the process.

## Script Explanation

The script performs the following steps:

1.  **Defines a function `copy_mods_contents`:** This function takes two arguments:
    * `workshop_content_path`: The path to the main workshop content folder.
    * `destination_path`: The path where the mod contents will be copied (typically your local mods directory).

2.  **Checks for the existence of the workshop content path:** It verifies if the provided `workshop_content_path` exists and is a directory. If not, it prints an error message and exits.

3.  **Identifies workshop ID subfolders:** It lists all the subdirectories within the `workshop_content_path`, assuming each subdirectory represents a workshop item ID.

4.  **Iterates through each workshop ID:** For each workshop ID subdirectory:
    * It constructs the path to the `mods` folder within that workshop ID.
    * It checks if the `mods` folder exists and is a directory.
    * If the `mods` folder exists, it iterates through its contents (files and subfolders).
    * For each item in the `mods` folder:
        * It constructs the source path and the destination path.
        * If the item is a directory, it uses `shutil.copytree` to recursively copy the entire directory and its contents to the destination. The `dirs_exist_ok=True` argument ensures that if a directory with the same name already exists in the destination, the contents will be merged.
        * If the item is a file, it uses `shutil.copy2` to copy the file to the destination, preserving the metadata (like timestamps).
        * It prints messages indicating whether a file or folder was copied or if an error occurred.
    * If no `mods` folder is found within a workshop ID, it prints a corresponding message.

5.  **Example Usage:** The script includes example values for `workshop_path` and `target_destination` that you need to replace with your actual paths. The `target_destination` should be the path to your game's local mods directory where you want the workshop mods to be copied. It then calls the `copy_mods_contents` function with these paths to execute the copying process.

## Important Notes

* **Local Mods:** This script, as currently written, focuses on copying from the Steam Workshop content. If you have local mods in a separate directory that you also want to include, you would need to modify the script to handle those directories as well. This might involve adding a new function or extending the existing one to take multiple source paths.
* **Existing Files/Folders:** If a file or folder with the same name already exists in the `target_destination`, the script's behavior will be as follows:
    * **Files:** Existing files will be overwritten by the files being copied.
    * **Folders:** If a folder with the same name exists, the contents of the source folder will be merged into the existing destination folder.
* **Error Handling:** The script includes basic error handling within the copying loop. If an exception occurs during the copying of a specific file or folder, it will print an error message and continue processing other items.
* **Permissions:** Ensure that the script has the necessary read and write permissions for the source and destination directories.
* **Large Number of Files:** If you have a very large number of mods, the script might take some time to complete.
* **Game Specifics:** The structure of the workshop content folder might vary slightly depending on the game. This script assumes a common structure where mods are located within a "mods" folder inside each workshop item ID directory. Adjust the script if your game uses a different structure.
