import pandas as pd
import matplotlib.pyplot as plt

# Import the csv file
df = pd.read_csv('planettData.csv')

# Make a new data frame which only has the stars with distance less than or equal to 100 light years
df = df[df['distance'] <= 100]

# Keep the stars having gravity in range of 150 to 350
df = df[(df['gravity'] >= 150) & (df['gravity'] <= 350)]

# Create a new csv file
df.to_csv('filtered_stars.csv', index=False)
