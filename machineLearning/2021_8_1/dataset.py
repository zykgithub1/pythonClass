from sklearn.datasets import load_iris,fetch_20newsgroups
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris=load_iris()

"""news=fetch_20newsgroups()
# print("data's feature is ->:\n",iris.data)
# print("target value of dataset is ->\n",iris["target"])
# print("data's feature names are ->:\n",iris.feature_names)
# print("target names value of dataset are ->\n",iris.target_names)
# print("target names value of dataset are ->\n",iris.DESCR)"""

iris_df=pd.DataFrame(data=iris.data,columns=["Sepal_Length","Sepal_Width","Prtal_Length","Petal_Width"])
iris_df["target"]=iris.target


def iris_plot(data,col1,col2):
    sns.lmplot(x=col1,y=col2,data=data,hue="target",fit_reg=False)
    plt.title("iris data display")
    plt.show()


iris_plot(iris_df,"Sepal_Width","Prtal_Length")

