## 🧩 Python Challenges 🐍

![Python](https://badgen.net/badge/Built%20with/Python/blue)
[![codecov](https://codecov.io/gh/aleattene/advent-of-code/graph/badge.svg?token=1GAFPNSUMB)](https://codecov.io/gh/aleattene/advent-of-code)
[![Tests](https://github.com/aleattene/advent-of-code/actions/workflows/aoc-tests.yml/badge.svg)](https://github.com/aleattene/advent-of-code/actions/workflows/aoc-tests.yml)
[![GitHub commits](https://badgen.net/github/commits/aleattene/python-challenges)](https://github.com/aleattene/python-challnges/commits/)
[![GitHub last commit](https://img.shields.io/github/last-commit/aleattene/python-challenges)](https://github.com/aleattene/python-challenges/commits/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/aleattene/advent-of-code/pulls)
[![License](https://img.shields.io/github/license/aleattene/python-challenges?color=blue)](https://github.com/aleattene/python-challenges/blob/main/LICENSE)

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
