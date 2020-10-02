import os
import requests
import tarfile
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import OrdinalEncoder, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    with open(tgz_path, "wb") as f:
        response = requests.get(housing_url)
        f.write(response.content)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def stratified_sample_split(data, test_ratio):
    data["income_cat"] = pd.cut(data["median_income"],
                                bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                labels=[1, 2, 3, 4, 5])
    split = StratifiedShuffleSplit(n_splits=1,
                                   test_size=test_ratio,
                                   random_state=42)
    for train_index, test_index in split.split(data, data["income_cat"]):
        strat_train_set = data.loc[train_index]
        strat_test_set = data.loc[test_index]

    # noinspection PyUnboundLocalVariable
    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    return strat_train_set, strat_test_set


def clean_data(data):
    imputer = SimpleImputer(strategy="median")
    data_num = data.drop("ocean_proximity", axis=1)
    imputer.fit(data_num)
    X = imputer.transform(data_num)
    data_tr = pd.DataFrame(X, columns=data_num.columns,
                           index=data_num.index)
    return data_tr


def convert_categorical(data_cat):
    ordinal_encoder = OrdinalEncoder()
    data_cat_encoded = ordinal_encoder.fit_transform(data_cat)
    print(ordinal_encoder.categories_)
    return data_cat_encoded


def prepare_training_data(training_data):
    data = training_data.drop("median_house_value", axis=1)
    data_numerical = data.drop("ocean_proximity", axis=1)

    numerical_attributes = list(data_numerical)
    categorical_attributes = ["ocean_proximity"]

    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("attribs_adder", CombinedAttributesAdder()),
        ("std_scaler", StandardScaler())])

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, numerical_attributes),
        ("cat", OneHotEncoder(), categorical_attributes)
    ])

    return full_pipeline.fit_transform(data)


df = load_housing_data()  # total_bedrooms has only 20433 non-null values
train_set, test_set = stratified_sample_split(df, 0.2)
housing = train_set.copy()

housing_prepared = prepare_training_data(train_set)
