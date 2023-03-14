from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

#  this is for pickup the libraries whenwe call 
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #  for removing the /n with every object 
        requirements=[req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
name='ML_PROJECT',
version='0.0.1',
author='Minal',
author_email='minalv270027@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
# // instead of writing this  we create funtion 
install_requires=get_requirements('requirements.txt')

)