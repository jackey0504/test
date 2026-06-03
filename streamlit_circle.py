import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('我的第一个数学 App 🎉')

# 1. 加一个交互控件（滑块）
r = st.slider('选择圆的半径', min_value=1, max_value=20, value=5)

# 2. 画图逻辑（和之前几乎一样）
theta = np.linspace(0, 2*np.pi, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
st.pyplot(fig)
