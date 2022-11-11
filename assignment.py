"""
Created on Fri Nov  4 22:39:39 2022

@author: aparnapinto
"""

import pandas as pd
import matplotlib.pyplot as plt

#Reading a csv file 
treatment_data = pd.read_csv('Tuberculosis_Treatment_Success_Rate.csv')

#Choosing specific rows(Country name) and year from the csv file 
selected_data = treatment_data[203:212]
year = ['2017', '2018', '2019']



def lineplot():
    """This function is used to create a lineplot using iteration"""
    plt.figure()
    lab=["2017","2018","2019"]
    for i in range(year.__len__()):
        plt.plot(selected_data['Country Name'], selected_data[year[i]],label = lab[i])
    plt.xlabel("Countries")
    plt.ylabel("Treatment success rate (in %)")
    plt.title("Tuberculosis Treatment Success Rate (in %)")
    plt.xticks(rotation = 90)
    plt.legend(loc="upper left")
    plt.savefig("lineplot.png", bbox_inches = "tight")
    plt.show()
    

def bargraph():
    """This function is used to create a bar graph"""
    plt.figure(1)
    plt.bar(selected_data["Country Name"],selected_data['2017'])
    plt.xlabel("Countries")
    plt.ylabel("Treatment success rate (in %)")
    plt.title("Tuberculosis Treatment Success Rate in 2017 (in %)")
    plt.xticks(rotation = 90)
    plt.savefig("bargraph.png", bbox_inches = "tight")
    plt.show(1)


def boxplot():
    """This function is used to create a boxplot"""
    plt.figure(2)
    selected1 = treatment_data[203:207]
    plt.boxplot([selected1["2017"], selected1["2018"], selected1["2019"] ],
                labels = ["2017","2018","2019"])
    plt.xlabel("Year")
    plt.ylabel("Treatment success rate (in %)")
    plt.title("Comparison of Tuberculosis Treatment Success Rate of Rwanda,\n South Asia, Saudi Arabia, Sudan in 2017,2018 and 2019(in %)")
    plt.savefig("boxplot.png")
    plt.show(2)


#Calling functions
lineplot()
bargraph()
boxplot()
