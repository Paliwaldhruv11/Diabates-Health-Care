import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to visualize health metrics
def app():
    st.title("📊 Patient Health Metrics Dashboard")

    sns.set_theme(style="whitegrid", palette="Set2")
    plt.rcParams.update(
        {
            "figure.facecolor": "#ffffff",
            "axes.facecolor": "#f8fafc",
            "axes.edgecolor": "#94a3b8",
            "axes.labelcolor": "#134e4a",
            "text.color": "#134e4a",
            "xtick.color": "#365451",
            "ytick.color": "#365451",
            "grid.color": "#cbd5e1",
            "grid.alpha": 0.6,
        }
    )

    # Simulated glucose level data (With & Without Medication)
    days = np.arange(1, 31)
    glucose_no_med = np.random.normal(loc=180, scale=20, size=len(days))
    glucose_with_med = glucose_no_med - np.random.normal(loc=40, scale=10, size=len(days))

    # Line chart: Glucose trend with & without medication
    fig, ax = plt.subplots()
    ax.plot(days, glucose_no_med, marker="o", linestyle="-", label="Without Medication", color="#c026d3", linewidth=2)
    ax.plot(days, glucose_with_med, marker="s", linestyle="--", label="With Medication", color="#0d9488", linewidth=2)
    ax.set_title("Glucose Level Trend", fontweight="bold")
    ax.set_xlabel("Days")
    ax.set_ylabel("Glucose Level (mg/dL)")
    ax.legend(frameon=True, facecolor="white", edgecolor="#e2e8f0")
    fig.tight_layout()
    st.pyplot(fig)

    # Simulated Insulin level comparison (Patient vs Healthy)
    patient_insulin = np.random.normal(loc=12, scale=2, size=1)[0]
    healthy_insulin = 15

    # Bar chart: Insulin level comparison
    fig, ax = plt.subplots()
    ax.bar(["Patient"], [patient_insulin], color="#0d9488", label="Patient", width=0.45)
    ax.bar(["Healthy"], [healthy_insulin], color="#7c3aed", label="Healthy", width=0.45)
    ax.set_title("Insulin Levels Comparison", fontweight="bold")
    ax.set_ylabel("Insulin Level (μU/mL)")
    ax.legend(frameon=True, facecolor="white", edgecolor="#e2e8f0")
    fig.tight_layout()
    st.pyplot(fig)

    # Simulated Diabetes Class Distribution
    diabetes_classes = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"]
    diabetes_distribution = np.random.randint(10, 50, size=len(diabetes_classes))

    # Pie chart: Diabetes class distribution
    fig, ax = plt.subplots()
    colors = ["#0d9488", "#14b8a6", "#7c3aed", "#a78bfa", "#c026d3"]
    ax.pie(
        diabetes_distribution,
        labels=diabetes_classes,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        textprops={"color": "#134e4a", "fontsize": 10},
    )
    ax.set_title("Diabetes Classification Distribution", fontweight="bold")
    fig.tight_layout()
    st.pyplot(fig)

# Run the dashboard
if __name__ == "__main__":
    app()