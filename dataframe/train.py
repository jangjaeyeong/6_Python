import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""1. pandas를 사용하여 train.csv 파일 데이터를 불러와 DataFrame 으로 저장하시오."""

df = pd.read_csv('data/train.csv')

"""2. 저장된 데이터에서 상위 5개 행을 출력하시오."""

print(df.head())

print("=" * 60)
print("=" * 60)

"""
    3. 각 열의 이름, 결측치 여부, 데이터 타입(dtype)을 한 번에 확인하시오.
    `df.info()`를 실행한 후, 출력 결과를 바탕으로 다음을 기술하시오.

    - 결측치가 존재하는 열과 결측 개수
    - `dtype`이 예상과 다르거나 주의가 필요한 열
"""

df.info()
null_count = df.isnull().sum()
print(null_count)

print("=" * 60)
print("=" * 60)

# 4. Age(나이), Fare(요금) 열의 평균값, 최솟값, 최댓값을 구하시오.

result = df[['Age', 'Fare']].agg(['mean', 'min', 'max'])

print(result)

print("=" * 60)
print("=" * 60)

# ### 5. 탑승객 중 생존자와 사망자가 각각 몇 명인지 계산하시오.
# - 생존자 : `Survived`=1 / 사망자 : `Survived`=0

survived_counts = df["Survived"].value_counts()
print(survived_counts)

print("=" * 60)
print("=" * 60)

# 6. 객실 등급(Pclass)별로 탑승객이 몇 명인지 계산하시오.

pclass_counts = df["Pclass"].value_counts()
print(pclass_counts)

print("=" * 60)
print("=" * 60)

# 7. 나이가 50세 이상인 탑승객만 추출하여 새로운 데이터프레임을 만드시오.

age_over = df[df["Age"] >= 50]
print(age_over)

print("=" * 60)
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
print("=" * 60)

# 9. 성별(Sex)과 객실 등급(Pclass)을 기준으로 그룹화하여 각각의 평균 생존율을 계산하시오

survival_rate = df.groupby(['Sex', 'Pclass'])['Survived'].mean()

print(survival_rate)

print("=" * 60)
print("=" * 60)

"""
    10. 나이대별 평균 생존율을 계산하시오.

    - 8번에서 생성한 `AgeGroup` 열을 기준으로 그룹화하여 계산하시오.
"""
AG = df.groupby(['AgeGroup'])['Survived'].mean()
print(AG)
print("=" * 60)
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
print("=" * 60)
"""
    12. `Sex`열의 'male'은 0으로, 'female'은 1로 변경하여 Gender_Encoded라는 새로운 열을 추가하시오.
    - `map()`, `replace()`, `apply()` 중 편한 방식을 사용해도 됩니다.
"""
df['Gender_Encoded'] = df['Sex'].map({'male': 0, 'female': 1})

print(df[['Sex', 'Gender_Encoded']].head())

print("=" * 60)
print("=" * 60)

# 13. 탑승지(Embarked)별로 승객이 지불한 요금(Fare)의 평균을 계산하시오.

vudrbs = df.groupby(['Embarked'])['Fare'].mean()
print(vudrbs)

print("=" * 60)
print("=" * 60)

# 14. Pclass를 인덱스로, Sex를 컬럼으로, 값으로 Fare의 평균을 사용하여 피벗 테이블을 생성하시오.
pivot_table = df.pivot_table(index='Pclass', columns='Sex', values='Fare')
print(pivot_table)

print("=" * 60)
print("=" * 60)

# 15. SibSp (형제/배우자 수)와 Parch (부모/자녀 수)를 합산하여 FamilySize 열을 추가하고, 이 열의 요약 통계를 확인하세요.

df['FamilySize'] = df['SibSp'] + df['Parch']
print(df['FamilySize'].describe())

print("=" * 60)
print("=" * 60)


### 16. `Name` 열에서 호칭(Mr., Mrs., Miss., Master. 등)을 정규 표현식 또는 문자열 함수를 사용하여 추출하고 `Title`이라는 새로운 열을 생성한 뒤, 가장 흔한 5개의 호칭을 출력하시오.
# 정규 표현식 예시: `r', ([A-Za-z]+)\.'` - 성(Last name) 뒤에 오는 호칭을 추출한다.

df['Title'] = df['Name'].str.extract(r', ([A-Za-z]+)\.', expand=False)
print(df['Title'].value_counts().head(5))

print("=" * 60)
print("=" * 60)

### 17. 16번에서 생성한 `Title` 열을 기준으로 그룹화하여, 각 호칭별 **승객 수**, **평균 나이**, **평균 생존율**을 한 번에 계산하시오.
# - `groupby().agg()`의 Named Aggregation을 활용하면 집계 결과 열 이름을 직접 지정할 수 있다.

result = df.groupby('Title').agg(
    passenger_count=('PassengerId', 'count'),
    average_age=('Age', 'mean'),
    average_survival_rate=('Survived', 'mean')
).reset_index()

print(result)

print("=" * 60)
print("=" * 60)

### 18. 생존한 사람과 사망한 사람의 나이(`Age`) 분포를 비교할 수 있도록 시각화하시오.
# - 히스토그램 또는 KDE(밀도) 플롯 중 하나를 사용하시오.
# - 그래프에는 다음 요소를 반드시 포함하시오.
#     - 제목 (`set_title`)
#     - x축·y축 라벨 (`set_xlabel`, `set_ylabel`)
#     - 생존/사망 구분 범례 (`legend`)
# - 결과를 화면에 출력하지 않고 **이미지 파일로 저장**하시오. (`savefig` 사용)
survived_age = df[df['Survived'] == 1]['Age'].dropna()
died_age = df[df['Survived'] == 0]['Age'].dropna()

plt.hist(survived_age, bins=20, alpha=0.5, label='Survived')
plt.hist(died_age, bins=20, alpha=0.5, label='Died')

plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()

plt.savefig('age_distribution_by_survival.png')

### 19. 16번에서 추출한 `Title`과 `Pclass`를 **동시에** 고려하여 해당 그룹의 나이 중앙값으로 `Age` 열의 결측치를 대치하시오. (원본 프레임에 적용)
# ex. 'Master' 타이틀을 가진 1등급 승객 그룹의 나이 중앙값으로 해당 그룹의 결측치를 채운다.
# `groupby().transform("median")`을 활용하면 그룹별 중앙값을 원본과 같은 길이로 얻을 수 있다.
# ⚠️ 이 문제는 반드시 **16번 완료 후** 진행하시오. `Title` 열이 존재해야 그룹 기준으로 사용할 수 있습니다.

group_median = df.groupby(['Title', 'Pclass'])['Age'].transform('median')
df['Age'] = df['Age'].fillna(group_median)
print(df[['Title', 'Pclass', 'Age']])

print("=" * 60)
print("=" * 60)

### 20. `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare` 등의 수치형 변수들 간의 상관관계 행렬을 계산하고, 그 결과를 **히트맵(Heatmap)** 으로 시각화하시오.
# - `corr()` : 상관관계 행렬 계산 함수
# - `sns.heatmap(..., annot=True, cmap="coolwarm", center=0)` 형식으로 작성하면 값이 셀 안에 표시됩니다.
# - 결과를 화면에 출력하지 않고 **이미지 파일로 저장**하시오. (`savefig` 사용)

numeric_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

corr = df[numeric_cols].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    center=0
)

plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')