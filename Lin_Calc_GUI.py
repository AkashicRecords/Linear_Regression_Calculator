import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from Lin_Calc import LinearRegression

class LinearRegressionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear Regression Calculator")
        self.model = LinearRegression()
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Data input section
        ttk.Label(main_frame, text="Input Data", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=5)
        
        # X values input
        ttk.Label(main_frame, text="X values (comma-separated):").grid(row=1, column=0, sticky=tk.W)
        self.x_entry = ttk.Entry(main_frame, width=40)
        self.x_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # Y values input
        ttk.Label(main_frame, text="Y values (comma-separated):").grid(row=2, column=0, sticky=tk.W)
        self.y_entry = ttk.Entry(main_frame, width=40)
        self.y_entry.grid(row=2, column=1, padx=5, pady=2)
        
        # Fit button
        ttk.Button(main_frame, text="Fit Model", command=self.fit_model).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Model status
        self.status_label = ttk.Label(main_frame, text="Model Status: Not Fitted", foreground="red")
        self.status_label.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Prediction section
        ttk.Label(main_frame, text="Make Prediction", font=('Helvetica', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=5)
        
        # X value for prediction
        ttk.Label(main_frame, text="X value to predict:").grid(row=6, column=0, sticky=tk.W)
        self.predict_entry = ttk.Entry(main_frame, width=40)
        self.predict_entry.grid(row=6, column=1, padx=5, pady=2)
        
        # Predict button
        ttk.Button(main_frame, text="Predict", command=self.make_prediction).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Result display
        self.result_label = ttk.Label(main_frame, text="")
        self.result_label.grid(row=8, column=0, columnspan=2, pady=5)
        
        # Create matplotlib figure for plotting
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().grid(row=9, column=0, columnspan=2, pady=10)
        
        # Add some sample data
        self.x_entry.insert(0, "1, 2, 3, 4, 5")
        self.y_entry.insert(0, "2, 4, 5, 4, 5")
    
    def parse_input(self, input_str):
        """Convert comma-separated string to list of floats"""
        try:
            # Split and strip whitespace
            values = [x.strip() for x in input_str.split(',')]
            
            # Check for empty input
            if not values or all(x == '' for x in values):
                raise ValueError("Please enter some values")
                
            # Convert to floats
            return [float(x) for x in values if x]
        except ValueError as e:
            if str(e) == "Please enter some values":
                raise
            raise ValueError("Please enter valid numbers separated by commas")
    
    def fit_model(self):
        """Fit the model with input data and update the plot"""
        try:
            # Get and parse input data
            X = self.parse_input(self.x_entry.get())
            y = self.parse_input(self.y_entry.get())
            
            # Fit the model
            self.model.fit(X, y)
            
            # Update the plot
            self.ax.clear()
            self.ax.scatter(X, y, color='blue', label='Data points')
            
            # Plot the regression line
            x_line = np.linspace(min(X), max(X), 100)
            y_line = self.model.predict(x_line)
            self.ax.plot(x_line, y_line, color='red', label='Regression line')
            
            self.ax.set_xlabel('X')
            self.ax.set_ylabel('Y')
            self.ax.legend()
            self.ax.grid(True)
            
            self.canvas.draw()
            
            # Update status
            self.status_label.config(text="Model Status: Fitted", foreground="green")
            messagebox.showinfo("Success", "Model fitted successfully!")
            
        except Exception as e:
            self.status_label.config(text="Model Status: Not Fitted", foreground="red")
            messagebox.showerror("Error", str(e))
    
    def make_prediction(self):
        """Make a prediction for the input X value"""
        try:
            if not self.model.is_fitted:
                messagebox.showerror("Error", "Please fit the model first by clicking 'Fit Model'")
                return
                
            x_pred = float(self.predict_entry.get())
            y_pred = self.model.predict(x_pred)
            
            self.result_label.config(text=f"Predicted Y value: {y_pred:.2f}")
            
            # Update plot to show prediction point
            self.ax.scatter([x_pred], [y_pred], color='green', s=100, label='Prediction')
            self.ax.legend()
            self.canvas.draw()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for prediction")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearRegressionGUI(root)
    root.mainloop() 