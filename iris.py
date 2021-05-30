from sklearn.datasets import load_iris

iris = load_iris()          #iris 토이 데이터 세트를 iris변수에 저장
print(iris.feature_names)   #특징(feature)들을 저장
print(iris.target_names)    #학습 라벨에 해당하는 target을 출력
print(iris.data[0])         #첫 번쨰 데이터에 저장된 feature값 출력
print(iris.target[0])       #첫 번쨰 데이터에 저장된 target값 출력