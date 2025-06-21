import streamlit as st
from PIL import Image, ImageDraw
import os
from streamlit_drawable_canvas import st_canvas
import io
import time

# Set up directories
DATASET_DIR = "handwriting_dataset"
os.makedirs(DATASET_DIR, exist_ok=True)

# Title
st.title("🖍️ Handwriting Dataset Collector")
st.write("Draw a symbol, choose its label, and save it to the dataset.")

# Canvas for drawing
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=8,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

# Label input
label = st.text_input("Label for the symbol (e.g., 3, x, +, =)")

# Save image
if st.button("Save Drawing"):
    if canvas_result.image_data is not None and label:
        image = Image.fromarray((255 - canvas_result.image_data[:, :, 0]).astype("uint8"))
        label_dir = os.path.join(DATASET_DIR, label)
        os.makedirs(label_dir, exist_ok=True)
        timestamp = int(time.time() * 1000)
        image_path = os.path.join(label_dir, f"{label}_{timestamp}.png")
        image.save(image_path)
        st.success(f"Saved to {image_path}")
    else:
        st.error("Draw something and enter a label!")

# Preview
if label:
    files = os.listdir(os.path.join(DATASET_DIR, label)) if os.path.exists(os.path.join(DATASET_DIR, label)) else []
    st.write(f"🔢 You have {len(files)} samples for label '{label}'")
