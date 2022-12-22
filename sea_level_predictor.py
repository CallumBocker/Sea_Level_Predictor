import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    best_fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_Year = pd.Series([i for i in range(1880, 2051)])
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(extended_Year, best_fit1.intercept + best_fit1.slope*extended_Year, 'r')

    # Create second line of best fit
    df2 = df.loc[120:]
    best_fit2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    extended_Year2 = pd.Series([i for i in range(2000, 2051)])
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(extended_Year2, best_fit2.intercept + best_fit2.slope*extended_Year2, 'r')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()