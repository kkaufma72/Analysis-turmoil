from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Prepare data for linear regression
X = trend_data.index.values.reshape(-1, 1)  # Using index as a proxy for time since linear regression requires numerical values
y = trend_data['Proportion of Nonfamily Households (%)'].values.reshape(-1, 1)

# Initialize and fit the linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Predictions
y_pred = lin_reg.predict(X)

# Plotting the regression line over the actual data
plt.figure(figsize=(12, 8))
plt.scatter(X + 2014, y, color='blue', label='Actual Data')
plt.plot(X + 2014, y_pred, color='red', linewidth=2, label='Regression Line')

plt.xlabel('Year', fontsize=14)
plt.ylabel('Proportion of Nonfamily Households (%)', fontsize=14)
plt.title('Linear Regression on Proportion of Nonfamily Households (2014-2021)', fontsize=16)
plt.legend()
plt.grid(True)
plt.show()

# Displaying the model's performance metrics
print(f"Coefficient of determination (R^2): {r2_score(y, y_pred):.2f}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y, y_pred):.2f}")
