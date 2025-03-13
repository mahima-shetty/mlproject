from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str) -> List[str]:
    '''
    This funtion will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]  # Remove empty lines & whitespace

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


    return requirements

setup(

    name='mlproject',
    version='0.0.1',
    description='Basic End to End Implementation for Machine learning project' ,
    author='Mahima Shetty',
    author_email='msshetty237@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)