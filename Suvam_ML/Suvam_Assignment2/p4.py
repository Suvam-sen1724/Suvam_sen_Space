"""
Question 4:
A two-dimensional NumPy array representing student scores in different subjects. Each
row represents a student, and each column represents a subject. Write Python code to the
following tasks:
A. Calculate the average score for each subject.
B. Determine which student has the highest average score across all subjects.
C. Find the subject in which the highest-scoring student has scored the lowest.
scores = [
[80, 90, 70, 85, 95],
[75, 85, 95, 70, 80],
[85, 95, 75, 80, 90],
[90, 80, 85, 75, 70]
]
"""
import numpy as np

scores = np.array([
    [80, 90, 70, 85, 95],
    [75, 85, 95, 70, 80],
    [85, 95, 75, 80, 90],
    [90, 80, 85, 75, 70]
])

subject_averages = np.mean(scores, axis=0)
print(f"Average scores for each subject: {subject_averages}\n")

highest_avg_student = np.argmax(np.mean(scores, axis=1))
print(f"Student {highest_avg_student} has the highest average score across all subjects.\n")


lowest_score_subject = np.argmin(scores[highest_avg_student])
print(f"The subject in which the highest-scoring student has scored the lowest is subject {lowest_score_subject}.\n")


"""
Answer:
Average scores for each subject: [82.5  87.5  81.25 77.5  83.75]

Student 2 has the highest average score across all subjects.

The subject in which the highest-scoring student has scored the lowest is subject 2.
"""