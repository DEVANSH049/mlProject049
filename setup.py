from setuptools import find_packages, setup
from typing import List

HYPEB_E_DOT = '-e .'

def get_requirements(fil_path:str)->List[str]:
    '''
    Function to read the requirements.txt file'''
    requirements=[]
    with open(fil_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]

        if HYPEB_E_DOT in requirements:
            requirements.remove(HYPEB_E_DOT)
    return requirements





setup(
    name='Mlproject',
    version='0.0.1',
    author='devansh049',
    author_email='devanshgupta049@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas', 'numpy', 'seaborn'],
    install_requires=get_requirements('requirements.txt')
)