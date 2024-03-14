#################################
# This program lets you:         #
# - Create a dashboard          #
# - Every dashboard page is     #
# - Created in a separate file  #
#################################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from cook import cook


def main():
    
    st.markdown(
    """
    <style>
    .main {
    background-color: #99ffcc
    }

    .block-container {
    background-color: #99ffcc;
    }
    .stHeader {
    background-color: #99ffcc;
    }

    </style>
    """,
    unsafe_allow_html=True,
    )
    
    
    #############
    # Main page #
    #############

    options = ['Home',"Let's Cook Today",'End']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if ( choice == 'Home' ):
      st.image('./images/Lets_cook.jpg')
      st.title("Let's cook and we will be the Luigi Team")
      st.image('./images/Luigi.png')
      pass

    elif ( choice == "Let's Cook Today" ):
      cook()
      pass

    else:
      st.image('./images/Thanks.jpg',width=200)
      st.image('./images/welcome.jpg', width=400)
      st.stop()

main()
