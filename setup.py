from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

get_requirements('./requirements_dev.txt')



setup(  # here inisde by this package version number my package which is DimondPricePrediction going to install in the virtual environment which is python 3.9.17 , so the moment we install the required dependiencies which i mention in the requirements_dev.txt file by just typing this command pip install -r requirements_dev.txt when the virtual environment is active , then by this packge name DimondPricePredictio with mention version name in this setup fucntion by this details my packge going to install in the virtual environment , we can check that by using command pip list by this we can get to know wether mentioned dependiencies are all got installed inside my created virtual environment or not , if install then only we can develop our diamond price prediction application by using the dependencies which i have mention in the requirement_dev.txt file
    name='DimondPricePrediction',
    version='0.0.1',
    author='mahendramahi',
    author_email='mahendramahesh2001@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)

