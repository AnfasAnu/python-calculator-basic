import streamlit as st
st.set_page_config(
    page_title="Anfas Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Anfas Calculator")
st.caption("A simple calculator built with Python & Streamlit")

if "history" not in st.session_state:
    st.session_state.history = []
    
col1, col2 =st.columns(2)
with col1:
    num1=st.number_input("Enter first number")
with col2:
    num2=st.number_input("Enter second number")    

operator = st.selectbox(
    "Choose Operation",
    ["+", "-", "*", "/","%"]
)
st.write("")
if st.button("🧮 Calculate", use_container_width=True):
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

with st.expander("📜 Calculation History"):
    
    if st.session_state.history:
        for item in st.session_state.history:
            st.write(item)

        if st.button("🗑️ Clear History"):
            st.session_state.history.clear()
            st.rerun()
    else:
        st.info("No calculations yet")
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
            **Anfas Calculator**
            
            Version: 1.0   """)    
    st.markdown("### 👨‍💻 Developer")
    st.write(" Mohamad Anfas PK")
            
    st.markdown("""
                ### 🛠 Built With
                 - Python    
                 - Streamlit
                 """)
           
    st.markdown("### 🚀 Motto")
    st.write("Learning by building.")

st.divider()

st.caption("""
           © 2026 Mohamad Anfas PK    
Forge Project P01 • Version 1.0
""")