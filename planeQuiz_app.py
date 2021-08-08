import streamlit as st
import time, os, sys, glob
from PIL import Image

#import pandas as pd
#import numpy as np
st.header('Welcome to PilotY plane quiz application !')
# initialize the pictures
dataFolder = "pictures/"
# All files ending with _daily.csv
picList = glob.glob(f"{dataFolder}*.png")

totalScore = len(picList)
userScore = 0

for n,pic in enumerate(picList) :
    image = Image.open(pic)    
    st.image(image)
    st.text('Which plane is shown in the above picture?')
    user_input = st.text_input(f"Quiz {n+1}, please enter your anwser here !", '')
    answer = pic.split('/')[-1][:-4]
    if pic.split('/')[-1][:-4] == user_input :
        st.text(f'Your anwser is {user_input}, the correct answer is {answer}, you are right !')
        userScore +=1
    else : 
        st.text(f'Your anwser {user_input} is not correct ! Try again. ')

st.header(f'Congratulation! Your final score is {userScore} out of {totalScore} !')    