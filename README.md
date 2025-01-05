# Diwali Sales Analysis

### The table of contents

- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Data Preparation](#data-preparation)
- [Data Cleansing](#data-cleansing)
- [Exploratory Data Analysis](#exploratory-data-analysis)


### Project Overview

This project aims to demonstrate the step by step data cleaning and EDA process on Diwali Sales Dataset to uncover insights and patterns in consumer behavior during the Diwali festival. By analyzing sales data from various age catagories, this project seeks to identify trends that can inform future sales strategies and improve customer engagement.

### Data Source

The dataset used for the project was taken from a GitHub repositry with clients, product and sale revenue information. It has 11251 rows and 15 columns. 

### Data Preparation

The raw data (CSV) file was uploaded directly to the Jupytor Notebook without making any changes to perform Data Cleaning steps later. It had 11251 rows and 15 columns initially, which came down to 11239 rows and 13 columns after cleaning the data.


## Data Cleansing

**1. Importing the dataset**

```python
df = pd.read_csv(r"C:\Users\aslam\OneDrive\Desktop\Python\Data Analytics Panda\Diwali Sales Data.csv")
```
![image](https://github.com/user-attachments/assets/aad56e48-4fea-47ff-9188-4cd0252423eb)


**2. Dropping unwantted columns "Status" & "unnamed1"**

```python
df = df.drop(columns = 'Status')
```
```python
df = df.drop(columns = 'unnamed1')
```
![image](https://github.com/user-attachments/assets/2ac984eb-f995-4913-8aee-4842b89c46e5)


**3. Checking Null values and dropping them from the database**

```python
df = df.isnull().sum()
```
```python
df = df.dropna()
```
![image](https://github.com/user-attachments/assets/fba7bff9-69f9-4226-beda-15268b7b80c3)


## Exploratory Data Analysis

**4. Who spent the most amount while shopping?**

```python
df.groupby('Gender')['Amount'].sum()
```
![image](https://github.com/user-attachments/assets/356cdad2-c3d3-4818-8453-d3800f4a8cf0)


**5. What is the total spent based on age groups?**

```python
df.groupby('Age Group')['Amount'].sum()
```
![image](https://github.com/user-attachments/assets/dff19694-2863-4239-b050-bb7f8e0067c8)

**6. What is the order count statewise?**

```python
df.groupby('State')['Orders'].sum().sort_values(ascending=False)
```
![image](https://github.com/user-attachments/assets/e09992b6-2375-489c-9044-6bfbfdd8851c)


**7. What are the best performing states from top to bottom?**

```python
df.groupby('State').agg({'Amount': 'sum', 'Orders': 'sum'}).sort_values(by='Amount', ascending=False)
```
![image](https://github.com/user-attachments/assets/35f1fd84-7ec4-4dd3-8cf2-31a89dc1fc9e)


**8. What is the total sales revenue generated by different sectors?**

```python
df.groupby('Occupation')['Amount'].sum().sort_values(ascending=False)
```
![image](https://github.com/user-attachments/assets/37559c18-edfa-4873-acff-f06523839ff4)


**9. What are the top 5 peoduct catagories in terms of sale revenue?**

```python
df.groupby('Product_Category').agg({'Amount': 'sum', 'Orders': 'sum'}).sort_values(by='Amount', ascending=False).head()
```
![image](https://github.com/user-attachments/assets/243ba9f7-1d01-47b8-907d-4c170a4f1a16)


> [!NOTE]
> The full coding details can be found on the file attached to the repositry.


