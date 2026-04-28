# 🃏 Poker Odds Calculator (CLI)

A command-line poker odds calculator written in Python.

It calculates the probability of each player winning a Texas Hold'em hand using:

- ✅ Exact brute-force enumeration (when feasible or forced)
- ⚡ Monte Carlo simulation (for large search spaces)

This is V1 Version!

It is not extremely polished but works well 

I will keep working on it and publish the second version soon 

## ⚠️ Status

This is **Version 1 (V1)** of the project.

The core functionality is complete and accurate, but there is still room for improvements in performance, usability, and features.

Future updates will include optimizations and additional enhancements.

Feedback is welcome!

---

## 🚀 Features

- Supports multiple players
- Exact odds calculation from flop/turn/river
- Monte Carlo simulation for preflop / large cases
- Handles:
  - ties and split pots
  - all hand rankings
  - Ace-low straights (A-2-3-4-5)
- Clean CLI output

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/steampunk-wonderer/cli-poker-calc.git
cd cli-poker-calc

# Run with Python 3.10+:
python3 main.py ...

#Or use 
./main_test.sh #to run a test scenario
```

## 🧠 Usage

```bash
python3 main.py \
  --players 3 \
  --player_cards 5dJh \
  --other_players_cards 8s9s 5hAc \
  --community_cards Qh2cAh \
  --mode auto \
  --simulations 10000
```

```See section below for more examples ```

## 🔧 Arguments


```--players: Number of players```

```--player_cards: Your cards (e.g. AhKd)```

```--other_players_cards: Other players' cards```

```--community_cards: Known board cards```

```--mode: auto, exact, or monte-carlo```

```--simulations: Number of Monte Carlo iterations```

## ⚙️ Modes

```exact```

Checks all possible board combinations (guaranteed correct, slower).

```monte-carlo```

Randomly samples boards (fast, approximate).

```auto```

Chooses automatically:

Monte Carlo when combinations are large
Exact when feasible

## 📊 Example Output

```text
===========================
      Poker Odds
===========================

Players:
   player-0 | 5d Jh
   player-1 | 8s 9s
   player-2 | 5h Ac

Board:
   No community cards

Method:
   Exact

Cases checked:
   1,370,754

---------------------------
Results:
---------------------------
   player-0: 19.02%
   player-1: 40.41%
   player-2: 40.56%
```

## 🎲 Monte Carlo Example

```text
Method:
   Monte Carlo

Simulations:
   10,000

Estimated error:
   ±1%

---------------------------
Results:
---------------------------
   player-0: 26.08% (±0.90%)
   player-1: 22.15% (±0.85%)
   player-2: 51.77% (±1.00%)
```

## 🧮 How it Works

- Generates all possible remaining boards (exact mode)
- OR samples random boards (Monte Carlo)
- Evaluates best hand per player
- Handles ties by splitting probability


## Usage Examples

### Correct Examples 

```bash
#Exact mode — no community cards
python3 main.py \
  --players 3 \
  --player_cards 5dJh \
  --other_players_cards 8s9s 5hAc \
  --mode exact

#Exact mode — flop known
python3 main.py \
  --players 3 \
  --player_cards 3c4d \
  --other_players_cards 10s7c 3h2d \
  --community_cards Qh2cAh \
  --mode exact

#Monte Carlo mode
python3 main.py \
  --players 3 \
  --player_cards 3c4d \
  --other_players_cards 10s7c 3h2d \
  --community_cards Ad8s \
  --mode monte-carlo \
  --simulations 10000

#Auto mode
python3 main.py \
  --players 3 \
  --player_cards 5dJh \
  --other_players_cards 8s9s 5hAc \
  --mode auto \
  --simulations 10000

# Heads-up example
python3 main.py \
  --players 2 \
  --player_cards AhKd \
  --other_players_cards QsQh \
  --community_cards 2c7d9h \
  --mode exact

# Turn example
python3 main.py \
  --players 2 \
  --player_cards AhKd \
  --other_players_cards QsQh \
  --community_cards 2c7d9hJc \
  --mode exact

#River example
python3 main.py \
  --players 2 \
  --player_cards AhKd \
  --other_players_cards QsQh \
  --community_cards 2c7d9hJcAs \
  --mode exact
```

### Invalid / Missing Input Examples

```bash
#Missing player cards
python3 main.py \
  --players 3 \
  --other_players_cards 8s9s 5hAc

# Missing other players' cards
python3 main.py \
  --players 3 \
  --player_cards 5dJh

#Wrong number of opponents
python3 main.py \
  --players 3 \
  --player_cards 5dJh \
  --other_players_cards 8s9s

#Invalid card format
python3 main.py \
  --players 2 \
  --player_cards Hello \
  --other_players_cards QsQh

#Duplicate card 
python3 main.py \
  --players 2 \
  --player_cards AhKd \
  --other_players_cards AhQh
```

## 🛠️ Future Improvements
GUI or web interface

Multi-threaded simulations

Adaptive Monte Carlo (auto accuracy)

Support for unknown opponent hands

Performace encahing 

## 🤝 Contributing

Feel free to open issues or submit pull requests.

## Author

Alexandros Papadopoulos