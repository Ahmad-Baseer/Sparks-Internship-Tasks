import pickle
import numpy as np
from sklearn import datasets
import pandas as pd

iris_k_mean_model=pickle.load(open('model.sav', 'rb'))
classes=['versicolor', 'setosa' , 'virginica']

iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])


def predict_class_way1(new_data_point):
    # Calculate the Euclidean distances between the new data point and each of the training data points.
    distances = np.linalg.norm(x - new_data_point, axis=1)
    # print(distances,len(distances),np.argmin(distances))

    # The data point with the minimum Euclidean distance is the class of the new data point.
    class_label = classes[iris_k_mean_model.labels_[np.argmin(distances)]]

    return class_label

def predict_class_way2(new_data_point):
    # Calculate the distances between the new data point and each of the cluster centers.
    distances = np.linalg.norm(iris_k_mean_model.cluster_centers_ - new_data_point, axis=1)
    # print(distances,len(distances),np.argmin(distances))

    # The data point with the minimum Euclidean distance is the class of the new data point.
    class_label = classes[np.argmin(distances)]

    return class_label
