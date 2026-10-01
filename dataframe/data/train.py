import pandas as pd
import numpy as np

"""1. pandas를 사용하여 train.csv 파일 데이터를 불러와 DataFrame 으로 저장하시오."""

df = pd.read_csv('/data/train.csv')

"""2. 저장된 데이터에서 상위 5개 행을 출력하시오."""
print(df.head())
print('-'*60)
"""
    3. 각 열의 이름, 결측치 여부, 데이터 타입(dtype)을 한 번에 확인하시오.
    `df.info()`를 실행한 후, 출력 결과를 바탕으로 다음을 기술하시오.

    - 결측치가 존재하는 열과 결측 개수
    - `dtype`이 예상과 다르거나 주의가 필요한 열
"""
df.info()
null_count = df.isnull().sum()
print(null_count)
print('-'*60)

# 4. Age(나이), Fare(요금) 열의 평균값, 최솟값, 최댓값을 구하시오.
result = df[['Age', 'Fare']].agg(['mean', 'min', 'max'])

print(result)
print('-'*60)

# ### 5. 탑승객 중 생존자와 사망자가 각각 몇 명인지 계산하시오.
# - 생존자 : `Survived`=1 / 사망자 : `Survived`=0

survived_counts = df["Survived"].value_counts()
print(survived_counts)

print("=" * 60)

# 6. 객실 등급(Pclass)별로 탑승객이 몇 명인지 계산하시오.
pclass_counts = df["Pclass"].value_counts()
print(pclass_counts)

print("=" * 60)
# 7. 나이가 50세 이상인 탑승객만 추출하여 새로운 데이터프레임을 만드시오.

passenger = df[df["Age"] >= 50]
print(passenger)

print("=" * 60)

# 8. 탑승객을 나이대 기준으로 그룹화하여 새로운 열 AgeGroup을 추가한 후, 상위 5개 행을 확인하시오.
conditions = [
    (df['Age'] >= 0) & (df['Age'] < 10),
    (df['Age'] >= 10) & (df['Age'] < 20),
    (df['Age'] >= 20) & (df['Age'] < 30),
    (df['Age'] >= 30) & (df['Age'] < 40),
    (df['Age'] >= 40) & (df['Age'] < 50),
    (df['Age'] >= 50) & (df['Age'] < 60),
    (df['Age'] >= 60)
]
choices = ['아동', '10대', '20대', '30대', '40대', '50대', '60대 이상']

df['AgeGroup'] = np.select(conditions, choices, default='미확인')
print(df[['Age', 'AgeGroup']].head())
print("=" * 60)

# 9. 성별(Sex)과 객실 등급(Pclass)을 기준으로 그룹화하여 각각의 평균 생존율을 계산하시오
survival_rate = df.groupby(['Sex', 'Pclass'])['Survived'].mean()

print(survival_rate)
print("=" * 60)

"""
    10. 나이대별 평균 생존율을 계산하시오.

    - 8번에서 생성한 `AgeGroup` 열을 기준으로 그룹화하여 계산하시오.
"""
AG = df.groupby(['AgeGroup'])['Survived'].mean()
print(AG)
print("=" * 60)
# 11. 각 열에 존재하는 결측치(NaN)의 총 개수와 전체 데이터 대비 비율을 계산하여 내림차순으로 출력하시오.
null_count = df.isnull().sum()  
null_rate = df.isnull().mean() * 100
missing_df = pd.DataFrame({
    '결측치 개수': null_count,
    '비율(%)': null_rate
})
missing_df = missing_df.sort_values(by='결측치 개수', ascending=False)
print(missing_df)
print("=" * 60)
"""
    12. `Sex`열의 'male'은 0으로, 'female'은 1로 변경하여 Gender_Encoded라는 새로운 열을 추가하시오.
    - `map()`, `replace()`, `apply()` 중 편한 방식을 사용해도 됩니다.
"""
df['Gender_Encoded'] = df['Sex'].map({'male': 0, 'female': 1})

print(df[['Sex', 'Gender_Encoded']].head())
print("=" * 60)

# 13. 탑승지(Embarked)별로 승객이 지불한 요금(Fare)의 평균을 계산하시오.
vudrbs = df.groupby(['Embarked'])['Fare'].mean()
print(vudrbs)