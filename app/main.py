import streamlit as st
import os
from PIL import Image
from io import BytesIO
import base64

# Page configuration
st.set_page_config(
    page_title="Marketing Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and apply custom CSS
def load_css():
    css = """
    <style>
        /* Main container styling */
        .main {
            background-color: #f5f7fa;
        }
        
        /* Banner styling */
        .banner {
            padding: 0;
            margin: 0;
            width: 100%;
        }
        
        /* Card styling */
        .card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        /* Card header styling */
        .card-header {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 10px;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        
        /* Feature list styling */
        .feature-list {
            list-style-type: none;
            padding-left: 0;
        }
        
        .feature-item {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 5px;
            background-color: #f8f9fa;
            display: flex;
            align-items: center;
        }
        
        .feature-icon {
            margin-right: 10px;
            font-size: 1.2rem;
        }
        
        /* Section title styling */
        .section-title {
            font-size: 2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
            background: linear-gradient(90deg, #3498db, #2c3e50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Metric card styling */
        .metric-card {
            background-color: #3498db;
            color: white;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            margin-bottom: 10px;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .metric-label {
            font-size: 1rem;
            opacity: 0.8;
        }
        
        /* Custom image gallery */
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }
        
        .gallery-item {
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .gallery-item:hover {
            transform: scale(1.05);
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #2c3e50;
            color: white;
        }
        
        /* Button styling */
        .custom-button {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            margin-top: 10px;
            transition: background-color 0.3s ease;
        }
        
        .custom-button:hover {
            background-color: #2980b9;
        }
        
        /* Timeline styling */
        .timeline {
            position: relative;
            margin: 20px 0;
            padding-left: 30px;
        }
        
        .timeline:before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 2px;
            background-color: #3498db;
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 20px;
            padding-left: 20px;
        }
        
        .timeline-item:before {
            content: '';
            position: absolute;
            left: -30px;
            top: 5px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #3498db;
            border: 2px solid white;
        }
        
        /* Fade-in animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.6s ease-out forwards;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_css()

# Obtener la ruta absoluta de la carpeta actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar las imágenes
main_banner_path = os.path.join(current_dir, "portada.png")
sidebar_logo_path = os.path.join(current_dir, "menu.png")

main_banner = Image.open(main_banner_path)
sidebar_logo = Image.open(sidebar_logo_path)

# Helper functions for visual components
def create_card(title, content, icon=""):
    return f"""
    <div class="card fade-in">
        <div class="card-header">{icon} {title}</div>
        {content}
    </div>
    """

def create_feature_list(features):
    items = ""
    for icon, text in features:
        items += f'<li class="feature-item"><span class="feature-icon">{icon}</span> {text}</li>'
    return f'<ul class="feature-list">{items}</ul>'

# Función para mostrar la página principal
def show_home():
    # Banner principal
    st.image(main_banner, use_container_width=True, output_format="PNG")
    
    # Título principal con estilo
    st.markdown('<div class="section-title fade-in">Marketing Analysis Project</div>', unsafe_allow_html=True)
    
    # Descripción breve
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <div class="card-header">📊 Welcome</div>
            <p>Interactive marketing analytics dashboard combining Power BI and Python for data-driven insights.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features en forma de tarjetas visuales
        features = [
            ("📊", "<strong>Interactive Dashboards</strong> - Explore metrics and KPIs via Power BI"),
            ("🧹", "<strong>Data Analysis</strong> - Cleaning, transformation, and analysis with Python"),
            ("📈", "<strong>Visualizations</strong> - Uncover patterns and trends in marketing data"),
            ("🔍", "<strong>In-Depth Insights</strong> - Understand customer behavior and performance"),
            ("📅", "<strong>Temporal Analysis</strong> - Identify patterns and opportunities over time")
        ]
        
        st.markdown(create_card("Key Features", create_feature_list(features), "✨"), unsafe_allow_html=True)
    
    with col2:
        # Añadir una imagen estática en lugar de la animación
        st.markdown("""
        <div class="card fade-in">
            <div style="text-align:center;">
                <img src="https://cdn.pixabay.com/photo/2018/03/22/02/37/analytics-3249888_1280.png" 
                     style="max-width:100%; border-radius:5px;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Beneficios en formato de tarjetas en columnas
    st.markdown('<div class="section-title fade-in">Benefits</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    benefits = [
        ("📈 Better Decisions", "Make informed decisions based on accurate data insights."),
        ("👥 Customer Understanding", "Gain deeper insights into customer behavior and preferences."),
        ("🌟 Enhanced Performance", "Identify areas for improvement in marketing strategies.")
    ]
    
    for i, (col, (title, desc)) in enumerate(zip([col1, col2, col3], benefits)):
        with col:
            st.markdown(f"""
            <div class="card fade-in" style="animation-delay: {i*0.2}s">
                <div class="card-header">{title}</div>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <a href="https://github.com/Jotis86/Marketing-Analysis-Project" target="_blank" class="custom-button">
            View Project on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

# Función para mostrar la sección de objetivos con enfoque visual
def show_objectives():
    st.image(main_banner, use_container_width=True)
    st.markdown('<div class="section-title fade-in">Project Objectives</div>', unsafe_allow_html=True)
    
    # Breve introducción
    st.markdown("""
    <div class="card fade-in">
        <p>This project provides interactive marketing metrics analysis to support data-driven decision-making.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Objetivos principales en forma de tarjetas
    col1, col2 = st.columns(2)
    
    specific_goals = [
        ("🔗", "<strong>Data Integration</strong> - Combine data from multiple sources"),
        ("🧹", "<strong>Data Cleaning</strong> - Ensure data quality and reliability"),
        ("📈", "<strong>Data Enrichment</strong> - Add calculated columns and metrics"),
        ("📊", "<strong>Interactive Dashboards</strong> - Develop Power BI visualizations"),
        ("🐍", "<strong>Detailed Analysis</strong> - Use Python for in-depth analysis")
    ]
    
    with col1:
        st.markdown(create_card("Specific Goals", create_feature_list(specific_goals), "🎯"), unsafe_allow_html=True)
    
    with col2:
        # Añadir una imagen estática en lugar de la animación
        st.markdown("""
        <div class="card fade-in">
            <div style="text-align:center;">
                <img src="https://cdn.pixabay.com/photo/2018/09/04/10/27/business-3653346_1280.jpg" 
                     style="max-width:100%; border-radius:5px;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Beneficios en formato de métricas
    st.markdown('<div class="section-title fade-in">Expected Benefits</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    benefits = [
        ("📈", "Improved Decisions", "Data-driven strategy"),
        ("👥", "Customer Insights", "Better targeting"),
        ("💡", "Increased Efficiency", "Streamlined analysis"),
        ("🔄", "Continuous Improvement", "Optimized marketing")
    ]
    
    for i, (col, (icon, title, desc)) in enumerate(zip([col1, col2, col3, col4], benefits)):
        with col:
            st.markdown(f"""
            <div class="metric-card fade-in" style="animation-delay: {i*0.15}s">
                <div class="metric-value">{icon}</div>
                <div class="metric-label">{title}</div>
                <div>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

# Función para mostrar la sección de proceso de desarrollo con enfoque en el flujo de trabajo
def show_development_process():
    st.image(main_banner, use_container_width=True)
    st.markdown('<div class="section-title fade-in">Development Process</div>', unsafe_allow_html=True)
    
    # Visual timeline of the process
    st.markdown("""
    <div class="card fade-in">
        <div class="card-header">🔄 Project Workflow</div>
        <div class="timeline">
            <div class="timeline-item">
                <h3>Data Extraction</h3>
                <p>Collected data from various sources and consolidated into CSV files</p>
            </div>
            <div class="timeline-item">
                <h3>Data Transformation</h3>
                <p>Cleaned, normalized, and enriched data using Power BI and Python</p>
            </div>
            <div class="timeline-item">
                <h3>Analysis & Visualization</h3>
                <p>Created interactive dashboards and detailed visualizations</p>
            </div>
            <div class="timeline-item">
                <h3>Insights & Recommendations</h3>
                <p>Extracted actionable insights to drive business decisions</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tools and technologies used
    col1, col2 = st.columns(2)
    
    with col1:
        tools = [
            ("🖥️", "<strong>Power BI</strong> - Interactive dashboards and visualization"),
            ("🐍", "<strong>Python</strong> - Data cleaning, transformation, and analysis"),
            ("🐼", "<strong>Pandas</strong> - Data manipulation and preprocessing"),
            ("📊", "<strong>Visualization Libraries</strong> - Seaborn & Matplotlib")
        ]
        
        st.markdown(create_card("Tools & Technologies", create_feature_list(tools), "🛠️"), unsafe_allow_html=True)
    
    with col2:
        # Visualización del proceso ETL
        st.markdown("""
        <div class="card fade-in">
            <div class="card-header">ETL Process Overview</div>
            <img src="https://miro.medium.com/max/1400/1*L_QoAG863l-SUBSYvL_j8A.png" style="width:100%; border-radius:5px; margin-top:10px;">
        </div>
        """, unsafe_allow_html=True)

# Función para mostrar la sección de resultados con visualizaciones atractivas
def show_results():
    st.image(main_banner, use_container_width=True)
    st.markdown('<div class="section-title fade-in">Key Results</div>', unsafe_allow_html=True)
    
    # KPIs y métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    kpis = [
        ("📊", "KPIs", "Performance indicators"),
        ("📏", "Measures", "Calculated metrics"),
        ("➕", "Enrichment", "Added data context"),
        ("🔍", "Segmentation", "Customer insights")
    ]
    
    for i, (col, (icon, title, desc)) in enumerate(zip([col1, col2, col3, col4], kpis)):
        with col:
            st.markdown(f"""
            <div class="metric-card fade-in" style="animation-delay: {i*0.15}s; background-color: #2980b9;">
                <div class="metric-value">{icon}</div>
                <div class="metric-label">{title}</div>
                <div>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Visualizaciones de resultados
    st.markdown('<div class="section-title fade-in">Analysis Highlights</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Customer Insights
        st.markdown("""
        <div class="card fade-in">
            <div class="card-header">👥 Customer Insights</div>
            <ul>
                <li><strong>Behavior Analysis:</strong> Understanding customer purchase patterns</li>
                <li><strong>Segmentation:</strong> Identification of key customer segments</li>
                <li><strong>Lifetime Value:</strong> Calculation of customer lifetime value</li>
            </ul>
            <div style="text-align:center; margin-top:15px;">
                <img src="https://www.datapine.com/blog/wp-content/uploads/2019/05/customer-analytics-dashboard-2.png" 
                     style="max-width:100%; border-radius:5px;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Marketing Performance
        st.markdown("""
        <div class="card fade-in">
            <div class="card-header">📈 Marketing Performance</div>
            <ul>
                <li><strong>Campaign Effectiveness:</strong> ROI and conversion analysis</li>
                <li><strong>Channel Performance:</strong> Evaluation of marketing channels</li>
                <li><strong>Content Engagement:</strong> Analysis of content effectiveness</li>
            </ul>
            <div style="text-align:center; margin-top:15px;">
                <img src="https://www.datapine.com/blog/wp-content/uploads/2019/05/marketing-performance-dashboard.png" 
                     style="max-width:100%; border-radius:5px;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Key takeaways
    st.markdown("""
    <div class="card fade-in">
        <div class="card-header">🔑 Key Takeaways</div>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 15px;">
            <div style="flex: 1; min-width: 200px; margin: 10px; text-align: center; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                <div style="font-size: 2rem;">📊</div>
                <div style="font-weight: 600; margin-top: 10px;">Data-Driven Decisions</div>
                <div style="margin-top: 5px; color: #666;">Informed marketing strategy</div>
            </div>
            <div style="flex: 1; min-width: 200px; margin: 10px; text-align: center; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                <div style="font-size: 2rem;">👥</div>
                <div style="font-weight: 600; margin-top: 10px;">Customer Understanding</div>
                <div style="margin-top: 5px; color: #666;">Better targeting and engagement</div>
            </div>
            <div style="flex: 1; min-width: 200px; margin: 10px; text-align: center; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                <div style="font-size: 2rem;">📈</div>
                <div style="font-weight: 600; margin-top: 10px;">Optimization</div>
                <div style="margin-top: 5px; color: #666;">Enhanced marketing performance</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Función para mostrar la sección de Power BI con galería de capturas
def show_power_bi():
    st.image(main_banner, use_container_width=True)
    st.markdown('<div class="section-title fade-in">Power BI Dashboard</div>', unsafe_allow_html=True)
    
    # Descripción breve
    st.markdown("""
    <div class="card fade-in">
        <p>Interactive Power BI dashboards provide comprehensive analysis of key marketing metrics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Características del dashboard
    col1, col2 = st.columns(2)
    
    with col1:
        dashboard_features = [
            ("📈", "<strong>Interactive Visualizations</strong> - Pivot charts and dynamic tables"),
            ("📊", "<strong>Key Metrics</strong> - Sales, channels, products, and campaign KPIs"),
            ("📅", "<strong>Temporal Analysis</strong> - Trends and patterns over time"),
            ("🗂️", "<strong>Multiple Tabs</strong> - Global, Orders, Products, Campaigns, Customers")
        ]
        
        st.markdown(create_card("Dashboard Features", create_feature_list(dashboard_features), "✨"), unsafe_allow_html=True)
    
    with col2:
        # Video clip with preview
        video_file = os.path.join(current_dir, "clip.mp4")
        if os.path.exists(video_file):
            st.video(video_file)
    
    # Mostrar capturas de pantalla
    st.markdown('<div class="section-title fade-in">Dashboard Gallery</div>', unsafe_allow_html=True)
    
    # Crear una galería simple de imágenes
    screenshots = [
        {"path": "screenshot_1.png", "caption": "Global View Dashboard"},
        {"path": "screenshot_2.png", "caption": "Products Analysis"},
        {"path": "screenshot_3.png", "caption": "Customer Segmentation"},
        {"path": "screenshot_4.png", "caption": "Campaign Performance"},
        {"path": "screenshot_5.png", "caption": "Sales Trends"}
    ]
    
    # Crear layout de 2 columnas para las imágenes
    col1, col2 = st.columns(2)
    
    for i, screenshot in enumerate(screenshots):
        img_path = os.path.join(current_dir, screenshot["path"])
        
        if os.path.exists(img_path):
            # Alternar entre las dos columnas
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"""
                <div class="card fade-in" style="animation-delay: {i*0.2}s">
                    <div class="card-header">{screenshot["caption"]}</div>
                    <div style="text-align:center;">
                        <img src="data:image/png;base64,{get_image_base64(img_path)}" 
                             style="max-width:100%; border-radius:5px;">
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Función para convertir imágenes a base64 para mostrarlas en HTML
def get_image_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Función para mostrar la sección de conclusiones con enfoque visual
def show_conclusions():
    st.image(main_banner, use_container_width=True)
    st.markdown('<div class="section-title fade-in">Key Conclusions</div>', unsafe_allow_html=True)
    
    # Conclusiones principales en tarjetas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card fade-in">
            <div class="card-header">📊 Insights & Findings</div>
            <ul>
                <li><strong>Data-Driven Decision Making:</strong> The analysis provided actionable insights for marketing strategy optimization.</li>
                <li><strong>Customer Behavior Patterns:</strong> Identified key behavioral patterns among different customer segments.</li>
                <li><strong>Campaign Effectiveness:</strong> Evaluated and optimized marketing campaign performance.</li>
                <li><strong>Channel Optimization:</strong> Determined the most effective marketing channels for different products and audiences.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Imagen estática en lugar de animación
        st.markdown("""
        <div class="card fade-in">
            <div style="text-align:center;">
                <img src="https://cdn.pixabay.com/photo/2018/07/14/11/32/network-3537400_1280.png" 
                     style="max-width:100%; border-radius:5px;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Métricas finales
    st.markdown('<div class="section-title fade-in">Value Delivered</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    outcomes = [
        ("📈", "Data-Driven Strategy", "Better marketing decisions"),
        ("👥", "Deeper Customer Insights", "Enhanced targeting"),
        ("⚡", "Improved Performance", "Optimized marketing ROI")
    ]
    
    for i, (col, (icon, title, desc)) in enumerate(zip([col1, col2, col3], outcomes)):
        with col:
            st.markdown(f"""
            <div class="metric-card fade-in" style="animation-delay: {i*0.15}s; background-color: #27ae60;">
                <div class="metric-value">{icon}</div>
                <div class="metric-label">{title}</div>
                <div>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Future work
    st.markdown("""
    <div class="card fade-in">
        <div class="card-header">🚀 Future Directions</div>
        <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 15px;">
            <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                <div style="font-weight: 600; color: #3498db; margin-bottom: 5px;">Expand Data Sources</div>
                <div>Integrate additional data sources for comprehensive analysis</div>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                <div style="font-weight: 600; color: #3498db; margin-bottom: 5px;">Advanced Analytics</div>
                <div>Implement machine learning for predictive marketing insights</div>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f8f9fa; border-radius: 5px;">
                <div style="font-weight: 600; color: #3498db; margin-bottom: 5px;">Real-Time Dashboard</div>
                <div>Develop real-time analytics capabilities for instant insights</div>
            </div>
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 30px; margin-bottom: 30px;">
        <a href="https://github.com/Jotis86/Marketing-Analysis-Project" target="_blank" class="custom-button">
            View Complete Analysis on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

# Menú de navegación mejorado
with st.sidebar:
    st.image(sidebar_logo, use_container_width=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="color: #3498db; margin-bottom: 5px;">Marketing Dashboard</h2>
        <p style="opacity: 0.8; font-size: 0.9rem;">Data-driven marketing insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Menú con íconos
    menu_options = {
        "Home": "🏠",
        "Objectives": "🎯",
        "Development Process": "⚙️",
        "Results": "📈",
        "Power BI": "📊",
        "Conclusions": "📝"
    }
    
    menu = st.radio(
        "Navigation",
        list(menu_options.keys()),
        format_func=lambda x: f"{menu_options[x]} {x}"
    )
    
    # Separador
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Botón para ir al repositorio de GitHub con estilo
    st.markdown("""
    <div style="text-align: center;">
        <a href="https://github.com/Jotis86/Marketing-Analysis-Project" target="_blank" 
           style="display: inline-block; padding: 8px 16px; background-color: #333; color: white; 
                  text-decoration: none; border-radius: 5px; font-size: 0.9rem;">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
                 style="height: 20px; vertical-align: middle; margin-right: 5px;">
            GitHub Repository
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Información de contacto
    st.markdown("""
    <div style="margin-top: 50px; text-align: center; font-size: 0.8rem; color: #333333;">
        <p>© 2023 Marketing Analysis Project</p>
        <p><a href="mailto:contact@example.com" style="color: #3498db;">contact@example.com</a></p>
    </div>
    """, unsafe_allow_html=True)

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