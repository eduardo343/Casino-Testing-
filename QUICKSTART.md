# 🚀 Quick Start Guide

Get the Martingale Strategy Educational Hub running in 3 minutes!

## ⚡ Instant Setup

### 1. Install Dependencies
```bash
pip install streamlit pandas plotly
```

### 2. Launch the App

**Option A: Unified App (RECOMMENDED!) ⭐**
```bash
streamlit run martingale_unified.py
```
**All games in one app with navigation menu!**

**Option B: Individual Games (Simple)**
```bash
streamlit run fibonacci_bot.py        # Just Fibonacci
streamlit run pages/main_dashboard.py # Educational overview
```
**Standalone games without navigation.**

**Option C: Multi-page System (Advanced/Experimental)**
```bash
streamlit run pages/main_dashboard.py  # Start multi-page system
```
**⚠️ Navegación experimental que puede fallar**

### 3. Start Learning!
Your browser will open automatically to `http://localhost:8501`

## 🎯 What to Try First

### Option 1: Complete Beginner
1. Read the main dashboard overview
2. Click "🪙 Launch Coin Flip Martingale"
3. Try a few flips with default settings
4. Watch how bet sizes double after losses

### Option 2: Want Realistic Casino Experience  
1. Click "🎲 Launch Roulette Martingale"
2. Start betting on Red/Black
3. Notice table limits and house edge effects
4. See how martingale fails in real casinos

### Option 3: Compare Different Strategies
1. Click "📈 Launch Fibonacci Strategy"  
2. See how Fibonacci progression differs
3. Compare risk profiles between systems

## 🔧 Troubleshooting

**Command not found?**
```bash
python -m streamlit run main_dashboard.py
```

**Missing modules?**
```bash
pip install --upgrade streamlit pandas plotly
```

**Need Python?** 
- Download from [python.org](https://python.org)
- macOS: `brew install python`
- Windows: Use Python from Microsoft Store

## 📱 Quick Demo

1. **Launch**: `streamlit run coin_flip_martingale.py`
2. **Choose**: Heads or Tails  
3. **Bet**: Start with $5 base bet
4. **Watch**: How losses double the next bet
5. **Learn**: Why this strategy fails even with 50/50 odds

## 🎓 5-Minute Learning Path

1. **Minute 1**: Launch dashboard, read overview
2. **Minute 2**: Try coin flip with 3-4 flips
3. **Minute 3**: Look at progression table in sidebar  
4. **Minute 4**: Try roulette, see table limits
5. **Minute 5**: Check risk analysis during losing streak

## 💡 Key Takeaways

- Martingale **seems** foolproof but isn't
- Losing streaks **will** happen 
- Bet sizes grow **exponentially** fast
- Table limits **break** the strategy
- House edge **guarantees** casino profits

**Remember**: This is educational only - don't gamble with real money! 🎰

---

**Need help?** Check the full [README.md](README.md) for detailed instructions.