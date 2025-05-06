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

# Load and apply simplified CSS
def load_css():
    css = """
    <style>
        /* Global styling */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
        }
        
        /* Clean container styling */
        .container {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            border: 1px solid #eaeaea;
        }
        
        /* Simple header styling */
        .header {
            color: #1E88E5;
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 15px;
            border-bottom: 2px solid #1E88E5;
            padding-bottom: 8px;
        }
        
        /* Feature list */
        .feature {
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            background-color: #f7f9fc;
            padding: 10px 15px;
            border-radius: 6px;
        }
        
        .feature-icon {
            margin-right: 12px;
            font-size: 18px;
            color: #1E88E5;
        }
        
        .feature-text {
            color: #333;
        }
        
        /* Simple metric box */
        .metric {
            background-color: #1E88E5;
            color: white;
            text-align: center;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        
        .metric-value {
            font-size: 24px;
            font-weight: bold;
        }
        
        .metric-label {
            margin-top: 5px;
            font-size: 14px;
            opacity: 0.9;
        }
        
        /* Button styling */
        .button {
            display: inline-block;
            background-color: #1E88E5;
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: 500;
            margin-top: 10px;
        }
        
        /* Timeline */
        .step {
            padding: 15px;
            background-color: #f7f9fc;
            border-left: 3px solid #1E88E5;
            margin-bottom: 15px;
        }
        
        .step-title {
            font-weight: 600;
            color: #1E88E5;
            margin-bottom: 5px;
        }
        
        /* Image gallery */
        .image-container {
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #eaeaea;
            margin-bottom: 15px;
        }
        
        /* Menu styling */
        .menu-item {
            display: flex;
            align-items: center;
            padding: 10px;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 5px;
        }
        
        .menu-item:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        .menu-icon {
            margin-right: 10px;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

load_css()

# Load images
current_dir = os.path.dirname(os.path.abspath(__file__))
main_banner_path = os.path.join(current_dir, "portada.png")
sidebar_logo_path = os.path.join(current_dir, "menu.png")

main_banner = Image.open(main_banner_path)
sidebar_logo = Image.open(sidebar_logo_path)

# Helper functions
def create_container(title, content):
    return f"""
    <div class="container" style="background-color: white; color: #333333;">
        <div class="header" style="color: #1E88E5;">{title}</div>
        {content}
    </div>
    """

def create_feature(icon, title, description):
    return f"""
    <div class="feature">
        <div class="feature-icon">{icon}</div>
        <div class="feature-text">
            <strong>{title}</strong> - {description}
        </div>
    </div>
    """

def create_metric(icon, value, label):
    return f"""
    <div class="metric">
        <div class="metric-value">{icon}</div>
        <div class="metric-label">{value}</div>
        <div>{label}</div>
    </div>
    """

def create_step(title, description):
    return f"""
    <div class="step">
        <div class="step-title">{title}</div>
        <div>{description}</div>
    </div>
    """

# Home page
def show_home():
    # Banner and title
    st.image(main_banner, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Marketing Analysis Project</h1>", 
                unsafe_allow_html=True)
    
    # Introduction
    intro_content = """
    <p style='font-size: 16px; margin-bottom: 20px; color: #333333;'>
        An interactive marketing analytics dashboard combining Power BI and Python for data-driven insights.
    </p>
    """
    st.markdown(create_container("Welcome", intro_content), unsafe_allow_html=True)
    
    # Key features with columns
    st.markdown("<h2 style='color: #1E88E5; text-align: center;'>Key Features</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        features1 = [
            create_feature("📊", "Interactive Dashboards", "Explore metrics and KPIs via Power BI"),
            create_feature("🧹", "Data Analysis", "Cleaning, transformation, and analysis with Python"),
            create_feature("📈", "Visualizations", "Uncover patterns and trends in marketing data")
        ]
        features_content1 = "".join(features1)
        st.markdown(create_container("Analysis Tools", features_content1), unsafe_allow_html=True)
    
    with col2:
        features2 = [
            create_feature("🔍", "In-Depth Insights", "Understand customer behavior and performance"),
            create_feature("📅", "Temporal Analysis", "Identify patterns and opportunities over time"),
            create_feature("🛠️", "Customizable Views", "Tailor the analysis to your specific needs")
        ]
        features_content2 = "".join(features2)
        st.markdown(create_container("Insights", features_content2), unsafe_allow_html=True)
    
    # Benefits section
    st.markdown("<h2 style='color: #1E88E5; text-align: center;'>Benefits</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    cols = [col1, col2, col3]
    benefits = [
        create_metric("📈", "Better Decisions", "Data-driven strategy"),
        create_metric("👥", "Customer Understanding", "Enhanced targeting"),
        create_metric("🌟", "Improved Performance", "Optimized ROI")
    ]
    
    for col, benefit in zip(cols, benefits):
        with col:
            st.markdown(benefit, unsafe_allow_html=True)
    

# Objectives page
def show_objectives():
    st.image(main_banner, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Project Objectives</h1>", 
                unsafe_allow_html=True)
    
    # Brief overview
    overview = """
    <p style='color: #333333; font-size: 16px;'>
        This dashboard provides interactive marketing metrics analysis to support data-driven decision-making.
    </p>
    """
    st.markdown(create_container("Overview", overview), unsafe_allow_html=True)
    
    # Goals
    goals = [
        create_feature("🔗", "Data Integration", "Combine data from multiple sources"),
        create_feature("🧹", "Data Cleaning", "Ensure data quality and reliability"),
        create_feature("📈", "Data Enrichment", "Add calculated columns and metrics"),
        create_feature("📊", "Interactive Dashboards", "Develop Power BI visualizations"),
        create_feature("🐍", "Detailed Analysis", "Use Python for in-depth analysis")
    ]
    goals_content = "".join(goals)
    st.markdown(create_container("Key Goals", goals_content), unsafe_allow_html=True)
    
    # Expected benefits
    st.markdown("<h2 style='color: #1E88E5; text-align: center;'>Expected Benefits</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(create_metric("📈", "Improved Decisions", "Data-driven strategy"), unsafe_allow_html=True)
        st.markdown(create_metric("👥", "Customer Insights", "Better targeting"), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric("💡", "Increased Efficiency", "Streamlined analysis"), unsafe_allow_html=True)
        st.markdown(create_metric("🔄", "Continuous Improvement", "Optimized marketing"), unsafe_allow_html=True)

# Development Process page
def show_development_process():
    st.image(main_banner, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Development Process</h1>", 
                unsafe_allow_html=True)
    
    # Project workflow
    workflow = [
        create_step("Data Extraction", "Collected data from various sources and consolidated into CSV files"),
        create_step("Data Transformation", "Cleaned, normalized, and enriched data using Power BI and Python"),
        create_step("Analysis & Visualization", "Created interactive dashboards and detailed visualizations"),
        create_step("Insights & Recommendations", "Extracted actionable insights to drive business decisions")
    ]
    workflow_content = "".join(workflow)
    st.markdown(create_container("Project Workflow", workflow_content), unsafe_allow_html=True)
    
    # Tools used
    col1, col2 = st.columns(2)
    
    with col1:
        tools = [
            create_feature("🖥️", "Power BI", "Interactive dashboards and visualization"),
            create_feature("🐍", "Python", "Data cleaning, transformation, and analysis"),
            create_feature("🐼", "Pandas", "Data manipulation and preprocessing"),
            create_feature("📊", "Visualization Libraries", "Seaborn & Matplotlib")
        ]
        tools_content = "".join(tools)
        st.markdown(create_container("Tools & Technologies", tools_content), unsafe_allow_html=True)
    
    with col2:
        # Empty or add another content section here if needed
        st.markdown("""
        <div class="container" style="background-color: white; color: #333333;">
            <div class="header" style="color: #1E88E5;">Project Approach</div>
            <p>This project follows an iterative approach to data analysis, with continuous refinement of insights and visualizations based on stakeholder feedback.</p>
            <ul>
                <li><strong>Data-First:</strong> Let the data guide the analysis, not preconceptions</li>
                <li><strong>User-Focused:</strong> Design visualizations with the end user in mind</li>
                <li><strong>Actionable Insights:</strong> Prioritize findings that can drive business decisions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # ETL workflow with columns - keeping this part
    st.markdown("<h2 style='color: #1E88E5; text-align: center; margin-top: 30px;'>ETL Workflow</h2>", 
                unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #e3f2fd; border-radius: 8px; height: 100%;">
            <div style="font-size: 36px; margin-bottom: 10px;">📥</div>
            <div style="font-weight: bold; color: #1E88E5; font-size: 20px;">Extract</div>
            <ul style="text-align: left; color: #333; margin-top: 15px;">
                <li>CSV data files</li>
                <li>API connections</li>
                <li>Database queries</li>
                <li>Web scraping</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #e8f5e9; border-radius: 8px; height: 100%;">
            <div style="font-size: 36px; margin-bottom: 10px;">🔄</div>
            <div style="font-weight: bold; color: #43a047; font-size: 20px;">Transform</div>
            <ul style="text-align: left; color: #333; margin-top: 15px;">
                <li>Data cleaning</li>
                <li>Feature engineering</li>
                <li>Normalization</li>
                <li>Aggregation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #fff8e1; border-radius: 8px; height: 100%;">
            <div style="font-size: 36px; margin-bottom: 10px;">📤</div>
            <div style="font-weight: bold; color: #ff8f00; font-size: 20px;">Load</div>
            <ul style="text-align: left; color: #333; margin-top: 15px;">
                <li>Power BI datasets</li>
                <li>Visualization models</li>
                <li>Interactive dashboards</li>
                <li>Reporting databases</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Results page
def show_results():
    st.image(main_banner, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Key Results</h1>", 
                unsafe_allow_html=True)
    
    # KPIs in row
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        create_metric("📊", "KPIs", "Performance indicators"),
        create_metric("📏", "Measures", "Calculated metrics"),
        create_metric("➕", "Enrichment", "Added data context"),
        create_metric("🔍", "Segmentation", "Customer insights")
    ]
    
    for col, metric in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(metric, unsafe_allow_html=True)
    
    # Analysis highlights - Without the problematic images
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="container" style="background-color: white; color: #333333;">
            <div class="header" style="color: #1E88E5;">Customer Insights</div>
            <ul style="color: #333; padding-left: 20px;">
                <li><strong>Behavior Analysis:</strong> Understanding customer purchase patterns</li>
                <li><strong>Segmentation:</strong> Identification of key customer segments</li>
                <li><strong>Lifetime Value:</strong> Calculation of customer lifetime value</li>
                <li><strong>Purchase Frequency:</strong> Analysis of repeat purchase behavior</li>
                <li><strong>Customer Journey:</strong> Mapping touchpoints and interactions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="container" style="background-color: white; color: #333333;">
            <div class="header" style="color: #1E88E5;">Marketing Performance</div>
            <ul style="color: #333; padding-left: 20px;">
                <li><strong>Campaign Effectiveness:</strong> ROI and conversion analysis</li>
                <li><strong>Channel Performance:</strong> Evaluation of marketing channels</li>
                <li><strong>Content Engagement:</strong> Analysis of content effectiveness</li>
                <li><strong>Budget Allocation:</strong> Optimization of marketing spend</li>
                <li><strong>Conversion Rates:</strong> Analysis of the sales funnel</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Add a summary section
    st.markdown("""
    <div class="container" style="background-color: white; color: #333333; margin-top: 20px;">
        <div class="header" style="color: #1E88E5;">Key Takeaways</div>
        <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 15px;">
            <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f7f9fc; border-radius: 6px; color: #333333;">
                <div style="font-weight: 600; color: #1E88E5; margin-bottom: 5px;">Data-Driven Decisions</div>
                <div>Marketing strategies informed by comprehensive data analysis</div>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f7f9fc; border-radius: 6px; color: #333333;">
                <div style="font-weight: 600; color: #1E88E5; margin-bottom: 5px;">Customer Understanding</div>
                <div>Better targeting and engagement through segmentation</div>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f7f9fc; border-radius: 6px; color: #333333;">
                <div style="font-weight: 600; color: #1E88E5; margin-bottom: 5px;">Optimization</div>
                <div>Enhanced performance through continuous improvement</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Power BI page
def show_power_bi():
    st.image(main_banner, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Power BI Dashboard</h1>", 
                unsafe_allow_html=True)
    
    # Brief description
    description = """
    <p style="color: #333333;">Interactive Power BI dashboards provide comprehensive analysis of key marketing metrics.</p>
    """
    st.markdown(create_container("Overview", description), unsafe_allow_html=True)
    
    # Dashboard features in full width
    dashboard_features = [
        create_feature("📈", "Interactive Visualizations", "Pivot charts and dynamic tables"),
        create_feature("📊", "Key Metrics", "Sales, channels, products, and campaign KPIs"),
        create_feature("📅", "Temporal Analysis", "Trends and patterns over time"),
        create_feature("🗂️", "Multiple Tabs", "Global, Orders, Products, Campaigns, Customers")
    ]
    features_content = "".join(dashboard_features)
    st.markdown(create_container("Dashboard Features", features_content), unsafe_allow_html=True)
    
    # Video demo in full width
    st.markdown("<h2 style='color: #1E88E5; text-align: center; margin-top: 20px;'>Dashboard Demo</h2>", 
                unsafe_allow_html=True)
    
    video_file = os.path.join(current_dir, "clip.mp4")
    if os.path.exists(video_file):
        st.video(video_file)
    else:
        st.warning("Demo video not found. Please add a 'clip.mp4' file to your application directory.")
    
    # Dashboard screenshots
    st.markdown("<h2 style='color: #1E88E5; text-align: center; margin-top: 30px;'>Dashboard Gallery</h2>", 
                unsafe_allow_html=True)
    
    # Keep the gallery with 2 columns
    col1, col2 = st.columns(2)
    
    screenshots = [
        {"path": "screenshot_1.png", "caption": "Global View"},
        {"path": "screenshot_2.png", "caption": "Products Analysis"},
        {"path": "screenshot_3.png", "caption": "Customer Segmentation"},
        {"path": "screenshot_4.png", "caption": "Campaign Performance"}
    ]
    
    for i, screenshot in enumerate(screenshots):
        img_path = os.path.join(current_dir, screenshot["path"])
        
        if os.path.exists(img_path):
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"""
                <div class="container" style="padding: 10px;">
                    <div class="header">{screenshot["caption"]}</div>
                    <div class="image-container">
                        <img src="data:image/png;base64,{get_image_base64(img_path)}" 
                             style="width:100%;">
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            with col1 if i % 2 == 0 else col2:
                st.info(f"Screenshot '{screenshot['path']}' not found.")

# Conclusions page
def show_conclusions():
    st.image(main_banner, use_container_width=True)
    
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Key Conclusions</h1>", 
                unsafe_allow_html=True)
    
    # Insights section
    insights = """
    <ul>
        <li><strong>Data-Driven Decision Making:</strong> The analysis provided actionable insights for marketing strategy optimization.</li>
        <li><strong>Customer Behavior Patterns:</strong> Identified key behavioral patterns among different customer segments.</li>
        <li><strong>Campaign Effectiveness:</strong> Evaluated and optimized marketing campaign performance.</li>
        <li><strong>Channel Optimization:</strong> Determined the most effective marketing channels for different products and audiences.</li>
    </ul>
    """
    st.markdown(create_container("Key Insights & Findings", insights), unsafe_allow_html=True)
    
    # Outcome metrics
    st.markdown("<h2 style='color: #1E88E5; text-align: center;'>Value Delivered</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    metrics = [
        create_metric("📈", "Data-Driven Strategy", "Better marketing decisions"),
        create_metric("👥", "Customer Insights", "Enhanced targeting"),
        create_metric("⚡", "Improved Performance", "Optimized marketing ROI")
    ]
    
    for col, metric in zip([col1, col2, col3], metrics):
        with col:
            st.markdown(metric, unsafe_allow_html=True)
    
    # Future directions
    future_content = """
    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 15px;">
        <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f7f9fc; border-radius: 6px;">
            <div style="font-weight: 600; color: #1E88E5; margin-bottom: 5px;">Expand Data Sources</div>
            <div>Integrate additional data sources for comprehensive analysis</div>
        </div>
        <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f7f9fc; border-radius: 6px;">
            <div style="font-weight: 600; color: #1E88E5; margin-bottom: 5px;">Advanced Analytics</div>
            <div>Implement machine learning for predictive marketing insights</div>
        </div>
        <div style="flex: 1; min-width: 200px; padding: 15px; background-color: #f7f9fc; border-radius: 6px;">
            <div style="font-weight: 600; color: #1E88E5; margin-bottom: 5px;">Real-Time Dashboard</div>
            <div>Develop real-time analytics capabilities for instant insights</div>
        </div>
    </div>
    """
    st.markdown(create_container("Future Directions", future_content), unsafe_allow_html=True)
    

# Function to convert images to base64
def get_image_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Sidebar navigation
with st.sidebar:
    st.image(sidebar_logo, use_container_width=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <h2 style="color: white; margin-bottom: 5px;">Marketing Dashboard</h2>
        <p style="font-size: 14px; color: #ddd;">Data-driven insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Simple navigation menu
    menu_options = {
        "Home": "🏠",
        "Objectives": "🎯",
        "Development Process": "⚙️",
        "Results": "📈",
        "Power BI": "📊",
        "Conclusions": "📝"
    }
    
    menu = st.radio("", list(menu_options.keys()), 
                     format_func=lambda x: f"{menu_options[x]} {x}")
    
    st.markdown("<hr style='margin: 20px 0; opacity: 0.3;'>", unsafe_allow_html=True)
    
    # GitHub button
    st.markdown("""
    <div style="text-align: center;">
        <a href="https://github.com/Jotis86/Marketing-Analysis-Project" target="_blank" 
           style="display: inline-block; padding: 8px 16px; background-color: #555; color: white; 
                  text-decoration: none; border-radius: 4px; font-size: 14px;">
            GitHub Repository
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact information - Fixed to ensure visibility on dark sidebar
    st.markdown("""
    <div style="margin-top: 40px; text-align: center; font-size: 12px; color: #ddd;">
        <p>© 2023 Marketing Analysis Project</p>
        <p><a href="mailto:jotaduranbon@gmail.com" style="color: #80c1ff;">contact@example.com</a></p>
    </div>
    """, unsafe_allow_html=True)

# Display selected page
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