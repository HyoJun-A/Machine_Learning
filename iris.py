from sklearn.datasets import load_iris

iris = load_iris()          #iris 토이 데이터 세트를 iris변수에 저장
#아이리스 데이터의 일부를 출력
print(iris.feature_names)   #특징(feature)들을 저장
print(iris.target_names)    #학습 라벨에 해당하는 target을 출력
print(iris.data[0])         #첫 번쨰 데이터에 저장된 feature값 출력
print(iris.target[0])       #첫 번쨰 데이터에 저장된 target값 출력

#아이리스 데이터 세트에 저장된 모든 내용을 모두 출력
'''for i in range(len(iris)):
    print("Exampe %d: label %s, features %s" % (i, iris.target[1], iris.data[i]))'''
    #0~49 세토사, 50~99 버시컬러, 100~149 버지니카