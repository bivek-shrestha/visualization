import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Sample data creation
np.random.seed(42)
data = {
    'CustomerID': np.arange(1, 101),
    'Age': np.random.randint(18, 70, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'AnnualIncome': np.random.randint(20000, 120000, 100),
    'SpendingScore': np.random.randint(1, 100, 100)
}

df = pd.DataFrame(data)
df.head()


plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=20, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='AnnualIncome', data=df)
plt.title('Annual Income by Gender')
plt.xlabel('Gender')
plt.ylabel('Annual Income')
plt.show()


plt.figure(figsize=(10, 6))
sns.barplot(x='Gender', y='SpendingScore', data=df, ci=None)
plt.title('Average Spending Score by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Spending Score')
plt.show()

plt.figure(figsize=(10, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix Heatmap')
plt.show()

sns.pairplot(df, hue='Gender', diag_kind='kde', palette='coolwarm')
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(df['CustomerID'], df['AnnualIncome'], marker='o', linestyle='-')
plt.title('Annual Income Trend')
plt.xlabel('CustomerID')
plt.ylabel('Annual Income')
plt.show()

gender_counts = df['Gender'].value_counts()
fig = go.Figure(data=[go.Pie(labels=gender_counts.index, values=gender_counts.values)])
fig.update_layout(title_text='Gender Distribution')
fig.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='AnnualIncome', y='SpendingScore', hue='Gender', data=df, palette='coolwarm')
plt.title('Annual Income vs. Spending Score')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()
