
import pandas as pd

# Load the dataset
def load_dataset():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    try:
        df = pd.read_csv(url)
        print("Dataset loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Compute basic statistics
def compute_statistics(df):
    print("\nBasic statistics of numerical columns:")
    print(df.describe())  # Includes mean, median (50%), std, min, max, etc.

# Perform groupings and compute mean for each group
def perform_grouping(df):
    print("\nMean of numerical columns grouped by 'species':")
    grouped = df.groupby("species").mean()  # Compute mean for each group
    print(grouped)
    return grouped

# Analyze patterns or findings
def analyze_findings(grouped):
    print("\nAnalysis of patterns:")
    # Identify patterns or findings
    for column in grouped.columns:
        max_group = grouped[column].idxmax()
        min_group = grouped[column].idxmin()
        print(
            f"- For '{column}', '{max_group}' species has the highest mean ({grouped.loc[max_group, column]:.2f}) and "
            f"'{min_group}' species has the lowest mean ({grouped.loc[min_group, column]:.2f})."
        )

# Main function
def main():
    # Load dataset
    df = load_dataset()
    if df is None:
        return

    # Compute basic statistics
    compute_statistics(df)

    # Perform groupings and compute mean
    grouped = perform_grouping(df)

    # Analyze patterns or interesting findings
    analyze_findings(grouped)

if __name__ == "__main__":
    main()
