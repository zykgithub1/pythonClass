"""
1->get data
2->basic deal with data
 2.1->data partitioning
3-> feature project standardization
4-> machine learning linear regression
5-> estimate model
"""
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def linear_model():
    """
    normal equation of linear regression
    """
    # get data
    boston=load_boston()
    # data split
    x_train,x_test,y_train,y_test=train_test_split(boston.data,boston.target,test_size=0.2)
    #standardization
    # print("x_train:\n",x_train)
    # print("y_train:\n",x_train)
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.fit_transform(x_test)

    #machine learning linear regression
    estimator=LinearRegression()
    estimator.fit(x_train,y_train)
    print("intercept of model",estimator.intercept_)
    print("coefficient of model",estimator.coef_)

    y_pre=estimator.predict(x_test)
    print("result of prediction",y_pre)
    ret=mean_squared_error(y_test,y_pre)
    print("error of mean square",ret)



linear_model()