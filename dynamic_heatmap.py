import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import time

# array size
X_MAX = 10
Y_MAX = 10
MAX_HEAT = 1
MIN_HEAT = 0


x_strike_center = 5
y_strike_center = 5
X_STRIKE_RADIUS = X_MAX/6
Y_STRIKE_RADIUS = Y_MAX/6
SLEEP_SECONDS =0.5

rng = np.random.default_rng()

# App title
st.title("Dynamic Heatmap")

# Create a placeholder for the heatmap
placeholder = st.empty()

# Function to generate random data for the heatmap
def generate_random_data(size=(X_MAX, Y_MAX)):
    return np.random.rand(*size)

# Start the dynamic heatmap
st.write("The heatmap below will update every %s seconds:" % SLEEP_SECONDS)

# Generate new random data
data = generate_random_data()

while True:
    
    # Find a cell to modify using a random gausian distribution from strike center
    x=x_strike_center + int(rng.normal(loc=0.0, scale=float(X_STRIKE_RADIUS )))
    x=np.clip(x,0,X_MAX-1)

    y=y_strike_center + int(rng.normal(loc=0.0, scale=float(Y_STRIKE_RADIUS )))
    y=np.clip(y,0,Y_MAX-1)

    # Increment the random new cell location with a random increment of heat
    data[x,y] += rng.random() /4

    # Make sure it is not too hot or else the scale will keep changing - so go find another cell 
    if data[x,y] >= MAX_HEAT:
        data[x,y] = MAX_HEAT
        time.sleep(SLEEP_SECONDS/50)
    else:

        # Create the heatmap
        fig, ax = plt.subplots()
        sns.heatmap(data, ax=ax, cmap="coolwarm", cbar=True)
        ax.set_title("Dynamic Heatmap")

        # Display the heatmap in the placeholder
        placeholder.pyplot(fig)

        # Explicitly close the figure to avoid memory issues
        plt.close(fig)  

        # Pause for 500ms
        time.sleep(SLEEP_SECONDS)
