import numpy as np
import matplotlib.pyplot as plt

y = np.array([0.0, 1.0, 2.0])
x = np.array([3.0, 3.5, 5.5])

W = 0   #기울기
b = 0   #절편

lrate = 0.01    #학습률
epochs = 1000   #반복횟수

for i in range(epochs):
    y_pred = W*x + b    #예측값
    dW = (2/n) * sum(x * (y_pred-y))
    db = (2/n) * sum(y_pred-y)
    W = W -lrate * dW   #기울기 수정
    b = b - lrate * db  #절편 수정

print(W, b)
#기울기와 절편을 출력한다.
y pred = W * x + b
#예측값을 만든다.
plt.scatter(x, y)
#입력 데이터를 그래프 상에 찍는다.
plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)])
plt.show()