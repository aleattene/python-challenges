## 🧩 Python Challenges 🐍

A collection of my **python coding challenges** and practice **exercises**, focusing on **problem solving**, **data structures**, and **algorithms**.

---

### Contents
- [**Advent of Code** 🎄](https://github.com/aleattene/python-challenges/tree/main/advent_of_code)
- [**Everybody Codes** 🧠](https://github.com/aleattene/python-challenges/tree/main/everybody-codes)
- [**Codewars** ⚔️](https://github.com/aleattene/python-challenges/tree/main/codewars)
- [**Edabit** 🎯](https://github.com/aleattene/python-challenges/tree/main/edabit)
- [**Python Workbook** 📓](https://github.com/aleattene/python-challenges/tree/main/learning/python-workbook)

---

### Quickstart
**1) Clone and enter the repo**
```bash
git clone https://github.com/aleattene/python-challenges.git
cd python-challenges
```

**2) (optional) create & activate a virtual environment**
```bash
python -m venv env_name
(mac) source env_name/bin/activate
(win) env_name\Scripts\activate
```

**3) Install dependencies**
```bash
pip install -U pip
pip install -r requirements.txt
```

**4) Run all tests**
```bash
pytest -q
```

**or run tests for a specific area**
```bash
# Advent of Code
pytest advent-of-code -q

# Everybody Codes
pytest everybody_codes -q

# Codewars
pytest codewars -q

# Edabit
pytest edabit -q

# Python Workbook
pytest learning/python-workbook -q
```

---

### Repository Structure
```bash
python-challenges/
├─ advent-of-code/                # Advent of Code solutions + tests
├─ codewars/                      # Codewars kata + tests
├─ edabit/                        # Edabit kata + tests
├─ everybody_codes/               # Everybody Codes quests + tests
└─ learning/
   └─ python-workbook/            # Python exercises
```
---
