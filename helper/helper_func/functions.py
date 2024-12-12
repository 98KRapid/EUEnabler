from exploit.restore import restore_files
from pymobiledevice3.exceptions import PyMobileDevice3Exception
from pymobiledevice3.services.diagnostics import DiagnosticsService
from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux

from pathlib import Path
from tempfile import TemporaryDirectory
import traceback
import plistlib
import time

# Function to replace the region code in a plist file
def replace_region_code(plist_path, original_code="US", new_code="US"):
    try:
        # Open and load the plist file
        with open(plist_path, 'rb') as f:
            plist_data = plistlib.load(f)

        # Replace the original region code with the new one
        plist_str = str(plist_data)
        updated_plist_str = plist_str.replace(original_code, new_code)

        # Convert the string back to a dictionary and return the updated plist data
        updated_plist_data = eval(updated_plist_str)  # Caution: eval can be dangerous, ensure data is trusted
        return plistlib.dumps(updated_plist_data)

    except Exception as e:
        print(f"Error updating plist file: {e}")
        raise

# Function to handle file restoration with retries
def restore(files, max_retries=3):
    for attempt in range(max_retries):
        try:
            print(f"Attempting to restore files... (Attempt {attempt + 1}/{max_retries})")
            restore_files(files=files, reboot=True)  # Perform restore and reboot
            print("Restoration successful.")
            break  # Exit the loop on success
        except ConnectionAbortedError:
            print(f"Connection aborted, retrying... ({attempt + 1}/{max_retries})")
            time.sleep(2)  # Pause before retrying
        except PyMobileDevice3Exception as e:
            print(f"Mobile device error: {e}")
            break  # Stop retries on PyMobileDevice3Exception
        except Exception as e:
            print(f"Unexpected error occurred: {traceback.format_exc()}")
            break  # Stop retries on unexpected error

# Function to prompt the user for an action
def prompt_for_action():
    print("Select an option:")
    print("1. Restore files with no data")
    print("2. Apply eligibility and config patches")
    print("3. Restore files with no data and apply patches")
    
    while True:
        try:
            choice = input("Enter your choice (1, 2, or 3): ").strip()
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except Exception as e:
            print(f"Error processing input: {e}")
