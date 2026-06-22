# ❌ Python Tic Tac Toe ⭕

A clean **2-player terminal Tic Tac Toe game** built in Python with scoreboard and multi-round support.

---

## 🎮 Features

- ✅ 2-player local game (X vs O)
- ✅ Simple 1-9 number input
- ✅ Win detection (rows, columns, diagonals)
- ✅ Draw detection
- ✅ Winning cells highlighted on board
- ✅ Scoreboard across multiple rounds
- ✅ Play again option
- ✅ Overall winner at the end
- ✅ Clean terminal UI

---

## 📁 Project Structure

```
tictactoe/
│
├── main.py      → Entry point — run this
├── game.py      → Game loop & logic
├── board.py     → Board state & win detection
├── player.py    → Player class & scores
├── display.py   → Terminal UI & rendering
└── README.md    → This file
```

---

## ▶️ How to Run

### Requirements
- Python 3.6+
- No external libraries needed!

```bash
git clone https://github.com/YOUR_USERNAME/python-tictactoe.git
cd python-tictactoe
python main.py
```

---

## 🕹️ How to Play

Use number keys **1–9** matching board positions:

```
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9
```

| Command | Action             |
|---------|--------------------|
| `1`–`9` | Place your mark    |
| `help`  | Show position guide|
| `quit`  | Exit the game      |

---

## 📸 Screenshot

```
========================================
      ❌  TIC TAC TOE  ⭕
        2 Player Game
========================================

  Round 1

  📊 Ahmed (X): Wins: 1  Draws: 0
  📊 Ali (O):   Wins: 0  Draws: 0

   Board          Positions
  ───────────    ───────────
   X | O | X      1 | 2 | 3
  ───────────    ───────────
   . | X | O      4 | 5 | 6
  ───────────    ───────────
  [X]| O |[X]     7 | 8 | 9
  ───────────    ───────────

  🏆  Ahmed (X) WINS!
```

---

## 📄 License

MIT License — free to use and modify!
