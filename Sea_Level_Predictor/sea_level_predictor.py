import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])    

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    start = df["Year"].min()
    end = 2050
    bestFit_years = pd.Series(range(start, end+1))
    bestFit_value = pd.Series([result.slope*y + result.intercept for y in range(start, end+1)])
    ax.plot(bestFit_years, bestFit_value, 'b')
    
    # Create second line of best fit
    start = 2000
    result = linregress(df.loc[df['Year']>=start]["Year"], df.loc[df['Year']>=start]["CSIRO Adjusted Sea Level"])
    bestFit_years = pd.Series(range(start, end+1))
    bestFit_value = pd.Series([result.slope*y + result.intercept for y in range(start, end+1)])
    ax.plot(bestFit_years, bestFit_value, 'r')

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()