# 🌐 Streamlit Web Calculator

A modern, responsive web application for performing calculations, built using Streamlit.

---

## 🛠️ Features

- **Web UI**: User-friendly input fields and selector boxes.
- **Extended Arithmetic**: Support for addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulo (`%`).
- **Real-time Validations**:
  - Division-by-zero checks.
  - Modulo-by-zero checks.
- **Clean Success/Error Banners**: Uses Streamlit's native success and error styling for results and error messages.

---

## 🚀 Installation & Setup

To run this application, you need to install `streamlit`.

### 1. Install Dependencies
```bash
pip install streamlit
```

### 2. Launch the Web Server
Run the Streamlit application from the root of the project directory:
```bash
streamlit run calculator_streamlit.py
```

After running, the application will automatically open in your default browser at:
`http://localhost:8501` (or next available port)

---

## 📖 Step-by-Step Usage

1. **Enter First Number**: Type or adjust the first number in the numerical input block.
2. **Enter Second Number**: Type or adjust the second number.
3. **Choose Operation**: Click the dropdown select box and choose one of `+`, `-`, `*`, `/`, `%`.
4. **Calculate**: Click the **Calculate** button to compute the result. The result is displayed immediately in a highlighted banner.

---

## 🔍 Code Overview

The web UI is created using Streamlit components:
- `st.title` for header title banner.
- `st.number_input` for number input boxes.
- `st.selectbox` for operator selection.
- `st.button` for calculating when pressed.
- `st.success` / `st.error` for displaying results.
