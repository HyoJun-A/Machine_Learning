import numpy as np
import matplotlib.pyplot as plt

dogs = 1000 #개의 수 지정
cats = 1000 #고양이의 수 지정

dog_height = 35 + (5 * np.random.randn(dogs)) # 35를 기준으로 Numpy를 이용하여 키를 지정
cat_height = 30 + (5 * np.random.randn(cats)) # 30를 기준으로 Numpy를 이용하여 키를 지정

plt.xlabel('Height') # x레이블 이름 지정
plt.ylabel('Number of Species') # y레이블 이름 지정
plt.hist([dog_height, cat_height], label=['Dogs', 'Cats'], stacked=True, color=['r', 'y'])

plt.legend()
plt.show()
#히스토그램사용
#30이하의 동물이 고양이가 더 많고 40이상은 강아지가 더 많다.
#특징을 가지고 구분 (키)
