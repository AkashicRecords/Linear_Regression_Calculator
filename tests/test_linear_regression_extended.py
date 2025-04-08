import pytest
from Lin_Calc import LinearRegression
from typing import List, Union

def test_fit_with_invalid_input_types():
    """Test fit method with invalid input types"""
    model = LinearRegression()
    
    # Test with non-list/tuple inputs
    with pytest.raises(TypeError, match="X and y must be lists or tuples"):
        model.fit("1,2,3", [1,2,3])
    
    with pytest.raises(TypeError, match="X and y must be lists or tuples"):
        model.fit([1,2,3], "1,2,3")
    
    # Test with non-numeric values
    with pytest.raises(TypeError, match="All values in X and y must be numeric"):
        model.fit([1,2,"3"], [1,2,3])
    
    with pytest.raises(TypeError, match="All values in X and y must be numeric"):
        model.fit([1,2,3], [1,2,"3"])

def test_fit_with_insufficient_data():
    """Test fit method with insufficient data points"""
    model = LinearRegression()
    
    # Test with single data point
    with pytest.raises(ValueError, match="Need at least 2 data points"):
        model.fit([1], [2])
    
    # Test with empty lists
    with pytest.raises(ValueError, match="Need at least 2 data points"):
        model.fit([], [])

def test_fit_with_mismatched_lengths():
    """Test fit method with mismatched X and y lengths"""
    model = LinearRegression()
    
    with pytest.raises(ValueError, match="X and y must have the same length"):
        model.fit([1,2,3], [1,2])

def test_fit_with_same_x_values():
    """Test fit method with all same X values"""
    model = LinearRegression()
    
    with pytest.raises(ZeroDivisionError, match="Cannot compute slope: all X values are the same"):
        model.fit([1,1,1], [2,3,4])

def test_predict_with_invalid_inputs():
    """Test predict method with invalid inputs"""
    model = LinearRegression()
    
    # Test prediction before fitting
    with pytest.raises(RuntimeError, match="Model must be fitted before making predictions"):
        model.predict(1)
    
    # Fit the model first
    model.fit([1,2,3], [2,4,6])
    
    # Test with non-numeric values
    with pytest.raises(TypeError, match="All input values must be numeric"):
        model.predict("1")
    
    with pytest.raises(TypeError, match="All input values must be numeric"):
        model.predict([1, "2", 3])

def test_predict_with_multiple_values():
    """Test predict method with multiple values"""
    model = LinearRegression()
    model.fit([1,2,3], [2,4,6])
    
    # Test with single value
    assert model.predict(4) == 8.0
    
    # Test with multiple values
    predictions = model.predict([4,5,6])
    assert len(predictions) == 3
    assert all(isinstance(p, float) for p in predictions)
    assert predictions[0] == 8.0
    assert predictions[1] == 10.0
    assert predictions[2] == 12.0 