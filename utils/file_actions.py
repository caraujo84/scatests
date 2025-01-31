import os
from pathlib import Path


class FileActions:
    def __init__(self, driver):
        self.driver = driver

    def new_html_file(self, test_name, file_data):
        current_directory = Path(__file__).parent.parent.resolve()
        file_path = f"{current_directory}\\html_files\\{test_name}.html"
        with open(file_path, "w") as file:
            file.write(file_data)
        return file_path.replace("\\\\", "/")

    def remove_file(self, file_path):
        os.remove(file_path)
