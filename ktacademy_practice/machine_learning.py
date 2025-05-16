from sklearn import datasets

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.3
)

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(hidden_layer_sizes=(100, 100))
clf.fit(X_train, y_train)
y_train_pred = clf.predict(X_train)
print((y_train_pred == y_train).mean())

y_test_pred = clf.predict(X_test)
print((y_test_pred == y_test).mean())