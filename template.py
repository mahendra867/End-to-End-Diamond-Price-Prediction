import os  # by importing the os which helps us to intertact with the OS 
from pathlib import Path # In the given code, the line from pathlib import path imports the path class from the pathlib module. This class handles system paths and allows you to perform operations such as joining paths, resolving relative paths, and checking file existence.and it handles the system paths even if we run those system path in Linux terimnal which is vscode terminal this path class takecares the system path without throwing errors because system file path present in backward slash \ and linux system file path present in forward slash /

# Now iam going to create a list of file and folder  in workspace which are going to useful for developing our whole project

list_of_files=[ # below iam going to create different path which consist of directory+file, so path=dir+file with extension

    ".github/workflows/.gitkeep", # here iam creating a file named as .github and inside iam creating workflows file and created one .gitkeep file inside the .github folder because by wrtitng this.gitkeep file we can able to push the folder to github even the folder is empty and Git doesn't track empty directories by default. It might seem logical, why waste storage space on something with nothing in it? But sometimes, empty directories are important. They might serve as placeholders for future files, organize the codebase, or be part of build processes.
    "src/__init__.py", # Now iam going to create a SRC folder which conatins some files those file contains our whole project source code , so thatsy iam writing the source code inside SRC folder and other than sorce code whatever other infrastructure is there iam keeping outside  the SRC folder, so SRC just represinting the Source code of our project , and here i have created file named as __init__.py which is a constructer file
    "src/components/__init__.py" ,# And components file contains some file which are our ML stages like from EDA to Model evaluation so these seperate stages acts as components and pipeline means collection of mulitple components so these collection of multiple components acts as Training pipeline, so in ML we have 2 pipeline 1st is Training Pipeline and 2nd one is Prediction Piepline
    "src/components/data_ingestion.py", 
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_piepline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py", # till here i have created 3 folders inside the src folder which are components,pipeline,utils
    "src/logger/logger.py", # basically we can create a __init__.py file inside the logger.py and exception.py , even if we dont create our root __init__.py which is present just below the Src folder that take cares of this without throwing error whenever we are going to import that root __init__.py even if we dont mention __init__.py file inside the logger and exception
    "src/exception/exception.py",
    "tests/unit/__inti__.py", # now iam going to create a file named as test which we can test our different different testcases ,actually that iam going to mention inside my code itself, so there are 2 types of testing one is Unit testing and 2nd is integrating testing so both we are going to do regrading different different test cases , so basically unit testing means we test for the individual components and integrated testing means we are going to test the all components, os we use integrating testing if we want to test our enitre components in single go, so 1st file iam going to create inside test is __inti__.py
    "tests/integration/__inti__.py" ,
    "init_setup.sh", # now iam going to created a file named as init_setup.sh here sh means shell scrip
    "requirements.txt",
    "requirements_dev.txt",# here iam going to create 1 more requirements file which is requirements_dev.txt so basically this file for development environment only, so if we want to deploy this code or productioniz this code so for the production all the requirements will be available inside this requirments_dev.txt, so whenever  i want to install requirement related to development iam going to run this file 
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"



]


# here iam writing a code which can able to create a files and folder lets consider this path=directory+file "src/components/data_ingestion.py" here files without extension are consider as directory example "src/components"  and file with extension are consider as an filename which is "data_ingestion.py"

for filepath in list_of_files: # here iam by using for loop iam interating over the every individual list_of_files 
    filepath=Path(filepath) # here 1st it selects the 1st file which acts as path which is github/workflows/.gitkeep
    filedir,filename=os.path.split(filepath)  # here iam going to split the selected 1st file (path) of list of files and iam going to split the path which consist of path+folder and iam saving it in filedir,filename for example a/b/c.txt here a/b is the path of the folder and c.txt is the file so iam going to split the path and file and saving it in respective firdir,filename
    if filedir!="": # here iam using the file condition to making the directory of the first list of directory+file and iam taking only the directory of the 1st file which is present in filedir and given condtion like by using if, if the taken directory is not exist in os then and by using os iam going to make dir of the selected 1st file directory 
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # Condition 1: not os.path.exists(filepath): This verifies if the file specified by filepath doesn't exist yet. Condition 2: os.path.getsize(filepath)==0: This checks if the file exists but is empty (has zero size). If either of these conditions is true, the code proceeds to create or open the file. or if the above condition that creating a directory is already exist then we check the directory folder size if it is equal to 0 then its going to open those folders 
        with open(filepath,"w") as f: # . File Creation or Opening: with open(filepath, "w") as f: This line uses a with statement to open the file in write mode ("w"): If the file doesn't exist, this action creates it. If the file exists but is empty, it's opened for writing. The as f: part assigns the opened file object to the variable f, allowing you to work with it within the with block.
            pass  # pass: This keyword doesn't perform any specific action. It's often used as a placeholder when you need a statement but don't have any code to execute yet.