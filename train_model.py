import pandas as pd 
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# load dataset 
data = pd.read_csv("dataset/diabetes.csv")
# read data 
print(data.head())
print(data.columns)
print(data.info())
# seperate x and y values 
x = data.drop("Outcome" , axis = 1)
y = data["Outcome"]
# train_test_split data 
x_train , x_test , y_train , y_test = train_test_split(
    x ,
    y , 
    test_size = 0.2 , 
    random_state = 42 ,
    stratify = y
)
# scaller data
scaler = StandardScaler ()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# apply LogesticRegression
model = LogisticRegression (max_iter = 1000 , class_weight = {0:1 , 1:12})
# train the model
model.fit(x_train , y_train)
# predict the model 
y_prob = model.predict_proba(x_test)[:,1]
y_pred = (y_prob >= 0.4).astype(int)
print("sample prediction: ",y_pred[:5])
# check predictions using confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
# save model & scaler files 
with open("model/model.pkl","wb") as f:
    pickle.dump(model,f)
with open("model/scaler.pkl","wb") as f:
    pickle.dump(scaler,f)
    

