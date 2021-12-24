# knn
x = [[0], [1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(x, y)

print(neigh.predict([[2.8]]))
print(neigh.predict_proba([[2.8]]))