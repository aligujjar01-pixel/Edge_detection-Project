🧠 Interactive Edge Detection Visualizer

Project Description

This is a single-file, interactive web application built using Streamlit and OpenCV (cv2). It allows users to upload an image and immediately experiment with the three most common computer vision edge detection algorithms: Canny, Sobel, and Laplacian.

The application is designed to be highly responsive and visually appealing, featuring an off-white background, a light blue sidebar for controls, and cached computation for fast parameter adjustments.

Setup and Installation

This project requires Python and three main libraries: opencv-python, numpy, and streamlit.

Ensure Python is installed (3.8 or higher is recommended).

Install necessary libraries using pip:

pip install opencv-python numpy streamlit


How to Run the Application

create the folder withe name .streamlit and keep the config.toml file inside and then run the command given below.

.streamlit/config.toml // this how path should look.

Save the Python code provided above as main.py.

Open your terminal or command prompt in the directory where you saved the file.

Execute the application using the Streamlit CLI:

streamlit run main.py


The application will automatically open in your default web browser.

Core Features and Enhancements

These points highlight the main capabilities and recent improvements for easy review.

Three Edge Algorithms: Supports Canny (optimal), Sobel (gradient), and Laplacian (second derivative) methods.

Optimized Performance: Uses the @st.cache_data decorator to prevent unnecessary reprocessing, ensuring smooth slider adjustments.

Responsive and Modern UI: Features Custom CSS styling for a professional, high-contrast look, including a soft off-white background and a distinct sidebar.

Intuitive Controls: Parameters are organized using Expander sections to reduce clutter, showing only the relevant options for the selected algorithm.

Single-Slider Thresholds: Canny edge detection parameters are simplified using a single range slider for combined control of lower and upper thresholds.

Dynamic Metrics: Key parameter values (like Canny's Upper Threshold or Sobel's Kernel Size) are displayed in the sidebar using st.metric widgets for quick reference.

Application Interface Summary

The interface is clearly separated into two functional areas:

1. Parameter Adjustment UI (Sidebar)

Controls are efficiently organized within the dedicated sidebar.

Algorithm-specific parameters are hidden/shown via Expander sections.

A dynamic metric displays the active value of a key parameter when an algorithm is selected.

2. Side-by-Side Visualization.

The main area clearly displays the Original Image next to the Edge-Detected Output.

Results are visually framed within a dedicated container with a high-contrast header.
