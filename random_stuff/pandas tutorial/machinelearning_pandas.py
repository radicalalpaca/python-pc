import pandas as pd
import sklearn
from sklearn import svm, preprocessing

test_size = 200

df = pd.read_csv("data/diamonds.csv", index_col=0)
cut_class_dict = {"Fair": 1,
                  "Good": 2,
                  "Very Good": 3,
                  "Premium": 4,
                  "Ideal": 5}
clarity_dict = {"I1": 1,
                "SI2": 2,
                "SI1": 3,
                "VS2": 4,
                "VS1": 5,
                "VVS2": 6,
                "VVS1": 7,
                "IF": 8}
color_dict = {"J": 1,
              "I": 2,
              "H": 3,
              "G": 4,
              "F": 5,
              "E": 6,
              "D": 7}

df["cut"] = df["cut"].map(cut_class_dict)
df["clarity"] = df["clarity"].map(clarity_dict)
df["color"] = df["color"].map(color_dict)

df = sklearn.utils.shuffle(df)

X = df.drop("price", axis=1).values
X = preprocessing.scale(X)
Y = df["price"].values

X_train = X[:-test_size]
Y_train = Y[:-test_size]
X_test = X[-test_size:]
Y_test = Y[-test_size:]

clf = svm.SVR()
clf.fit(X_train, Y_train)
print(clf.score(X_test, Y_test))

for X, Y in list(zip(X_test, Y_test))[:10]:
    print(clf.predict([X])[0], Y)