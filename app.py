 
import pickle
import streamlit as st
 
# loading the trained model
pickle_input = open('RandomForestclassifier.pkl', 'rb') 
classifier = pickle.load(pickle_input)
 
@st.cache()
  

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age, Gender, JobSatisfaction, MaritalStatus, MonthlyIncome, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole):   
    st.title("Employee Attrition Prediction")
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    if MaritalStatus == "Married":
        Married = 1
    else:
        Married = 0
  
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Age, Gender, JobSatisfaction, MaritalStatus, MonthlyIncome, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole]])
     
    if prediction == 0:
        pred = 'No'
    else:
        pred = 'Yes'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction
    Age = st.number_input("Age")
    Gender = st.selectbox('Gender',("Male","Female"))
    JobSatisfaction = st.number_input("Job Satisfcation on a scale of 1 to 4")
    MaritalStatus = st.selectbox('Marital Status',("Married","Single"))
    MonthlyIncome = st.number_input("Monthly Income")
    TrainingTimesLastYear = st.number_input("Training Times last year")
    WorkLifeBalance = st.number_input("Work life balance on a scale of 1 to 4")
    YearsAtCompany = st.number_input("Years at company")
    YearsInCurrentRole = st.number_input("Years in current role")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age, Gender, JobSatisfaction, MaritalStatus, MonthlyIncome, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole) 
        st.success('This answer is {}'.format(result))
        print(result)
     
if __name__=='__main__': 
    main()
