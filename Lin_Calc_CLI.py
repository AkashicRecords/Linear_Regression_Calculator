#!/usr/bin/env python3
import argparse
import sys
from Lin_Calc import LinearRegression

def parse_numbers(input_str):
    """Convert comma-separated string to list of floats"""
    try:
        return [float(x.strip()) for x in input_str.split(',')]
    except ValueError:
        raise ValueError("Please enter valid numbers separated by commas")

def main():
    parser = argparse.ArgumentParser(description='Linear Regression Calculator')
    parser.add_argument('--fit', action='store_true', help='Fit the model with X and Y values')
    parser.add_argument('--predict', type=float, help='Predict Y value for given X')
    parser.add_argument('--x', help='Comma-separated X values')
    parser.add_argument('--y', help='Comma-separated Y values')
    
    args = parser.parse_args()
    model = LinearRegression()
    
    try:
        if args.fit:
            if not args.x or not args.y:
                print("Error: Both --x and --y values are required for fitting")
                sys.exit(1)
                
            X = parse_numbers(args.x)
            y = parse_numbers(args.y)
            model.fit(X, y)
            
        if args.predict is not None:
            if not model.is_fitted:
                print("Error: Model must be fitted before making predictions")
                print("Use --fit with --x and --y values first")
                sys.exit(1)
                
            y_pred = model.predict(args.predict)
            print(f"\nPrediction for x = {args.predict}:")
            print(f"y = {y_pred:.2f}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 