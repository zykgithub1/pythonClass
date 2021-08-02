from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# get data
iris = load_iris()
# basic deal with data  -> divide data

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
# feature project->precessing feature
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# machine learning by KNN model training
# instantiate a KNN object
estimator = KNeighborsClassifier()
# improve model  GridSearch
param_grid={"n_neighbors":[1,3,5,7]}
estimator=GridSearchCV(estimator,param_grid=param_grid,cv=5)
# train model
estimator.fit(x_train, y_train)
# estimate model
y_pre=estimator.predict(x_test)
print("prediction of data:->",y_pre)
print("y  _test:->          ",y_test)
print("parallel of y_pre and y_test is:->",y_pre==y_test)
# calculate accuracy
score=estimator.score(x_test,y_test)
print("accrucy is ->",score)

# check
print("best ans of cv->:\n",estimator.best_score_)
print("best model of cv->:\n",estimator.best_estimator_)
print("best ans of model of cv->:\n",estimator.cv_results_)
