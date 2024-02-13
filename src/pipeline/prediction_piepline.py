import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logger import logging
from src.utils.utils import load_object


class PredictPipeline:

            
            def __init__(self):
                print("init.. the object")

            def predict(self,features):   # here i have passed 1 parameter which is features and these features parameter takes arguments from user interface by user 
                try:  # Inorder to predict the data we need to load the objects which are present in artifacts folder 1)  preprocessor.pkl object 2) model.pkl object, then only we can able to predict the unseen data
                    preprocessor_path=os.path.join("artifacts","preprocessor.pkl")  # here iam taking those 2 objects which are available inside the artifacts folder
                    model_path=os.path.join("artifacts","model.pkl")

                    preprocessor=load_object(preprocessor_path)
                    model=load_object(model_path)

                    scaled_fea=preprocessor.transform(features)  # here iam performing the feature transformation on features varaible , so here the question is where iam getting these features basically iam getting these features from User interface and  by using the preprocessor object  iam performing the data transformation on these features which are collected by user from UI and saving it in scaled_fea
                    pred=model.predict(scaled_fea)  # here iam predicting the scaled features by using my loaded best model from artifacts which is available model variable

                    return pred  # here iam returning the prediction

                except Exception as e:
                    raise customexception(e,sys)


class CustomData:   # here i have created class which is custome data 
            def __init__(self,  # here by this method iam going to collect the data from the user from user interface of predict , so by just calling this customdata class with object by just passing the arguments or values which the users get requests this backend server which is this soruce code and then this class gets executed automatically
                        carat:float,
                        depth:float,
                        table:float,
                        x:float,
                        y:float,
                        z:float,
                        cut:str,
                        color:str,
                        clarity:str):
                
                # THESE ARE MY INSTANCE VARIABLE to these user passed arguments gets stored inside these each individual varibale and we REUSE THESE VARAIBLE INSIDE THE get_data_as_dataframe METHOD  to convert the taken data from user to dataframe of these each individual variable data
                self.carat=carat
                self.depth=depth
                self.table=table
                self.x=x
                self.y=y
                self.z=z
                self.cut = cut
                self.color = color
                self.clarity = clarity
                    
            def get_data_as_dataframe(self):   # here i have defined another method which is get_data_as_dataframe which it converts the data which is taken from user from user interface to  a dataframe
                try:
                    custom_data_input_dict = {  # here i have created the dictionary like feature name : value   
                        'carat':[self.carat],
                        'depth':[self.depth],
                        'table':[self.table],
                        'x':[self.x],
                        'y':[self.y],
                        'z':[self.z],
                        'cut':[self.cut],
                        'color':[self.color],
                        'clarity':[self.clarity]
                        }
                    df = pd.DataFrame(custom_data_input_dict)   # here iam finally converting the taken data which is in dictionary to a dataframe, and these converted data which is actually in dataframe which i pass this dataframe to my model
                    logging.info('Dataframe Gathered')
                    return df # so when we call this method get_data_as_dataframe by the object of customdata class , the object gets stored this df which has values of each individual feature in the form of dataframe
                
                except Exception as e:
                    logging.info('Exception Occured in prediction pipeline')
                    raise customexception(e,sys)