import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: [%(message)s]',
)

project_name = "text_summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    ".gitignore",
    "README.md"
]

for filepath in list_of_files:
    path = Path(filepath)
    if path.parent != Path(""):
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"📁 Directory ensured: {path.parent}")
    
    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"📄 Created file: {path}")
    else:
        logging.info(f"✔️ File already exists: {path}")
