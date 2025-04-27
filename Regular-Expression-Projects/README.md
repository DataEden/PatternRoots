# 📧 Email Pattern Matcher (Python)

### 🌿 A Simple Email Validation Utility
**"Finding structure in the wildness of text — one email at a time."**

---

### 🌍 Part of the PatternRoots Lab  
**DataEden's** exploration of pattern-matching in natural and digital forms.

---

This Python microproject provides a **basic email pattern matcher and validator** using regular expressions.  
It supports recognizing both:
- **Prefixed emails** like `email:example@domain.com`
- **Plain emails** like `example@domain.com`

It can **validate**, **standardize**, and **format** email strings into a consistent structure.

---

## 🔧 Features

- ✅ Validates if a string is a correctly formatted email address.
- ✅ Recognizes both prefixed (`email:`) and unprefixed formats.
- ✅ Standardizes detected emails into a consistent `email:you@example.com` format.
- ✅ Gracefully handles missing prefixes.
- ✅ Uses both Python’s built-in `re` module and the `regex` library for enhanced pattern matching.

---

## 🚀 How It Works

```python
import re
import regex

def regex_email(str) -> str:
    # Match 'email:' prefix first
    # Validate the email pattern
    # If no prefix found, search and prepend
    # Return standardized email or 'invalid email'
```

Examples:

| Input | Output |
|:---|:---|
| `email:someone@example.com` | `email:someone@example.com` |
| `someone@example.com` | `email:someone@example.com` |
| `random text` | `invalid email` |

---

## 🛠 Installation & Setup

A Python virtual environment (`.venv`) is recommended.

See [`setup.md`](setup.md) for detailed instructions.

Quick setup:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install regex
```

---

## 📁 File Structure

| File | Purpose |
|:---|:---|
| `app.py` | Main email matcher script |
| `README.md` | Project documentation |
| `setup.md` | Setup and environment guide |

---

## 🧪 Future Enhancements

- [ ] Extend to validate additional domain structures (`.edu`, `.co.uk`, etc.)
- [ ] Bulk email checking from files
- [ ] Command Line Interface (CLI) for real-time validation
- [ ] Unit tests (`unittest` or `pytest`)

---

## 🔒 License

This project is licensed under the **MIT License** — freely usable and extensible.  
See [LICENSE](../LICENSE).

---

## 🌱 Part of the PatternRoots Ecosystem

🌿 "Grow your skills, your tools, and your creativity — one pattern at a time."