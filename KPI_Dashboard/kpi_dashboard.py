import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

# Step 1: Load the dataset
def load_data(file_path):
    """Load the sales dataset from an Excel file."""
    df = pd.read_excel(file_path)
    print(df.columns)
    return df
# Step 2: Calculate KPIs
def calculate_kpis(df):
    """Calculate the required KPIs."""
    # Adding necessary columns
    df['Year'] = pd.to_datetime(df['Date']).dt.year

    # Grouping by year and category
    grouped = df.groupby(['Year', 'Category'])

    # Calculating KPIs
    kpi_data = grouped.agg(
        Total_Sales=('TotalSales', 'sum'),
        Quantity_Sold=('QuantitySold', 'sum'),
        Avg_Price=('PricePerUnit', 'mean')
    ).reset_index()

    # Average Order Value (AOV)
    kpi_data['AOV'] = kpi_data['Total_Sales'] / kpi_data['Quantity_Sold']

    # Placeholder for ROMS (assuming a fixed marketing spend)
    marketing_spend = 10000  # Example static spend per category per year
    kpi_data['ROMS'] = kpi_data['Total_Sales'] / marketing_spend

    return kpi_data

# Step 3: Create Visualizations
def create_visualizations(kpi_data, output_dir):
    """Generate and save visualizations for the KPIs."""

    os.makedirs(output_dir, exist_ok=True)

    sns.set_theme(style="whitegrid")

    # Visualization 1: Total Sales per Category
    plt.figure(figsize=(10, 6))
    sns.barplot(data=kpi_data, x='Category', y='Total_Sales', hue='Year')
    plt.title('Total Sales by Category and Year')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/total_sales.png")

    # Visualization 2: ROMS per Category
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=kpi_data, x='Category', y='ROMS', hue='Year', marker='o')
    plt.title('Return on Marketing Spend (ROMS) by Category and Year')
    plt.xlabel('Category')
    plt.ylabel('ROMS')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/roms.png")

    # Visualization 3: Average Order Value per Category
    plt.figure(figsize=(10, 6))
    sns.barplot(data=kpi_data, x='Category', y='AOV', hue='Year')
    plt.title('Average Order Value (AOV) by Category and Year')
    plt.xlabel('Category')
    plt.ylabel('AOV')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/aov.png")

# Step 4: Generate Dashboard Output
def generate_dashboard(df, kpi_data, output_path):
    """Generate a PDF dashboard containing visualized KPIs and raw data."""
    with PdfPages(output_path) as pdf:
        # Page 1: Raw Data
        plt.figure(figsize=(10, 6))
        plt.axis('tight')
        plt.axis('off')
        table_data = df.head(20)  # Display first 20 rows
        plt.table(cellText=table_data.values, colLabels=table_data.columns, loc='center', cellLoc='center')
        plt.title('Raw Data')
        pdf.savefig()
        plt.close()

        # Page 2: Total Sales Chart
        img = plt.imread("output/total_sales.png")
        plt.figure(figsize=(10, 6))
        plt.imshow(img)
        plt.axis('off')
        pdf.savefig()
        plt.close()

        # Page 3: ROMS Chart
        img = plt.imread("output/roms.png")
        plt.figure(figsize=(10, 6))
        plt.imshow(img)
        plt.axis('off')
        pdf.savefig()
        plt.close()

        # Page 4: AOV Chart
        img = plt.imread("output/aov.png")
        plt.figure(figsize=(10, 6))
        plt.imshow(img)
        plt.axis('off')
        pdf.savefig()
        plt.close()

# Main Function
def main():
    file_path = 'D:\Pilgrims\KPI_Dashboard\Sales Data.xls'  # Replace with your file path
    output_dir = 'output'
    output_pdf = f'{output_dir}/kpi_dashboard.pdf'

    # Load data
    df = load_data(file_path)

    # Calculate KPIs
    kpi_data = calculate_kpis(df)

    # Create visualizations
    create_visualizations(kpi_data, output_dir)

    # Generate dashboard
    generate_dashboard(df, kpi_data, output_pdf)
    print(f"Dashboard generated: {output_pdf}")

if __name__ == "__main__":
    main()
