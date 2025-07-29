#  Plagiarism Detector CLI (Python Project)

A simple command-line Python application that compares two essays and detects word-level similarities to estimate potential plagiarism.

---
##  Features

- ✅ Preprocesses essays (removes punctuation, lowercase conversion)  
- ✅ Calculates word frequency for each essay  
- ✅ Detects and displays common words between the two essays  
- ✅ Computes a **plagiarism score** based on shared word usage  
- ✅ Allows users to:
  - Search how many times a word appears in each essay  
  - Export common words to a CSV file  
  - View similarity levels (Low/None, High)
---


##  Requirements

- Python 3 
- No external libraries required (uses only built-in modules)

---

##  Project Structure

```
plagiarism-detector/
│
├── essay-1.txt               # First essay to compare
├── essay-2.txt               # Second essay to compare
├── plagiarism_results.csv    # Auto-generated CSV of common words
└── plagiarism_detector.py    # Main Python script
```

---

##  How to Run

1. **Prepare the essays**  
   Place your two text files in the same directory as the script and name them:
   - `essay-1.txt`
   - `essay-2.txt`

2. **Run the script**  
   ```bash
   python3 plagiarism_detector.py
   ```

3. **Choose an option from the menu:**  
   ```
   Plagiarism Detector Menu:
   1. Show plagiarism score
   2. Search for a word
   3. Export CSV
   4. Exit
   ```

---

##  Plagiarism Score Levels

| Score Range | Interpretation         |
|-------------|------------------------|
| 0%–49.9%    | No plagarism           |
| 50%–100%    | Plagarism              |

---

##  Output

- The program prints the similarity score directly in the terminal.
- A CSV file `plagiarism_results.csv` is generated containing common words and their counts.

---

