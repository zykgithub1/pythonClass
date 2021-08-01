from sklearn.neighbors import KNeighborsClassifier

x=[[1],[2],[10],[20]]
y=[0,0,1,1]

#train model
# 1-> instantiate a obj
estimator=KNeighborsClassifier(n_neighbors=1)
# 2-> use fit to training
estimator.fit(x,y)

ret=estimator.predict([[1]])
print(ret)