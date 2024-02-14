import pandas as pd


Data=[ {"name":"mahendra","age":28,"city":"Andhrapradesh"}
       {"name":"Alex","age":22,"city":"Andhrapradesh"}
       {"name":"Aravind","age":24,"city":"Andhrapradesh"}
       {"name":"Sheshu","age":23,"city":"Andhrapradesh"}
       {"name":"Lokesh","age":22,"city":"Andhrapradesh"}
       {"name":"Omkar","age":21,"city":"Andhrapradesh"}
       {"name":"Tarun","age":26,"city":"Andhrapradesh"}
    ]


Data=pd.DataFrame(Data)

Data.to_csv("data/data.csv",index=False)



 