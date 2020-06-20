import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('california_housing_train.csv')
age = np.array(df['housing_median_age'])
income = np.array(df['median_income'])
population = np.array(df['population'])
bedroom = np.array(df['total_bedrooms'])
households = np.array(df['households'])
longitude = np.array(df['longitude'])
latitude = np.array(df['latitude'])
coordinates = np.array(df[['longitude','latitude']])
price = np.array(df['median_house_value'])

print(df.head(5))
print(df.tail(5))

avg_age = sum(age)/sum(population)                  
avg_income = sum(income)/sum(population) 
          
print(f'Average Age:{avg_age}')
print(f'Average Income:{avg_income}')

bedroom_max = np.amax(bedroom)
print(f'Maximum number of bedrooms:{bedroom_max}')

household_of_max_bedroom = households[np.argmax(bedroom)]
longitude_of_max_bedroom = longitude[np.argmax(bedroom)]
latitude_of_max_bedroom = latitude[np.argmax(bedroom)]
print(f'Household corresponding to max bedroom:{household_of_max_bedroom}')     
print(f'Longitude corresponding to max bedroom:{longitude_of_max_bedroom}')
print(f'Latitude corresponding to max bedroom:{latitude_of_max_bedroom}')


less_populated_index = np.where(population<600)
less_populated_coordinates = []

for index in less_populated_index:
    less_populated_coordinates.append(coordinates[index])
    
print('Co-ordinates of less populated areas:',less_populated_coordinates)

ax = plt.figure()
boxplot = df.boxplot()
ax = df.plot.kde()
df.plot(kind='hexbin', x=bedroom, y=price, gridsize=25)

range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0
range6 = 0
for house_age in age:
    if house_age<=10:
        range1+=1
    elif house_age>10 and house_age<=20:
        range2+=1
    elif house_age>20 and house_age<=30:
        range3+=1
    elif house_age>30 and house_age<=40:
        range4+=1
    elif house_age>40 and house_age<=50:
        range5+=1
    else:
        range6+=1

fig = plt.figure()
bx = fig.add_axes([0,0,1,1])
bx.axis('equal')

plt.scatter(latitude,longitude)
plt.plot(households,population)
overall_range = [range1,range2,range3,range4,range5,range6]
bx.pie(overall_range , autopct='%1.2f%%')
plt.show()