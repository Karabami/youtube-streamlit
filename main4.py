from tkinter import Image
from turtle import right
from matplotlib.pyplot import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

#空のイテレーションを準備
latest_iteration = st.empty()
#進捗０のバーを準備
bar = st.progress(0)


#0から100までの数でまわす
for i in range(100):
    #増えていく数を表示させている1ずつ増やしている
    latest_iteration.text(f'Iteration {i + 1}')
    #バーの進捗も1ずつ増やしている
    bar.progress(i + 1)
    #0.1秒ずつバーも表示数も増やすようにしている
    time.sleep(0.01)

'Done!!!!!'





left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ１回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ２回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ３回答')

#webに公開する前でおわった