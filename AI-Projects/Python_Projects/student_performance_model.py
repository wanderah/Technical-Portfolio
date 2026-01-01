import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# import pandas as pd: Imports the Pandas library, which we'll use to create and manipulate our DataFrame.
# import numpy as np: Imports NumPy, which provides high-performance array operations crucial for calculations.
# import matplotlib.pyplot as plt: Imports the Matplotlib plotting module for creating visualizations.
# from sklearn...: We import the necessary modules from Scikit-learn early, although we won't use them until the modeling step.

# =================================================================
# PART 2: DATA PREPARATION AND VISUALIZATION (Requirements 1 - 5)
# =================================================================

# 1. Input the dataset manually and convert it to a Pandas DataFrame
data = {
    'Hours': [1, 2, 3, 4.5, 5, 6, 7, 8, 9, 10],
    'Scores': [20, 30, 50, 52, 60, 62, 70, 78, 85, 95]
}
df = pd.DataFrame(data)

# data = {...}: We define a Python dictionary. Each key ('Hours', 'Scores') represents a column, and the associated
# ...list holds the data points for that column.

#df = pd.DataFrame(data): This is the Pandas function that converts the structured dictionary into a DataFrame (df),
# ....which is essentially a structured table, fulfilling requirement 1.

# 2. Display the entire dataset
print("--- 2. Initial Dataset (DataFrame) ---")
print(df)

# =================================================================
# PART 3: LINEAR REGRESSION AND MODEL TRAINING (Requirements 6 - 7)
# =================================================================

# 6. Split the dataset into training and testing sets
X = df[['Hours']].values  # Feature (2D array)
y = df['Scores'].values   # Target (1D array)

# 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# 7. Train a Linear Regression model (Univariate Model)
uni_model = LinearRegression()
uni_model.fit(X_train, y_train)

print("\n--- 7. Model Training Results (Univariate) ---")
print(f"Intercept (c): {uni_model.intercept_:.2f}")
print(f"Coefficient (m): {uni_model.coef_[0]:.2f}")
print("-" * 50)

# =================================================================
# PART 4: IMPLEMENT PREDICTIONS (Requirements 8 - 9)
# =================================================================

# 8. Predict the score of a student who studies for 6.5 hours
hours_to_predict = np.array([[6.5]])
predicted_score_6_5 = uni_model.predict(hours_to_predict)

# 9. Display the prediction with clear formatting
print("--- 8 & 9. Prediction for 6.5 Hours ---")
print(f"Predicted Exam Score for 6.5 hours: {predicted_score_6_5[0]:.2f}")
print("-" * 50)

# =================================================================
# PART 5: CALCULATE ERRORS (Requirements 10 - 11)
# =================================================================

# 10. Predict scores for ALL samples in the original DataFrame
df_predictions = uni_model.predict(X)

# Add Predicted Score column
df['Predicted Score'] = df_predictions

# 11. Calculate and add the 'Error' column: Error = Actual Score - Predicted Score
df['Error'] = df['Scores'] - df['Predicted Score']

print("--- 10 & 11. DataFrame with Predicted Score and Error ---")
print(df.round(2))
print("-" * 50)

# =================================================================
# PART 6: VISUALIZATION AND INTERPRETATION (Requirements 12 - 19)
# =================================================================

# 12. Display summary statistics of the dataset
print("--- 12. Summary Statistics ---")
print(df.describe().round(2))

# 13. Check for missing/null values
print("\n--- 13. Missing Values Check ---")
print(df.isnull().sum()) # Output should be all zeros.

# 14, 15, 16, 17, 18, 19. Plotting
plt.figure(figsize=(10, 7))

# 15. Scatter plot of the original data ('Hours' vs. 'Scores')
plt.scatter(df['Hours'], df['Scores'], color='blue', label='Actual Scores', marker='o')

# 16. Scatter plot of 'Hours' vs. 'Predicted Scores'
plt.scatter(df['Hours'], df['Predicted Score'], color='red', label='Predicted Scores', marker='x')

# 14. Plot the regression line
plt.plot(df['Hours'], df['Predicted Score'], color='green', linewidth=2, label='Regression Line (y=mx+c)')

# 4 & 18. Label the plot (Title, X-axis, Y-axis)
plt.title('Hours Studied vs. Scores: Model Fit and Predictions')
plt.xlabel('Study Hours (Feature)')
plt.ylabel('Exam Scores (Target)')

# 17. Add a legend
plt.legend()
plt.grid(True)

# 5 & 19. Display the plot
plt.show()

# =================================================================
# PART 7: MULTIVARIATE REGRESSION (Requirements 20 - 23)
# =================================================================

# 20. Update dataset to include new column Practice_Exams
practice_exams_data = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
df['Practice_Exams'] = practice_exams_data

# 21. Display the new DataFrame
print("--- 21. Multivariate DataFrame ---")
print(df[['Hours', 'Practice_Exams', 'Scores']].round(2))

# 22. Train a new Linear Regression model using both Hours and Practice_Exams
X_multi = df[['Hours', 'Practice_Exams']].values
y_multi = df['Scores'].values

multi_model = LinearRegression()
multi_model.fit(X_multi, y_multi)

# 23. Predict the score for a student who studies 6.5 hours and has 3 practice exams
prediction_case = np.array([[6.5, 3]])
predicted_score_multi = multi_model.predict(prediction_case)

print("\n--- 23. Multivariate Prediction ---")
print(f"Features: Hours=6.5, Practice_Exams=3")
print(f"Multivariate Predicted Score: {predicted_score_multi[0]:.2f}")
print("-" * 50)

# =================================================================
# PART 8: MODEL EVALUATION (Requirement 24)
# =================================================================

# 24. Predict on the test set (using the initial univariate model)
y_pred_test = uni_model.predict(X_test)

print("--- 24. Evaluation on Unseen Test Set ---")
test_results = pd.DataFrame({
    'Actual Score': y_test,
    'Predicted Score': y_pred_test
})
test_results['Difference'] = test_results['Actual Score'] - test_results['Predicted Score']

print("Test Set Prediction vs. Actual (Difference is the error):")
print(test_results.round(2))
print("-" * 50)