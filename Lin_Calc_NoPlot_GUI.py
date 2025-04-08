import tkinter as tk
from tkinter import ttk, messagebox
from Lin_Calc import LinearRegression

class LinearRegressionSimpleGUI:
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
        
        # Model equation
        self.equation_label = ttk.Label(main_frame, text="Equation: y = mx + b")
        self.equation_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Prediction section
        ttk.Label(main_frame, text="Make Prediction", font=('Helvetica', 12, 'bold')).grid(row=6, column=0, columnspan=2, pady=5)
        
        # X value for prediction
        ttk.Label(main_frame, text="X value to predict:").grid(row=7, column=0, sticky=tk.W)
        self.predict_entry = ttk.Entry(main_frame, width=40)
        self.predict_entry.grid(row=7, column=1, padx=5, pady=2)
        
        # Predict button
        ttk.Button(main_frame, text="Predict", command=self.make_prediction).grid(row=8, column=0, columnspan=2, pady=10)
        
        # Result display
        self.result_label = ttk.Label(main_frame, text="")
        self.result_label.grid(row=9, column=0, columnspan=2, pady=5)
        
        # Data visualization (table)
        ttk.Label(main_frame, text="Data Points", font=('Helvetica', 12, 'bold')).grid(row=10, column=0, columnspan=2, pady=5)
        
        # Create treeview for data display
        self.tree = ttk.Treeview(main_frame, columns=('x', 'y', 'predicted'), show='headings', height=5)
        self.tree.grid(row=11, column=0, columnspan=2, pady=10)
        
        # Configure columns
        self.tree.heading('x', text='X value')
        self.tree.heading('y', text='Y value')
        self.tree.heading('predicted', text='Predicted Y')
        self.tree.column('x', width=100, anchor='center')
        self.tree.column('y', width=100, anchor='center')
        self.tree.column('predicted', width=100, anchor='center')
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=11, column=2, sticky='ns')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
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
        """Fit the model with input data and update the display"""
        try:
            # Get and parse input data
            X = self.parse_input(self.x_entry.get())
            y = self.parse_input(self.y_entry.get())
            
            # Fit the model
            self.model.fit(X, y)
            
            # Update the equation display
            self.equation_label.config(text=f"Equation: y = {self.model.slope:.2f}x + {self.model.intercept:.2f}")
            
            # Clear the tree
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Add data to the tree
            for i, (x_val, y_val) in enumerate(zip(X, y)):
                predicted = self.model.predict(x_val)
                self.tree.insert('', 'end', values=(f"{x_val:.2f}", f"{y_val:.2f}", f"{predicted:.2f}"))
            
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
            
            # Add prediction to the tree with a special tag
            self.tree.insert('', 'end', values=(f"{x_pred:.2f}", "N/A", f"{y_pred:.2f}"), tags=('prediction',))
            self.tree.tag_configure('prediction', background='light green')
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for prediction")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearRegressionSimpleGUI(root)
    root.mainloop() 