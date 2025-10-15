import steuptools

with open("README.md",'r' ,encoding='utf-8') as f :
    long_discription =f.read()

__version__ = "0.0.0"

REPO_NAME= "End-to-End-ML-Project"
AUTHOR_USER_NAME = "shruti0441"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "shrutiadsul04@gmail.com"

steuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    email=AUTHOR_EMAIL,
    decription = "A small python package for  ml app",
    long_discription =long_discription,
    long_discription_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "bug_tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"

    },
    package_dir = {"":"src"},
    packages =steuptools.find_packages(where = 'src')

)