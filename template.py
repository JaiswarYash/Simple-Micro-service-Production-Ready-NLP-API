import logging
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "app"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/mian.py",
    f"{project_name}/model.py",
    f"{project_name}/schemas.py",
    f"{project_name}/core/__init__.py",
    f"{project_name}/core/config.py",
    "tests/__init__.py",
    "tests/test_api.py",
    "tests/test_model.py",
    "model_cache/",
    ".dockerignore",
    "Dockerfile",
    "requirements.txt", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if not exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # Create empty file if not exists OR file is empty
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")