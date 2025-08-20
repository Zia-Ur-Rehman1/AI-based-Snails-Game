# 🐌 AI-Based Snails Game

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Arcade](https://img.shields.io/badge/Arcade-2.x-green)
![Status](https://img.shields.io/badge/Status-Project-blueviolet)

> **Authors:** Zia-ur-Rehman & Ali Raza Khan  
> **Institute:** Namal Institute, Mianwali

---

## 🎯 Overview
**Snails** is a 2D, turn-based grid game where a **human** competes against an **AI agent**. Players move one cell at a time to **occupy (score) more grid squares** in **fewer moves**. The AI uses **heuristics** (and attempted **minimax**) to choose strong moves while respecting game constraints.

---

## 🧩 Game Rules
- 🧭 **Objective:** Occupy more grid squares than the opponent.  
- 🔁 **Turns:** Human goes, then AI; one move per turn.  
- ➡️ **Movement:** Horizontal/vertical by **one adjacent empty** cell → **+1 score** and leaves a **trail (slime)**.  
- 🧪 **Own trail:** You may move onto your **own trail**; you **slide** to the farthest trail cell in that direction (**no score**).  
- 🚫 **Forbidden:** No diagonal moves, no skipping cells, no moving onto opponent’s **trail** or **snail**.  
- 🏁 **End:** When the board is filled or a player is stuck, **highest score wins**.

---

## 🎮 Controls
- ⬆️⬇️⬅️➡️ **Arrow keys:** Move the human snail  
- ⏯ **P:** Pause  
- 🔄 **R:** Reset/Restart  
- 🚪 **Esc:** Exit

---

## 🧠 AI Strategy (Heuristic & Minimax)
- 🎯 **Priorities:**  
  1) Prefer **empty neighbors** → score gain  
  2) Reduce **distance to center** (strategic control)  
  3) Reduce **distance to opponent** (pressure)  
  4) If no empty neighbors → **slide on own trail** to reach empties  
  5) If still blocked → **edge-seeking** fallback  
- 🌲 **Minimax (attempted):** Depth-first exploration with heuristics to prune; further depth planned.

---

## 🧰 Requirements
- ✅ **Python 3.8+**
- ✅ **arcade** (graphics/game loop)
- ✅ **pyinstaller** (optional, Windows only—Arcade doesn’t support it on Linux)
- ✅ **VS Code** (recommended)

```bash
pip install arcade
# Optional (Windows): build an exe
pip install pyinstaller
```
## 🚀 Setup & Run
# 1) Clone
git clone https://github.com/Zia-Ur-Rehman1/AI-based-Snails-Game.git
cd AI-based-Snails-Game

# 2) Install deps
pip install arcade

# 3) Run
python main.py

## 🗂️ Board & State (10×10)

- 0 → Empty
- 1 → Human trail (splash)
- 11 → Human snail
- 2 → AI trail (splash)
- 22 → AI snail

🗺️ Roadmap

⏫ Deeper minimax with heuristic pruning

- 🧮 Better scoring functions (e.g., mobility + territory potential)
- 🌐 Optional AI vs AI simulation mode
- ✨ Animations, SFX, and themes

👥 Credits

- Zia-ur-Rehman

- Ali Raza Khan
