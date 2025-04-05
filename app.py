import streamlit as st
import pandas as pd
import pickle
import numpy as np
import datetime

# Load the trained model
with open("flight_rf.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("Flight Fare Prediction")

# Inputs from user
airline = st.selectbox("Select Airline", ["IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara"])
source = st.selectbox("Source", ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"])
destination = st.selectbox("Destination", ["Cochin", "Delhi", "Hyderabad", "Bangalore", "Kolkata"])
total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])

# Input for Date of Journey
date_of_journey = st.date_input("Date of Journey", min_value=datetime.date.today())
journey_day = date_of_journey.day
journey_month = date_of_journey.month
day_of_week = date_of_journey.weekday()  # Monday = 0, Sunday = 6

# Weekend Indicator (1 if Saturday or Sunday, else 0)
is_weekend = 1 if day_of_week in [5, 6] else 0

# Season Indicator (Assuming peak season: May-June, December)
is_peak_season = 1 if journey_month in [5, 6, 12] else 0

# Booking Timeframe (Days between booking and journey date)
booking_date = st.date_input("Booking Date", min_value=datetime.date.today())
booking_timeframe = (date_of_journey - booking_date).days

# Input for Departure & Arrival Time
dep_time = st.time_input("Departure Time")
arrival_time = st.time_input("Arrival Time")

dep_hour, dep_minute = dep_time.hour, dep_time.minute
arr_hour, arr_minute = arrival_time.hour, arrival_time.minute

# Flight Duration
duration_hours = st.number_input("Duration Hours", min_value=0)
duration_minutes = st.number_input("Duration Minutes", min_value=0)

# Flight Timing Indicators
is_red_eye_flight = 1 if 0 <= dep_hour <= 6 else 0  # Flights between 12 AM - 6 AM
is_business_hour = 1 if 9 <= dep_hour <= 17 else 0  # Flights between 9 AM - 5 PM
is_early_morning = 1 if dep_hour < 8 else 0  # Before 8 AM
is_late_night = 1 if dep_hour > 22 else 0  # After 10 PM

# Additional Info
additional_info = st.selectbox("Additional Info", ["No info", "In-flight meal not included", "No check-in baggage included"])

# Flight Class
flight_class = st.selectbox("Flight Class", ["Economy", "Business", "First Class"])
flight_class_encoded = {"Economy": 0, "Business": 1, "First Class": 2}[flight_class]

# Is Direct Flight Indicator
is_direct_flight = 1 if total_stops == 0 else 0

# **🚀 New Features Added Below**
# Holiday Indicator
public_holidays = [(1, 26), (8, 15), (10, 2), (12, 25)]  # Example: Republic Day, Independence Day, etc.
is_holiday = 1 if (journey_month, journey_day) in public_holidays else 0

# Airline Rating (Assuming predefined ratings)
airline_ratings = {'IndiGo': 4.0, 'Air India': 3.5, 'Jet Airways': 4.5, 'SpiceJet': 3.8, 'Vistara': 4.2}
airline_rating = airline_ratings[airline]

# Seat Availability (Assuming a range 0-100)
seat_availability = st.slider("Seat Availability", 0, 100, 50)

# Layover Duration (If stops > 0, get input)
layover_duration = st.number_input("Layover Duration (Minutes)", min_value=0) if total_stops > 0 else 0

# Baggage Allowance
baggage_allowance = st.selectbox("Baggage Allowance (kg)", [15, 20, 25, 30, 35])

# Frequent Flyer Status
frequent_flyer = st.selectbox("Frequent Flyer", ["No", "Yes"])
is_frequent_flyer = 1 if frequent_flyer == "Yes" else 0

# One-hot encoding for categorical variables
airline_dict = {'IndiGo': 0, 'Air India': 1, 'Jet Airways': 2, 'SpiceJet': 3, 'Vistara': 4}
source_dict = {'Delhi': 0, 'Mumbai': 1, 'Bangalore': 2, 'Chennai': 3, 'Kolkata': 4}
destination_dict = {'Cochin': 0, 'Delhi': 1, 'Hyderabad': 2, 'Bangalore': 3, 'Kolkata': 4}
additional_info_dict = {"No info": 0, "In-flight meal not included": 1, "No check-in baggage included": 2}

# Convert categorical inputs to numerical values
airline_encoded = airline_dict[airline]
source_encoded = source_dict[source]
destination_encoded = destination_dict[destination]
additional_info_encoded = additional_info_dict[additional_info]

# Create input array with 29 features
input_features = np.array([[
    journey_day, journey_month, dep_hour, dep_minute, arr_hour, arr_minute, 
    total_stops, duration_hours, duration_minutes, 
    airline_encoded, source_encoded, destination_encoded, additional_info_encoded,
    day_of_week, is_weekend, is_peak_season, booking_timeframe,
    is_red_eye_flight, is_business_hour, is_early_morning, is_late_night,
    flight_class_encoded, is_direct_flight, 
    is_holiday, airline_rating, seat_availability, layover_duration, baggage_allowance, is_frequent_flyer
]])

# Ensure correct shape
if st.button("Predict Fare"):
    try:
        predicted_price = model.predict(input_features)
        st.success(f"Estimated Flight Fare: ₹ {round(predicted_price[0], 2)}")
    except ValueError as e:
        st.error(f"Model Input Error: {e}")
