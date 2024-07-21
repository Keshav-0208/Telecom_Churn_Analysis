# 📊 Telecom Churn Analysis

This Streamlit application provides a comprehensive analysis of telecom churn data. It allows users to upload a CSV file and generates various visualizations to explore key factors influencing customer churn.

## Features
- 📂 **CSV File Upload:** Users can upload their own CSV files for analysis.
- 🧩 **Data Overview:** Display dataset information including shape, column names, and a preview of the data.
- 📊 **Visualizations:**
  - **Network Usage by State:** Bar chart showing total minutes spent across different states.
  - **Churn Distribution:** Pie chart depicting the proportion of churned vs non-churned users.
  - **Correlation Heatmap:** Heatmap illustrating the correlations between different features.
  - **Churn vs Customer Service Calls:** Line chart showing the relationship between customer service calls and churn rates.
  - **Average Customer Service Calls by State:** Bar chart of the average number of customer service calls across states.

## Algorithms and Techniques
- **Data Processing:** Utilizes Pandas for data manipulation and transformation.
- **Visualization:** Leverages Seaborn and Matplotlib for creating insightful visualizations, including bar charts, pie charts, and heatmaps.
- **Statistical Analysis:** Computes feature correlations and analyzes the impact of customer service calls on churn rates.

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/telecom-churn-analysis.git
    cd telecom-churn-analysis
    ```

2. **Create and activate a virtual environment:**
    - On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Run the Streamlit app:
```sh
streamlit run app.py
