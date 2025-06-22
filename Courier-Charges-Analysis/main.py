"""
Project Name: "Optimizing Courier Costs: Analyzing Delivery Partner Charges for Accuracy"
Project Type: Data cleaning and Data Analysis
Project Creator: Prakhar Tripathi
Project Provided by: Cointab Software Private Limited
Project Description: This is a project based on the Courier Cost Optimization analysis, in which we have to verify the
reason of higher charge taken by courier company, for the delivery of the products.
Also, we have to create an Excel sheet of dataset that contain some specific data.
"""

"""
Business Problem......

You are a data analyst and your client has a large ecommerce company in India (let’s call it X).
X gets a thousand orders via their website on a daily basis and they have to deliver them as fast
as they can. For delivering the goods ordered by the customers, X has tied up with multiple
courier companies in India as delivery partners who charge them some amount per delivery.

The charges are dependent upon two factors:
    -Weight of the product
    -Distance between the warehouse (pickup location) and customer’s delivery address (destination location)

On an average, the delivery charges are Rs. 100 per shipment. So if X ships 1,00,000 orders
per month, they have to pay approximately Rs. 1 crore to the courier companies on a monthly
basis as charges.

As the amount that X has to pay to the courier companies is very high, they want to verify if the
charges levied by their Delivery partners per Order are correct. 
"""

# Step 1: Importing all the dependencies that we need in this project.

import pandas as pd  # It is used to analyze big data and make conclusions based on statistical theories.
import numpy as np  # It is used to work on array.
from datetime import date  # It is used to fetch the date.
import pandas_datareader as dr  # It provides very effective way to access data.

# We need openpyxl, to read the Excel data easily. (pip install openpyxl)

# Step 2: Dataset Description

"""
In this project we have five Excel sheets, that contain different information, 
we have to use all these information in this project, Name of the sheets are as follows....
1. Company-X Order Report
2. Company-X Pincode Zones
3. Company-X SKU Master
4. Courier Company-Invoice
5. Courier Company-Rates 
"""

# Step 3: Loading Dataset

# 1. Company X - Pincode Zones

pincode_z_data = pd.read_excel("./data/Company X - Pincode Zones.xlsx")

# Checking the dataset
print(pincode_z_data.info())

# Top 5 data value of pincode_z_data
print(pincode_z_data.head())

# Performing some data cleaning and transformation on data of pincode_z_data

# Renaming the Zone column in pincode_z_data
rename_zone_X = pincode_z_data.rename(columns={"Zone": "Delivery Zone as per X"}, inplace=True)

# Checking the changes
print(pincode_z_data.sample())

# 2. Courier Company - Invoice

courier_invoice_data = pd.read_excel("./data/Courier Company - Invoice.xlsx")

# Checking the dataset
print(courier_invoice_data.info())

# Top 5 data value of courier_invoice_data
print(courier_invoice_data.head())

# Performing some data cleaning and transformation on data of courier_invoice_data

# Renaming the Zone column in courier_invoice_data
courier_invoice_data.rename(columns={"Zone": "Delivery Zone charged by Courier Company",
                                     "Charged Weight": "Total Weight As Per Courier Company (KG)"}, inplace=True)

# Checking the changes
print(courier_invoice_data.sample())

# 3. Company X - Order Report

order_report_data = pd.read_excel("./data/Company X - Order Report.xlsx")

# Checking the dataset
print(order_report_data.info())

# Top 5 data value of order_report_data
print(order_report_data.head())

# Performing some data cleaning and transformation on data of order_report_data

# Renaming the Zone column in order_report_data
order_report_data.rename(columns={"ExternOrderNo": "Order ID"}, inplace=True)

# Checking the changes
print(order_report_data.sample())

# 4. Company X - SKU Master

sku_master_data = pd.read_excel("./data/Company X - SKU Master.xlsx")

# Checking the dataset
print(sku_master_data.info())

# Top 5 data value of sku_master_data
print(sku_master_data.head())

# 5. Courier Company - Rates

courier_rates_data = pd.read_excel("./data/Courier Company - Rates.xlsx")

# Checking the dataset
print(courier_rates_data.info())

# Describe data value of courier_rates_data
print(courier_rates_data.describe())

# Step 4: EDA(Exploratory data analysis) Task

# Merging the order_report_data and sku_master_data
sku_order_merge_data = pd.merge(order_report_data, sku_master_data, how="left", on="SKU")

# Checking the changes
print(sku_order_merge_data.info())
print(sku_order_merge_data.head())

# Removing the NA or NIL values from sku_order_merge_data
print(sku_order_merge_data.dropna())

# Removing duplicates from pincode_z_data with respect to Customer Pincode Column
X_courier_merge_data = pincode_z_data.drop_duplicates(subset=["Customer Pincode"])

# Fetching specific column from courier_invoice_data
courier_X_merge_data = courier_invoice_data[["Order ID", "Customer Pincode", "Type of Shipment"]]

# Merging the pincode_z_data with courier_invoice_data with respect to customer pincode
pincode_z_merge_data = courier_X_merge_data.merge(X_courier_merge_data, on="Customer Pincode")

# Checking the changes
print(pincode_z_merge_data.sample())

# Merging the sku_order_merge_data with pincode_z_merge_data by order id
sku_order_pincode_merge_data = sku_order_merge_data.merge(pincode_z_merge_data, on="Order ID")

# Checking the changes
print(sku_order_pincode_merge_data.sample())

# Rename some columns in sku_order_pincode_merge_data
sku_order_pincode_merge_rename_data = sku_order_pincode_merge_data.rename(
    columns={"Order Qty": "Order_Qty", "Weight (g)": "Weight_g"})

# Calculates the total weight per shipment based on the order quantity and weight in grams.

kg = 1000  # kg is a kind of variable that store 1000 as a value

convert_g_to_kg = """Total_Weight_Per_Shipment = (Order_Qty*Weight_g)/@kg"""

sku_order_pincode_merge_rename_data.eval(convert_g_to_kg, inplace=True, engine="python")

# Checking the weight column in sku_order_pincode_merge_rename_data
print(sku_order_pincode_merge_rename_data["Weight_g"].value_counts())

# Checking the Type of shipment column in sku_order_pincode_merge_rename_data
print(sku_order_pincode_merge_rename_data["Type of Shipment"].value_counts())

# Checking the columns of sku_order_pincode_merge_rename_data
print(sku_order_pincode_merge_rename_data.columns)

# Rename the columns name of sku_order_pincode_merge_rename_data
rename_data_sku_pincode_merge = sku_order_pincode_merge_rename_data.rename(
    columns={"Order_Qty": "Order Qty",
             "Total_Weight_Per_Shipment": "Total Weight AS Per X (KG)", "Weight_g": "Weight (g)"})

# Checking the changes in sku_order_pincode_merge_rename_data
print(rename_data_sku_pincode_merge.sample())


# Creating the Function for Assigning Weight Slab

def assign_weight_slab(weight):
    i = round(weight % 1, 1)
    if i == 0.0:
        return weight
    elif i > 0.5:
        return int(weight) + 1.0
    else:
        return int(weight) + 0.5


# Creating the weight slab column

rename_data_sku_pincode_merge["Weight Slab As Per X (KG)"] = (
    rename_data_sku_pincode_merge["Total Weight AS Per X (KG)"].apply(assign_weight_slab))

courier_invoice_data["Weight Slab Charged By Courier Company (KG)"] = (
    courier_invoice_data['Total Weight As Per Courier Company (KG)']).apply(assign_weight_slab)

# Checking the changes in sku_order_pincode_merge_rename_data
print(rename_data_sku_pincode_merge.columns)
print(courier_invoice_data["Weight Slab Charged By Courier Company (KG)"])

# Calculating Expected Charge
total_expected_charge = []

for i in range(len(rename_data_sku_pincode_merge)):
    fwd_category = "fwd_" + rename_data_sku_pincode_merge["Delivery Zone as per X"][i]
    fwd_fixed = courier_rates_data[fwd_category + '_fixed'][0]
    fwd_additional = courier_rates_data[fwd_category + "_additional"][0]
    rto_category = "rto_" + rename_data_sku_pincode_merge["Delivery Zone as per X"][i]
    rto_fixed = courier_rates_data[rto_category + "_fixed"][0]
    rto_additional = courier_rates_data[rto_category + "_additional"][0]

    if rename_data_sku_pincode_merge["Type of Shipment"][i] == "Forward charges":
        if rename_data_sku_pincode_merge["Weight Slab As Per X (KG)"][i] < 0.5:
            total_expected_charge.append(fwd_fixed)
        else:
            additional_weight = (rename_data_sku_pincode_merge["Weight Slab As Per X (KG)"][i] - 0.5) / 0.5
            total_expected_charge.append(fwd_fixed + additional_weight * fwd_additional)

    if rename_data_sku_pincode_merge["Type of Shipment"][i] == "Forward and RTO charges":
        if rename_data_sku_pincode_merge["Weight Slab As Per X (KG)"][i] <= 0.5:
            total_expected_charge.append(fwd_fixed + rto_fixed)
        else:
            additional_weight = (rename_data_sku_pincode_merge["Weight Slab As Per X (KG)"][i] - 0.5) / 0.5
            total_expected_charge.append(fwd_fixed + additional_weight * (fwd_additional + rto_additional))
rename_data_sku_pincode_merge["Expected Charge As Per X (Rs.)"] = total_expected_charge
print(rename_data_sku_pincode_merge.columns)

# Saving the columns in Output 2
Output2 = rename_data_sku_pincode_merge[['Order ID',
                                         'Type of Shipment', 'Delivery Zone as per X',
                                         'Total Weight AS Per X (KG)', 'Weight Slab As Per X (KG)',
                                         'Expected Charge As Per X (Rs.)']]

#  Printing the columns of courier_invoice_data
print(courier_invoice_data.columns)

# Saving all the columns in Output1
Output1 = courier_invoice_data[['AWB Code', 'Order ID', 'Total Weight As Per Courier Company (KG)',
                                'Delivery Zone charged by Courier Company', 'Billing Amount (Rs.)',
                                'Weight Slab Charged By Courier Company (KG)']]

# Merging the Output1 and Output2 data together
merge_output = Output2.merge(Output1, on="Order ID", how="left")

# Checking the changes
print(merge_output.columns)

# Step 5: Result Time

# Now we copy the output data into resultant_output_1
resultant_output1 = merge_output.copy()

# Renaming some columns of resultant_output1
resultant_output1 = resultant_output1.rename(
    columns={'AWB Code': 'AWB Number', 'Billing Amount (Rs.)': 'Charges_Billed_By_Courier_Company_Rs',
             'Expected Charge As Per X (Rs.)': 'Expected_Charge_As_Per_X_Rs'})

# Checking the changes in resultant_output_1
print(resultant_output1.columns)

# Calculating the Difference Between Expected Charges And Billed Charges
diff_bw_ec_bc = """
Difference_Between_Expected_Charges_and_Billed_Charges_Rs =(Expected_Charge_As_Per_X_Rs - Charges_Billed_By_Courier_Company_Rs)
"""
resultant_output1.eval(diff_bw_ec_bc, inplace=True, engine='python')

# Renaming the columns of resultant_output1
resultant_output1 = resultant_output1.rename(
    columns={'Charges_Billed_By_Courier_Company_Rs': 'Charges Billed By Courier Company (Rs.)',
             'Expected_Charge_As_Per_X_Rs': 'Expected Charge As Per X (Rs.)',
             'Difference_Between_Expected_Charges_and_Billed_Charges_Rs': 'Difference Between Expected Charges And '
                                                                          'Billed Charges (Rs.)'})

# Create an excel file of Result
writer = pd.ExcelWriter('./data/Final_Result.xlsx', if_sheet_exists="replace", engine='openpyxl', mode="a")

# Feed the data in the excel file Final_Result
resultant_output1.to_excel(writer, sheet_name='Calculations')
calculations = writer._save()

# Calculation Of Total Orders
correctly_charged = resultant_output1[
    resultant_output1['Difference Between Expected Charges And Billed Charges (Rs.)'] == 0.0]
correctly = ["Total Orders where ABC has been correctly charged", len(correctly_charged),
             sum(correctly_charged['Charges Billed By Courier Company (Rs.)'])]

over_charged = resultant_output1[
    resultant_output1['Difference Between Expected Charges And Billed Charges (Rs.)'] < 0.0]
over = ["Total Orders where ABC has been over charged", len(over_charged),
        np.absolute(sum(over_charged['Difference Between Expected Charges And Billed Charges (Rs.)']))]

under_charged = resultant_output1[
    resultant_output1['Difference Between Expected Charges And Billed Charges (Rs.)'] > 0.0]
under = ["Total Orders where ABC has been under charged", len(under_charged),
         np.absolute(sum(under_charged['Difference Between Expected Charges And Billed Charges (Rs.)']))]

resultant_output2 = pd.DataFrame([correctly, over, under], columns=['Description', 'Count', 'Amount (Rs.)'])

# Checking the changes in resultant_output2
print(resultant_output2)

# Feed the data in sheet
resultant_output2.to_excel(writer, sheet_name='Summary')
summary = writer._save()