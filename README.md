# 🎰 Martingale Strategy Educational Hub

An interactive educational project demonstrating the martingale betting strategy across different casino games and scenarios. This project helps users understand why progressive betting systems ultimately fail in real-world gambling situations.

![Martingale Strategy](https://img.shields.io/badge/Strategy-Martingale-red)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-green)
![License](https://img.shields.io/badge/License-Educational-yellow)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Educational Goals](#educational-goals)
- [Mathematical Background](#mathematical-background)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)

## 🎯 Overview

The **Martingale Strategy** is a betting system where you double your bet after every loss, with the goal of recovering all previous losses plus a profit equal to your original bet when you eventually win. While mathematically sound in theory, it fails in practice due to:

- **Bankroll limitations** - Players run out of money
- **Table limits** - Casinos cap maximum bets  
- **Exponential growth** - Bet sizes grow unsustainably fast
- **House edge** - Even "50/50" bets favor the casino

This project demonstrates these concepts through interactive simulations.

## ✨ Features

### 🎲 Multiple Game Implementations
- **Roulette Martingale** - Realistic casino simulation with house edge
- **Coin Flip Martingale** - Pure 50/50 odds demonstration
- **Fibonacci Strategy** - Alternative progressive betting system

### 📊 Educational Tools
- Real-time risk/reward analysis
- Losing streak probability calculations
- Interactive charts and visualizations
- Detailed progression tracking
- Bankruptcy scenario demonstrations

### 🎮 Interactive Experience
- Live betting simulations
- Customizable bet amounts
- Historical data tracking
- Export functionality for analysis
- Comprehensive statistics dashboard

## 🚀 Installation

### Prerequisites

- **Python 3.7+**
- **pip** (Python package installer)

### Quick Setup

1. **Clone or download this project:**
   ```bash
   cd /path/to/your/projects
   git clone <repository-url>  # or download ZIP and extract
   cd bot-test
   ```

2. **Install required packages:**
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Verify installation:**
   ```bash
   streamlit --version
   ```

### Alternative: Using Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv martingale_env

# Activate virtual environment
# On macOS/Linux:
source martingale_env/bin/activate
# On Windows:
# martingale_env\Scripts\activate

# Install packages
pip install streamlit pandas plotly

# When done, deactivate
deactivate
```

## 🎮 Usage

### Method 1: Unified App with Navigation Menu (RECOMMENDED!) ⭐

```bash
streamlit run martingale_unified.py
```

This opens a **single integrated application** where you can:
- Switch between games using the sidebar menu
- No need to open separate browser tabs
- All games in one place with individual game states
- Quick reset buttons for each game
- Seamless navigation between Dashboard, Coin Flip, Roulette, and Fibonacci

### Method 2: Run Individual Games (Simple)

```bash
# Individual games (basic versions)
streamlit run fibonacci_bot.py            # Fibonacci strategy only
streamlit run main_dashboard.py           # Educational overview
```

These are **standalone versions** without navigation menus.

### Method 3: Multi-page System (Advanced)

#### 🪙 Coin Flip Martingale (Best for beginners)
```bash
streamlit run coin_flip_martingale.py
```
**Perfect for understanding:**
- Pure martingale mathematics
- Risk/reward ratios
- Why even 50/50 odds fail

#### 🎲 Roulette Martingale (Most realistic)
```bash
streamlit run martingale_bot.py
```
**Perfect for understanding:**
- Casino table limits
- House edge impact
- Real-world betting scenarios

#### 📈 Fibonacci Strategy (Alternative approach)
```bash
streamlit run fibonacci_bot.py
```
**Perfect for understanding:**
- Alternative progressive systems
- Less aggressive bet growth
- Comparison with martingale

### Navigation Tips

1. **Start with the dashboard** to get an overview
2. **Try coin flip first** for pure concept understanding
3. **Move to roulette** for realistic casino simulation  
4. **Experiment with settings** in the sidebar
5. **Export data** to analyze your results

## 📁 Project Structure

```
bot-test/
├── README.md                     # This file  
├── martingale_unified.py         # ⭐ RECOMMENDED - All games in one app!
├── fibonacci_bot.py              # Standalone Fibonacci strategy
├── martingale_explanation.md     # Detailed mathematical explanation
├── QUICKSTART.md                 # 3-minute setup guide
├── roulette.gif                  # Animation file (optional)
└── pages/                        # Multi-page system (advanced/experimental)
    ├── README.md                 # Instructions for multi-page system
    ├── main_dashboard.py
    ├── coin_flip_martingale.py
    └── martingale_bot.py
```

## 🎯 Examples

### Example 1: Coin Flip Martingale Sequence

```
Starting Balance: $500, Base Bet: $5

Round 1: Bet $5 on Heads → Tails → LOSE (Balance: $495)
Round 2: Bet $10 on Heads → Tails → LOSE (Balance: $485) 
Round 3: Bet $20 on Heads → Heads → WIN (Balance: $505)

Result: +$5 profit after 3 rounds
Total wagered: $35, Total risk at round 3: $35
```

### Example 2: Martingale Failure Scenario

```
Starting Balance: $500, Base Bet: $10

Losing Streak Progression:
Round 1: Bet $10 → LOSE (Balance: $490, Next: $20)
Round 2: Bet $20 → LOSE (Balance: $470, Next: $40)  
Round 3: Bet $40 → LOSE (Balance: $430, Next: $80)
Round 4: Bet $80 → LOSE (Balance: $350, Next: $160)
Round 5: Bet $160 → LOSE (Balance: $190, Next: $320)
Round 6: Need $320 but only have $190 → BANKRUPTCY!

Total Lost: $310 attempting to win $10
Strategy Failed: Cannot continue doubling
```

## 🎓 Educational Goals

### Primary Learning Objectives

1. **Understand exponential growth** - How bet sizes escalate rapidly
2. **Recognize practical limitations** - Table limits and bankroll constraints  
3. **Grasp probability concepts** - Why losing streaks are inevitable
4. **Learn risk management** - Why progressive systems are dangerous

### Key Concepts Demonstrated

- **Gambler's Fallacy** - Past results don't affect future outcomes
- **Expected Value** - Why house edge guarantees casino profits
- **Risk of Ruin** - Probability of losing entire bankroll
- **Progressive Betting Pitfalls** - Increasing bets while losing

## 📊 Mathematical Background

### Martingale Bet Progression

| Round | Bet Amount | Total Risked | Probability of Loss |
|-------|------------|--------------|---------------------|
| 1     | $10        | $10          | 50%                 |
| 2     | $20        | $30          | 25%                 |
| 3     | $40        | $70          | 12.5%               |
| 4     | $80        | $150         | 6.25%               |
| 5     | $160       | $310         | 3.125%              |
| 6     | $320       | $630         | 1.56%               |
| 7     | $640       | $1,270       | 0.78%               |
| 8     | $1,280     | $2,550       | 0.39%               |

### Expected Value Calculation

For European Roulette (Red/Black bet):
- Win Probability: 18/37 ≈ 48.65%
- Loss Probability: 19/37 ≈ 51.35%  
- Expected Value: (18/37 × 1) + (19/37 × -1) = -0.027

**Result**: You lose 2.7 cents per dollar bet on average, regardless of betting system.

## 🚨 Disclaimer

**⚠️ IMPORTANT: FOR EDUCATIONAL PURPOSES ONLY ⚠️**

This project is designed to educate users about the mathematical principles behind betting strategies and demonstrate why they fail. It is **NOT** intended to:

- Encourage gambling
- Provide profitable betting strategies  
- Suggest that martingale can be profitable
- Replace professional financial advice

### Key Educational Messages

- **No betting system can overcome house edge**
- **Progressive systems increase risk, not profits**
- **Gambling should be entertainment, not investment**
- **The house always wins in the long run**

If you or someone you know has a gambling problem, please seek help:
- **National Problem Gambling Helpline**: 1-800-522-4700
- **Gamblers Anonymous**: www.gamblersanonymous.org

## 🛠️ Troubleshooting

### Common Issues

1. **"streamlit: command not found"**
   ```bash
   # Install streamlit
   pip install streamlit
   
   # Or use python -m
   python -m streamlit run main_dashboard.py
   ```

2. **"ModuleNotFoundError: No module named 'pandas'"**
   ```bash
   pip install pandas plotly
   ```

3. **Port already in use**
   ```bash
   # Use different port
   streamlit run main_dashboard.py --server.port 8502
   ```

4. **Browser doesn't open automatically**
   - Manually navigate to: http://localhost:8501
   - Or check terminal output for the correct URL

### System Requirements

- **Memory**: 512MB+ RAM
- **Storage**: 50MB+ free space
- **Network**: Internet connection for initial package downloads
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

## 🤝 Contributing

This is an educational project. If you'd like to contribute:

1. **Suggest improvements** to educational content
2. **Report bugs** or issues
3. **Add new gambling game examples**
4. **Improve mathematical explanations**
5. **Enhance visualizations**

### Ideas for Expansion

- **Blackjack martingale** implementation
- **Sports betting** scenarios  
- **Cryptocurrency trading** examples
- **Monte Carlo simulations** for long-term analysis
- **Mobile-responsive** design improvements

## 📚 Additional Resources

### Recommended Reading

- **"Beat the Dealer" by Edward Thorp** - Mathematical approach to gambling
- **"The Theory of Gambling and Statistical Logic" by Richard Epstein**
- **"Gambling Theory and Other Topics" by Mason Malmuth**

### Online Resources

- [Khan Academy: Probability and Statistics](https://www.khanacademy.org/math/statistics-probability)
- [MIT OpenCourseWare: Probability](https://ocw.mit.edu/courses/mathematics/)
- [Stanford CS109: Probability for Computer Scientists](http://cs109.stanford.edu/)

## 📄 License

This project is released under an **Educational Use License**. It may be used for:
- Learning and educational purposes
- Academic research and teaching
- Non-commercial personal use

**Not permitted:**
- Commercial gambling applications
- Real-money betting implementations  
- Promotion of gambling activities

---

**Remember: The best strategy in gambling is not to gamble at all!** 🎓

---

*Created for educational purposes to demonstrate the mathematical realities of progressive betting systems.*