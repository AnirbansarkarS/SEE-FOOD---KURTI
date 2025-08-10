import streamlit as st
from services.gemini_service import identify_food
from services.nutrition_service import get_nutrition
from utils.image_utils import load_image

st.set_page_config(page_title="FoodSnap Nutrition", page_icon="🍔", layout="centered")

st.title("🍔 FoodSnap Nutrition")
st.write("Upload a food photo and get detailed nutritional information.")

uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze"):
        with st.spinner("Identifying food..."):
            image_bytes = uploaded_file.read()
            food_name = identify_food(image_bytes)

        st.subheader("Detected Food : ")
        st.success(food_name)

        with st.spinner("Fetching nutrition info..."):
            nutrition = get_nutrition(food_name)

        if nutrition:
            st.subheader("Nutrition Facts (per 100g or serving)")
            st.table({
                "Calories": [nutrition.get("calories", "N/A")],
                "Protein (g)": [nutrition.get("protein_g", "N/A")],
                "Fat (g)": [nutrition.get("fat_total_g", "N/A")],
                "Carbs (g)": [nutrition.get("carbohydrates_total_g", "N/A")],
                "Sugar (g)": [nutrition.get("sugar_g", "N/A")]
            })
        else:
            st.error("No nutrition data found.")
