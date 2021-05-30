from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz

iris = load_iris()          #iris 토이 데이터 세트를 iris변수에 저장
test = [0, 50, 100]

#아이리스 데이터의 일부를 출력
print(iris.feature_names)   #특징(feature)들을 저장
print(iris.target_names)    #학습 라벨에 해당하는 target을 출력
print(iris.data[0])         #첫 번쨰 데이터에 저장된 feature값 출력
print(iris.target[0])       #첫 번쨰 데이터에 저장된 target값 출력

#아이리스 데이터 세트에 저장된 모든 내용을 모두 출력
'''for i in range(len(iris)):
    print("Exampe %d: label %s, features %s" % (i, iris.target[1], iris.data[i]))'''
    #0~49 세토사, 50~99 버시컬러, 100~149 버지니카

#훈련 데이터, 테스트 데이터 생성및 출력
train_data = np.delete(iris.data, test, axis=0) #3개의 데이터를 데이터 변수에서 제거, 2차원 리스트이기때문에 axis사용
train_target = np.delete(iris.target, test)     #3개의 데이터를 타겟 데이터 변수에서 제거, 1차원 리스트

#testing data
test_data = iris.data[test]
test_target = iris.target[test]

#결정트리 생성
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

'''print(test_target)
print(clf.predict(test_data))'''

# 아이리스 데이터 세트로 생성된 결정트리
dot_data = tree.export_graphviz(clf, out_file = None)
graph = graphviz.Source(dot_data)
graph.render("iris")
dot_data = tree.export_graphviz(clf, out_file = None,
                                feature_names = iris.feature_names,
                                class_names = iris.target_names,
                                filled = True, rounded = True,
                                special_characters = True)
graph = graphviz.Source(dot_data)
graph

print(test_data[1], test_target[1])
print(iris.feature_names, iris.target_names)