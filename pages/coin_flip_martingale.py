import streamlit as st
import random
import time
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Coin Flip Martingale Hub", 
    page_icon="🪙", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize navigation state
if 'current_game' not in st.session_state:
    st.session_state.current_game = "Coin Flip"

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
        if new_game == "Dashboard":
            st.switch_page("main_dashboard.py")
        elif new_game == "Roulette":
            st.switch_page("martingale_bot.py")
        elif new_game == "Fibonacci":
            st.switch_page("fibonacci_bot.py")
        # If Coin Flip is selected, stay on current page
    
    st.session_state.current_game = new_game
    
    st.write("---")
    
    # Quick game info for Coin Flip
    st.write("🪙 **Coin Flip Martingale**")
    coin_balance = st.session_state.get('balance', 500)
    coin_current_bet = st.session_state.get('current_bet', 5)
    coin_consecutive_losses = st.session_state.get('consecutive_losses', 0)
    
    st.write(f"💰 Balance: ${coin_balance}")
    st.write(f"🎯 Bet: ${coin_current_bet}")
    st.write(f"📉 Streak: {coin_consecutive_losses}")
    
    if st.button("🔄 Reset Coin Game"):
        st.session_state.balance = 500
        st.session_state.current_bet = st.session_state.get('base_bet', 5)
        st.session_state.consecutive_losses = 0
        st.session_state.history = []
        st.session_state.total_wagered = 0
        st.session_state.peak_balance = 500
        st.session_state.total_flips = 0
        st.success("Coin game reset!")
    
    st.write("---")
    
    # Navigation instructions
    st.info("💡 **Navegación Rápida**\n\nUsa el menú desplegable arriba para cambiar entre juegos sin perder tu progreso.")
    
    st.write("---")
    st.write("**⚠️ Educacional Solamente**")
    st.write("Estos juegos demuestran por qué las estrategias progresivas fallan.")

st.title("🪙 Coin Flip Martingale - Martingale Hub")

# Educational content
with st.expander("📚 Pure Martingale Strategy Explained"):
    st.write("""
    **Coin Flip Martingale** is the simplest form of the martingale betting strategy.
    
    **How it works:**
    - Choose Heads or Tails
    - Start with a base bet (e.g., $5)
    - **When you lose**: Double your bet
    - **When you win**: Return to base bet
    - **Goal**: Each winning cycle recovers all losses + base bet profit
    
    **Perfect 50/50 Example:**
    - Bet $5 on Heads → Tails (Lose: -$5)
    - Bet $10 on Heads → Tails (Lose: -$15 total)
    - Bet $20 on Heads → **Heads** (Win: -$15 + $20 = +$5 profit)
    
    **⚠️ Key Risk**: Even with perfect 50/50 odds, long losing streaks can bankrupt you!
    """)

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 500
if 'base_bet' not in st.session_state:
    st.session_state.base_bet = 5
if 'current_bet' not in st.session_state:
    st.session_state.current_bet = 5
if 'consecutive_losses' not in st.session_state:
    st.session_state.consecutive_losses = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'total_wagered' not in st.session_state:
    st.session_state.total_wagered = 0
if 'peak_balance' not in st.session_state:
    st.session_state.peak_balance = 500
if 'total_flips' not in st.session_state:
    st.session_state.total_flips = 0

# Display current status
st.subheader("📊 Current Status")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("💰 Balance", f"${st.session_state.balance}")
with col2:
    st.metric("🎯 Current Bet", f"${st.session_state.current_bet}")
with col3:
    st.metric("📉 Losing Streak", st.session_state.consecutive_losses)
with col4:
    st.metric("🪙 Total Flips", st.session_state.total_flips)

# Martingale progression display
st.write("**Martingale Progression:**")
progression = []
bet = st.session_state.base_bet
total_risk = 0
for i in range(10):
    if i == st.session_state.consecutive_losses:
        progression.append(f"**→ ${bet}**")
    else:
        progression.append(f"${bet}")
    total_risk += bet
    bet *= 2
    if bet > st.session_state.balance * 2:  # Practical limit
        progression.append("🚫 BANKROLL LIMIT")
        break
st.write(" → ".join(progression))

# Risk analysis
if st.session_state.consecutive_losses > 0:
    total_at_risk = sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses + 1)])
    potential_profit = st.session_state.base_bet
    risk_ratio = total_at_risk / potential_profit
    
    if st.session_state.consecutive_losses >= 4:
        st.error(f"""
        🚨 **EXTREME RISK WARNING**
        - Total invested in sequence: ${total_at_risk - st.session_state.current_bet}
        - Current bet required: ${st.session_state.current_bet}
        - Total at risk: ${total_at_risk}
        - Potential profit: ${potential_profit}
        - Risk/Reward Ratio: **{risk_ratio:.1f}:1**
        
        You're risking ${total_at_risk} to win ${potential_profit}!
        """)
    elif st.session_state.consecutive_losses >= 2:
        st.warning(f"""
        ⚠️ **Risk Analysis**
        - Sequence investment: ${total_at_risk - st.session_state.current_bet}
        - Next bet: ${st.session_state.current_bet}
        - Risk/Reward: {risk_ratio:.1f}:1
        """)

# Coin selection
st.write("### 🪙 Choose Your Side")
choice = st.radio("Call it:", ["Heads", "Tails"], horizontal=True)

# Check if can afford current bet
can_afford = st.session_state.current_bet <= st.session_state.balance

if not can_afford:
    st.error(f"""
    💸 **INSUFFICIENT FUNDS!**
    Need: ${st.session_state.current_bet}
    Have: ${st.session_state.balance}
    
    Martingale sequence broken! Must reset to base bet.
    """)

# Flip button
if st.button("🪙 Flip the Coin!", disabled=not can_afford):
    # Animation
    with st.spinner("Flipping coin..."):
        time.sleep(1.5)
    
    # Perfect 50/50 coin flip
    result = random.choice(["Heads", "Tails"])
    
    # Display result with emoji
    coin_emoji = "👑" if result == "Heads" else "⚡"
    st.write(f"## {coin_emoji} {result}!")
    
    win = (choice == result)
    bet_amount = st.session_state.current_bet
    
    # Update counters
    st.session_state.total_wagered += bet_amount
    st.session_state.total_flips += 1
    
    if win:
        # Won the bet
        st.success(f"🎉 **WINNER!** You called {choice} and got {result}")
        st.session_state.balance += bet_amount
        
        # Martingale win explanation
        if st.session_state.consecutive_losses > 0:
            total_recovered = sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses)])
            st.balloons()
            st.success(f"""
            🎊 **MARTINGALE SUCCESS!**
            - Losing streak: {st.session_state.consecutive_losses} flips
            - Total recovered: ${total_recovered}
            - Profit: ${st.session_state.base_bet}
            - Net gain: ${total_recovered + st.session_state.base_bet}
            """)
        else:
            st.success(f"💰 Simple win! Profit: ${bet_amount}")
        
        # Reset to base bet
        st.session_state.current_bet = st.session_state.base_bet
        st.session_state.consecutive_losses = 0
        
        st.info(f"🔄 **Martingale Reset**: Next bet returns to ${st.session_state.base_bet}")
        
    else:
        # Lost the bet
        st.error(f"💸 **LOST!** You called {choice} but got {result}")
        st.session_state.balance -= bet_amount
        st.session_state.consecutive_losses += 1
        
        # Calculate next bet
        next_bet = bet_amount * 2
        
        # Check if we can continue
        if next_bet > st.session_state.balance:
            st.error(f"""
            🚫 **MARTINGALE FAILURE - BANKROLL EXHAUSTED!**
            - Next required bet: ${next_bet}
            - Your balance: ${st.session_state.balance}
            - Cannot continue doubling!
            - Total lost in sequence: ${sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses)])}
            
            **The martingale strategy has failed.**
            """)
            # Reset to base bet (or max affordable)
            st.session_state.current_bet = min(st.session_state.base_bet, st.session_state.balance)
            st.session_state.consecutive_losses = 0
        else:
            st.session_state.current_bet = next_bet
            sequence_loss = sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses)])
            st.warning(f"""
            📈 **Martingale Progression**
            - Previous bet: ${bet_amount} → Next bet: ${next_bet}
            - Losing streak: {st.session_state.consecutive_losses}
            - Total sequence loss: ${sequence_loss}
            - Need ${next_bet} to continue (and ${st.session_state.base_bet} profit if you win)
            """)
    
    # Update peak balance
    if st.session_state.balance > st.session_state.peak_balance:
        st.session_state.peak_balance = st.session_state.balance
    
    # Save to history
    st.session_state.history.append({
        "Flip": st.session_state.total_flips,
        "Called": choice,
        "Result": result,
        "Win": "✅" if win else "❌",
        "Bet": bet_amount,
        "Balance": st.session_state.balance,
        "Streak": st.session_state.consecutive_losses if not win else 0
    })

# Statistics and History
if st.session_state.history:
    st.subheader("📊 Statistics")
    
    df = pd.DataFrame(st.session_state.history)
    
    # Basic stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Flips", len(df))
    with col2:
        wins = df[df['Win'] == '✅'].shape[0]
        win_rate = (wins / len(df) * 100) if len(df) > 0 else 0
        st.metric("Win Rate", f"{win_rate:.1f}%")
    with col3:
        st.metric("Total Wagered", f"${st.session_state.total_wagered}")
    with col4:
        profit_loss = st.session_state.balance - 500
        st.metric("Profit/Loss", f"${profit_loss:+}")
    
    # Advanced stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Peak Balance", f"${st.session_state.peak_balance}")
    with col2:
        max_streak = df['Streak'].max()
        st.metric("Max Losing Streak", max_streak)
    with col3:
        max_bet = df['Bet'].max()
        st.metric("Largest Bet", f"${max_bet}")
    with col4:
        drawdown = st.session_state.peak_balance - st.session_state.balance
        st.metric("Current Drawdown", f"${drawdown}")
    
    # Theoretical vs Actual
    st.subheader("🎯 Theoretical vs Actual Performance")
    expected_wins = len(df) * 0.5
    actual_wins = wins
    variance = actual_wins - expected_wins
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Expected Wins (50%)", f"{expected_wins:.1f}")
    with col2:
        st.metric("Actual Wins", f"{actual_wins} ({variance:+.1f})")
    
    # Charts
    st.subheader("📈 Performance Charts")
    
    # Balance over time
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df['Flip'],
        y=df['Balance'],
        mode='lines+markers',
        name='Balance',
        line=dict(color='blue', width=2),
        marker=dict(size=6, color=['green' if w == '✅' else 'red' for w in df['Win']])
    ))
    fig1.add_hline(y=500, line_dash="dash", line_color="gray", annotation_text="Starting Balance")
    fig1.update_layout(
        title="Balance Over Time",
        xaxis_title="Flip Number",
        yaxis_title="Balance ($)",
        hovermode='x unified'
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Bet progression
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=df['Flip'],
        y=df['Bet'],
        marker_color=['red' if w == '❌' else 'green' for w in df['Win']],
        name='Bet Amount'
    ))
    fig2.update_layout(
        title="Bet Progression (Red = Loss, Green = Win)",
        xaxis_title="Flip Number",
        yaxis_title="Bet Amount ($)",
        hovermode='x'
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Recent history table
    st.subheader("📋 Recent Flip History")
    recent_df = df.tail(10)
    st.dataframe(recent_df, use_container_width=True)
    
    # Download option
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Full History", csv, "coin_flip_history.csv", "text/csv")

# Settings Sidebar
with st.sidebar:
    st.header("⚙️ Game Settings")
    
    # Base bet setting
    new_base = st.number_input("Base Bet Amount", min_value=1, max_value=50, value=st.session_state.base_bet, step=1)
    if new_base != st.session_state.base_bet:
        st.session_state.base_bet = new_base
        if st.session_state.consecutive_losses == 0:
            st.session_state.current_bet = new_base
    
    st.write("---")
    
    # Martingale progression preview
    st.write("**Martingale Progression Preview:**")
    preview_bet = st.session_state.base_bet
    for i in range(8):
        required_balance = sum([st.session_state.base_bet * (2**j) for j in range(i+1)])
        if required_balance <= st.session_state.balance:
            st.write(f"Loss {i+1}: ${preview_bet} (Total risk: ${required_balance})")
        else:
            st.write(f"Loss {i+1}: ${preview_bet} ❌ **Can't afford**")
            break
        preview_bet *= 2
    
    st.write("---")
    
    # Reset options
    if st.button("🔄 Reset Game"):
        st.session_state.balance = 500
        st.session_state.current_bet = st.session_state.base_bet
        st.session_state.consecutive_losses = 0
        st.session_state.history = []
        st.session_state.total_wagered = 0
        st.session_state.peak_balance = 500
        st.session_state.total_flips = 0
        st.success("Game Reset!")
    
    st.write("---")
    
    # Probability insights
    st.write("**📊 Probability Insights**")
    st.write("Perfect coin flip odds:")
    st.write("• Heads: 50%")
    st.write("• Tails: 50%")
    st.write("")
    st.write("**Losing streak probabilities:**")
    for i in range(1, 8):
        prob = (0.5 ** i) * 100
        st.write(f"• {i} losses: {prob:.1f}%")
    
    st.write("---")
    st.write("**⚠️ Educational Only**")
    st.write("This demonstrates why martingale fails even with perfect 50/50 odds!")