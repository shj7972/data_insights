import streamlit as st
from streamlit_option_menu import option_menu

# Streamlit main page configuration
st.set_page_config(page_title='Multi-App Home', layout='wide')
# Set the page configuration to use the dark theme
#st.set_page_config(page_title='Your App Title', layout='wide', theme={"primaryColor":"#F63366","backgroundColor":"#0E1117","secondaryBackgroundColor":"#31333F","textColor":"#FAFAFA","font":"sans serif"})

# Function to read in custom CSS
#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Use the local_css function to inject your custom CSS
#local_css(r".\style.css")

# Import your app modules here
from korean_stocks_app import run_k_stocks_app
from foreign_stocks_app import run_f_stocks_app
from bonds_app import run_bonds_app
from materials_app import run_materials_app
from cryptocurrency_app import run_cryptocurrency_app
from forex_app import run_forex_app
from population_app import run_population_app
from real_estate_app import run_real_estate_app
from mbti_app import run_mbti_app
from book_quiz_app import run_book_quiz_app
from baskin_robbins_31_app import run_baskin_robbins_31_app

# Define a dictionary to hold your apps
apps = {
    "Korean Stocks": "run_k_stocks_app",
    "Foreign Stocks": "run_f_stocks_app",
    "Bonds": "run_bonds_app",
    "Materials": "run_materials_app",
    "Cryptocurrency": "run_cryptocurrency_app",
    "Forex": "run_forex_app",
    #"Population": "run_population_app", # icons : people
    "Real Estate": "run_real_estate_app",
    "MBTI Matcher": "run_mbti_app",
    #"Book Recommendation": "run_book_quiz_app",
    "Basking Robbins31 Game": "run_baskin_robbins_31_app",
}

def main_page():
    st.title('Main Page')
    st.write("Select an app from the sidebar to get started.")
    #run_k_stocks_app()

# Streamlit sidebar for navigation
#st.sidebar.title('Navigation')
#selected_app = st.sidebar.selectbox('Choose an app', options=list(apps.keys()))
with st.sidebar:
    selected_app = option_menu("Navigation", list(apps.keys()),
                               icons=['house', 'file-bar-graph', 'graph-up-arrow','fuel-pump','coin','currency-exchange', 'buildings', 'person-lines-fill', 'controller'],
                               menu_icon="cast", default_index=0)

# Load the selected app
if selected_app == 'Korean Stocks':
    run_k_stocks_app()
elif selected_app == 'Foreign Stocks':
    run_f_stocks_app()
elif selected_app == 'Bonds':
    run_bonds_app()
elif selected_app == 'Materials':
    run_materials_app()
elif selected_app == 'Cryptocurrency':  
    run_cryptocurrency_app()
elif selected_app == 'Forex':  
    run_forex_app()
elif selected_app == 'Population':  
    run_population_app()
elif selected_app == 'Real Estate':  
    run_real_estate_app()
elif selected_app == 'MBTI Matcher':  
    run_mbti_app()
elif selected_app == 'Basking Robbins31 Game':  
    run_baskin_robbins_31_app()
else:
    main_page()
