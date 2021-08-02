from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris=load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
print("feature of training data is:\n",x_train)
print("goal of training data is:\n",y_train)
print("feature of test data is:\n",x_test)
print("goal of test data is:\n",y_test)