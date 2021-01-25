
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("data//insurance.csv")
df['smoker'] = df['smoker'].replace(to_replace={'no':0,'yes':1})

def pred_ins():
    features = ['age','bmi','smoker']
    X=df[features]
    y=df['charges']

    regressor=LinearRegression()
    return regressor, X, y

