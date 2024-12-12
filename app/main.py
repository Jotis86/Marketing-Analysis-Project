import streamlit as st
from PIL import Image
import os

# Obtener la ruta absoluta de la carpeta actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar imágenes
main_image_path = os.path.join(current_dir, "portada.png")
menu_image_path = os.path.join(current_dir, "menu.png")
main_image = Image.open(main_image_path)
menu_image = Image.open(menu_image_path)

# Función para mostrar la página principal
def show_home():
    st.image(main_image, use_column_width=True)
    st.title("📊 Marketing Analysis Project")
    st.write("""
    Welcome to the Marketing Analysis Project. This application provides an interactive and detailed analysis of key marketing metrics to support strategic decision-making.
    
    ## Introduction
    In today's competitive market, understanding customer behavior and optimizing marketing strategies are crucial for business success. This project aims to leverage data analysis and visualization tools to provide actionable insights into marketing performance.

    ## Features
    - **Interactive Dashboards**: Explore various metrics and KPIs through interactive Power BI dashboards.
    - **Data Analysis**: Detailed data cleaning, transformation, and analysis using Python.
    - **Visualizations**: Comprehensive visualizations to uncover patterns and trends in the data.
    """)

# Función para mostrar la sección de objetivos
def show_objectives():
    st.image(main_image, use_column_width=True)
    st.title("📌 Objectives")
    st.write("""
    The objective of this project is to provide an interactive and detailed analysis of key marketing metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.
    
    ## Specific Goals
    - **Data Integration**: Combine data from various sources to create a unified dataset.
    - **Data Cleaning**: Remove duplicates, handle missing values, and normalize data to ensure accuracy.
    - **Data Enrichment**: Add calculated columns and transform data to enhance analysis.
    - **Interactive Dashboards**: Develop Power BI dashboards to visualize key metrics and KPIs.
    - **Detailed Analysis**: Use Python for in-depth data analysis and visualization.
    """)

# Función para mostrar la sección de proceso de desarrollo
def show_development_process():
    st.image(main_image, use_column_width=True)
    st.title("🔄 Development Process")
    st.write("""
    The development process for this project involved several key steps to ensure accurate and insightful analysis.

    ## Steps
    1. **Extraction**: Data obtained from CSV files.
    2. **Transformation**:
       - **Power BI**:
         - Combining tables using Power Query.
         - Data cleaning: Removing duplicates, handling null values, and normalizing data.
         - Data enrichment: Adding calculated columns and transforming data to improve analysis.
       - **Python**:
         - Data cleaning with pandas: Removing duplicates, handling null values, and normalizing data.
         - Data enrichment: Adding calculated columns and transforming data to improve analysis.
    3. **Load**:
       - **Power BI**: Integrating transformed data into Power BI for analysis and visualization.
       - **Python**: Preparing data for visualization and analysis in Jupyter notebooks and Streamlit.

    ## Tools Used
    - **Power BI**: For interactive dashboards and data visualization.
    - **Python**: For data cleaning, transformation, and analysis.
    - **Pandas**: For data manipulation and analysis.
    - **Seaborn & Matplotlib**: For creating visualizations.
    """)

# Función para mostrar la sección de resultados
def show_results():
    st.image(main_image, use_column_width=True)
    st.title("📈 Results")
    st.write("""
    Various metrics have been created using **DAX (Data Analysis Expressions)** in Power BI to provide detailed and customized analysis.

    ## Key Metrics
    - **KPIs Calculation**: Key Performance Indicators to measure marketing effectiveness.
    - **Calculated Measures**: Specific measures for detailed analysis.
    - **Calculated Columns**: Enriching the dataset with additional information.
    - **Filtering and Dynamic Segmentation**: Allowing for detailed and customized views of the data.

    ## Python Analysis
    - **Data Cleaning**: Detailed processes to ensure data accuracy.
    - **Visualizations**: Creation of visualizations to explore and present data insights.
    - **Interactive App**: Development of an interactive Streamlit app to dynamically explore the results.

    ## Insights
    - **Customer Behavior**: Understanding how different customer segments behave.
    - **Marketing Performance**: Evaluating the effectiveness of various marketing campaigns.
    - **Sales Trends**: Identifying trends and patterns in sales data.
    """)

# Función para mostrar la sección de Power BI
def show_power_bi():
    st.image(main_image, use_column_width=True)
    st.title("📊 Power BI Dashboard")
    st.write("""
    Here are some screenshots of the Power BI dashboard:

    - **Dashboard 1**: Overview of key metrics and KPIs.
    - **Dashboard 2**: Detailed analysis of customer segments.
    - **Dashboard 3**: Performance of marketing campaigns.
    - **Dashboard 4**: Sales trends and patterns.
    - **Dashboard 5**: Interactive filters and dynamic views.
    """)
    st.image(os.path.join(current_dir, "screenshot_1.png"), caption="Power BI Dashboard 1", use_column_width=True)
    st.image(os.path.join(current_dir, "screenshot_2.png"), caption="Power BI Dashboard 2", use_column_width=True)
    st.image(os.path.join(current_dir, "screenshot_3.png"), caption="Power BI Dashboard 3", use_column_width=True)
    st.image(os.path.join(current_dir, "screenshot_4.png"), caption="Power BI Dashboard 4", use_column_width=True)
    st.image(os.path.join(current_dir, "screenshot_5.png"), caption="Power BI Dashboard 5", use_column_width=True)

# Función para mostrar la sección de conclusiones
def show_conclusions():
    st.image(main_image, use_column_width=True)
    st.title("📜 Conclusions")
    st.write("""
    The analysis provided valuable insights into key marketing metrics and customer behavior. The interactive dashboards and visualizations helped identify patterns and opportunities for strategic decision-making. The combination of Power BI and Python proved to be effective in handling and analyzing large datasets.

    ## Key Takeaways
    - **Data-Driven Decisions**: Leveraging data to make informed marketing decisions.
    - **Customer Insights**: Gaining a deeper understanding of customer behavior and preferences.
    - **Marketing Optimization**: Identifying areas for improvement in marketing strategies.
    - **Future Work**: Potential areas for further analysis and exploration.

    ## Acknowledgements
    We would like to thank everyone who contributed to this project, including data providers, analysts, and developers.
    """)

# Menú de navegación
st.sidebar.image(menu_image, use_column_width=True)
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Objectives", "Development Process", "Results", "Power BI", "Conclusions"])

# Botón para ir al repositorio de GitHub
st.sidebar.markdown("[GitHub Repository](https://github.com/Jotis86/Marketing-Analysis-Project)")

# Mostrar la sección seleccionada
if menu == "Home":
    show_home()
elif menu == "Objectives":
    show_objectives()
elif menu == "Development Process":
    show_development_process()
elif menu == "Results":
    show_results()
elif menu == "Power BI":
    show_power_bi()
elif menu == "Conclusions":
    show_conclusions()