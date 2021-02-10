from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
import pickle

data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

# Prediction with gradient boosted tree
clf = GradientBoostingRegressor()
clf.fit(X_train, y_train)

# Saving the model to file
with open('classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)
