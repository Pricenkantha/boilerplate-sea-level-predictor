import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
     
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    #Perform linear regression for the entire dataset 
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])


    # Create first line of best fit

    years = pd.Series(range(1880, 2051)) 
    sea_levels = intercept + slope * years
    
    #plot the line of best fit for the entite dataset
    plt.plot(years, sea_levels, label='Best Fit Line 1880-2050', color='red')
    
    #Filter data from the year 2000 onwards 
    recent_data = data[data['Year'] >= 2000]
    
    # Perform linear regression on recent data 
    recent_slope, recent_intercept, recent_r_value, recent_p_value, recent_std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    
    #Create a line of best fit for recent data 
    recent_years = pd.Series(range(2000, 2051)) 
    recent_sea_levels = recent_intercept + recent_slope * recent_years
    
    # Plot the recent line of best fit 
    plt.plot(recent_years, recent_sea_levels, label='Best Fit Line 2000-2050', color='green')

    # Add labels and title
    plt.xlabel('Year') 
    plt.ylabel('Sea Level (inches)') 
    plt.title('Rise in Sea Level') 
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()