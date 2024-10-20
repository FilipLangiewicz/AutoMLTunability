import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def perform_eda(path):
    
    df = pd.read_csv(path)
    
    print("###### Head of the dataset #####")
    print(df.head(10))
    
    print("##### Tail of the dataset #####")
    print(df.tail(10))
    
    print("##### Info #####")
    df.info()
    
    print("##### Description #####")
    df.describe()
    
    print("##### Null number #####")
    df.isnull().sum()
    
    print("##### Types of the variables #####")
    df.dtypes
    
    print("##### Number of unique values #####")
    df.nunique()
    
    correlation = df.corr().round(2)
    plt.figure(figsize = (14,7))
    sns.heatmap(correlation, annot = True, cmap = 'YlOrBr')
    
    return df

df = perform_eda('./data/college.csv')
    
    
    
    


























def performeda(df):
    # Display basic information about the dataframe
    print("Dataframe Information:")
    print(df.info())
    print("\n")

    # Display basic statistics
    print("Basic Statistics:")
    print(df.describe())
    print("\n")

    # Check for missing values
    print("Missing Values:")
    print(df.isnull().sum())
    print("\n")

    # Display the first few rows of the dataframe
    print("First 5 Rows:")
    print(df.head())
    print("\n")

    # Plot histograms for each numerical feature
    df.hist(bins=30, figsize=(20, 15))
    plt.suptitle('Histograms of Numerical Features')
    plt.show()

    # Plot correlation matrix
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

    # Plot pairplot for numerical features
    sns.pairplot(df)
    plt.suptitle('Pairplot of Numerical Features', y=1.02)
    plt.show()

# Example usage:
# df = pd.read_csv('your_dataset.csv')
# perform_eda(df)