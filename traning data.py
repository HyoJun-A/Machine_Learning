from sklearn import tree
imput_data = [[200, 0], [210, 0], [220, 0], [230, 1], [240, 1], [250, 1]]
fruits = [0, 0, 0, 1, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(imput_data, fruits)
print(clf.predict([[200, 1]]))
# 0 사과
# 1 오렌지