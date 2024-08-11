from setuptools import find_packages,setup

from typing import List

HYPHEN_E_dot = '-e.'
def get_packages(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_dot in requirements:
        requirements.remove(HYPHEN_E_dot)

    return  requirements 

setup( name='mlproject', version='0.0.1', author='Shrihari', packages=find_packages(), install_requires=get_packages('requirements.txt') )