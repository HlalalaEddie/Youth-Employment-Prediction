import streamlit as st
import pickle

# Function to load the selected model
def load_model(model_name):
    model_path = 'rf'
    with open('rf', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    # Title of the web app
    st.title('Sendy Logistics')

    # Subheader
    st.subheader('Welcome! Select a model and input features for prediction.')

    # Dropdown to select the model
    model_options = ['rf', 'Ridge', 'DecisionTreeRegressor', 'XGBRegressor', 'RandomForestRegressor']
    selected_model = st.selectbox('Select Model', model_options)

    # Load the selected model
    model = load_model(selected_model)

    # User input for features
    st.header('Feature Input')
    feature1 = st.number_input('Placement - Day of Month', value=0.0)
    feature2 = st.number_input('Pickup - Time', value=0.0)
    feature3 = st.number_input('Distance (KM)', value=0.0)
    feature4 = st.number_input('Pickup Lat', value=0.0)
    feature5 = st.number_input('Pickup Long', value=0.0)
    feature6 = st.number_input('Destination Lat', value=0.0)
    feature7 = st.number_input('Arrival at Destination - Time', value=0.0)

    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])

        # Display the prediction result
        st.header('Prediction')
        st.write(f'The prediction result is: {prediction[0]}')

if __name__ == '__main__':
    main()
