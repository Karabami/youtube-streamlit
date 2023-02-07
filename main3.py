from tkinter import Image
from turtle import right
from matplotlib.pyplot import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')



st.write('Interactive Widgets')

#サイドバー
#stの後ろにsidebarいれると横にいく
#text = st.text_input('あなたの趣味を教えて下さい。')
#condision = st.slider('あなたの今の調子は？', 0, 100, 50)


#'あなたの趣味:', text
#'コンディション：', condision

#2カラムにしたい

#バージョンが変わった？みたいで、"st.beta_columns"⇒"st.columns"になる。
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


#こちらも、バージョンの変更により、betaバージョンはなくなるので、
#"st.beta_expander"⇒"st.expander"になる。
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ１回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ２回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ３回答')


