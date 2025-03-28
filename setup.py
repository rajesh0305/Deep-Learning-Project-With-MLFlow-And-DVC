import setuptools

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Metadata for the package
REPO_NAME = "Deep-Learning-Project-With-MLFlow-And-DVC"
AUTHOR_USER_NAME = "Rajesh_Kumar"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "rajesh8368568776@gmail.com"

# Setup function to define the package details
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN APP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)

# Usage:
# To build the package, run: python setup.py sdist bdist_wheel
# To install the package locally, run: pip install dist/cnnClassifier-0.0.0-py3-none-any.whl