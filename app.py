import pandas as pd
import matplotlib.pyplot as plt

# In order to read .csv file , we need to use "pd.read_csv("filename")" function.
file = pd.read_csv('dataforanalysis.csv')

# ".head()" method is used to print first few rows of "file"
print(f"{file.head()}")

# ".describe()" : A method used to get statistical(count, mean, min, max, median,quartile etc) values of those column which contains "number"

print(file.describe())

# "file.isnull().sum()" : It will show the missing values in each column and if no values is missing , it will simply display 0 against column(missed value)
print(f"Missing Values : \n {file.isnull().sum()}")

# In order to calculate average , we use "mean()" method
print("Average of Age column : \n", file['Age'].mean())

# ".nunique()" : A methods which returns number of unique values in given column.
print(f"Unique values in Age column : \n {file['Name'].nunique()}")


# If we want to filter data we can do like this ...
# Let's say we want those whose department is 'Engineering',we can get like this..
print(f'Engineering Employess are :\n {file[file['Department'] == 'Sales']}')

# Can get the maximum salary among all the salaries by using 'max()'
print(f"Maximum Salary is : {file['Salary'].max()}")

# This is how we can get the data of those who get paid most among all
print(f'The Data of Person who get maximum salary is :\n {file[file['Salary']==file['Salary'].max()]}')

# Can get the number of emoloyee in each department like this or count frequency by using '.value_counts()'
print("The Number of Employee in Each Department are : \n", file['Department'].value_counts())

# Can get the number of emoloyee in specific department like this or count frequency by using '.value_counts()'
print("The Number of employee in Sales is : \n", file[file['Department'] == 'Sales'].value_counts())


# We can sort data by using ".sort_values(by='column_name')"
# note : .sort_values(by='Age', ascending=False) will trigger descending order or vice-versa.
print(f"Senior to Junior Sorting : \n{file.sort_values(by="Age", ascending=False)}")
# print(file.sort_values(by='Salary'))

# 
print(file[file["Age"] >= 30])


# Creating a Column "Experience" and assignig "senior/junior"
file['Experience'] = file["Age"].apply(lambda x : 'senior' if x >= 30 else 'junior')
print("The file with another Column named Experience is : \n\n",file)

# Data Visualisation
# With the help of "matplotlib" we can represent data in charts
# here we are going to represent no of employee in each department in "pie_chart"


#                       --- This is how we plot a piechart ---
# here, labels = file["Department"].value_counts().index : here ".index" will get the index of departments and store it into labels
# 'autopct = %1.1f%%' says no fraction value will be shown ,only in whole number.
# plt.figure(figsize=(8, 6))      # setting up window size

# ".pie(number_count, labels_of_each_count, percentage, viewing_angle)" : a method used to create a 'pie-chart'.
# plt.pie(file["Department"].value_counts(), labels=file["Department"].value_counts().index, autopct='%1.1f%%', startangle=90)
# plt.title("Department")
# plt.show()