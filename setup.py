from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' 

def get_requirements(file_path: str) -> List[str]:
    """ 
    This function will return the list of requirements
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name = 'ml project',
version = '0.0.1',
author= 'Sultan',
author_email= 'sultanrajwan@gmail.com',
packages=find_packages(),
# install_requires=['numpy','pandas','matplotlib','seaborn']
install_requires = get_requirements('requirements.txt')

)


# python setup.py install -> runing the setup file
# -e . -> this will install the package in editable mode if we type pip install requirements.txt