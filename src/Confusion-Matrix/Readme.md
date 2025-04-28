# What is a Confusion Matrix and What is it Used For?

A **confusion matrix** is a technique used to evaluate the performance of a classification model. It shows the relationship between the actual and predicted classes. The matrix contains four important values:

- **True Positives (TP)**: The number of instances that were correctly classified as positive.
- **True Negatives (TN)**: The number of instances that were correctly classified as negative.
- **False Positives (FP)**: The number of instances that were incorrectly classified as positive (Type I error).
- **False Negatives (FN)**: The number of instances that were incorrectly classified as negative (Type II error).

A confusion matrix helps in assessing model performance, and also allows us to compute metrics like accuracy, precision, recall, and F1 score.

## Steps:
1. **Generate a synthetic dataset with 50 instances.**
2. **Train a classification model on this data.**
3. **Compute and visualize the confusion matrix.**
