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
st.write("You have **10 attempts** to find the correct number.")

guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)
if st.session_state.attempts <= 9:
    if st.button("Guess",type="primary"):
        if guess > 0 and guess <= 100:
            if not st.session_state.game_over:
                st.session_state.attempts += 1

                if guess < st.session_state.number:
                    st.warning("📉 Too Low - Try a Higher Number.")
                elif guess > st.session_state.number:
                    st.warning("📈 Too High - Try a Lower Number.")
                else:
                    st.success(
                        f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} Attempts."
                    )
                    st.balloons()
                    st.session_state.game_over = True
        else:
            st.error("⚠️ Invalid Input — Please Enter a Number Between 1 and 100.")
else:
    if st.session_state.game_over:
        st.write("**Start a New Game!**")
    else:
        st.error("Out of Tries! The Number Got Away This Time.")
        st.write(f"**The Number Was - {st.session_state.number}.**")

if st.button("New Game",type="primary"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

    with st.spinner("🔃 Restarting..."):
        time.sleep(3)
    
    st.rerun()


st.write(f"**Attempts:** {st.session_state.attempts}")
