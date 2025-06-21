import streamlit as st
import time

st.set_page_config(page_title="Fate Flip", layout="centered")

st.title("🎲 Fate-Flip")
st.caption("Toss a magical coin — let destiny decide.")
st.divider()

with st.form("fate_form"):
    heads = st.text_input("🔮 Customise the HEADS fate:").lower().strip()
    tails = st.text_input("🪬 Customise the TAILS fate:").lower().strip()
    submitted = st.form_submit_button("🪙 Toss the Coin")

if submitted:
    if heads == "" or tails == "":
        st.error("You must fill in both the fates")
    else:
        def rewrite(text):
            return text.replace(" i am ", " you are ") \
                .replace(" my ", " your ") \
                .replace(" me ", " you ") \
                .replace(" mine ", " yours ") \
                .replace(" am ", " are ") \
                .replace(" i ", " you ")

        rewrite_heads = rewrite(f" {heads} ")
        rewrite_tails = rewrite(f" {tails} ")


        gif_slot = st.empty()

        gif_slot.image("https://i.ibb.co/D8jGrY2/coin-flip.gif", caption="Flipping the coin...")  # you can replace with your own gif URL
        time.sleep(2.5)

        gif_slot.empty()

        if len(heads) % 2 == 0:
            output = f"🪙 Your Fate: {rewrite_heads.strip().title()}"
        else:
            output = f"🪙 Your Fate: {rewrite_tails.strip().title()}"

        st.success(output)




