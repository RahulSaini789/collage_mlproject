from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path : str)->List[str]:
    '''
    this function will return a list of requirements
    '''

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

    return requirements

setup(
name='MLproject',
version='0.0.1',
author='Rahul Saini',
autho_email='rs5778882@gmail.com',
packeges=find_packages(),
install_requires=get_requirements('requirements.txt')
)


