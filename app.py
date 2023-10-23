import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def main():
    st.title("YouthEmployment Prediction")
    st.write("This app predicts the probability of employment for youth.")

    # Add user input for new ID

    
    # ls2 = [  'Survey_date', 'Round','Status','Province','Degree','Diploma','Home_lang' ,'Science','Female','Sa_citizen' ,'Birthyear' ,'Tenure_log' ]

    # df = pd.DataFrame.from_records(ls, columns=ls2)
    
    
    
#     data = {
#     "Survey_date": (Survey_date),
#   "Round": (Round), "Status": (Status),
#   "Province": (Province),"Degree":(Degree),
#   "Diploma": (Diploma), "Home_lang": (Home_lang),
#   "Science": (Science),"Female": (Female),
#   "Sa_citizen": (Sa_citizen), "Birthyear":(Birthyear),
#   "Tenure_log": (Tenure_log)
# }
#     df = pd.DataFrame(data)




# file = open('rf', 'rb')
# rf = pickle.load(file)

Survey_date = st.number_input("yfy sd", key="fdhuif")
Round = st.number_input("Enter a new round", key="2")
Status = st.number_input("Enter a new ID mvl", key="3")
Province = st.number_input("Enter a new provine", key="4")
Degree = st.number_input("Enter a new degree", key="5")
Diploma = st.number_input("Enter a new diploma", key="6")
Home_lang = st.number_input("Enter a new hl", key="7")
Science = st.number_input("Enter a new science", key="8")
Female = st.number_input("Enter a new gender", key="9")
Sa_citizen = st.number_input("Enter a new sa", key="10")
Birthyear = st.number_input("Enter a new birth", key="11")
Tenure_log = st.number_input("Enter a newtenure", key="12")

ls = [[  Survey_date, Round,Status,Province,Degree,Diploma,Home_lang ,Science,Female,Sa_citizen ,Birthyear ,Tenure_log] ]
print(type(ls))


scalertest = StandardScaler()
X_test_scaled = scalertest.fit_transform(ls)

def predict_target(rf, ):
    # # target_index = person_ids.tolist().index(target_id)
    # target_probability = rf.predict_proba(X_test_scaled)[:, 1]
    # # return target_probability[0]
    # st.write(f"Predicted Probability for ID: {target_probability[0]:.4f}", key="16")


#load data into a DataFrame object:
# df = pd.DataFrame(data)
# 0	33	2	1	3	0	0	2	2	0	1	25	278

    # Display predicted target for the new ID based on the selected model
    # 
     if st.button("Predict"):
        model_choice = st.radio("Select a model to use:", ["Logistic Regression", "Random Forest"])
        print(type(ls))

        # if model_choice == "Logistic Regression":
        #         target_probability = predict_target(rf, X_test_scaled)
        #         st.write(f"Predicted Probability for ID: {target_probability:.4f}")
        # else:  # Random Forest
        #         target_probability = predict_target(classifier_rf, X_test_scaled, person_ids, target_id)
        #         st.write(f"Predicted Probability for ID {target_id}: {target_probability:.4f}")

if __name__ == "__main__":
    main()
