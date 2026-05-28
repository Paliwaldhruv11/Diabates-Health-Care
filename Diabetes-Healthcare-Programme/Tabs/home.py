import streamlit as st
import PIL

def app():
    st.title("Integrated Diabetes Health Care Program")
    st.image("./images/diabetic.png", use_container_width=True)

    st.markdown(
        """
        <div style="
            font-size:1.1rem;
            line-height:1.75;
            color:#365451;
            background:rgba(255,255,255,0.72);
            border:1px solid rgba(13,148,136,0.18);
            border-radius:16px;
            padding:1.35rem 1.5rem;
            margin-top:0.5rem;
            box-shadow:0 8px 30px rgba(19,78,74,0.06);
        ">
            Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
            There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
            This web app helps predict whether a person has diabetes or may be prone to it in the future by analysing several clinical features using a Random Forest classifier.
        </div>
        """,
        unsafe_allow_html=True,
    )
    