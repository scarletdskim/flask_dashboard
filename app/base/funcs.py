import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


def preprocessing(df):
    # preprocessing categorical data 
    X_cat = df[['neighbourhood_group', 'room_type']]
    X_cat = pd.get_dummies(X_cat)

    # Normalizing numerical data with StandardScaler
    scaler = StandardScaler()
    X_num = df[['minimum_nights']]

    scaler.fit(X_num) 
    X_scaled = scaler.transform(X_num)
    X_scaled = pd.DataFrame(X_scaled, index=X_num.index, columns=X_num.columns)

    X_train = pd.concat([X_scaled, X_cat], axis=1)
    y_train = df['price']

    return X_train, y_train

def predict_price(X_train, y_train, X_test):

    model_reg = LinearRegression()
    model_reg.fit(X_train, y_train)

    prediction = model_reg.predict(X_test)
    
    return prediction[0]
    

