import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os
import csv
import math

# Create data file if it doesn't exist
filename = "students_data.csv"
if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math", "Physics", "Chemistry"])

# Load data
def load_data():
    return pd.read_csv(filename)

# Save data
def save_data(df):
    df.to_csv(filename, index=False)
# Add a new student
def add_student(name, math_score, physics_score, chemistry_score):
    df = load_data()
    new_row = {"Name": name, "Math": math_score, "Physics": physics_score, "Chemistry": chemistry_score}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)

# Delete a student by name
def delete_student(name):
    df = load_data()
    df = df[df["Name"] != name]
    save_data(df)

# Calculate average scores
def calculate_averages():
    df = load_data()
    df["Average"] = df[["Math", "Physics", "Chemistry"]].mean(axis=1)
    return df

# Show statistics
def show_statistics():
    df = calculate_averages()
    print(df.describe())
# Plot data
def plot_scores():
    df = calculate_averages()
    plt.figure(figsize=(10,6))
    sns.barplot(x="Name", y="Average", data=df, palette="Set2")
    plt.title("Student Averages")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("student_averages.png")
    plt.show()

# Example usage
add_student("Ahmet", 80, 75, 90)
add_student("Ayşe", 85, 88, 92)
add_student("Mehmet", 70, 60, 65)

print("📄 Veriler yüklendi:")
print(load_data())

print("\n📊 İstatistikler:")
show_statistics()

print("\n📈 Grafik çiziliyor...")
plot_scores()