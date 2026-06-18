# 🧮 Python Calculator Suite

A clean, easy-to-use Python calculator suite featuring two distinct implementations: a **Command Line Interface (CLI) Calculator** and a modern **Streamlit Web Application**.

---

## 📂 Project Structure

- **`calculator.py`**: A CLI-based interactive terminal calculator.
- **`calculator_streamlit.py`**: A web-based GUI calculator built with Streamlit.
- **`README_CLI.md`**: Dedicated documentation for the CLI Calculator.
- **`README_STREAMLIT.md`**: Dedicated documentation for the Streamlit Web Application.

---

## 🚀 Quick Start & Installation

### Prerequisites

Ensure you have Python 3.8+ installed on your system. You can verify your installation by running:

```bash
python --version
```

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/AnfasAnu/python-calculator-basic.git
   cd python-calculator-basic
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install Streamlit (required only for the Web App version):
   ```bash
   pip install streamlit
   ```

---

## 💻 1. CLI Calculator (`calculator.py`)

An interactive command-line application that runs directly in your terminal.

### Features
- Support for addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Built-in division-by-zero validation.
- Infinite runtime loop until exited by the user.

### How to Run
```bash
python calculator.py
```

### Usage Instructions
1. Choose an operation: `+`, `-`, `*`, `/` or enter `!` to exit.
2. Enter the first and second numbers when prompted.
3. View the calculated result and repeat, or enter `!` to exit.

👉 **For detailed documentation, see [README_CLI.md](./README_CLI.md).**

---

## 🌐 2. Streamlit Web Calculator (`calculator_streamlit.py`)

A beautiful, reactive web application providing an intuitive graphical user interface.

### Features
- Interactive input fields for both numbers.
- Dropdown menu for operations: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulo (`%`).
- Modulo and division-by-zero validation.
- Responsive design with instant result calculation.

### How to Run
```bash
streamlit run calculator_streamlit.py
```

### Usage Instructions
1. Enter your first and second numbers in the input fields.
2. Select your desired operation from the dropdown box.
3. Click the **Calculate** button to view the result displayed in a success message block.

👉 **For detailed documentation, see [README_STREAMLIT.md](./README_STREAMLIT.md).**

---

## 📜 License

This project is open-source and available under the MIT License.