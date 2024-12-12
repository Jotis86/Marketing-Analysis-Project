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
    - 📊 **Interactive Dashboards**: Explore various metrics and KPIs through interactive Power BI dashboards.
    - 🧹 **Data Analysis**: Detailed data cleaning, transformation, and analysis using Python.
    - 📈 **Visualizations**: Comprehensive visualizations to uncover patterns and trends in the data.
    - 🔍 **In-Depth Insights**: Gain a deeper understanding of customer behavior and marketing performance.
    - 🌐 **User-Friendly Interface**: An intuitive and easy-to-use interface for exploring the data.
    - 📅 **Temporal Analysis**: Analyze trends over time to identify patterns and opportunities.
    - 🛠️ **Customizable Dashboards**: Customize the dashboards to suit your needs, adding or removing widgets and adjusting the layout as required.

    ## Benefits
    - 📈 **Improved Decision-Making**: By providing detailed and accurate insights, this project helps stakeholders make informed decisions that can drive business growth.
    - 👥 **Better Customer Understanding**: Gain a deeper understanding of customer behavior and preferences, enabling more targeted and effective marketing strategies.
    - 💡 **Increased Efficiency**: Streamline the data analysis process with automated data cleaning and enrichment, saving time and resources.
    - 🌟 **Enhanced Performance**: Identify areas for improvement in marketing strategies and optimize performance to achieve better results.
    - 🔄 **Continuous Improvement**: Use the insights gained from the analysis to continuously refine and improve marketing efforts.

    ## Future Goals
    - 🚀 **Expand Data Sources**: Integrate additional data sources to provide a more comprehensive view of marketing performance.
    - 🧠 **Advanced Analytics Techniques**: Explore more advanced analytics techniques, such as machine learning and AI, to gain deeper insights.
    - 🌐 **Broader Application**: Apply the analysis framework to other areas of the business to drive data-driven decision-making across the organization.
    - 📊 **Enhanced Visualizations**: Continuously improve the visualizations and dashboards to provide even more value to stakeholders.
    - 📅 **Regular Updates**: Keep the data and analysis up-to-date with regular updates to ensure the insights remain relevant and accurate.
    """)

# Función para mostrar la sección de objetivos
def show_objectives():
    st.image(main_image, use_column_width=True)
    st.title("📌 Objectives")
    st.write("""
    The objective of this project is to provide an interactive and detailed analysis of key marketing metrics to support strategic decision-making. This includes leveraging both Power BI for interactive dashboards and Python for data analysis, cleaning, and visualization.

    ## Specific Goals
    - 🔗 **Data Integration**: Combine data from various sources to create a unified dataset.
    - 🧹 **Data Cleaning**: Remove duplicates, handle missing values, and normalize data to ensure accuracy.
    - 📈 **Data Enrichment**: Add calculated columns and transform data to enhance analysis.
    - 📊 **Interactive Dashboards**: Develop Power BI dashboards to visualize key metrics and KPIs.
    - 🐍 **Detailed Analysis**: Use Python for in-depth data analysis and visualization.

    ## Detailed Objectives
    - 📊 **Comprehensive Data Analysis**: Perform a thorough analysis of marketing data to uncover insights and trends that can drive strategic decisions.
    - 🧹 **Data Quality Improvement**: Ensure the data is clean, accurate, and reliable by removing duplicates, handling missing values, and normalizing data.
    - 📈 **Enhanced Data Visualization**: Create interactive and visually appealing dashboards in Power BI to present key metrics and KPIs.
    - 🧠 **Advanced Analytics**: Utilize Python for advanced data analysis, including statistical analysis, machine learning, and predictive modeling.
    - 🌐 **User-Friendly Interface**: Develop an intuitive and easy-to-use Streamlit app to present the analysis results interactively.
    - 🔍 **In-Depth Insights**: Provide detailed insights into customer behavior, marketing performance, and sales trends to support data-driven decision-making.
    - 📅 **Temporal Analysis**: Analyze trends over time to identify patterns and opportunities for optimization.
    - 🛠️ **Customizable Dashboards**: Allow users to customize the dashboards to suit their needs, adding or removing widgets and adjusting the layout as required.

    ## Benefits
    - 📈 **Improved Decision-Making**: By providing detailed and accurate insights, this project helps stakeholders make informed decisions that can drive business growth.
    - 👥 **Better Customer Understanding**: Gain a deeper understanding of customer behavior and preferences, enabling more targeted and effective marketing strategies.
    - 💡 **Increased Efficiency**: Streamline the data analysis process with automated data cleaning and enrichment, saving time and resources.
    - 🌟 **Enhanced Performance**: Identify areas for improvement in marketing strategies and optimize performance to achieve better results.
    - 🔄 **Continuous Improvement**: Use the insights gained from the analysis to continuously refine and improve marketing efforts.

    ## Future Goals
    - 🚀 **Expand Data Sources**: Integrate additional data sources to provide a more comprehensive view of marketing performance.
    - 🧠 **Advanced Analytics Techniques**: Explore more advanced analytics techniques, such as machine learning and AI, to gain deeper insights.
    - 🌐 **Broader Application**: Apply the analysis framework to other areas of the business to drive data-driven decision-making across the organization.
    - 📊 **Enhanced Visualizations**: Continuously improve the visualizations and dashboards to provide even more value to stakeholders.
    - 📅 **Regular Updates**: Keep the data and analysis up-to-date with regular updates to ensure the insights remain relevant and accurate.
    """)

# Función para mostrar la sección de proceso de desarrollo
def show_development_process():
    st.image(main_image, use_column_width=True)
    st.title("🔄 Development Process")
    st.write("""
    The development process for this project involved several key steps to ensure accurate and insightful analysis.

    ## Steps
    1. 📥 **Extraction**: Data obtained from CSV files.
    2. 🔄 **Transformation**:
       - 🖥️ **Power BI**:
         - 🔗 Combining tables using Power Query.
         - 🧹 Data cleaning: Removing duplicates, handling null values, and normalizing data.
         - 📈 Data enrichment: Adding calculated columns and transforming data to improve analysis.
       - 🐍 **Python**:
         - 🧹 Data cleaning with pandas: Removing duplicates, handling null values, and normalizing data.
         - 📈 Data enrichment: Adding calculated columns and transforming data to improve analysis.
    3. 📤 **Load**:
       - 🖥️ **Power BI**: Integrating transformed data into Power BI for analysis and visualization.
       - 🐍 **Python**: Preparing data for visualization and analysis in Jupyter notebooks and Streamlit.

    ## Tools Used
    - 🖥️ **Power BI**: For interactive dashboards and data visualization.
    - 🐍 **Python**: For data cleaning, transformation, and analysis.
    - 🐼 **Pandas**: For data manipulation and analysis.
    - 📊 **Seaborn & Matplotlib**: For creating visualizations.

    ## Detailed Process
    The development process was meticulously planned and executed to ensure the highest quality of data analysis and visualization. Each step was crucial in transforming raw data into actionable insights.

    ### Extraction
    - 📥 **Data Collection**: Data was collected from various sources and consolidated into CSV files for further processing.

    ### Transformation
    - 🖥️ **Power BI**:
      - 🔗 **Combining Tables**: Using Power Query to merge tables and create a unified dataset.
      - 🧹 **Data Cleaning**: Removing duplicates, handling null values, and normalizing data to ensure accuracy.
      - 📈 **Data Enrichment**: Adding calculated columns and transforming data to enhance analysis.
    - 🐍 **Python**:
      - 🧹 **Data Cleaning with Pandas**: Utilizing pandas for efficient data cleaning and preprocessing.
      - 📈 **Data Enrichment**: Adding calculated columns and transforming data to improve analysis.

    ### Load
    - 🖥️ **Power BI**: Integrating the transformed data into Power BI to create interactive dashboards and visualizations.
    - 🐍 **Python**: Preparing the data for visualization and analysis in Jupyter notebooks and Streamlit.

    ## Additional Tools and Techniques
    - 🛠️ **Advanced Analytics**: Leveraging advanced analytics techniques to gain deeper insights.
    - 🌐 **Interactive Visualizations**: Creating interactive visualizations to allow users to explore the data dynamically.
    - 📊 **Custom Dashboards**: Developing customizable dashboards to meet the specific needs of different stakeholders.

    The combination of Power BI and Python provided a robust framework for data analysis and visualization, enabling us to deliver comprehensive insights and support data-driven decision-making.
    """)

# Función para mostrar la sección de resultados
def show_results():
    st.image(main_image, use_column_width=True)
    st.title("📈 Results")
    st.write("""
    Various metrics have been created using **DAX (Data Analysis Expressions)** in Power BI to provide detailed and customized analysis.

    ## Key Metrics
    - 📊 **KPIs Calculation**: Key Performance Indicators to measure marketing effectiveness.
    - 📏 **Calculated Measures**: Specific measures for detailed analysis.
    - ➕ **Calculated Columns**: Enriching the dataset with additional information.
    - 🔍 **Filtering and Dynamic Segmentation**: Allowing for detailed and customized views of the data.

    ## Python Analysis
    - 🧹 **Data Cleaning**: Detailed processes to ensure data accuracy.
    - 📊 **Visualizations**: Creation of visualizations to explore and present data insights.
    - 🌐 **Interactive App**: Development of an interactive Streamlit app to dynamically explore the results.

    ## Insights
    - 👥 **Customer Behavior**: Understanding how different customer segments behave.
    - 📈 **Marketing Performance**: Evaluating the effectiveness of various marketing campaigns.
    - 📊 **Sales Trends**: Identifying trends and patterns in sales data.

    ## Detailed Analysis
    The results section provides a comprehensive analysis of the marketing data, focusing on key metrics and insights that drive strategic decision-making. By leveraging both Power BI and Python, we have created a robust framework for data analysis and visualization.

    ### Power BI Analysis
    Power BI has been used to create interactive dashboards that allow users to explore the data dynamically. Key metrics such as sales, channels, products, complaints, and campaign performance are analyzed to provide a holistic view of the marketing landscape.

    ### Python Analysis
    Python has been utilized for in-depth data cleaning and visualization. Using libraries such as pandas, matplotlib, and seaborn, we have created detailed visualizations that uncover patterns and trends in the data. The interactive Streamlit app further enhances the user experience by providing a dynamic platform to explore the results.

    ### Key Takeaways
    - 📊 **Data-Driven Decisions**: Leveraging data to make informed marketing decisions.
    - 👥 **Customer Insights**: Gaining a deeper understanding of customer behavior and preferences.
    - 📈 **Marketing Optimization**: Identifying areas for improvement in marketing strategies.
    - 🔍 **Future Work**: Potential areas for further analysis and exploration.

    The combination of Power BI and Python has proven to be effective in handling and analyzing large datasets, providing valuable insights that drive strategic decision-making.
    """)

# Función para mostrar la sección de Power BI
def show_power_bi():
    st.image(main_image, use_column_width=True)
    st.title("📊 Power BI Dashboard")
    st.write("""
    This project includes:

    - 📈 **Interactive visualizations**: Pivot charts and tables in Power BI to explore data.
    - 📊 **Key metrics**: Analysis of important KPIs such as sales, channels, products, complaints, campaign performance, and more.
    - 📅 **Temporal analysis**: Trends over time to identify patterns and opportunities.
    - 🗂️ **Five tabs in Power BI**:
      - 🌍 **Global**: General view of all metrics.
      - 📦 **Orders**: Detailed analysis of orders.
      - 🛍️ **Products**: Monitoring and analysis of different products.
      - 📢 **Campaigns**: Evaluation of marketing campaigns.
      - 👥 **Customers**: Customer information and analysis.

    Here are some screenshots of the Power BI dashboard:
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
    - 📊 **Data-Driven Decisions**: Leveraging data to make informed marketing decisions.
    - 👥 **Customer Insights**: Gaining a deeper understanding of customer behavior and preferences.
    - 📈 **Marketing Optimization**: Identifying areas for improvement in marketing strategies.
    - 🔍 **Future Work**: Potential areas for further analysis and exploration.

    ## Detailed Insights
    The project has demonstrated the power of combining Power BI and Python to create a comprehensive data analysis framework. By integrating data from various sources, cleaning and enriching it, and then visualizing it through interactive dashboards, we have been able to uncover valuable insights that drive strategic decision-making.

    ### Data-Driven Decisions
    - 📊 **Informed Choices**: The detailed analysis allows stakeholders to make informed decisions based on accurate and up-to-date data.
    - 📈 **Performance Tracking**: Key metrics and KPIs help track the performance of marketing campaigns and identify areas for improvement.

    ### Customer Insights
    - 👥 **Behavior Analysis**: Understanding customer behavior helps in tailoring marketing strategies to better meet their needs.
    - 📊 **Segmentation**: Analyzing different customer segments provides insights into their preferences and purchasing patterns.

    ### Marketing Optimization
    - 📈 **Campaign Effectiveness**: Evaluating the performance of marketing campaigns helps in optimizing them for better results.
    - 🔄 **Continuous Improvement**: Using the insights gained to continuously refine and improve marketing efforts.

    ### Future Work
    - 🚀 **Expand Data Sources**: Integrate additional data sources to provide a more comprehensive view of marketing performance.
    - 🧠 **Advanced Analytics Techniques**: Explore more advanced analytics techniques, such as machine learning and AI, to gain deeper insights.
    - 🌐 **Broader Application**: Apply the analysis framework to other areas of the business to drive data-driven decision-making across the organization.
    - 📊 **Enhanced Visualizations**: Continuously improve the visualizations and dashboards to provide even more value to stakeholders.
    - 📅 **Regular Updates**: Keep the data and analysis up-to-date with regular updates to ensure the insights remain relevant and accurate.

    ## Acknowledgements
    We would like to thank everyone who contributed to this project, including data providers, analysts, and developers. Your efforts have been invaluable in making this project a success.
    """)

# Menú de navegación
st.sidebar.image(menu_image, use_column_width=True)
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Objectives", "Development Process", "Results", "Power BI", "Conclusions"])

# Botón para ir al repositorio de GitHub
if st.sidebar.button('GitHub Repository'):
    st.sidebar.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Jotis86/Marketing-Analysis-Project)")

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