import numpy as np
from typing import List, Union, Tuple

class LinearRegression:
    """
    A simple linear regression calculator.
    
    This class implements basic linear regression functionality including:
    - Model fitting
    - Prediction
    - Input validation
    
    Requirements:
    - Must call fit() before predict()
    - Input lists must contain only numbers (int or float)
    - Will raise appropriate errors for invalid input or unfitted model
    """
    
    def __init__(self):
        self.slope: float = 0.0
        self.intercept: float = 0.0
        self.is_fitted: bool = False
    
    def fit(self, X: List[float], y: List[float]) -> None:
        """
        Fit the linear regression model to the data.
        
        Args:
            X: List of independent variable values
            y: List of dependent variable values
            
        Raises:
            ValueError: If inputs are invalid or insufficient
            TypeError: If inputs contain non-numeric values
            ZeroDivisionError: If X values are all the same
        """
        # Input validation
        if not isinstance(X, (list, tuple, np.ndarray)) or not isinstance(y, (list, tuple, np.ndarray)):
            raise TypeError("X and y must be lists, tuples, or numpy arrays")
            
        if len(X) != len(y):
            raise ValueError("X and y must have the same length")
            
        if len(X) < 2:
            raise ValueError("Need at least 2 data points for linear regression")
            
        # Check for numeric types
        try:
            X = np.array(X, dtype=float)
            y = np.array(y, dtype=float)
        except (ValueError, TypeError):
            raise TypeError("All values in X and y must be numeric (int or float)")
            
        # Calculate means
        mean_x = np.mean(X)
        mean_y = np.mean(y)
        
        # Calculate slope and intercept
        numerator = np.sum((X - mean_x) * (y - mean_y))
        denominator = np.sum((X - mean_x) ** 2)
        
        if denominator == 0:
            raise ZeroDivisionError("Cannot compute slope: all X values are the same")
            
        self.slope = numerator / denominator
        self.intercept = mean_y - self.slope * mean_x
        self.is_fitted = True
        
        # Print the equation
        print(f"Linear Regression Equation: y = {self.slope:.2f}x + {self.intercept:.2f}")
    
    def predict(self, x: Union[float, List[float]]) -> Union[float, List[float]]:
        """
        Predict y values for given x values.
        
        Args:
            x: Single value or list of values to predict for
            
        Returns:
            Predicted y value(s)
            
        Raises:
            RuntimeError: If model hasn't been fitted
            TypeError: If input contains non-numeric values
        """
        if not self.is_fitted:
            raise RuntimeError("Model must be fitted before making predictions. Call fit() first.")
            
        try:
            if isinstance(x, (int, float)):
                return self.slope * float(x) + self.intercept
            return [self.slope * float(xi) + self.intercept for xi in x]
        except (ValueError, TypeError):
            raise TypeError("All input values must be numeric (int or float)")

# Example usage
if __name__ == "__main__":
    # Sample data
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    
    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    x_new = 6
    y_pred = model.predict(x_new)
    print(f"Predicted y for x = {x_new}: {y_pred:.2f}")
    
    # Example of predicting multiple values
    x_multiple = [6, 7, 8]
    y_pred_multiple = model.predict(x_multiple)
    print(f"Predictions for x = {x_multiple}: {[f'{y:.2f}' for y in y_pred_multiple]}")