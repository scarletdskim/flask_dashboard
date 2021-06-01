import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from category_encoders import OrdinalEncoder



def preprocessing(df):
    # preprocessing categorical data 
    ordinal_enc_params = {
        'neighbourhood_group' : 'neighbourhood_group',
        'mapping' : {
            'Brooklyn':0,
            'Manhattan':1,
            'Queens':2, 
            'Staten Island':3, 
            'Bronx':4
        },
        'room_type' : 'room_type',
        'mapping' : {
            'Private room':0, 
            'Entire home/apt':1, 
            'Shared room':2     
        }
    }
    # preprocessing categorical data 
    X_cat = df[['neighbourhood_group', 'room_type']]
    encoder = OrdinalEncoder(ordinal_enc_params)
    X_encoded = encoder.fit_transform(X_cat)

    # Normalizing numerical data with StandardScaler
    scaler = StandardScaler()
    X_num = df[['minimum_nights']]

    scaler.fit(X_num) 
    X_scaled = scaler.transform(X_num)
    X_scaled = pd.DataFrame(X_scaled, index=X_num.index, columns=X_num.columns)

    X_train = pd.concat([X_scaled, X_encoded], axis=1)

    return X_train

def predict_price(X_train, y_train, X_test):

    model_reg = LinearRegression()
    model_reg.fit(X_train, y_train)

    prediction = model_reg.predict(X_test)
    
    return round(prediction[0], 2)
    

