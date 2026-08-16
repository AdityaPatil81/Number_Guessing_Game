import streamlit as st
import random
import time

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯"
)

st.title("🎯 Number Guessing Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("Guess a number between **1 to 100**.")

guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)
if st.session_state.attempts <= 9:
    if st.button("Guess"):
        if not st.session_state.game_over:
            st.session_state.attempts += 1

            if guess < st.session_state.number:
                st.warning("📉 Too Small!")
            elif guess > st.session_state.number:
                st.warning("📈 Too Large!")
            else:
                st.success(
                    f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts."
                )
                st.balloons()
                st.session_state.game_over = True
else:
    st.error(
        "You lost⛔."
    )

if st.button("New Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

    with st.spinner("Restarting..."):
        time.sleep(3)
    
    st.rerun()


st.write(f"**Attempts:** {st.session_state.attempts}")
