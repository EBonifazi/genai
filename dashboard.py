import streamlit as st
import anthropic
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

current_page = "Sustainability AI Analysis"
st.header(current_page)
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

with st.sidebar:
    import smenu
    smenu.menu()


# This function can be called inside your Streamlit app to render the chart
def get_chart():
    # Your original data and projection logic here
    # For demonstration, using your provided data structure
    data = {
        'Year': [2022, 2023, 2024],
        'Scope 1': [100, 90, 80],
        'Scope 2': [200, 180, 160],
        'Scope 3': [300, 270, 240],
    }
    df = pd.DataFrame(data)
    
    # Assuming the projection logic remains the same
    projections = {
        'Year': np.arange(2025, 2051),
        'Scope 1': np.linspace(df.loc[2, 'Scope 1'], 50, len(np.arange(2025, 2051))),
        'Scope 2': np.linspace(df.loc[2, 'Scope 2'], 30, len(np.arange(2025, 2051))),
        'Scope 3': np.linspace(df.loc[2, 'Scope 3'], 20, len(np.arange(2025, 2051))),
    }
    df_projections = pd.DataFrame(projections)
    df = pd.concat([df, df_projections])

    # Convert to long format for Plotly
    df_long = pd.melt(df, id_vars=['Year'], value_vars=['Scope 1', 'Scope 2', 'Scope 3'], 
                      var_name='Scope', value_name='GHG Emissions (tCO2e)')

    # Create the bar chart using Plotly Express
    fig = px.bar(df_long, x='Year', y='GHG Emissions (tCO2e)', color='Scope', 
                 title='GHG Emissions Reductions with Targets')

    # Add target lines and annotations
    targets = {2025: 500, 2030: 400, 2050: 300}
    for year, target in targets.items():
        fig.add_trace(go.Scatter(x=[year, year], y=[0, target], mode='lines', line=dict(color='grey', dash='dash'), showlegend=False))
        fig.add_annotation(x=year, y=target, text=f'Target {year}', showarrow=False, yshift=10)

    # Display the plot in Streamlit within tabs for different themes
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)


st.title("🦜🔗 Sustainability AI Analysis")

query = st.text_input("Request Analysis:")
if st.button("Perform Analysis"):
    data, fig = perform_analysis(query)
    st.table(data)
    st.plotly_chart(fig)
            
col1, col2 = st.columns(2, gap="small")
with col1:
    with st.form("my_form0"):
        get_chart()
with col2:
    with st.form("my_form"):
        text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
        
        
        import streamlit as st
        import pandas as pd
        import numpy as np
        import pydeck as pdk

        # Function to generate random data around a central point (latitude, longitude)
        # Adjusting the spread to generate data over a wider area
        def generate_data(lat, lon, num_points=1000, spread=1):
            return pd.DataFrame(
                np.random.randn(num_points, 2) * spread + [lat, lon],  # Increase spread for a wider distribution
                columns=['lat', 'lon'])

        # Generate data with a wider spread for each city
        rome_data = generate_data(41.9028, 12.4964, num_points=1000, spread=0.1)  # Spread the points wider around Rome
        berlin_data = generate_data(52.5200, 13.4050, num_points=1500, spread=0.1)  # Spread the points wider around Berlin
        paris_data = generate_data(48.8566, 2.3522, num_points=2000, spread=0.1)  # Spread the points wider around Paris

        # Concatenate the data into a single DataFrame
        chart_data = pd.concat([rome_data, berlin_data, paris_data])

        # Define PyDeck chart
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=48.8566,
                longitude=10.3522,
                zoom=4,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=chart_data,
                    get_position='[lon, lat]',
                    radius=3000,  # Adjusted to cover a wider area
                    elevation_scale=200,  # Adjust elevation for visibility
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                    colorRange=[
                        [1, 152, 189],  # Cooler colors for lower pollution
                        [73, 227, 206],
                        [216, 254, 181],
                        [254, 237, 177],
                        [254, 173, 84],
                        [209, 55, 78]  # Warmer colors for higher pollution
                    ],
                ),
            ],
        ))




