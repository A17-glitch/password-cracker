# password-cracker
A simple Python-based password cracker that randomly guess the user-provided password character by character. Longer passwords take more time to crack, so patience is required.

# 🔑 Password Cracking Simulation (Python)

This poject is a **password guessing simulation** written entirely in Python.
The user enter a password, and the program tries to guess it **randomly character** until it matchs the original password.

⚠️**Note:**
- This project is for **educational purpose only**.
- It is **not** a real-world password cracker and should not be used for malicious activities.
- The purpose is to demostrate how brute-force/random guessing works in principle.

---

## 🛠️ Technologies Used
- **Python 3**
- `random` module (for random guessing)
- `os` module (to clear consol for better visualization)
- `string` module (to include characters, digits, and punctuation)

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/password-cracker-simulation.git

2. Navigate into the folder:
cd password-cracker-simulation

3. Run the script:
python pass-crack.py

4. Enter a password of your choice, and watch the program try to crack it.

📊 Example Output
Enter a password: ab
Cracking Password...Please Wait!
b
ab
Your Passwordd id: ab

⚡Limitations
- The program uses random guesses, so the cracking time can vary greatly.
- The more complex and longer the password, the longer it takes to crack.
- This is not optimized for efficiency---it's designed for learning and fun.

🎯 Purpose
This project is created as a fun learning experiment to understand the concept of brute force password guessing.
It demostrates how random guessing works, and why strong passwords make brute-force attacks impractical.

