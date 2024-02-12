from flask import Flask,request,render_template,jsonify

from src.pipeline.prediction_piepline import PredictPipeline,CustomData # Here ihave imported the prediction pipeline 2 classes

app=Flask(__name__)  # Flask: This is the class provided by the Flask framework that you use to create web applications. (__name__): This is a special Python variable that represents the name of the current module. When you use __name__ as the argument to the Flask constructor, it helps Flask to determine the root path of the application. This is important for Flask to know where to look for templates, static files, and other resources.


@app.route('/') # here i have created 1st URL in order to display  html code content for the index.html file in the local host server  , so this '/' this means its my 1ts URL which iam not mentioning no name , so this 1st URL gets run in the port number localhost:8000  which it runs the User interface of index.html file code content
def home_page(): # here i have defined home_page() fucntion which returns the index.html render_template
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"]) # here i have created 2nd URL which we given URL name as predict in order to display  form.html code content for the form.html file in the local host server on top of the 1st url , so basically this form.html file code contain gets run in this 2nd URL which name is predict so  the form.html code which helps us to take or fetch or GET the values from the users thats why we mention GET method  and our best model which is in prediciotn pipeline by using the POST method our model predicts those fetched values 
def predict_datapoint():  # so this method iam going to mention inside the action form of form.html code at starting 
    if request.method=="GET":  # here by using this GET method to the 2nd url which is /predict client(user) sending the requesting to the backend code which is this source code ,by taking this form.html code content it provides the user interface so the client or user pass the data to the backend server so as soons as i click on submit button user or client sends request or submites  to the backend source code which the post Method perform this 
        return render_template("form.html")  
    
    else: # if i fail to get request from the backend code which is form.html code then this else part will execute , like i do submit the fetched or sending the requested data to the customdata class which has the variables of each feature , so then these fetched values gets submitted to the defined varaibles in customdata class which is in predict pipeline   , so we will get prediction
        data=CustomData(  # here basically i have created object to the CustomData class and passing the data or arguments to this parameters which we initlized in the customdata class , so how we are passing the data ,the process is exactly work like this way like we first open this site localhost:8000/predict, actually this localhost:8000/predict is client server , there client(user) enter the values to the 2nd url which is predict , basically the (users) client requests  the backend server which is our source code by using this predict UI , so for as per the request of the client passed data to the backend server, the backend server gives response by submitting our data as arguements  to the customdata class
            carat=float(request.form.get("carat")), # here iam client requested the data by using the predict URL then its passed data gets submitted to the carat variable and by default its submit the string value but our feature we need to submit is float thats why iam performing the type casting it means changing the varaible data type from string to float of carat varaible and storing in the varaible of carat
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            cut=request.form.get("cut"),
            color=request.form.get("color"),
            clarity=request.form.get("clarity")
        )
        final_data=data.get_data_as_dataframe()  # here iam calling the get_data_as_dataframe() method with  data which is obejct for the class customdata and we are storing the gathered data of individual feature which is in the form of dataframe  gets stored  in final_data variable 

        predict_pipeline=PredictPipeline() # now here i have created object for the predictionpipeline class to assign the gathered data in the form of dataframe to the best model which i have defined inisde this PredictPipeline() class 

        pred=predict_pipeline.predict(final_data) # here iam passing the gathered data which is in form of dataframe to the best model by calling the method predict which is in PredictionPipeline class and by just passing the gathered dataframe inside this predict method its get preprocessed and data gets predicted by the best model

        result=round(pred[0],2)  # here in the result variable we have prediction value with array datatype so iam taking the intial value by just rounding off to 2 points

        return render_template("result.html",final_result=result) # now iam going to create another html file which is result.html to that iam passing this result which consist of prediction value 
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000) # so this localhost:8000 portnumber is my home page which is 1st URL index.html web application gets open  and if i want to open the 2nd URL which that 2nd URL name is predict we need to type add predict to this  localhost:8000  like localhost:8000/predict


# Flask application working
# SO the moment we access this appliction by this specific localhost:8000/predict  this GET method gets triggered and it helps us to  render form.html code contnet in 2nd URL predict and here render refers to the process of generating HTML content dynamically and sending it as a response to a client's request. to display the form.html code content in 2nd url which is /predict , and then the user enters the input data from his side and as soons as he click on submit the POST method gets executed means the input data which we given to the from.html in the 2nd url predict gets requested to the backend server which is the soruce code and it performs the form data from the request, process it (e.g., convert it to the appropriate data types), and then use it for prediction or any other necessary operations