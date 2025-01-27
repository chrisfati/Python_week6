
import pandas as pd

# Load the dataset
def load_dataset():
    # Iris dataset URL (can be replaced with a local file path if needed)
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(url)
        print("Dataset loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Inspect the dataset
def inspect_dataset(df):
    print("\nFirst few rows of the dataset:")
    print(df.head())

    print("\nDataset structure:")
    print(df.info())

    print("\nChecking for missing values:")
    print(df.isnull().sum())

# Clean the dataset
def clean_dataset(df):
    if df.isnull().values.any():
        print("\nCleaning the dataset by filling missing values...")
        df.fillna(method='ffill', inplace=True)
        print("Missing values filled using forward fill method.")
    else:
        print("\nNo missing values found. No cleaning needed.")
    return df

# Main function
def main():
    # Step 1: Load the dataset
    df = load_dataset()
    if df is None:
        return

    # Step 2: Inspect the dataset
    inspect_dataset(df)

    # Step 3: Clean the dataset
    df_cleaned = clean_dataset(df)

    # Step 4: Display the cleaned dataset's structure
    print("\nCleaned dataset structure:")
    print(df_cleaned.info())

if __name__ == "__main__":
    main()
