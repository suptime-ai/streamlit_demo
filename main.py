import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Check the version of Streamlit
print(st.__version__)


# Streamlit app setup
st.title("Moving Sine Wave2")

# Create a placeholder for the graph
placeholder = st.empty()

# Initial setup for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 10)   # Set the x-axis range
ax.set_ylim(-1.5, 1.5)  # Set the y-axis range
line, = ax.plot([], [], label="Moving Sine Wave")
ax.set_title("Moving Sine Wave")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()



# Initial x and y data for the sine wave
x = np.linspace(0, 10, 1000)  # X-values for the sine wave (initial)
x_shift = x
y = np.sin(x)  # Y-values for the sine wave

# Display the static axes once
placeholder.pyplot(fig)

# Loop for updating the sine wave (moving effect)
while True:
    # Shift the x-values by a small amount to create the "moving" effect
    x_shift = np.roll(x_shift, 1)  # Shift all elements by 1 position (left)
    y = np.roll(y,1)  #  shift the y values
    y[-1]=np.sin((x_shift[-1]) + np.random.normal(scale=0.1))
    # Update the line data (don't redraw axes)
    line.set_data(x, y)
    
    # Redraw the line (static axes remain fixed)
    placeholder.pyplot(fig)
    
    # Sleep for a short time to control the speed of movement
    time.sleep(0.05)  # Update every 50 milliseconds

