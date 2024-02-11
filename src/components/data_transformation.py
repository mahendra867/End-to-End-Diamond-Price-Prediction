import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.utils.utils import save_object

@dataclass
class DataTransformationConfig:  # eere by using the dataclass i have given configuration to create artifacts folder which it consist of preprocessor.pkl file
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()  # here i have created a varaible which is object for the DataTransformationConfig()  class , so we can have the DataTransformationConfig() class varible data which gets stored inside these varaible  self.data_transformation_confi

        
    
    def get_data_transformation(self):
        
        try:  # inisde this try block i have given the preprocessing steps which i have performed in the exeperiments.ipynb file
            logging.info('Data Transformation initiated')
            
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')
            
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )
            
            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]

            )
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor
            

            
            
        
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            
    
    def initialize_data_transformation(self,train_path,test_path):  # here i have defined 1 method which is initialize_data_transformation inside i have given parameters like train_path,test_path which iam taken from data_ingestion code  
        try:  # here i have 
            train_df=pd.read_csv(train_path)  # here iam taking train_path,test_path from the artifacts folder of data_ingestion
            test_df=pd.read_csv(test_path)
            
            logging.info("read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')
            
            preprocessing_obj = self.get_data_transformation()  # here i have created a varaible  to save the try block code of get_data_transformation method , so this preprocessor_obj consist of preprocessing steps which we performed in try block of get_data_transformatio 
            
            target_column_name = 'price' # price is the target column
            drop_columns = [target_column_name,'id'] # here iam dropping the id column
            
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)  # this is the independent feature which we can consider as x_train
            target_feature_train_df=train_df[target_column_name]   # # this is the dependent feature which we can consider as y_train
            
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1) # # this is the independent feature which we can consider as x_test
            target_feature_test_df=test_df[target_column_name]  # this is the dependent feature which we can consider as y_test
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)  # here iam performing the data preprocessing to the x_train,x_test by using the variable of preprocessor_obj
            
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]  # here iam performing the horizontal concatination by concatinating the X_train+y_train preprocessed data ,because i need to train the model to this preprocessed data to train our model
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]    #here iam performing the horizontal concatination by concatinating the X_test+y_test preprocessed data ,because i need to pass the model to this preprocessed data to test our model

            save_object(  # here iam saving the object which it requires 2 things location and model object , and i have taken this method which i have written configuration in utils.py file
                file_path=self.data_transformation_config.preprocessor_obj_file_path, # this is the location or path of the object where we are going to save the location or path of the object  in file_path variale
                obj=preprocessing_obj   # this obj variable consist of model
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (  # here finally iam returining the train_arr,test_arr to the modeltrainer.py file 
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            