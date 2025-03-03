# -*- coding: utf-8 -*-
"""Assignment_8 _Data_Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18Aty5Oi0klt387dGLcinuEIus5xocRlz

Create a line plot using matplotlib pyplot that displays the population of four different cities over time.
"""

import matplotlib.pyplot as plt

# Data for the four cities
city_a_population = [500000, 550000, 600000, 650000, 700000, 750000, 800000]
city_b_population = [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
city_c_population = [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000]
city_d_population = [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]

# Years for the x-axis
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

# Create the line plot
plt.plot(years, city_a_population, label='City A')
plt.plot(years, city_b_population, label='City B')
plt.plot(years, city_c_population, label='City C')
plt.plot(years, city_d_population, label='City D')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth of Four Cities')

# Add legend
plt.legend()

# Show the plot
plt.show()

"""Create a scatter plot using seaborn that shows the relationship between the number of hours studied and the test scores obtained by a group of students."""

import seaborn as sns
import matplotlib.pyplot as plt

# Data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]

# Create the scatter plot
sns.scatterplot(x=hours_studied, y=test_scores)

# Add labels and title
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.title('Relationship Between Hours Studied and Test Scores')

# Show the plot
plt.show()

"""Create a bar chart using matplotlib pyplot that shows the total sales for each month of the year."""

import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]

# Create the bar chart
plt.bar(months, sales)

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Total Sales per Month")

# Show the plot
plt.show()