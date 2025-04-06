from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str)->List[str]:
    '''
    This function will return the list of requiremnts 

    input: file_path (str): requirements.txt file
    output: requirements 
    '''
    with open(file_path) as f:
        requirements = f.readline()
        requirements = [requiremnt.replace("\n", "") for requiremnt in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="UniBro",
    version="0.0.1",
    author="Rahul George",
    author_email="rahulgeorge1212@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("./requirements.txt"),
)
