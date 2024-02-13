# Experimenting the Usage of MLFLOW , so here in this file i have written the basic calculator for perfoming the arthmetic operations , so now lets open the terminal and type command python give the path of this mlflow_experment.py file path , and then press enter so by just changing the parameter of operation for the calculator fucntion like add,subtraction,multiplication,division we are getting the result of that specifci operation
import mlflow

def calculator(a,b,operation=None):
    if operation=="add":
        return (a+b)
    
    if operation=="Subtraction":
        return (a-b)
    
    if operation=="Multiplication":
        return (a*b)
    
    if operation=="Division":
        return (a/b)
    

if __name__=="__main__":

    a,b,opt=1102,12212,"Subtraction"  # suppose if we change the parameters to subtraction and if we run this calculator code, my mlflow creates the another log file which has the experiment of this specific code execution with this subtraction parameter
    with mlflow.start_run(): # First I need to start the MLflow server in order to integrate the mlflow services inside my calcualator code, so there code to start the mlflow server so this the code  with mlflow.start_run()  to start the mlflow server, so when start the mlflow server we get one folder name which is 0 and which gets created inside the mlruns , so the moment we run this calculator code which consist of integration of mlflow this mlruns folder gets created under the file of mlflow_experiments.py file, this file name 0 contains the experiments or no of execution times of our calculator code
        result=calculator(a,b,opt)
        # now iam going to log the parameters of this calculator code , so here by using the log_param fucntion i can able to send the parameters of my calculator code 
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("opt",opt)
        print(f"My result is {result}")
        mlflow.log_param("result",result)
        