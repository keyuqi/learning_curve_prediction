import numpy as np
from sklearn import linear_model
#from sklearn.linear_model import LinearRegression
from data import load_data_four_points
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error


if __name__ == '__main__':

    inputs, labels = load_data_four_points()
    kf = KFold(n_splits=3, shuffle=True)

    total_loss = np.zeros((1,))
    # print(total_loss)
    score_avg = 0.0
    mse_avg = 0.0

    for train, val in kf.split(labels):
        X_train, y_train, X_val, y_val = inputs[train], labels[train], inputs[val], labels[val]
        #linreg = LinearRegression()
        linreg = linear_model.Ridge(alpha=0.5)
        linreg.fit(X_train, y_train)
        
        score = linreg.score(X_val, y_val)
        score_avg += score * len(y_val) / len(labels)
        
        y_pred = linreg.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        mse_avg += mse * len(y_val) / len(labels)
        
        print("3-fold cross validation score: % f" % score)
        print("3-fold cross validation mse: % f" % mse)
        
    
    print("average cross validation score: % f" % score_avg)
    print("average cross validation mse: % f" % mse_avg)
        
        
        