import streamlit as st

st.title("Anfas Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operator = st.selectbox(
    "Choose Operation",
    ["+", "-", "*", "/","%"]
)
if st.button("Calculate"):
    if operator == "+":
       st.success(f"Result: {num1 + num2}")
    elif operator == "-":
        st.success(f"Result: {num1 - num2}")
    elif operator == "*":
        st.success(f"Result: {num1 * num2}")
    elif operator == "/":
        if num2 == 0:
            st.error("error: division by zero")
        else:
            st.success(f"Result: {num1 / num2}")
    elif operator == "%":
        if num2 == 0:
            st.error("error: modulo by zero")
        else:
            st.success(f"Result: {num1 % num2}")