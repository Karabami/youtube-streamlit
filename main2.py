from tkinter import Image
from matplotlib.pyplot import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#インタラクティブとは、対話式・動的な変化を起こすもの・相互にやり取りできる
#ウィジェットとは、UI(user interface)各機能のパーツ

st.title('Streamlit 超入門')

st.write('Display Image')

#st.checkbox(チェックボックスのメッセージ)
#チェックをすれば画像が表示される
#if st.checkbox('Show Image'):
#    img = Image.open('key2.jpg')
#    st.image(img, caption='key2', use_column_width=True)

#セレクトボックス
#option = st.selectbox(
#    'あなたが好きな数字を教えて下さい。',
#)

#'あなたの好きな数字は、', option, 'です。'


#テキスト入力
st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味:', text

#スライダー
#0, 100, 50は、最小値,最大値,始まる値の順
condistion = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', text