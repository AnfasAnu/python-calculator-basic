import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []
    
st.title("Anfas Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operator = st.selectbox(
    "Choose Operation",
    ["+", "-", "*", "/","%"]
)
if st.button("Calculate"):
    result = None
    if operator == "+":
     result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            st.error("error: division by zero")
        else:
            result = num1 / num2
    elif operator == "%":
        if num2 == 0:
            st.error("error: modulo by zero")
        else:
            result = num1 % num2

    if result is not None:
        st.success(f"Result: {result}")
        st.session_state.history.append(f"{num1} {operator} {num2} = {result}")
st.subheader("Calculation History")
for item in st.session_state.history:
    st.write(item)
if st.button("Clear History"):
    st.session_state.history.clear()