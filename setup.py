from setuptools import setup,find_packages

def read_lines(file_path):
    """
        it reads a requirements.txt file and take librarys and conver it into list
    """
    with open(file_path,'r') as f:
        return f.read().splitlines()
    
setup(
    name="Intrusion Detection System",
    version='0.0.3',
    author="Jay Narigara",
    author_email="jaynarigara@gmail.com",
    packages=find_packages(),
    install_requires=read_lines('requirements.txt')
)


# Run: python setup.py install