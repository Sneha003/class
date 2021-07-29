import cv2
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from PIL import Image
import PIL.ImageOps
import os,ssl,time

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and 
getattr(ssl, '_create_unverified_context', None)): ssl._create_default_https_context = ssl._create_unverified_context

X,y=fetch_openml("mnist_784",version=1,return_X_y=True)
print(pd.Series(y).value_counts())
classes=["0","1","2","3","4","5","6","7","8","9"]
#nclasses=len(classes)
#print(nclasses)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=2500,train_size=7500)

X_train_Scaled=X_train/255
X_test_Scaled=X_test/255

classifier= LogisticRegression(solver="saga",multi_class="multinomial").fit(X_train_Scaled,y_train)

y_predict=classifier.predict(X_test_Scaled)
accuracy=accuracy_score(y_test,y_predict)
print("{}% is accuracy in the model".format(accuracy))