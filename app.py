# import streamlit as st
# import pandas as pd
# import time

# st.title('Startup Dashboard')



# st.header("I am learning streamlit")
# st.subheader('And I am loving it so I would do it more')
# st.write("I am Gaurav Patel")

# writing code as we want
# st.markdown("""M
#             # MY fav Movie 
#             -Race 3
#             - Batman """)

# writing code 

# st.code(""" 
# def foo(input):
#         return foo*2

# x = foo(2)
# """)

# st.latex('x^2')

# # dataframe

# df = pd.DataFrame({
#     'name' : ['Mahadev', 'Shiva', 'Ganesh-Kartik'],
#     'marks': [100 ,100,100],
#     'package': [100,100,100]
# })

# st.dataframe(df)

# # display dashborad

# st.metric('Revenue', 'RS 3L', '3%')
# st.metric('Revenue2', 'RS 3L', '-3%')

# # display json file

# st.json({
#     'name' : ['Mahadev', 'Shiva', 'Ganesh-Kartik'],
#     'marks': [100 ,100,100],
#     'package': [100,100,100]
# })

# # display image and video

# st.image('images.jpg')
# # st.video()

# #### sidebar for site 
# st.sidebar.title('Sidebar ka title')

# kind of grid which devide page inot columns
# col1, col2 = st.columns(2)
# with col1:
#     st.image('images.jpg')
# with col2:
#     st.image('images.jpg')

# erros, success, info , warning mess 

# st.error("Login Failed")
# st.success("Login success")
# st.info("This is training page")
# st.warning("Dont try at home")

# showing status() --> what is the progress of the current task ex uploading file 

# bar = st.progress(0)

# for i in range(1,100):
#     time.sleep(0.1)
#     bar.progress(i)


# user input taking button and uploding


# email = st.text_input("Enter Email")

# age = st.number_input("Add numver")

# date = st.date_input("Ener date")

# email = st.text_input("Enter Email")
# password = st.text_input("Enter password")
# gender = st.selectbox("Select gender", ['Male', 'Female', 'Other'])

# btn = st.button("Button")

# if btn:
#     if email == 'Gaurav@gmail.com' and password == '1234':
#         st.success("Login successfull")
#         st.write(gender)
#         st.balloons()
#     else:
#         st.error("Wrong email or password")

file = st.file_uploader('Upload csv File')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())