import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("圆的参数方程 🎉")

r = st.slider("半径 r", 1, 20, 5)

theta = np.linspace(0, 2*np.pi, 200)
x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect("equal")
ax.set_title(f"r = {r}")
st.pyplot(fig)
