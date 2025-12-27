# Exam Score Predictor

## Summary
This project is a simple AI tool that predicts a student's exam score based on the number of hours they have studied. It helps students plan their study schedule to achieve their desired grades.

## Background
The problem is that students often struggle to manage their time effectively. They don't know how much effort is needed to pass or get an 'A'.
This is common among high school and university students.
* Problem: Time management and grade anxiety.
* Solution: A linear regression model to estimate scores.

## How is it used?
The user inputs the number of hours they intend to study. The AI calculates and outputs the predicted score (0-100).
It can be used as a simple command-line tool or integrated into a study planning app.

## Data sources and AI methods
I am using a simple Linear Regression method.
The logic is based on the formula: `Score = Base_Knowledge + (Learning_Rate * Hours)`.
For this prototype, I used synthetic data to simulate the relationship between hours and grades.

## Challenges
The model assumes a linear relationship, which isn't always true (studying 20 hours a day might reduce efficiency due to tiredness). Also, it doesn't account for the difficulty of the subject.

## What next?
To improve this, I would:
* Add more features like "Sleep hours" and "Previous grades".
* Use real student data to train the model.
* Create a web interface.

## Acknowledgments
* Elements of AI course for the inspiration.
