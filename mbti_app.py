import streamlit as st

def run_mbti_app():
    # Main page header
    st.title("Discover Your MBTI Personality Type!")

    st.header("Answer the following questions:")

    q1 = st.radio("You prefer to spend your free time:", 
                ["Alone or with a few close friends", "In a lively environment with many people"])
    q2 = st.radio("When making decisions, you rely more on:", 
                ["Facts and details", "Your intuition and imagination"])
    q3 = st.radio("You tend to be more:", 
                ["Logical and analytical", "Considerate and empathetic"])
    q4 = st.radio("You prefer your life to be:", 
                ["Planned and organized", "Spontaneous and flexible"])
    q5 = st.radio("In a group discussion, do you:",
                  ["Prefer to lead and direct the conversation", "Listen more and speak when you have a specific point to make"])
    q6 = st.radio("When learning something new, do you:",
                  ["Prefer concrete facts and proven methods", "Enjoy exploring theoretical and abstract concepts"])
    q7 = st.radio("In a disagreement, are you more likely to:",
                  ["Stand firm on logical reasoning", "Strive to maintain harmony and consider others' feelings"])
    q8 = st.radio("Do you prefer tasks that:",
                  ["Have a clear deadline and structured approach", "Are flexible and open to last-minute changes"])
    q9 = st.radio("Which resonates more with you:",
                  ["Setting and achieving specific goals", "Going with the flow and embracing new opportunities as they come"])


    if st.button("Submit"):
        # Counters for each MBTI dimension
        E, I, S, N, T, F, J, P = 0, 0, 0, 0, 0, 0, 0, 0

        # Tally responses for E/I
        E += 1 if q1 == "In a lively environment with many people" else 0
        E += 1 if q5 == "Prefer to lead and direct the conversation" else 0
        I += 1 if q1 != "In a lively environment with many people" else 0
        I += 1 if q5 != "Prefer to lead and direct the conversation" else 0

        # Tally responses for S/N
        S += 1 if q2 == "Facts and details" else 0
        S += 1 if q6 == "Prefer concrete facts and proven methods" else 0
        N += 1 if q2 != "Facts and details" else 0
        N += 1 if q6 != "Prefer concrete facts and proven methods" else 0

        # Tally responses for T/F
        T += 1 if q3 == "Logical and analytical" else 0
        T += 1 if q7 == "Stand firm on logical reasoning" else 0
        F += 1 if q3 != "Logical and analytical" else 0
        F += 1 if q7 != "Stand firm on logical reasoning" else 0

        # Tally responses for J/P
        J += 1 if q4 == "Planned and organized" else 0
        J += 1 if q8 == "Have a clear deadline and structured approach" else 0
        J += 1 if q9 == "Setting and achieving specific goals" else 0
        P += 1 if q4 != "Planned and organized" else 0
        P += 1 if q8 != "Have a clear deadline and structured approach" else 0
        P += 1 if q9 != "Going with the flow and embracing new opportunities as they come" else 0

        # Determine MBTI type
        mbti_type = ""
        mbti_type += "E" if E > I else "I"
        mbti_type += "S" if S > N else "N"
        mbti_type += "T" if T > F else "F"
        mbti_type += "J" if J > P else "P"

        st.success(f"Your MBTI type is: {mbti_type}")

if __name__ == '__main__':
    run_mbti_app()        

