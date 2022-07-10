import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("App exemplo")

st.markdown("Isso vai ser um bloco de texto")

df = pd.DataFrame({
    "Dados":np.random.normal(0, 1, 100)
})

plt.plot(df.Dados)
st.pyplot()
st.markdown("Final do webapp")
