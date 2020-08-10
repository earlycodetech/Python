#import csv module to perform csv operations
import csv

#load excel file into jupiter notebook
file = open('npl.csv',mode='r',encoding='utf-8') #using utf-8 encoding ensures that special characters like '@' can be read

#read file as a csv file
reader = csv.reader(file)

#compile read csv data as a python list
data = list(reader)

#iterate through the list to collect data, in this case all ages of the players in the league
age = []
for line in data[1:]:
    age.append(int(line[3]))

#print the list to see the content
print(age)
