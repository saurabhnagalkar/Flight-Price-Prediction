# Flight-Price-Prediction
Predict flight prices with this project! Built using machine learning, it analyzes factors like airline, route (Delhi to Cochin), stops (non-stop), travel date (2025/04/05), booking date (2025/04/05), time (14:09), class (Economy), seat availability (56/100), baggage (15kg), and frequent flyer status (No) to estimate fares. 


# Flight Price Prediction Project

## Overview

This project aims to predict flight prices based on various factors such as airline, source, destination, number of stops, date of journey, booking date, departure time, arrival time, duration, class, seat availability, baggage allowance, and whether the passenger is a frequent flyer. The goal is to build a machine learning model that can accurately estimate the cost of a flight given these input features.

## Features

- **Airline Selection:** Allows users to choose from a list of available airlines (e.g., IndiGo).
- **Source and Destination:** Enables users to specify their origin and final destination airports (e.g., Delhi to Cochin).
- **Number of Stops:** Indicates whether the flight is non-stop or has layovers.
- **Date of Journey and Booking Date:** Captures the travel date and the date the ticket was booked.
- **Departure and Arrival Times:** Specifies the scheduled takeoff and landing times.
- **Flight Duration:** Represents the total time taken for the journey in hours and minutes.
- **Additional Information:** Any extra details about the flight.
- **Flight Class:** The cabin class selected by the passenger (e.g., Economy).
- **Seat Availability:** The number of seats currently available on the flight.
- **Baggage Allowance:** The permitted weight of checked-in baggage in kilograms.
- **Frequent Flyer Status:** Indicates if the passenger is enrolled in a frequent flyer program.
- **Fare Prediction:** A button to trigger the prediction based on the selected inputs.

## Project Details

This project likely involves the following steps:

1.  **Data Collection:** Gathering historical flight data, which typically includes the features listed above and the corresponding ticket prices. This data might be obtained from publicly available datasets, airline APIs, or web scraping.
2.  **Data Preprocessing:** Cleaning and preparing the collected data for model training. This involves handling missing values, encoding categorical features (like airline names, source, and destination) into numerical representations, and potentially feature scaling.
3.  **Feature Engineering:** Creating new features from the existing ones that might improve the model's predictive power. For example, extracting the month or day of the week from the date features, or calculating the time difference between booking date and date of journey.
4.  **Model Selection:** Choosing an appropriate machine learning model for regression. Common choices for price prediction include:
    * Linear Regression
    * Random Forest Regression
    * Gradient Boosting algorithms (like XGBoost or LightGBM)
    * Support Vector Regression
    * Neural Networks
5.  **Model Training:** Training the selected model using the preprocessed historical data. This involves fitting the model to the training data to learn the relationship between the features and the flight prices.
6.  **Model Evaluation:** Assessing the performance of the trained model on a separate test dataset using appropriate evaluation metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared.
7.  **Deployment (Optional):** Creating a user interface (like the one shown in the image) where users can input flight details and get a price prediction from the trained model. This can be done using frameworks like Flask or Streamlit.

## Key Factors Influencing Flight Price

Several factors typically play a significant role in determining flight prices:

* **Airline:** Different airlines have varying pricing strategies based on their brand, services, and operational costs.
* **Route (Source and Destination):** Prices can vary greatly depending on the popularity and distance of the route. High-demand routes or those covering longer distances generally have higher fares.
* **Number of Stops:** Direct flights are usually more expensive than flights with one or more layovers due to convenience and reduced travel time.
* **Date and Time of Travel:** Prices fluctuate based on seasonality, holidays, and the day of the week. Flights during peak travel periods or on weekends tend to be more expensive. Similarly, flight timings (e.g., early morning or late evening flights) can sometimes be cheaper.
* **Booking Timing:** Generally, booking in advance can lead to lower fares. Prices tend to increase as the departure date approaches.
* **Flight Duration:** Longer flights might be priced higher due to increased operational costs.
* **Class of Service:** Higher classes like Business or First Class have significantly higher fares than Economy.
* **Seat Availability:** As more seats are booked, the prices for the remaining seats may increase, following the principle of supply and demand.
* **Baggage Allowance:** Airlines may charge extra for checked baggage beyond a certain limit, influencing the overall cost of travel.
* **Frequent Flyer Programs:** Participation in these programs might offer discounts or benefits that affect the final price for frequent travelers.
* **Day of the Week of Booking:** Some studies suggest that booking on certain days might yield slightly lower prices due to airline pricing algorithms.

## Potential Improvements

* **Integration with Real-time Data:** Connecting the prediction model to live flight data for more up-to-date predictions.
* **Advanced Feature Engineering:** Exploring more complex features, such as the time of year or specific events at the destination.
* **Ensemble Methods:** Combining multiple models to potentially improve prediction accuracy and robustness.
* **Hyperparameter Tuning:** Optimizing the parameters of the chosen machine learning model for better performance.
* **User Feedback Integration:** Allowing users to provide feedback on the predictions to further refine the model over time.
