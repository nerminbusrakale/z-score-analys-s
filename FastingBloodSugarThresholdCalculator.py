from scipy.stats import norm

mu = 120  # Mean value
sigma = 25  # Standard deviation

# Calculate the Z-score
z_score = norm.ppf(1 - 0.05)  # Calculate the Z-score for the upper 5% tail

# Calculate the fasting blood sugar threshold
fasting_blood_sugar_threshold = mu + z_score * sigma

print(f"The threshold value for considering fasting blood sugar as high for 5% of adults is: {fasting_blood_sugar_threshold:.2f} mg/dL and above.")
