from sklearn import tree


features = [[270, 0], [250, 0], [220, 1], [240, 1]]
labels = [0, 0, 1, 1]
#입력 특징일 2차원 리스트로 features 변수에 저장
#결과는 labels 변수에 리스트형으로 저장

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#Training

print(clf.predict([[245, 1]]))
#Prediction and Testing

# 1. DecisionTreeClassifier()메소드 이용
# 2. 훈련데이터 규칙 파악 > 규칙생성
# 3. clf.fit(features, labels) > 실행
# 4. 훈련결과 > 트리생성
