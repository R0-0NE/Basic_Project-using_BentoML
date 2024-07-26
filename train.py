import bentoml

from sklearn import svm
from sklearn import datasets

#load iris dataset
iris=datasets.load_iris()
X,y=iris.data,iris.target

#train the model
clf=svm.SVC(gamma="scale")
clf.fit(X,y)

#save the model to bentoml local model store
saved_model=bentoml.sklearn.save_model("iris_clf",clf)
print(f"Model saved: {saved_model}")

#Model saved: Model(tag="iris_clf:lgovz3cld6prw4c2")