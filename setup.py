"""
This is a setup Script that does the following:

1. Get the Name for the project
2. Asks the User for a Port for the Project
3. Creates a virtual environment
4. Installs the requirements
5. Renames all the occurences of the template name to the project name
6. Inserts the Port Numbers for the project
"""

import os
import sys
import shutil
import subprocess
import re
from pathlib import Path

folders_to_rename = [
    "./app/dbi_pyton_service_template",
]

files_with_project_name = [
    "./.github/workflows/createImage.yml",
    "./app/Dockerfile",
]

if __name__ == "__main__":
    print("Hello World")