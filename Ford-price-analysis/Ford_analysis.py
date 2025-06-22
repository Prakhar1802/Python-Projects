import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

data_frame = pd.read_csv("Enter the location of the dataset")
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

print("\nExploratory Data Analysis")

print("\nInformation About Dataset")
print(data_frame.info())

print("\nTop 10 rows of dataset")
print(data_frame.head(10))

print("\nLast 10 rows of dataset")
print(data_frame.tail(10))

print("\ncolumns of dataset")
print(data_frame.columns)

print("\nNumber of rows and columns of dataset")
print("Number of rows:", data_frame.shape[0])
print("Number of columns:", data_frame.shape[1])

print("\nCount of Values in dataset")
print(data_frame.value_counts())

print("\nCount values of model")
print(data_frame.model.value_counts())

print("\nRemove values of model")
data_frame = data_frame.drop(data_frame[data_frame.model == "Focus"].index)
print(data_frame.model.value_counts())

print("\nCount values of year")
print(data_frame.year.value_counts())

print("\nRemove values of year")
data_frame = data_frame.drop(data_frame[data_frame.year == 2060].index)
print(data_frame.year.value_counts())

print("\nCount values of price")
print(data_frame.price.value_counts())

print("\nCount values of transmission")
print(data_frame.transmission.value_counts())

print("\nCount values of mileage")
print(data_frame.mileage.value_counts())

print("\nCount values of fuelType")
print(data_frame.fuelType.value_counts())

print("\nCount values of tax")
print(data_frame.tax.value_counts())

print("\nCount values of mpg")
print(data_frame.mpg.value_counts())

print("\nCount values of engineSize")
print(data_frame.engineSize.value_counts())

print("\nStatical description of dataset")
print(data_frame.describe(include="all"))

print("\nComplete dataset")
print(data_frame)


print("\nData Visualization and Analysis")
print("\nPrice analysis based on EngineSize")
print("Price of cars based on their EngineSize\n", data_frame[["engineSize", "price"]])
engine_sizes = data_frame.engineSize
car_prices = data_frame.price
plt.figure(figsize=(8, 6))
plt.scatter(engine_sizes, car_prices, c='grey', marker='o', label='Car Prices')
plt.title('Car Price vs Engine Size')
plt.xlabel('Engine Size in Liter')
plt.ylabel('Price in Dollar')
plt.legend()
plt.show()


print("\nPrice analysis based on mpg")
print("Price of cars based on their MPG\n", data_frame[["mpg", "price"]])
mpg = data_frame.mpg
car_prices = data_frame.price
plt.figure(figsize=(12, 9))
plt.bar(mpg, car_prices, color="g")
plt.title('Car Price vs Mpg')
plt.xlabel('Milage Per Gallon')
plt.ylabel('Price in Dollar')
plt.show()


print("\nPrice analysis based on Year")
print("Price of cars based on year\n", data_frame[["year", "price"]])
year = data_frame.year
car_prices = data_frame.price
plt.figure(figsize=(12, 9))
plt.bar(year, car_prices, color="pink")
plt.title('Car Price vs year')
plt.xlabel('Year')
plt.ylabel('Price in Dollar')
plt.show()


print("\nPrice analysis based on transmission")
print("Price of cars based on transmission\n", data_frame[["transmission", "price"]])
transmission = data_frame.transmission
car_prices = data_frame.price
plt.figure(figsize=(12, 9))
plt.bar(transmission, car_prices, color="orange")
plt.title('Car Price vs transmission')
plt.xlabel('Transmission')
plt.ylabel('Price in Dollar')
plt.show()


print("\nTransmission status in Different Years")
plt.figure(figsize=(12, 6))
ax1 = sns.countplot(x="year", hue="transmission", data=data_frame, palette=["orange", "green", "purple"])
legend_label, _ = ax1.get_legend_handles_labels()
ax1.legend()
plt.title("Transmission status in Different Years", size=20)
plt.xlabel("Year")
plt.ylabel("No. of cars")
plt.show()


print("\nTop 5 models with automatic Transmission status")
automatic_df = data_frame[data_frame['transmission'] == 'Automatic']
status = automatic_df['model'].value_counts()[:5]
print(status)
plt.figure(figsize=(8, 8))
plt.title('Top 5 models with automatic Transmission status')
plt.pie(status, autopct='%.2f', labels=status.index)
plt.show()


print("\nTop 5 models with manual Transmission status")
manual_df = data_frame[data_frame['transmission'] == 'Manual']
status_m = manual_df['model'].value_counts()[:5]
print(status_m)
plt.figure(figsize=(8, 8))
plt.title('Top 5 models with manual Transmission status')
plt.pie(status_m, autopct='%.2f', labels=status_m.index)
plt.show()


print("\nPrice analysis based on tax")
print("Price of cars based on tax\n", data_frame[["tax", "price"]])
tax = data_frame.tax
car_prices = data_frame.price
plt.figure(figsize=(12, 9))
plt.bar(tax, car_prices, color="orange")
plt.title('Car Price vs tax')
plt.xlabel('Tax')
plt.ylabel('Price in Dollar')
plt.show()


print("\nPrice analysis based on Fuel Type")
print("Price of cars based on Fuel Type\n", data_frame[["fuelType", "price"]])
fuel = data_frame.fuelType
car_prices = data_frame.price
plt.figure(figsize=(12, 9))
plt.bar(fuel, car_prices, color="brown")
plt.title('Car Price vs Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price in Dollar')
plt.show()

print("\nSold of different fuel type cars in Different Years")
plt.figure(figsize=(12, 6))
ax1 = sns.countplot(x="year", hue="fuelType", data=data_frame, palette=["grey", "brown", "yellow", "orange", "purple"])
legend_label, _ = ax1.get_legend_handles_labels()
ax1.legend()
plt.title("Sold of different fuel type cars in Different Years", size=20)
plt.xlabel("Year")
plt.ylabel("Number of cars")
plt.show()


print("\nPrice analysis based on mileage")
print("Price of cars based on Fuel Type\n", data_frame[["mileage", "price"]])
mileage = data_frame.mileage
car_prices = data_frame.price
plt.figure(figsize=(12, 9))
plt.scatter(mileage, car_prices, c='magenta', marker='o', label='Car Prices')
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.show()




