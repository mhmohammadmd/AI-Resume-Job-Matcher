def read_text_file(file_path):
    """Read text file and return as string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
