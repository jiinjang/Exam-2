import pandas as pd


path = "Titanic-Dataset.csv"
df = pd.read_csv(path)

age_missing_percent = (df["Age"].isnull().sum() / len(df)) * 100
cabin_missing_percent = (df["Cabin"].isnull().sum() / len(df)) * 100

print("Missing data:")
print("Age:", round(age_missing_percent, 2), "%")
print("Cabin:", round(cabin_missing_percent, 2), "%")

# Age is filled with the median to limit the effect of outliers.
# Cabin is filled with Unknown because most of its values are missing.
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Cabin"] = df["Cabin"].fillna("Unknown")

df.to_csv("cleaned_titanic.csv", index=False)

survivors = df[df["Survived"] == 1]

overall_average = df["Age"].mean()
survivor_average = survivors["Age"].mean()
survivor_average_class1 = (
    survivors[survivors["Pclass"] == 1]["Age"].mean()
)
survivor_average_class2 = (
    survivors[survivors["Pclass"] == 2]["Age"].mean()
)
survivor_average_class3 = (
    survivors[survivors["Pclass"] == 3]["Age"].mean()
)

print('Averages:')
print('Overall:' + str(overall_average))
print('Survivors:' + str(survivor_average))
print('Class 1:' + str(survivor_average_class1))
print('Class 2:' + str(survivor_average_class2))
print('Class 3:' + str(survivor_average_class3))
