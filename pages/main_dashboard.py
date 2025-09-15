import streamlit as st
import subprocess
import os

st.set_page_config(
    page_title="Martingale Strategy Hub", 
    page_icon="🎰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize navigation state
if 'current_game' not in st.session_state:
    st.session_state.current_game = "Dashboard"

# Sidebar navigation
with st.sidebar:
    st.title("🎰 Martingale Hub")
    st.write("---")
    
    # Game selection
    games = {
        "📊 Dashboard": "Dashboard",
        "🪙 Coin Flip": "Coin Flip",
        "🎲 Roulette": "Roulette", 
        "📈 Fibonacci": "Fibonacci"
    }
    
    selected_game = st.selectbox(
        "🎮 Selecciona un Juego:",
        options=list(games.keys()),
        index=list(games.values()).index(st.session_state.current_game),
        key="game_selector"
    )
    
    new_game = games[selected_game]
    
    # Handle navigation to other games
    if new_game != st.session_state.current_game:
        if new_game == "Coin Flip":
            st.switch_page("pages/coin_flip_martingale.py")
        elif new_game == "Roulette":
            st.switch_page("pages/martingale_bot.py")
        elif new_game == "Fibonacci":
            st.switch_page("../fibonacci_bot.py")
        # If Dashboard is selected, stay on current page
    
    st.session_state.current_game = new_game
    
    st.write("---")
    
    # Dashboard info
    st.write("📊 **Dashboard Overview**")
    st.write("Aprende sobre las estrategias de apuestas progresivas y sus riesgos.")
    
    st.write("---")
    
    # Navigation instructions
    st.info("💡 **Navegación Rápida**\n\nUsa el menú desplegable arriba para cambiar entre juegos.")
    
    st.write("---")
    st.write("**⚠️ Educacional Solamente**")
    st.write("Estos juegos demuestran por qué las estrategias progresivas fallan.")

st.title("🎰 Martingale Strategy Educational Hub")

st.write("""
Welcome to the **Martingale Strategy Educational Hub**! This collection demonstrates the famous 
martingale betting system across different casino games and scenarios.

⚠️ **Important**: All simulations are for educational purposes only. The martingale strategy, 
while mathematically sound in theory, fails in practice due to bankroll limits, table limits, 
and the reality of losing streaks.
""")

# Quick overview of available implementations
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎲 Roulette Martingale
    **File**: `martingale_bot.py`
    
    **Features**:
    - European roulette simulation
    - Red/Black/Green betting
    - Table limits ($10-$500)
    - Real-time progression tracking
    - Detailed failure analysis
    - Balance & bet charts
    
    **Best for**: Understanding casino table limits and house edge impact.
    """)

with col2:
    st.markdown("""
    ### 🪙 Coin Flip Martingale  
    **File**: `coin_flip_martingale.py`
    
    **Features**:
    - Perfect 50/50 odds
    - Pure martingale demonstration
    - No house edge complications
    - Losing streak probabilities
    - Risk/reward analysis
    - Bankruptcy scenarios
    
    **Best for**: Understanding pure martingale mathematics.
    """)

with col3:
    st.markdown("""
    ### 📈 Fibonacci Strategy
    **File**: `fibonacci_bot.py`
    
    **Features**:
    - Alternative progression system
    - Move forward on loss, back on win
    - Slower bet growth than martingale
    - Less aggressive risk profile
    - Sequence expansion
    
    **Best for**: Comparing progressive betting strategies.
    """)

st.write("---")

# Educational content
st.subheader("📚 Martingale Strategy Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### ✅ How Martingale "Works"
    1. **Start with base bet** (e.g., $10)
    2. **Double after every loss** ($10 → $20 → $40 → $80...)
    3. **Return to base bet after win**
    4. **Each cycle guarantees base bet profit**
    
    #### 🎯 Example Sequence
    - Bet $10 → **Lose** (Total: -$10)
    - Bet $20 → **Lose** (Total: -$30)  
    - Bet $40 → **Win** → Recover $40
    - **Net Result**: -$30 + $40 = **+$10 profit**
    """)

with col2:
    st.markdown("""
    #### ❌ Why Martingale Fails
    1. **Exponential growth**: Bets double each loss
    2. **Table limits**: Casinos cap maximum bets
    3. **Bankroll limits**: Most players can't afford long streaks
    4. **House edge**: Even "50/50" bets favor the house
    
    #### 🚫 Real Failure Scenarios
    - **10 losses in a row**: Need $10,240 next bet
    - **Table limit**: Usually $500-$5000 maximum
    - **Probability**: 10 losses ≈ 0.1% chance (happens!)
    - **Result**: Strategy breaks, losses unrecoverable
    """)

# Statistics and probabilities
st.subheader("📊 Martingale Mathematics")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Bet Progression**
    | Loss # | Bet Size | Total Risk |
    |--------|----------|------------|
    | 1      | $10      | $10        |
    | 2      | $20      | $30        |
    | 3      | $40      | $70        |
    | 4      | $80      | $150       |
    | 5      | $160     | $310       |
    | 6      | $320     | $630       |
    | 7      | $640     | $1,270     |
    | 8      | $1,280   | $2,550     |
    """)

with col2:
    st.markdown("""
    **Losing Streak Probabilities**
    | Streak | 50/50 Odds | Roulette (47.4%) |
    |--------|-------------|------------------|
    | 3      | 12.5%      | 14.8%           |
    | 4      | 6.3%       | 7.8%            |
    | 5      | 3.1%       | 4.1%            |
    | 6      | 1.6%       | 2.2%            |
    | 7      | 0.8%       | 1.1%            |
    | 8      | 0.4%       | 0.6%            |
    | 10     | 0.1%       | 0.2%            |
    """)

with col3:
    st.markdown("""
    **Risk Analysis**
    - **Risk**: Can lose thousands
    - **Reward**: Always just base bet
    - **After 8 losses**: Risk $2,550 to win $10
    - **Risk/Reward**: 255:1 ratio
    - **Expected Value**: Always negative
    - **Long-term Result**: Guaranteed loss
    """)

st.write("---")

# Launch buttons for each implementation
st.subheader("🚀 Try the Implementations")
st.write("Click the buttons below to run each martingale demonstration:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎲 Launch Roulette Martingale", key="roulette", type="primary"):
        st.write("**To run the Roulette Martingale:**")
        st.code("streamlit run martingale_bot.py", language="bash")
        st.info("This will open the roulette martingale simulation in a new browser tab.")

with col2:
    if st.button("🪙 Launch Coin Flip Martingale", key="coinflip", type="primary"):
        st.write("**To run the Coin Flip Martingale:**")
        st.code("streamlit run coin_flip_martingale.py", language="bash")
        st.info("This will open the coin flip martingale demonstration in a new browser tab.")

with col3:
    if st.button("📈 Launch Fibonacci Strategy", key="fibonacci", type="primary"):
        st.write("**To run the Fibonacci Strategy:**")
        st.code("streamlit run fibonacci_bot.py", language="bash")
        st.info("This will open the Fibonacci betting strategy simulation in a new browser tab.")

st.write("---")

# Quick comparison table
st.subheader("🆚 Strategy Comparison")

comparison_data = {
    "Strategy": ["Martingale", "Fibonacci", "Flat Betting"],
    "Progression": ["Double after loss", "Fibonacci sequence", "Same bet always"],
    "Risk Level": ["Very High", "Medium", "Low"],
    "Bet Growth": ["Exponential", "Linear", "None"],
    "Recovery": ["Full recovery + profit", "Gradual recovery", "No built-in recovery"],
    "Best Case": ["Quick profit", "Steady gains", "Consistent play"],
    "Worst Case": ["Total bankruptcy", "Significant losses", "Gradual losses"],
    "Table Limit Impact": ["Strategy killer", "Manageable", "No impact"]
}

st.table(comparison_data)

# Educational disclaimer
st.write("---")
st.error("""
🚨 **EDUCATIONAL DISCLAIMER** 🚨

These simulations are designed for educational purposes to demonstrate why progressive betting 
systems like martingale ultimately fail in real casino environments. Key points:

• **No system beats the house edge** - Casinos have mathematical advantages
• **Progressive systems increase risk** - You bet more when you're already losing  
• **Bankroll management is crucial** - Never risk money you can't afford to lose
• **Gambling should be entertainment** - Not a way to make money

**Remember**: If martingale actually worked, casinos would be out of business!
""")

# File listing for reference
st.write("---")
st.subheader("📁 Project Files")

files = [
    ("martingale_bot.py", "Main roulette martingale implementation with comprehensive tracking"),
    ("coin_flip_martingale.py", "Simple coin flip demonstration of pure martingale concept"),
    ("fibonacci_bot.py", "Fibonacci sequence betting strategy as alternative to martingale"),
    ("martingale_explanation.md", "Detailed mathematical explanation and casino examples"),
    ("main_dashboard.py", "This dashboard file for navigation between examples")
]

for filename, description in files:
    if os.path.exists(filename):
        st.write(f"✅ **{filename}** - {description}")
    else:
        st.write(f"❌ **{filename}** - {description} (Not found)")

st.write("---")
st.write("**Happy learning! 🎓 Remember: The house always wins in the long run.**")