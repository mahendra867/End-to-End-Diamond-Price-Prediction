import os
import sys
from src.logger.logger import logging
from src.exception.exception import customexception
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


obj=DataIngestion()  # here i have created object for DataIngestion() class

train_data_path,test_data_path=obj.initiate_data_ingestion()  # here iam getting 2 things traindatapath,testdatapath

data_transformation=DataTransformation() # here i have created object for DataTransformation() class

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)  # here iam getting the transformed data of both train,test sets

model_trainer_obj=ModelTrainer()  # here i have created object for ModelTrainer() class
model_trainer_obj.initate_model_training(train_arr,test_arr)  # here iam training the model by passing the transformed data which are train_arr,test_arr  to the models


# here i have given the object for modelevaluation class inisde the model_training pipeline
model_eval_obj = ModelEvaluation() # this class is used to evaluate my model evaluation with by using MLFLOW URI which i declared this class and integrated this mlflow URI inside the model_evalution.py file 
model_eval_obj.initiate_model_evaluation(train_arr,test_arr)