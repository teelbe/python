from pandas import read_csv

titanic_df = read_csv("titanic.csv")

# liczba osoób w klasach
class_count = titanic_df["PClass"] \
    .value_counts() \
    .sort_index()
print(class_count)

# przeżywalność w klasach
print(titanic_df \
      .groupby("PClass")["Survived"] \
      .mean())

# liczba osób wg płci
print(titanic_df["Sex"] \
      .value_counts() \
      .sort_index())

# przeżywalność wg płci
print(titanic_df \
      .groupby(["Sex"])["Survived"] \
      .mean())

# przezywalność wg klasy i płci
print(titanic_df \
      .groupby(["PClass", "Sex"])["Survived"] \
      .mean())

# przezywalność wg wieku
from pandas import cut

titanic_df['AgeGroup'] = cut(
    titanic_df['Age'],
    bins=[i * 10 for i in range(8)]
)
print(titanic_df \
      .groupby(["AgeGroup"])["Survived"] \
      .mean()
      )
