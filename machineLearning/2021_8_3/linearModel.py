from sklearn.linear_model import LinearRegression

x = [[80, 86],
     [82, 80],
     [85, 78],
     [90, 90],
     [86, 82],
     [82, 90],
     [78, 80],
     [92, 94]]
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

#model training
estimator=LinearRegression()
estimator.fit(x,y)
print("linear model:->\n",estimator.coef_)
print("result of linear model:->\n",estimator.predict([[100,80]]))
