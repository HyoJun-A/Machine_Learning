import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()
#선형 회귀 모델을 생성한다.

x = [[0], [1], [2]] #2차원으로 만들어야 함
y = [3, 3.5, 5.5]   #y = x + 3
#데이터는 파이썬의 리스트로 만들어도 되고 아니면 넘파이의 배열로 만들어도 됨

reg.fit(x, y)
#reg 객체의 fit(기계학습)
#학습을 수행 시킬떄 fit을 사용 한다.

print(reg.coef_)
# 직선의 기울기

print(reg.intercept_)
# 직선의 y-절편

print(reg.score(x, y))
print(reg.predict([[5]]))

plt.scatter(x, y)
# 학습 데이터와 y 값을 산포도로 그린다.

#y_pred = reg.predict(x)    // 학습데이터를 입력으로 예측값을 계산

#plt.plot(x, y, linewidth = 3)
#plt.show()
#학습 데이터와 예측값으로 선그래프로 그린다.
# 계산된 기울기와 y절편을 가지는 직선이 그려진다.
