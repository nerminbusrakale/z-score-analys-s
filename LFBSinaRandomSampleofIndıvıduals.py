from scipy.stats import norm
import csv

# Define the parameters
mu = 120  # Mean
sigma = 25  # Standard deviation
X = 70  # Fasting blood sugar threshold
n = 1000  # Sample size

# Calculate the Z-score
z_score = (X - mu) / sigma

# Calculate the proportion with low fasting blood sugar
low_sugar_proportion = norm.cdf(z_score)

# Calculate the number of people with low fasting blood sugar in a sample of 1000
low_sugar_count = int(low_sugar_proportion * n)

# Save the result in a CSV file
with open('respiratory.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Proportion of people with low fasting blood sugar", low_sugar_proportion])
    csvwriter.writerow(["Number of people with low fasting blood sugar in a sample of 1000", low_sugar_count])

print(f"Proportion of people with low fasting blood sugar: {low_sugar_proportion:.4f}")
print(f"Number of people with low fasting blood sugar in a sample of 1000: {low_sugar_count}")
