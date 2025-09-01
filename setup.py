import setuptools

def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        
        requirements = [
            req.strip()
            for req in requirements
            if req.strip() and req.strip() != '-e .'
        ]
    return requirements

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Text-Summarizer-NLP-Project'
AUTHOR_USER_NAME = 'zishan044'
SRC_REPO = 'text_summarizer'
AUTHOR_EMAIL = 'winchesterfelix007@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Simple text summarizer NLP app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
