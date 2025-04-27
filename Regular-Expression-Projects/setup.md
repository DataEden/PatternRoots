# 🛠 Setup Instructions for Email Pattern Matcher

## 1. Create and Activate Virtual Environment

To keep dependencies isolated, set up a virtual environment:

```bash
# Create environment
python -m venv .venv

# Activate environment
# On Linux/MacOS
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

---

## 2. Install Dependencies

Once inside the virtual environment, install the required packages:

```bash
pip install regex
```

> Note:  
> - The built-in `re` module does not require installation.
> - `regex` is an enhanced third-party library offering additional regular expression capabilities.

---

## 3. Run the Application

You can now run the matcher:

```bash
python app.py
```

or import it into other projects:

```python
from app import regex_email
print(regex_email("email:someone@example.com"))
```

---

## 📋 Notes

- The `.venv/` folder is excluded from version control via `.gitignore`.
- This setup ensures compatibility across different environments.