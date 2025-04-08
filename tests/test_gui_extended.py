import pytest
import tkinter as tk
from tkinter import messagebox
from Lin_Calc_GUI import LinearRegressionGUI
from unittest.mock import patch, MagicMock

@pytest.fixture
def root():
    root = tk.Tk()
    yield root
    root.destroy()

@pytest.fixture
def app(root):
    return LinearRegressionGUI(root)

def test_create_line_points(app):
    """Test create_line_points method"""
    x_data = [1, 2, 3, 4, 5]
    points = app.create_line_points(x_data)
    
    assert len(points) == 100  # Default num_points
    assert min(points) == 1.0  # min(x_data)
    assert max(points) == 5.0  # max(x_data)
    assert points[0] == 1.0
    assert points[-1] == 5.0
    
    # Test with custom num_points
    points = app.create_line_points(x_data, num_points=5)
    assert len(points) == 5
    assert points == [1.0, 2.0, 3.0, 4.0, 5.0]

@patch('tkinter.messagebox.showerror')
@patch('tkinter.messagebox.showinfo')
def test_fit_model_success(mock_showinfo, mock_showerror, app):
    """Test successful model fitting"""
    # Set up input data
    app.x_entry.insert(0, "1,2,3,4,5")
    app.y_entry.insert(0, "2,4,6,8,10")
    
    # Mock matplotlib methods
    app.ax = MagicMock()
    app.ax.clear = MagicMock()
    app.ax.scatter = MagicMock()
    app.ax.plot = MagicMock()
    app.ax.set_xlabel = MagicMock()
    app.ax.set_ylabel = MagicMock()
    app.ax.legend = MagicMock()
    app.ax.grid = MagicMock()
    app.canvas = MagicMock()
    app.canvas.draw = MagicMock()
    
    # Call fit_model
    app.fit_model()
    
    # Verify model was fitted
    assert app.model.is_fitted
    assert app.status_label.cget("text") == "Model Status: Fitted"
    assert app.status_label.cget("foreground") == "green"
    
    # Verify plot updates
    app.ax.clear.assert_called_once()
    app.ax.scatter.assert_called()
    app.ax.plot.assert_called()
    app.canvas.draw.assert_called_once()
    
    # Verify success message
    mock_showinfo.assert_called_once_with("Success", "Model fitted successfully!")

@patch('tkinter.messagebox.showerror')
def test_fit_model_error(mock_showerror, app):
    """Test model fitting with errors"""
    # Set up invalid input data
    app.x_entry.insert(0, "1,2,a")
    app.y_entry.insert(0, "2,4,6")
    
    # Call fit_model
    app.fit_model()
    
    # Verify error handling
    assert not app.model.is_fitted
    assert app.status_label.cget("text") == "Model Status: Not Fitted"
    assert app.status_label.cget("foreground") == "red"
    mock_showerror.assert_called()

@patch('tkinter.messagebox.showerror')
def test_make_prediction_not_fitted(mock_showerror, app):
    """Test prediction attempt without fitted model"""
    app.predict_entry.insert(0, "6")
    app.make_prediction()
    
    mock_showerror.assert_called_with("Error", "Please fit the model first by clicking 'Fit Model'")

@patch('tkinter.messagebox.showerror')
def test_make_prediction_invalid_input(mock_showerror, app):
    """Test prediction with invalid input"""
    # Fit the model first
    app.x_entry.insert(0, "1,2,3")
    app.y_entry.insert(0, "2,4,6")
    app.fit_model()
    
    # Try invalid prediction
    app.predict_entry.insert(0, "invalid")
    app.make_prediction()
    
    mock_showerror.assert_called_with("Error", "Please enter a valid number for prediction")

@patch('tkinter.messagebox.showerror')
def test_make_prediction_success(mock_showerror, app):
    """Test successful prediction"""
    # Set up and fit model
    app.x_entry.insert(0, "1,2,3")
    app.y_entry.insert(0, "2,4,6")
    app.fit_model()
    
    # Mock matplotlib methods
    app.ax = MagicMock()
    app.ax.scatter = MagicMock()
    app.ax.legend = MagicMock()
    app.canvas = MagicMock()
    app.canvas.draw = MagicMock()
    
    # Make prediction
    app.predict_entry.insert(0, "4")
    app.make_prediction()
    
    # Verify prediction
    assert "Predicted Y value: 8.00" in app.result_label.cget("text")
    app.ax.scatter.assert_called()
    app.canvas.draw.assert_called_once() 