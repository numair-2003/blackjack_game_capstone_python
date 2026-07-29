# 🃏 Blackjack Game Capstone in Python

A complete command-line Blackjack card game programmed in Python. Play against the computer with classic casino rules, proper Ace handling, Blackjack detection, and the ability to replay using recursion.

## 📌 Overview

This is a Capstone project that implements a fully playable Blackjack game in pure Python (no external packages needed). It demonstrates:

- Importing and printing multi-line ASCII art from a separate module (`art.py`)
- Random card dealing using Python’s `random` module
- Proper Blackjack scoring rules including Ace = 1 or 11 and Blackjack detection
- Recursive function design for continuous play
- Clean separation of concerns with helper functions and detailed docstrings

The entire program logic is also visually documented in the included flowchart.

## 🔗 Quick Links

| Resource                  | Link                                                                 | Description                                      |
|---------------------------|----------------------------------------------------------------------|--------------------------------------------------|
| **GitHub Repository**     | https://github.com/numair-2003/blackjack_game_capstone_python        | Full source code, README, and project files      |
| **Replit**                | https://replit.com/@numair-2003/blackjack_game_capstone_python       | Run the Blackjack game instantly in the browser  |
| **ASCII Art Source**      | https://ascii.co.uk/art                                              | Website where the Blackjack logo was selected    |
| **Flowchart (draw.io)**   | https://app.diagrams.net/#G1eL-1uHVe-hDPR7NPJAafO9n2geGRxSvu#%7B%22pageId%22%3A%22qhqUl6ha3pGELj7gXrGA%22%7D | Interactive version of the program flowchart     |
| **Blackjack Rules**       | https://listmoz.com/view/6h34DJpvJBFVRlZfJvxF                         | Detailed reference for Blackjack rules           |
| **Play / Learn Blackjack**| https://games.washingtonpost.com/games/blackjack                     | Free online Blackjack to practice and learn      |

## ✨ Key Features

- 🃏 Classic Blackjack rules with Ace handling (1 or 11)
- 🎯 Automatic Blackjack detection (Ace + 10-value card)
- 👤 Player can hit or stand
- 🤖 Computer (dealer) automatically hits until score ≥ 17
- 🔄 Recursive replay – play as many rounds as you want
- 🎨 Beautiful large ASCII Blackjack logo displayed at launch
- 🧠 Clean modular design with well-documented functions

## 📜 How to Play Blackjack (Rules)

Blackjack is a popular card game where the goal is to get a hand value as close to **21** as possible without going over.

### Card Values
- Number cards (2–10) → face value
- Face cards (Jack, Queen, King) → **10**
- Ace → **11** or **1** (whichever is better for the player)

### Basic Rules
1. Both the player and the computer (dealer) are dealt **two cards**.
2. The player can see both of their own cards and only the **first card** of the dealer.
3. The player decides whether to **Hit** (take another card) or **Stand** (keep current hand).
4. If the player’s score goes over 21 → **Bust** (player loses).
5. After the player stands, the dealer must keep taking cards until their score is **17 or higher**.
6. **Blackjack** (Ace + any 10-value card on the first two cards) is an automatic win.
7. Whoever is closer to 21 without going over wins. Equal scores result in a **draw**.

> 📚 **Want more details?**  
> - Full rules reference: [listmoz.com – Blackjack Rules](https://listmoz.com/view/6h34DJpvJBFVRlZfJvxF)  
> - Practice online: [Washington Post – Play Blackjack](https://games.washingtonpost.com/games/blackjack)

## 🧠 Skills & Concepts Learned

This Capstone project is excellent for practicing core Python concepts:

- **Docstrings** — Every function includes a clear docstring explaining its purpose and behaviour.
- **Recursion** — The main `play_game()` function calls itself so the player can keep playing new rounds.
- **Random Module** — Cards are dealt randomly using `random.choice()`.
- **List Manipulation** — Cards are stored in lists; Aces are dynamically converted from 11 → 1 when needed.
- **Modular Programming** — The ASCII art logo is cleanly separated into its own file (`art.py`).
- **Raw Strings** — The logo uses a raw string (`r""" ... """`) for clean multi-line ASCII art.
- **f-strings** — Modern and readable string formatting for displaying hands and scores.
- **Control Flow** — Combination of `while` loops, `if/elif/else`, and recursive calls for a smooth game experience.
- **Screen Clearing Trick** — Uses `print("\n" * 200)` to clear the terminal between games.

## 💻 Example Runs (Sample Console Output)

> **Note:** The large ASCII Blackjack logo from `art.py` is printed at the start of every new game.

### Example 1: Player Wins

```text
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
... (full ASCII logo) ...

Your cards: [10, 8], current score: 18
Computer's first card: 7
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 8], final score: 18
Computer's final hand: [7, 9], final score: 16
You win 😃
```

### Example 2: Player Gets Blackjack

```text
Your cards: [11, 10], current score: 0
Computer's first card: 5

Your final hand: [11, 10], final score: 0
Computer's final hand: [5, 8, 6], final score: 19
You have a Blackjack. You win 😎
```

### Example 3: Player Busts

```text
Your cards: [10, 6], current score: 16
Computer's first card: 9
Type 'y' to get another card, type 'n' to pass: y
Your cards: [10, 6, 9], current score: 25

Your final hand: [10, 6, 9], final score: 25
Computer's final hand: [9, 7], final score: 16
You went over. You lose 😭
```

## 🖼️ Visuals & Documentation

### ASCII Art Logo
The stylish Blackjack logo was hand-picked from the excellent collection at **[ASCII Art](https://ascii.co.uk/art)** and placed inside `art.py` as a raw string.

### Program Flowchart
![Program Flowchart](blackjack_flowchart.drawio.png)

[🔗 View the interactive flowchart on draw.io](https://app.diagrams.net/#G1eL-1uHVe-hDPR7NPJAafO9n2geGRxSvu#%7B%22pageId%22%3A%22qhqUl6ha3pGELj7gXrGA%22%7D)

## 📁 Project Structure

```
blackjack_game_capstone_python/
├── art.py                              # ASCII Blackjack logo (raw string)
├── main.py                             # Main game logic (recursive version)
├── blackjack_flowchart.drawio.png      # Program flowchart image
├── README.md
└── .git/                               # After running git init
```

## 🚀 How to Run the Project

### ▶️ Locally (Windows / macOS / Linux)

1. Open a terminal / Command Prompt / PowerShell
2. Navigate to your project folder
3. Run the program:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions:
   - Type `y` to start a new game
   - Type `y` to hit (take another card) or `n` to stand
   - After each round the game will ask if you want to play again

### 🌐 On Replit (Easiest for sharing / quick testing)

**Best Method: Import from GitHub**

1. Go to [https://replit.com](https://replit.com) and log in
2. Click **+ Create Repl** → choose **Import from GitHub**
3. Paste your repo URL:  
   `https://github.com/numair-2003/blackjack_game_capstone_python`
4. Click **Import**
5. Once the files appear, press the big green **Run** ▶️ button

**Alternative (Manual)**:
1. Create a new **Python** Repl
2. Drag & drop `art.py` and `main.py` into the file explorer
3. Click **Run**

## 📤 Pushing Your Project to GitHub

### Step 1: Create the Repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Fill in:
   - **Repository name**: `blackjack_game_capstone_python`
   - **Description** (copy & paste the text below)
   - Visibility: **Public**
   - **Important**: Leave **"Add a README file"** turned **OFF**
3. Click **Create repository**


### Step 2: Push from Your Local Machine

Open terminal in your project folder and run:

```bash
# Initialize git (only needed once)
git init

# Stage all files
git add .

# Create first commit
git commit -m "Initial commit: Blackjack Capstone with recursive gameplay and ASCII logo"

# Connect to your GitHub repo
git remote add origin https://github.com/numair-2003/blackjack_game_capstone_python.git

# Rename branch to main and push
git branch -M main
git push -u origin main
```

## 🤝 Ideas for Future Improvements

- Add a betting / chips system
- Keep track of win/loss statistics across multiple rounds
- Add colour to the terminal using `colorama` or `rich`
- Support multiple players
- Convert to a GUI version with `tkinter` or `customtkinter`
- Add more advanced Blackjack side bets (Insurance, Double Down, Split)

## 📜 License

This project is released under the **MIT License** — feel free to use, modify, and share!

**Made with ❤️ and lots of Python** by [numair-2003](https://github.com/numair-2003)
