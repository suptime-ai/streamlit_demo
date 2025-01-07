import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import time

# Generate random data
data = np.random.rand(10, 10)
x=np.random
while True:
	# Create a heatmap
	fig, ax = plt.subplots()
	sns.heatmap(data, ax=ax, cmap="coolwarm")

	# Display the heatmap in Streamlit
	st.write(fig)

	# Sleep for a short time to control the speed of movement
	time.sleep(0.05)  # Update every 50 milliseconds



	#update the data in a random location
	np.random.choice(data[1], size=5, replace=True)
