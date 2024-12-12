from pathlib import Path

# Function to read plist files safely
def read_plist(file_name):
    file_path = Path.joinpath(Path.cwd(), file_name)
    if file_path.exists() and file_path.is_file():
        with open(file_path, 'rb') as file:
            return file.read()
    else:
        raise FileNotFoundError(f"The file '{file_name}' does not exist at {file_path}")

# Read the eligibility plist file
try:
    eligibility_data = read_plist('eligibility.plist')
    print(f"Successfully read 'eligibility.plist'")
except FileNotFoundError as e:
    print(e)

# Read the config plist file
try:
    config_data = read_plist('Config.plist')
    print(f"Successfully read 'Config.plist'")
except FileNotFoundError as e:
    print(e)
