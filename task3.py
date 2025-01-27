
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
def load_dataset():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(url)

# Line chart: Trends over time
def plot_line_chart(df):
    # Creating a fake time-series column for demonstration
    df['time'] = range(1, len(df) + 1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['sepal_length'], label="Sepal Length", color='blue', linewidth=2)
    plt.plot(df['time'], df['sepal_width'], label="Sepal Width", color='green', linewidth=2)
    plt.title("Trends in Sepal Dimensions Over Time", fontsize=14)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Length (cm)", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Bar chart: Comparison of a numerical value across categories
def plot_bar_chart(df):
    avg_values = df.groupby("species")["petal_length"].mean().reset_index()
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x="species", y="petal_length", data=avg_values, palette="viridis")
    plt.title("Average Petal Length per Species", fontsize=14)
    plt.xlabel("Species", fontsize=12)
    plt.ylabel("Average Petal Length (cm)", fontsize=12)
    plt.show()

# Histogram: Distribution of a numerical column
def plot_histogram(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal_length'], bins=20, kde=True, color="skyblue")
    plt.title("Distribution of Sepal Length", fontsize=14)
    plt.xlabel("Sepal Length (cm)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.show()

# Scatter plot: Relationship between two numerical columns
def plot_scatter_plot(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species", palette="deep", s=100)
    plt.title("Sepal Length vs. Petal Length", fontsize=14)
    plt.xlabel("Sepal Length (cm)", fontsize=12)
    plt.ylabel("Petal Length (cm)", fontsize=12)
    plt.legend(title="Species")
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Load dataset
    df = load_dataset()

    # Generate visualizations
    print("1. Line Chart:")
    plot_line_chart(df)
    
    print("2. Bar Chart:")
    plot_bar_chart(df)
    
    print("3. Histogram:")
    plot_histogram(df)
    
    print("4. Scatter Plot:")
    plot_scatter_plot(df)

if __name__ == "__main__":
    main()
