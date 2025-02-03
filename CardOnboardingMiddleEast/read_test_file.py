from pathlib import Path


def read_file_from_folder_a():
    # Get the path to the current script
    current_script_path = Path(__file__).parent

    # Construct the path to folder_a/test.txt
    test_file_path = current_script_path.parent / "KianDigitalFundsV3Esign" / "identifiers.txt"

    # Ensure the file exists
    if not test_file_path.exists():
        raise FileNotFoundError(f"{test_file_path} does not exist")

    # Read the file content
    with test_file_path.open("r") as file:
        content = file.read()

    return content


# if __name__ == "__main__":
#     content = read_file_from_folder_a()
#     print("File Content:")
#     print(content)
