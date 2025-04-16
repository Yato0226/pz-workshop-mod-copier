import os
import shutil

def copy_mods_contents(workshop_content_path, destination_path):
    """
    Copies the contents of the 'mods' folder found within each workshop ID
    subfolder to the destination path.

    Args:
        workshop_content_path (str): The path to the workshop content folder
                                      (e.g., G:\SteamLibrary\steamapps\workshop\content\108600).
        destination_path (str): The path where the contents of the 'mods'
                                folder should be copied.
    """
    if not os.path.exists(workshop_content_path) or not os.path.isdir(workshop_content_path):
        print(f"Error: Workshop content path '{workshop_content_path}' not found.")
        return

    workshop_ids = [d for d in os.listdir(workshop_content_path) if os.path.isdir(os.path.join(workshop_content_path, d))]

    for workshop_id in workshop_ids:
        mods_folder_path = os.path.join(workshop_content_path, workshop_id, "mods")

        if os.path.exists(mods_folder_path) and os.path.isdir(mods_folder_path):
            print(f"Processing workshop ID: {workshop_id}")
            for item in os.listdir(mods_folder_path):
                source_item_path = os.path.join(mods_folder_path, item)
                destination_item_path = os.path.join(destination_path, item)

                try:
                    if os.path.isdir(source_item_path):
                        shutil.copytree(source_item_path, destination_item_path, dirs_exist_ok=True)
                        print(f"  Copied folder: {item}")
                    else:
                        shutil.copy2(source_item_path, destination_item_path)  # copy2 preserves metadata
                        print(f"  Copied file: {item}")
                except Exception as e:
                    print(f"  Error copying '{item}': {e}")
        else:
            print(f"  No 'mods' folder found in workshop ID: {workshop_id}")

# Example usage:
workshop_path = r"G:\SteamLibrary\steamapps\workshop\content\108600"  # Replace with the actual path to the folder containing 'mods'
target_destination = r"C:\Users\louiz\source\repos\PZ py\mods"  # Replace with your desired destination

copy_mods_contents(workshop_path, target_destination)
