Interactive Edge Detection Visualizer

Project Description

This is a single-file, interactive web application built using Streamlit and OpenCV (cv2). It allows users to upload an image and immediately experiment with the three most common computer vision edge detection algorithms: Canny, Sobel, and Laplacian.

The application is designed to be highly responsive and visually appealing, featuring an off-white background, a light blue sidebar for controls, and cached computation for fast parameter adjustments.

Setup and Installation

This project requires Python and three main libraries: opencv-python, numpy, and streamlit.

Ensure Python is installed (3.8 or higher is recommended).

Install necessary libraries using pip:

pip install opencv-python numpy streamlit


How to Run the Application

Save the Python code provided above as edge_detector_app.py.

Open your terminal or command prompt in the directory where you saved the file.

Execute the application using the Streamlit CLI:

streamlit run main.py


The application will automatically open in your default web browser.

Key Features

Feature

Description

Three Algorithms

Supports Canny (optimal edge detection), Sobel (gradient), and Laplacian (second derivative).

Responsive UI

Custom CSS styling provides a modern, high-contrast, off-white interface with a distinct sidebar.

Optimized Performance

Uses the @st.cache_data decorator to prevent the image decoding and core processing from running unnecessarily, ensuring smooth slider adjustments.

Interactive Controls

Parameters are grouped into intuitive Expander sections. Canny thresholds are simplified into a single range slider.

Dynamic Metrics

Key parameters (like Canny's Upper Threshold or Sobel's Kernel Size) are displayed prominently in the sidebar using st.metric widgets.

Application Interface and Outputs

The interface is divided into a control panel (sidebar) and the main visualization area.

1. Parameter Adjustment UI

The controls are organized within a dedicated sidebar. When an algorithm is selected, its parameters are displayed in an expanded section, along with a dynamic metric showing a key value.

2. Side-by-Side Visualization

The main application area displays the results in a clear, contrasting side-by-side format within a dedicated container.
