import random

def predict_score(hours_studied):
    # Simple Linear Regression Logic
    # Let's assume a student knows 20% of the material naturally (intercept)
    # And every hour of study adds roughly 5% to the score (coefficient)
    
    base_score = 20
    learning_rate = 5
    
    # Calculate score
    predicted_score = base_score + (learning_rate * hours_studied)
    
    # Add some randomness/uncertainty (noise)
    predicted_score += random.randint(-5, 5)
    
    # Cap the score at 100 and minimum at 0
    if predicted_score > 100:
        predicted_score = 100
    if predicted_score < 0:
        predicted_score = 0
        
    return predicted_score

# Main execution
if __name__ == "__main__":
    print("--- Exam Score Predictor AI ---")
    try:
        user_input = float(input("Enter hours you plan to study: "))
        result = predict_score(user_input)
        print(f"If you study for {user_input} hours, your predicted score is: {result}/100")
    except ValueError:
        print("Please enter a valid number.")
