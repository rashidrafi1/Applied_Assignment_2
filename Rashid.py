import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



agriculture_file_path = r'E:\NEW\Agriculture.csv'
cereal_file_path = r'E:\NEW\cereal.csv'

# Import Agriculture


# Remove null values from Agriculture.csv
agriculture_data = agriculture_data.dropna()

# Remove null values from cereal.csv
cereal_data = cereal_data.dropna()

# Display the first 5 rows of Agriculture.csv after removing null values
print("Agriculture.csv after removing null values:")
print(agriculture_data.head())

# Display the first 5 rows of cereal.csv after removing null values
print("\ncereal.csv after removing null values:")
print(cereal_data.head())




# Select the five countries from Agriculture.csv
# Select the five countries from Agriculture.csv
agriculture_data_selected = agriculture_data[agriculture_data['Country Name'].isin(['Berlin', 'Bangladesh', 'Brazil', 'Botswana', 'India'])]

# Select the five countries from cereal.csv
cereal_data_selected = cereal_data[cereal_data['Country Name'].isin(['Berlin', 'Bangladesh', 'Brazil', 'Botswana', 'India'])]

# Calculate mean, median, and mode for Agriculture.csv from 2012 to 2020
agriculture_mean = agriculture_data_selected.loc[:, '2012':'2020'].mean()
agriculture_median = agriculture_data_selected.loc[:, '2012':'2020'].median()
agriculture_mode = agriculture_data_selected.loc[:, '2012':'2020'].mode()

# Calculate mean, median, and mode for cereal.csv from 2012 to 2020
cereal_mean = cereal_data_selected.loc[:, '2012':'2020'].mean()
cereal_median = cereal_data_selected.loc[:, '2012':'2020'].median()
cereal_mode = cereal_data_selected.loc[:, '2012':'2020'].mode()

# Print the results
print("Mean of Agriculture.csv:")
print(agriculture_mean)
print("\nMedian of Agriculture.csv:")
print(agriculture_median)
print("\nMode of Agriculture.csv:")
print(agriculture_mode)

# Replace missing values in cereal_data_selected with the mean value of the column
cereal_data_selected.fillna(cereal_data_selected.mean(), inplace=True)
cereal_data_selected.fillna(cereal_data_selected.mean(), inplace=True)
cereal_data_selected.fillna(cereal_data_selected.mean(), inplace=True)

# Replace missing values in cereal_data_selected with zero
cereal_data_selected.fillna(12.3, inplace=True)

print("\nMean of cereal.csv:")
print(cereal_mean)
print("\nMedian of cereal.csv:")
print(cereal_median)
print("\nMode of cereal.csv:")
print(cereal_mode)


# Select the five countries from Agriculture.csv
agriculture_data_selected = agriculture_data[agriculture_data['Country Name'].isin(['Berlin', 'Bangladesh', 'Brazil', 'Botswana', 'India'])]

# Calculate mean for Agriculture.csv from 2012 to 2020
agriculture_mean = agriculture_data_selected.loc[:, '2012':'2020'].mean()

# Convert mean to a pandas DataFrame
agriculture_mean_df = pd.DataFrame(agriculture_mean, columns=['Mean'])

# Plot histogram of mean values
ax = agriculture_mean_df.plot(kind='bar', figsize=(10,6), legend=None)
ax.set_xticklabels(agriculture_mean_df.index, rotation=0)
ax.set_xlabel('Years')
ax.set_ylabel('Mean values')
ax.set_title('Mean of Agriculture.csv from 2012 to 2020')
plt.show()



# Create a sample Agriculture dataframe with manual values
agriculture_data = pd.DataFrame({
    'Country Name': ['Berlin', 'Bangladesh', 'Brazil', 'Botswana', 'India'],
    '2012': [15, 12, 18, 10, 20],
    '2013': [18, 14, 22, 12, 24],
    '2014': [20, 16, 26, 14, 28],
    '2015': [22, 18, 30, 16, 32],
    '2016': [25, 20, 34, 18, 36],
    '2017': [28, 24, 38, 20, 40],
    '2018': [30, 28, 42, 22, 44],
    '2019': [32, 32, 46, 24, 48],
    '2020': [35, 36, 50, 26, 52],
})

# Create a sample Cereal dataframe with manual values
cereal_data = pd.DataFrame({
    'Country Name': ['Berlin', 'Bangladesh', 'Brazil', 'Botswana', 'India'],
    '2012': [200, 180, 250, 150, 300],
    '2013': [220, 200, 280, 170, 320],
    '2014': [240, 220, 300, 190, 340],
    '2015': [260, 240, 320, 210, 360],
    '2016': [280, 260, 340, 230, 380],
    '2017': [300, 280, 360, 250, 400],
    '2018': [320, 300, 380, 270, 420],
    '2019': [340, 320, 400, 290, 440],
    '2020': [360, 340, 420, 310, 460],
})

# Set the 'Country Name' column as the index for both dataframes
agriculture_data.set_index('Country Name', inplace=True)
cereal_data.set_index('Country Name', inplace=True)

# Plot line chart for Agriculture dataframe
agriculture_data.T.plot(kind='line', xlabel='Year', ylabel='Value', title='Agriculture Data', figsize=(8,5))
plt.show()

# Plot line chart for Cereal dataframe
cereal_data.T.plot(kind='line', xlabel='Year', ylabel='Value', title='Cereal Data', figsize=(8,5))
plt.show()



# Create sample data for agriculture and cereal dataframes
agriculture_data = pd.DataFrame({
    'Country Name': ['India', 'Pakistan', 'Bangladesh', 'Nepal', 'Sri Lanka'],
    '2012': [50, 60, 70, 80, 90],
    '2013': [55, 65, 75, 85, 95],
    '2014': [60, 70, 80, 90, 100],
    '2015': [65, 75, 85, 95, 105],
    '2016': [70, 80, 90, 100, 110],
    '2017': [75, 85, 95, 105, 115],
    '2018': [80, 90, 100, 110, 120],
    '2019': [85, 95, 105, 115, 125],
    '2020': [90, 100, 110, 120, 130],
})

cereal_data = pd.DataFrame({
    'Country Name': ['India', 'Pakistan', 'Bangladesh', 'Nepal', 'Sri Lanka'],
    '2012': [10, 20, 30, 40, 50],
    '2013': [15, 25, 35, 45, 55],
    '2014': [20, 30, 40, 50, 60],
    '2015': [25, 35, 45, 55, 65],
    '2016': [30, 40, 50, 60, 70],
    '2017': [35, 45, 55, 65, 75],
    '2018': [40, 50, 60, 70, 80],
    '2019': [45, 55, 65, 75, 85],
    '2020': [50, 60, 70, 80, 90],
})

# Create a heatmap for agriculture data
plt.figure(figsize=(10, 5))
sns.heatmap(agriculture_data.loc[:, '2012':'2020'], cmap='YlGnBu', annot=True, fmt='.0f', linewidths=1)
plt.title('Agriculture Data Heatmap')
plt.xlabel('Year')
plt.ylabel('Country')
plt.show()

# Create a heatmap for cereal data
plt.figure(figsize=(10, 5))
sns.heatmap(cereal_data.loc[:, '2012':'2020'], cmap='YlGnBu', annot=True, fmt='.0f', linewidths=1)
plt.title('Cereal Data Heatmap')
plt.xlabel('Year')
plt.ylabel('Country')
plt.show()



