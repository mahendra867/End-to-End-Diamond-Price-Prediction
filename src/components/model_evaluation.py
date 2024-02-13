import os
import sys
import mlflow
import mlflow.sklearn
import numpy as np
from src.utils.utils import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from src.logger.logger import logging
from src.exception. exception import customexception

class ModelEvaluation:
    def __init__(self):
        logging.info("evaluation started")

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))# here is RMSE
        mae = mean_absolute_error(actual, pred)# here is MAE
        r2 = r2_score(actual, pred)# here is r3 value
        logging.info("evaluation metrics captured")
        return rmse, mae, r2

    def initiate_model_evaluation(self,train_array,test_array):
        try:
             X_test,y_test=(test_array[:,:-1], test_array[:,-1])

             model_path=os.path.join("artifacts","model.pkl")  # here iam loading the model from the artifacts folder so then only we can able to evaluate model performance by MLFLOW UI 
             model=load_object(model_path) # here iam loading the model by using the load_object function which i written this fucntionality in utils.py file 

             # mlflow.set_registry_uri("") # here i do mention my URI of cloud server where i want to save my model or where i want to register my model  that path i need to mention here and model registry or model saving is done and register my model inside the cloud location ,where in this case i dont get file here then i cloud not able to save inside the tracking_url_type_store variable as soon as i call the model registry with schema   , so as for now for this project iam not going to save or push my model in cloud server by using s3 bucket like that , thatsy i made this line comment 
             
             logging.info("model has register")

             tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme  # here for this project iam going to save my model or push my model or log the model inside the Dagshub , so iam going to log my model in the local only be registring the model inside the dagshub 

             print(tracking_url_type_store)  # here iam going to set the registry where iam going to save my model



             with mlflow.start_run(): # First I need to start the MLflow server in order to integrate the mlflow services inside my calcualator code, so there code to start the mlflow server so this the code  with mlflow.start_run()  to start the mlflow server, so when start the mlflow server we get one folder name which is 0 and which gets created inside the mlruns , so the moment we run this calculator code which consist of integration of mlflow this mlruns folder gets created under the file of mlflow_experiments.py file, this file name 0 contains the experiments or no of execution times of our calculator code

                prediction=model.predict(X_test)  # here i have passed the x_test value which is used to predict the value by model and iam saving it in predicition variable

                (rmse,mae,r2)=self.eval_metrics(y_test,prediction)  # here iam going to evaluate the model performance by passing the (real value , predicted value), and now iam going to collect the value in the varaibles rmse,mae,r2

                # here iam creating the log all values in order to show the values with name of parameters in MLFLOW URI
                mlflow.log_metric("rmse", rmse)  # so here iam using the log_parameters , And mlflow supports different different frameworks like log_params, log_artifacts,log_metrics,and log_pytorch,log_sagemaker and soon etc
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)

                 # Here iam giving the condition to Model registry does not work with file store , like 
                if tracking_url_type_store != "file":  # so while setting the modelregistry uri , suppose if i register my model or save my model  inside the cloud then i wont get file then this if conditon gets satisfied , and suppose if i registry my model or saves my model  inside the Dagshub i will get the log model file and then else statement gets executed 

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")  # and here iam performing log model or capturing the log model so where i perform this log model iam going to get one log message related to this saved model insie the mlruns
                else:
                    mlflow.sklearn.log_model(model, "model")


        except Exception as e:
            raise customexception(e,sys)