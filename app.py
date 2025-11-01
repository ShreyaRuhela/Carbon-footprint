import streamlit as st
import json

# --- 1. SET UP THE PAGE ---
st.set_page_config(
    page_title="Carbon Tracker",
    page_icon="🍃",
    layout="centered"
)

# --- 2. LOAD DATA ---
@st.cache_data
def load_emission_factors():
    with open('emission_factors.json') as f:
        data = json.load(f)
    return data

emission_factors = load_emission_factors()

# --- 3. BUILD THE APP UI ---
st.title("🍃 My Personal Carbon Footprint Tracker")
st.write("Welcome! Log your activities below to estimate your carbon footprint.")

# Create tabs for each category
tab1,tab2,tab3, tab4, tab5 = st.tabs(["Transport", "Food","Digital", "Home Energy", "Shopping"])

# --- TRANSPORT TAB ---
with tab1:
    st.header("🚗 Transport")
    factors_transport = emission_factors['transport']
    
    with st.form(key='transport_form'):
        mode = st.selectbox("How did you travel?", 
                            options=list(factors_transport.keys()))
        distance = st.number_input("Distance (in km)", 
                                   min_value=0.0, 
                                   step=0.1, 
                                   format="%.1f")
        submit_button = st.form_submit_button(label='Calculate Transport')

        if submit_button:
            factor = factors_transport[mode]
            footprint_kg = distance * factor
            st.success(f"Your footprint for this trip is: {footprint_kg:.2f} kg CO2e")
      #      st.write(f"(Calculation: {distance} km * {factor} kg/km)")


# --- FOOD TAB ---
with tab2:
    st.header("🍔 Food")
    st.write("Log your meals based on their main components.")
    
    # This line automatically reads your new JSON keys
    factors_food_meal = emission_factors['food_by_meal']
    
    with st.form(key='food_form'):
        meal_type = st.selectbox("What type of meal was it?", 
                                 options=list(factors_food_meal.keys()))
        
        meal_count = st.number_input("How many of this meal type?", 
                                     min_value=0, 
                                     step=1,
                                     value=1)
        
        submit_button = st.form_submit_button(label='Calculate Food')

        if submit_button:
            # This line finds the correct factor (e.g., 2.8 for a red meat meal)
            factor = factors_food_meal[meal_type]
            
            # The calculation is done
            footprint_kg = meal_count * factor
            
            st.success(f"Your footprint for this meal is: {footprint_kg:.2f} kg CO2e")
            st.write(f"(Calculation: {meal_count} meal(s) * {factor} kg/meal)")
            
# --- DIGITAL TAB ---
with tab3:
    st.header("💻 Digital")
    factors_digital = emission_factors['digital']
    
    with st.form(key='digital_form'):
        activity = st.selectbox("What did you do?", 
                                options=list(factors_digital.keys()))
        quantity = st.number_input("How many hours or GB ?", 
                                   min_value=0.0, 
                                   step=0.5, 
                                   format="%.1f")
        submit_button = st.form_submit_button(label='Calculate Digital')

        if submit_button:
            factor = factors_digital[activity]
            footprint_kg = quantity * factor
            st.success(f"Your footprint for this activity is: {footprint_kg:.2f} kg CO2e")
           # st.write(f"(Calculation: {quantity} * {factor} kg)")

# --- NEW: HOME ENERGY TAB ---
with tab4:
    st.header("⚡ Home Energy")
    st.write("Log your monthly utility usage. We will average it out per day.")
    factors_home = emission_factors['home_energy']
    
    with st.form(key='home_form'):
        energy_type = st.selectbox("What utility are you logging?", 
                                   options=list(factors_home.keys()))
        
        # We assume the user enters their MONTHLY total
        monthly_usage = st.number_input("What was your total MONTHLY usage (in kWh or therms)?", 
                                        min_value=0.0, 
                                        step=1.0, 
                                        format="%.1f")
        
        submit_button = st.form_submit_button(label='Calculate Home Energy')

        if submit_button:
            factor = factors_home[energy_type]
            
            # Calculate total monthly footprint
            monthly_footprint = monthly_usage * factor
            
            # Average it for a single day
            daily_footprint = monthly_footprint / 30.0
            
            st.success(f"Your daily footprint from this source is: {daily_footprint:.2f} kg CO2e")
            st.write(f"This is based on a monthly footprint of: {monthly_footprint:.2f} kg CO2e")


# --- NEW: SHOPPING TAB ---
with tab5:
    st.header("🛍️ Shopping & Consumption")
    st.write("Log new items and their estimated lifespan to find the *daily* footprint.")
    
    # This now reads from our new 'shopping_total_footprint' key
    factors_shopping = emission_factors['shopping_total_footprint']
    
    with st.form(key='shopping_form'):
        item_type = st.selectbox("What did you buy?", 
                                 options=list(factors_shopping.keys()))
        
        item_count = st.number_input("How many items?", 
                                     min_value=1, 
                                     step=1,
                                     value=1)
        
        # This is the new field you suggested
        lifespan_days = st.number_input("Estimated lifespan (in days)", 
                                        min_value=1, 
                                        step=30,
                                        value=365)
        
        submit_button = st.form_submit_button(label='Calculate Shopping Footprint')

        if submit_button:
            # Get the total manufacturing footprint
            factor = factors_shopping[item_type]
            total_footprint = item_count * factor
            
            # This is your new calculation
            daily_footprint = total_footprint / lifespan_days
            
            # Updated success message to show the daily average
            st.success(f"This adds {daily_footprint:.3f} kg CO2e to your daily footprint.")
            st.write(f"(Calculation: {total_footprint:.1f} kg total footprint / {lifespan_days} days)")