echo [$(date)]: "START"    # here we are using echo to print the message in the terminal data and with start word , so here data is the varaible which i have written by using $ symbol 


echo [$(date)]: "creating env with python 3.8 version"   # here iam trying to print this creating env with python 3.8 version message with data  in the terminal 


conda create --prefix ./venv python=3.8 -y  # here by using this command iam going to create with the name of venv of python 3.8 version inside this end to end Diamond price predicition file


echo [$(date)]: "activating the environment"  # here by using the echo iam prinitng the message which includes data and with activating the environment message 

source activate ./env  # This command helps us to activate the created venv file inside the end to end diamond price prediction folder 

echo [$(date)]: "installing the dev requirements"  # here by using the echo command iam prinitng the message which includes data and with installing the dev requirements message 

pip install -r requirements_dev.txt  # here by this command iam installing the libraries which are necessary  to develop the project

echo [$(date)]: "END"   # after installing the libraries this print message iam going to print  by using echo command