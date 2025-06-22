import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
data_frame = pd.read_csv("Enter the location of dataset")
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

print("\nTop 5 elements of dataset")
print(data_frame.head())

print("\nLast 5 elements of dataset")
print(data_frame.tail())

print("\nNumber of rows and columns in dataset")
print(data_frame.shape)

print("\nInformation about dataset")
print(data_frame.info())

print("\nName of the columns in dataset")
print(data_frame.columns)

print("\nFind Unique values in each column")
for col in data_frame.describe(include="object").columns:
    print(col)
    print(data_frame[col].unique())

print("\nSummarization of data from dataset")
print(data_frame.describe(include="all"))

print("\nData Analysis and Visualization")
# flight_status = data_frame["Flight Status"].value_counts(normalize=True)
# print(flight_status)

data_frame["age_group"] = np.where(data_frame["Age"] <= 25, "Adult", "Teenager")
print(data_frame["age_group"].value_counts())
#
print("\nNumber of teenagers and adult who use flight")
plt.figure(figsize=(10, 7))
plt.title("Age group Count")
plt.bar(["Adult", "Teenager"], data_frame["age_group"].value_counts(), width=0.5)
plt.xlabel("Age-Group")
plt.ylabel("Count")
plt.show()

print("\nTop 10 Nationality of Adults")
adult = data_frame[data_frame["age_group"] == "Adult"]
top_10_nationality = adult['Nationality'].value_counts()[:10]
print(top_10_nationality)

plt.figure(figsize=(10, 8))
plt.title('Top 10 Nationality of Adults')
plt.pie(top_10_nationality, autopct='%.2f', labels=top_10_nationality.index)
plt.show()


print("\nTop 10 Nationality of Teenagers")
teenager = data_frame[data_frame["age_group"] == "Teenager"]
top_10_nationality = teenager['Nationality'].value_counts()[:10]
print(top_10_nationality)

plt.figure(figsize=(10, 8))
plt.title('Top 10 Nationality of Teenagers')
plt.pie(top_10_nationality, autopct='%.2f', labels=top_10_nationality.index)
plt.show()


print("\nGender of Adult")
gender_adult = adult['Gender'].value_counts()
print(gender_adult)

plt.figure(figsize=(10, 8))
plt.title('Gender of Adult')
plt.pie(gender_adult, autopct='%.2f', labels=gender_adult.index)
plt.show()


print("\nGender of Teenager")
gender_teenager = teenager['Gender'].value_counts()
print(gender_teenager)

plt.figure(figsize=(10, 8))
plt.title('Gender of Teenagers')
plt.pie(gender_teenager, autopct='%.2f', labels=gender_teenager.index)
plt.show()


print("Flight Status Count")
print(data_frame["Flight Status"].value_counts())
plt.figure(figsize=(10, 7))
plt.title("Flight Status Count")
plt.bar(["Canceled", "On Time", "Delay"], data_frame["Flight Status"].value_counts(), width=0.9)
plt.xlabel("Flight status")
plt.ylabel("Count")
plt.show()


print(data_frame.columns)
male_df = data_frame[data_frame["Gender"] == "Male"]
female_df = data_frame[data_frame["Gender"] == "Female"]
print("Male flight status count\n", male_df["Flight Status"].value_counts())
print("\nFemale flight status count\n", female_df["Flight Status"].value_counts())
print("\nFlight status of Different Genders")
plt.figure(figsize=(18, 6))
ax1 = sns.countplot(x="Gender", hue="Flight Status", data=data_frame, palette="Greens", width=0.7)
legend_label, _ = ax1.get_legend_handles_labels()
ax1.legend()
plt.title("Flight status in Different Genders", size=20)
plt.xlabel("Gender")
plt.ylabel("Flight status count")
plt.show()


print(data_frame.columns)
print("\nFlight status in Different Continents")
plt.figure(figsize=(12, 6))
ax1 = sns.countplot(x="Continents", hue="Flight Status", data=data_frame, palette="bright")
legend_label1, _ = ax1.get_legend_handles_labels()
ax1.legend()
plt.title("Flight status in Different Continents", size=20)
plt.xlabel("Continents")
plt.ylabel("Flight status Count")
plt.show()


print("\nMonth of departure")
List = []
for data in data_frame["Departure Date"]:
    List.append(data.split("/")[0])
data_frame["month"] = List
ontime_flight = data_frame[data_frame["Flight Status"] == "On Time"]
delay_flight = data_frame[data_frame["Flight Status"] == "Delayed"]
cancel_flight = data_frame[data_frame["Flight Status"] == "Cancelled"]


print("\nTop 10 Pilots with Canceled flight status")
top_10_pilot = cancel_flight['Pilot Name'].value_counts()[:10]
print(top_10_pilot)

plt.figure(figsize=(10, 8))
plt.title('Top 10 Pilots with canceled flight status')
plt.pie(top_10_pilot, autopct='%.2f', labels=top_10_pilot.index)
plt.show()


print("\nTop 10 Pilots with delay flight status")
top_10_pilot = delay_flight['Pilot Name'].value_counts()[:10]
print(top_10_pilot)

plt.figure(figsize=(10, 8))
plt.title('Top 10 Pilots with delay flight status')
plt.pie(top_10_pilot, autopct='%.2f', labels=top_10_pilot.index)
plt.show()


print("\nTop 10 Airports with delay flight status")
top_10_airports = delay_flight['Airport Name'].value_counts()[:10]
print(top_10_airports)

plt.figure(figsize=(10, 8))
plt.title('Top 10 Airports with delay flight status')
plt.pie(top_10_airports, autopct='%.2f', labels=top_10_airports.index)
plt.show()


print("\nTop 10 Countries with delay flight status")
top_10_country = delay_flight['Country Name'].value_counts()[:10]
print(top_10_country)

plt.figure(figsize=(10, 8))
plt.title('Top 10 Countries with delay flight status')
plt.pie(top_10_country, autopct='%.2f', labels=top_10_country.index)
plt.show()


print("\nFlight Status according to month")
plt.figure(figsize=(12, 6))
plt.title("Flight Status according to month")
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ontime_flight["month"].value_counts(), label="On Time")
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], delay_flight["month"].value_counts(), label="Delayed")
plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], cancel_flight["month"].value_counts(), label="Cancelled")
plt.xlabel("Months")
plt.ylabel("Flight Status")
plt.legend()
plt.show()
