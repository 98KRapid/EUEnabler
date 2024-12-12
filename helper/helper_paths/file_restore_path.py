from exploit.restore import restore_files, FileToRestore, restore_file
from . import eligibility_path  # Ensure eligibility_path is properly imported

# Files with empty contents to be restored
files_to_restore_empty = [
    FileToRestore(
        contents=b'',  # Empty file content
        restore_path="/var/db/os_eligibility/",
        restore_name="eligibility.plist"
    ),
    FileToRestore(
        contents=b'',  # Empty file content
        restore_path="/var/MobileAsset/AssetsV2/com_apple_MobileAsset_OSEligibility/purpose_auto/c55a421c053e10233e5bfc15c42fa6230e5639a9.asset/AssetData/",
        restore_name="Config.plist"
    ),
]

# Files with patched data to be restored
files_to_restore_patches = [
    FileToRestore(
        contents=eligibility_path.eligibility_data,  # Assuming eligibility_data is loaded correctly
        restore_path="/var/db/os_eligibility/",
        restore_name="eligibility.plist"
    ),
    FileToRestore(
        contents=eligibility_path.config_data,  # Assuming config_data is loaded correctly
        restore_path="/var/MobileAsset/AssetsV2/com_apple_MobileAsset_OSEligibility/purpose_auto/c55a421c053e10233e5bfc15c42fa6230e5639a9.asset/AssetData/",
        restore_name="Config.plist"
    ),
]
