import pytest
import numpy as np
from Lin_Calc import LinearRegression

def test_linear_regression_fit():
    # Test case with perfect linear relationship
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]  # y = 2x
    
    model = LinearRegression()
    model.fit(X, y)
    
    assert abs(model.slope - 2.0) < 1e-10
    assert abs(model.intercept) < 1e-10

def test_predict():
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]  # y = 2x
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Test single prediction
    assert abs(model.predict(6) - 12.0) < 1e-10
    
    # Test multiple predictions
    predictions = model.predict([6, 7])
    assert abs(predictions[0] - 12.0) < 1e-10
    assert abs(predictions[1] - 14.0) < 1e-10

def test_input_validation():
    model = LinearRegression()
    
    # Test unequal lengths
    with pytest.raises(ValueError):
        model.fit([1, 2, 3], [1, 2])
    
    # Test insufficient data
    with pytest.raises(ValueError):
        model.fit([1], [1])
    
    # Test non-numeric data
    with pytest.raises(TypeError):
        model.fit(['a', 'b'], [1, 2])

def test_unfitted_model():
    model = LinearRegression()
    
    # Test prediction without fitting
    with pytest.raises(RuntimeError):
        model.predict(1)

def test_prediction_input_validation():
    model = LinearRegression()
    model.fit([1, 2, 3], [2, 4, 6])
    
    # Test non-numeric input
    with pytest.raises(TypeError):
        model.predict('a')
    
    # Test non-numeric list input
    with pytest.raises(TypeError):
        model.predict([1, 'a', 3]) 