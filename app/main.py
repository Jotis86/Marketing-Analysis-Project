import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Marketing Analysis Project", layout="wide")

# Cargar imágenes
main_image = Image.open("app/portada.png")
menu_image = Image.open("app/menu.png")

# Función para mostrar la página principal
def show_home():
    st.image(main_image, use_column_width=True)
    st.title("📊 Marketing Analysis Project")
    st.write("""
    Welcome to the Marketing Analysis Project. This application provides an interactive and detailed analysis of key marketing metrics to support strategic decision-making.
    """)

# Función para mostrar la sección de objetivos
def show_objectives():
    st.title("📌 Objectives")
    st.write("""
    The objective of this project is to provide an interactive and detailed analysis of key marketing metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.
    """)

# Función para mostrar la sección de proceso de desarrollo
def show_development_process():
    st.title("🔄 Development Process")
    st.write("""
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
    """)

# Función para mostrar la sección de resultados
def show_results():
    st.title("📈 Results")
    st.write("""
    Various metrics have been created using **DAX (Data Analysis Expressions)** in Power BI to provide detailed and customized analysis:
    - KPIs calculation.
    - Calculated measures for specific analyses.
    - Calculated columns to enrich the data.
    - Filtering and dynamic segmentation of data.

    In Python, the analysis includes:
    - Detailed data cleaning processes.
    - Creation of visualizations to explore and present data insights.
    - Development of an interactive Streamlit app to dynamically explore the results.
    """)

# Función para mostrar la sección de Power BI
def show_power_bi():
    st.title("📊 Power BI Dashboard")
    st.write("""
    Here are some screenshots of the Power BI dashboard:
    """)
    st.image("screenshot_2.png", caption="Power BI Dashboard 1", use_column_width=True)
    st.image("screenshot_3.png", caption="Power BI Dashboard 2", use_column_width=True)
    st.image("screenshot_4.png", caption="Power BI Dashboard 3", use_column_width=True)
    st.image("screenshot_5.png", caption="Power BI Dashboard 4", use_column_width=True)

# Función para mostrar la sección de conclusiones
def show_conclusions():
    st.title("📜 Conclusions")
    st.write("""
    The analysis provided valuable insights into key marketing metrics and customer behavior. The interactive dashboards and visualizations helped identify patterns and opportunities for strategic decision-making. The combination of Power BI and Python proved to be effective in handling and analyzing large datasets.
    """)

# Menú de navegación
st.sidebar.image(menu_image, use_column_width=True)
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Objectives", "Development Process", "Results", "Power BI", "Conclusions"])

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