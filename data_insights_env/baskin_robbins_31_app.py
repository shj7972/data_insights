import streamlit as st
import random

def run_baskin_robbins_31_app():
    st.title("Baskin Robbins 31 Game")
    st.write("Rules: Players take turns selecting 1 to 3 sequential numbers. The player to select 31 loses.")

    # Initialize game state
    if 'current_number' not in st.session_state:
        st.session_state.current_number = 0
        st.session_state.turn = 'user'
        st.session_state.selections = ['white'] * 31  # Color state for each number

    # User's turn with button selection
    if st.session_state.current_number < 31 and st.session_state.turn == 'user':
        #st.write("Your turn: Select how many numbers to add")
        st.markdown("<span style='color: green;'>Your turn: Select how many numbers to add</span>", unsafe_allow_html=True)
        button_cols = st.columns(3)
        for num in range(1, min(4, 32 - st.session_state.current_number)):
            with button_cols[num-1]:
                if st.button(f"Add {num}", key=f"user_select_{num}"):
                    for i in range(st.session_state.current_number, st.session_state.current_number + num):
                        st.session_state.selections[i] = 'green'
                    st.session_state.current_number += num
                    st.session_state.turn = 'program'

    # Program's turn
    if st.session_state.current_number < 31 and st.session_state.turn == 'program':
        program_choice = random.randint(1, min(3, 31 - st.session_state.current_number))
        for i in range(st.session_state.current_number, st.session_state.current_number + program_choice):
            st.session_state.selections[i] = 'red'
        st.session_state.current_number += program_choice
        #st.session_state.turn = 'user'
        #st.write(f"Program selected {program_choice} number(s), up to {st.session_state.current_number}")

    # Display balls in a 10x4 grid
    grid_cols = 10
    cols = st.columns(grid_cols)
    for i in range(31):
        with cols[i % grid_cols]:
            color = st.session_state.selections[i]
            st.markdown(f"<div style='width: 35px; height: 35px; background-color: {color}; border-radius: 50%; text-align: center; line-height: 35px;'>{i + 1}</div>", unsafe_allow_html=True)

    if st.session_state.current_number < 31 and st.session_state.turn == 'program':
        st.session_state.turn = 'user'
        #st.write(f"Program selected {program_choice} number(s), up to {st.session_state.current_number}")
        st.markdown(f"<span style='color: red;'>Program selected {program_choice} number(s), up to {st.session_state.current_number}</span>", unsafe_allow_html=True)

    # Endgame condition
    if st.session_state.current_number >= 31: # 승패 결과 출력 문제? 색상 등, 볼 테이블 정렬? ★
        loser = "You" if st.session_state.turn == 'user' else "Program"
        #st.write(f"Game Over! {loser} selected 31 and loses.")
        st.write("")
        if loser == "You":
            st.markdown(f"<span style='color: red;'>Game Over! {loser} selected 31 and loses.</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color: green;'>Game Over! {loser} selected 31 and loses.</span>", unsafe_allow_html=True)

# Remember to import and call this function in your main Streamlit app


if __name__ == '__main__':
    run_baskin_robbins_31_app()   