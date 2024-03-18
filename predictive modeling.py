# Predicting future proportions of nonfamily households for the next five years (2022-2026)
future_years_index = np.array([7, 8, 9, 10, 11]).reshape(-1, 1)  # Extending the index for prediction
future_years = np.array([2022, 2023, 2024, 2025, 2026])  # Future years for prediction
future_proportions = lin_reg.predict(future_years_index)

# Plotting future predictions along with the existing trend
plt.figure(figsize=(12, 8))
plt.scatter(X + 2014, y, color='blue', label='Historical Data')
plt.plot(X + 2014, y_pred, color='red', linestyle='--', label='Regression Line')
plt.scatter(future_years, future_proportions, color='green', label='Predicted Data')
plt.plot(future_years, future_proportions, color='green', linestyle='-', label='Predicted Trend')

plt.xlabel('Year', fontsize=14)
plt.ylabel('Proportion of Nonfamily Households (%)', fontsize=14)
plt.title('Predicted Trend in Proportion of Nonfamily Households (2022-2026)', fontsize=16)
plt.legend()
plt.grid(True)
plt.show()

# Displaying future proportions
for year, proportion in zip(future_years, future_proportions.flatten()):
    print(f"Year {year}: Predicted Proportion of Nonfamily Households (%) = {proportion:.2f}")
