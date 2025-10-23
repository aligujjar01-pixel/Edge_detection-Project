import cv2
import numpy as np
import streamlit as st

# Set page configuration for wide layout
st.set_page_config(page_title="🧠 Edge Detection Visualizer", layout="wide")


# --- Core Image Processing Functions ---

@st.cache_data
def run_edge_detection(img_bytes, algo, params):
    """
    Decodes the image bytes and runs the specified edge detection algorithm.
    Uses st.cache_data for performance optimization.
    """
    # 1. Decode image from bytes
    file_bytes = np.asarray(bytearray(img_bytes), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # 2. Convert to Grayscale for Processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = None

    if algo == "Sobel":
        ksize = params["ksize"]
        
        # Calculate gradients
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
        
        # Convert absolute values to 8-bit image format
        abs_sobelx = cv2.convertScaleAbs(sobelx)
        abs_sobely = cv2.convertScaleAbs(sobely)
        
        if params["direction"] == "X":
            result = abs_sobelx
        elif params["direction"] == "Y":
            result = abs_sobely
        else: # Both (combined gradient magnitude)
            # Use weighted addition to combine X and Y gradients
            result = cv2.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)

    elif algo == "Laplacian":
        ksize = params["ksize"]
        # Laplacian calculation
        laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
        # Convert to 8-bit absolute scale for display
        result = cv2.convertScaleAbs(laplacian)

    elif algo == "Canny":
        # We manually apply a Gaussian blur using the provided sigma first for better control.
        if params["sigma"] > 0:
            # Use a non-zero odd kernel size for Gaussian blur, e.g., (5, 5)
            # cv2.GaussianBlur uses 0,0 for automatic size calculation based on sigma
            blurred_img = cv2.GaussianBlur(gray, (0, 0), params["sigma"]) 
        else:
            blurred_img = gray
            
        result = cv2.Canny(
            blurred_img,
            params["lower"],
            params["upper"],
            apertureSize=params["aperture"]
        )

    return img, result


# --- Streamlit UI and Execution ---

def main():
    # ---- Title (Aesthetic Change 1: Colorful Title and Divider) ----
    st.title("🧠 Interactive Edge Detection Visualizer")
    st.markdown("### Experiment with Sobel, Laplacian, and Canny filters on your own images.")
    st.markdown("---") # Add a horizontal line separator

    # ---- Upload Image ----
    uploaded_file = st.file_uploader(
        " Upload an image (JPG, JPEG, PNG, BMP)", 
        type=["jpg", "jpeg", "png", "bmp"]
    )

    # ---- Sidebar Controls ----
    st.sidebar.header("⚙️ Controls")

    if uploaded_file is None:
        st.info("📥 Please upload an image to start experimenting with edge detection.")
        return

    # Read file bytes only once
    img_bytes = uploaded_file.read()
    
    # ---- Algorithm Selection (Kept as selectbox) ----
    algo = st.sidebar.selectbox(
        "Select Edge Detection Algorithm:",
        ("Canny", "Sobel", "Laplacian"), # Using selectbox for a cleaner look
        index=0 
    )

    # ---- Algorithm-specific Parameters (Using Expanders + Metrics) ----
    params = {}
    params_storage = {} # Temporary storage for active parameters
    apply_button_pressed = False 

    with st.sidebar:
        st.markdown("---")
        st.subheader("Algorithm Parameters")

        # 1. Canny Expander 
        with st.expander("Canny Parameters", expanded=(algo == "Canny")):
            # Get lower and upper thresholds in a single range slider
            thresholds = st.slider(
                "Threshold Range (Lower, Upper)", 0, 255, (50, 150), step=5, key="canny_thresholds"
            )
            
            if algo == "Canny":
                params_storage["lower"] = thresholds[0]
                params_storage["upper"] = thresholds[1]
                params_storage["aperture"] = st.selectbox(
                    "Aperture Size (Sobel Kernel)", (3, 5, 7), index=1, key="canny_aperture"
                )
                params_storage["sigma"] = st.slider("Gaussian Sigma (Pre-blur)", 0.0, 5.0, 1.0, key="canny_sigma")
                
                # Metric display for Canny (Aesthetic Change 2)
                st.metric("Upper Threshold", params_storage["upper"])
                apply_button_pressed = True 

        # 2. Sobel Expander
        with st.expander("Sobel Parameters", expanded=(algo == "Sobel")):
            if algo == "Sobel":
                params_storage["ksize"] = st.slider("Kernel Size (odd number)", 1, 7, 3, step=2, key="sobel_ksize")
                params_storage["direction"] = st.selectbox("Gradient Direction", ("X", "Y", "Both"), index=2, key="sobel_dir")
                
                # Metric display for Sobel (Aesthetic Change 2)
                st.metric("Kernel Size", params_storage["ksize"])


        # 3. Laplacian Expander
        with st.expander("Laplacian Parameters", expanded=(algo == "Laplacian")):
            if algo == "Laplacian":
                params_storage["ksize"] = st.slider("Kernel Size (odd number)", 1, 7, 3, step=2, key="laplacian_ksize")
                
                # Metric display for Laplacian (Aesthetic Change 2)
                st.metric("Kernel Size", params_storage["ksize"])
        
        # --- Apply Button Logic ---
        st.markdown("---")
        if algo != "Canny":
            apply_button_pressed = st.button("🖼️ Apply / Update", key="apply_btn")
            
    # Assign the final active parameters
    params = params_storage
            
    # ---- Apply Algorithm and Display ----
    
    if apply_button_pressed or algo == "Canny":
        
        # Run the cached function
        original_img, result_img = run_edge_detection(img_bytes, algo, params)

        # ---- Display Images Side by Side (Aesthetic Change 3: Use Container) ----
        
        # Use a container to visually group the results
        with st.container(border=True): 
            st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>🔍 {algo} Edge Detection Results</h3>", unsafe_allow_html=True)
            st.markdown("---")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("####  Original Image")
                st.image(original_img, channels="BGR", use_container_width=True)
            with col2:
                st.markdown(f"#### {algo} Output")
                st.image(result_img, channels="GRAY", use_container_width=True)

if __name__ == "__main__":
    main()
