import streamlit as st
import random
import time
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Martingale Roulette Hub", 
    page_icon="🎰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize navigation state
if 'current_game' not in st.session_state:
    st.session_state.current_game = "Roulette"

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
        elif new_game == "Coin Flip":
            st.switch_page("coin_flip_martingale.py")
        elif new_game == "Fibonacci":
            st.switch_page("fibonacci_bot.py")
        # If Roulette is selected, stay on current page
    
    st.session_state.current_game = new_game
    
    st.write("---")
    
    # Quick game info for Roulette
    st.write("🎲 **Roulette Martingale**")
    roulette_balance = st.session_state.get('balance', 1000)
    roulette_current_bet = st.session_state.get('current_bet', 10)
    roulette_consecutive_losses = st.session_state.get('consecutive_losses', 0)
    
    st.write(f"💰 Balance: ${roulette_balance}")
    st.write(f"🎯 Bet: ${roulette_current_bet}")
    st.write(f"📉 Streak: {roulette_consecutive_losses}")
    
    if st.button("🔄 Reset Roulette Game"):
        st.session_state.balance = 1000
        st.session_state.current_bet = st.session_state.get('base_bet', 10)
        st.session_state.consecutive_losses = 0
        st.session_state.history = []
        st.session_state.total_wagered = 0
        st.session_state.peak_balance = 1000
        st.success("Roulette game reset!")
    
    st.write("---")
    
    # Navigation instructions
    st.info("💡 **Navegación Rápida**\n\nUsa el menú desplegable arriba para cambiar entre juegos sin perder tu progreso.")
    
    st.write("---")
    st.write("**⚠️ Educacional Solamente**")
    st.write("Estos juegos demuestran por qué las estrategias progresivas fallan.")

st.title("🎰 Roulette Martingale - Martingale Hub")

# Educational content
with st.expander("📚 How does the Martingale Strategy work?"):
    st.write("""
    **The Martingale betting strategy** is the most famous casino betting system, based on doubling your bet after every loss.
    
    **Core Principle:**
    - Start with a base bet (e.g., $10)
    - **When you lose**: Double your bet (2x)
    - **When you win**: Return to base bet
    - **Goal**: One win recovers all losses + profit equal to base bet
    
    **Example Sequence:**
    - Bet $10 → Lose (Total: -$10)
    - Bet $20 → Lose (Total: -$30)  
    - Bet $40 → Win (Total: -$30 + $40 = +$10 profit!)
    
    **⚠️ WARNING**: This strategy can lead to catastrophic losses due to exponential bet growth!
    """)

# Initialize session state
if 'balance' not in st.session_state:
    st.session_state.balance = 1000  # Start with more money for Martingale
if 'base_bet' not in st.session_state:
    st.session_state.base_bet = 10
if 'current_bet' not in st.session_state:
    st.session_state.current_bet = 10
if 'consecutive_losses' not in st.session_state:
    st.session_state.consecutive_losses = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'max_bet_reached' not in st.session_state:
    st.session_state.max_bet_reached = False
if 'total_wagered' not in st.session_state:
    st.session_state.total_wagered = 0
if 'peak_balance' not in st.session_state:
    st.session_state.peak_balance = 1000

# Table limits (realistic casino limits)
MIN_BET = 10
MAX_BET = 500  # Typical table maximum

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
    doubles_left = 0
    temp_bet = st.session_state.current_bet
    while temp_bet * 2 <= MAX_BET and temp_bet * 2 <= st.session_state.balance:
        doubles_left += 1
        temp_bet *= 2
    st.metric("🔄 Doubles Left", doubles_left)

# Martingale progression display
st.write("**Martingale Progression:**")
progression = []
bet = st.session_state.base_bet
total_risk = 0
for i in range(8):
    if i == st.session_state.consecutive_losses:
        progression.append(f"**→ ${bet}**")
    else:
        progression.append(f"${bet}")
    total_risk += bet
    bet *= 2
    if bet > MAX_BET:
        progression.append("🚫 TABLE LIMIT")
        break
st.write(" → ".join(progression))

# Risk warning
if st.session_state.consecutive_losses > 0:
    total_at_risk = sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses + 1)])
    potential_profit = st.session_state.base_bet
    risk_ratio = total_at_risk / potential_profit if potential_profit > 0 else 0
    
    if st.session_state.consecutive_losses >= 3:
        st.error(f"""
        ⚠️ **HIGH RISK WARNING**
        - Total invested in this sequence: ${total_at_risk - st.session_state.current_bet}
        - Current bet required: ${st.session_state.current_bet}
        - Total at risk: ${total_at_risk}
        - Potential profit if you win: ${potential_profit}
        - Risk/Reward Ratio: {risk_ratio:.1f}:1
        """)
    else:
        st.warning(f"""
        📊 **Current Sequence Status**
        - Total invested so far: ${total_at_risk - st.session_state.current_bet}
        - Next bet: ${st.session_state.current_bet}
        - Potential profit if you win: ${potential_profit}
        """)

# Bet color selection
option = st.selectbox("Which color do you want to bet on?", ["Red", "Black", "Green"], key="color_select")

# Check if can afford current bet
can_afford = st.session_state.current_bet <= st.session_state.balance
hit_table_limit = st.session_state.current_bet > MAX_BET

if hit_table_limit:
    st.error(f"🚫 TABLE LIMIT REACHED! Maximum bet is ${MAX_BET}. Martingale sequence broken!")
    if st.button("Reset to base bet"):
        st.session_state.current_bet = st.session_state.base_bet
        st.session_state.consecutive_losses = 0
        st.success("Reset to base bet")
elif not can_afford:
    st.error(f"💸 INSUFFICIENT FUNDS! You need ${st.session_state.current_bet} but only have ${st.session_state.balance}")
    if st.button("Reset to base bet"):
        st.session_state.current_bet = st.session_state.base_bet
        st.session_state.consecutive_losses = 0
        st.success("Reset to base bet")

# Spin button
if st.button("🎲 Spin the roulette", key="spin_btn", disabled=(not can_afford or hit_table_limit)):
    # Animation
    with st.spinner("Spinning the wheel..."):
        time.sleep(2)
    
    # Realistic roulette probabilities
    result = random.choices(
        population=["Red", "Black", "Green"],
        weights=[18, 18, 2],  # European roulette (single zero)
        k=1
    )[0]
    
    win = (option == result)
    bet_amount = st.session_state.current_bet
    
    # Update total wagered
    st.session_state.total_wagered += bet_amount
    
    if win:
        # Calculate winnings
        if result == "Green":
            payout = bet_amount * 35  # Green pays 35:1
        else:
            payout = bet_amount  # Red/Black pays 1:1
        
        st.success(f"✅ **YOU WON!** The ball landed on {result}")
        st.session_state.balance += payout
        
        # Martingale explanation for win
        if st.session_state.consecutive_losses > 0:
            total_recovered = sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses)])
            st.balloons()
            st.success(f"""
            🎊 **MARTINGALE SUCCESS!**
            - You recovered ${total_recovered} in losses
            - Plus ${st.session_state.base_bet} profit
            - Streak of {st.session_state.consecutive_losses} losses ended!
            """)
        
        # Reset to base bet after win
        st.session_state.current_bet = st.session_state.base_bet
        st.session_state.consecutive_losses = 0
        
        st.info(f"💡 **Martingale Action**: Returning to base bet of ${st.session_state.base_bet}")
        
    else:
        # Lost the bet
        st.error(f"❌ **YOU LOST!** The ball landed on {result}")
        st.session_state.balance -= bet_amount
        st.session_state.consecutive_losses += 1
        
        # Calculate next Martingale bet
        next_bet = bet_amount * 2
        
        # Check if we can continue Martingale
        if next_bet > MAX_BET:
            st.error(f"""
            🚫 **MARTINGALE FAILURE - TABLE LIMIT!**
            - Next required bet: ${next_bet}
            - Table maximum: ${MAX_BET}
            - Cannot continue doubling!
            - Total lost in this sequence: ${sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses)])}
            """)
            st.session_state.current_bet = st.session_state.base_bet
            st.session_state.consecutive_losses = 0
        elif next_bet > st.session_state.balance:
            st.error(f"""
            💸 **MARTINGALE FAILURE - INSUFFICIENT FUNDS!**
            - Next required bet: ${next_bet}
            - Your balance: ${st.session_state.balance}
            - Cannot continue doubling!
            - Total lost in this sequence: ${sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses)])}
            """)
            st.session_state.current_bet = st.session_state.base_bet
            st.session_state.consecutive_losses = 0
        else:
            st.session_state.current_bet = next_bet
            st.warning(f"""
            📈 **Martingale Action**: Doubling bet
            - Previous bet: ${bet_amount}
            - Next bet: ${next_bet}
            - Consecutive losses: {st.session_state.consecutive_losses}
            - Total at risk if next bet loses: ${sum([st.session_state.base_bet * (2**i) for i in range(st.session_state.consecutive_losses + 1)])}
            """)
    
    # Update peak balance
    if st.session_state.balance > st.session_state.peak_balance:
        st.session_state.peak_balance = st.session_state.balance
    
    # Save to history
    st.session_state.history.append({
        "Round": len(st.session_state.history) + 1,
        "Bet Color": option,
        "Result": result,
        "Win": "✅" if win else "❌",
        "Bet Amount": bet_amount,
        "Balance": st.session_state.balance,
        "Streak": st.session_state.consecutive_losses if not win else 0
    })

# Display statistics and history
if st.session_state.history:
    st.subheader("📈 Statistics")
    
    df = pd.DataFrame(st.session_state.history)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        total_bets = len(df)
        st.metric("Total Spins", total_bets)
    with col2:
        wins = df[df['Win'] == '✅'].shape[0]
        win_rate = (wins / total_bets * 100) if total_bets > 0 else 0
        st.metric("Win Rate", f"{win_rate:.1f}%")
    with col3:
        st.metric("Total Wagered", f"${st.session_state.total_wagered}")
    with col4:
        profit_loss = st.session_state.balance - 1000
        st.metric("Profit/Loss", f"${profit_loss:+.0f}")
    
    # Additional metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Peak Balance", f"${st.session_state.peak_balance}")
    with col2:
        max_streak = df['Streak'].max() if not df.empty else 0
        st.metric("Longest Losing Streak", max_streak)
    with col3:
        max_bet = df['Bet Amount'].max() if not df.empty else 0
        st.metric("Largest Bet", f"${max_bet}")
    with col4:
        drawdown = st.session_state.peak_balance - st.session_state.balance
        st.metric("Drawdown", f"${drawdown}")
    
    # Chart of balance over time
    st.subheader("📊 Balance Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Round'],
        y=df['Balance'],
        mode='lines+markers',
        name='Balance',
        line=dict(color='blue', width=2),
        marker=dict(size=8)
    ))
    fig.add_hline(y=1000, line_dash="dash", line_color="gray", annotation_text="Starting Balance")
    fig.update_layout(
        title="Balance Over Time",
        xaxis_title="Round",
        yaxis_title="Balance ($)",
        hovermode='x'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Bet size chart
    st.subheader("📊 Bet Size Progression")
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=df['Round'],
        y=df['Bet Amount'],
        marker_color=['red' if w == '❌' else 'green' for w in df['Win']],
        name='Bet Amount'
    ))
    fig2.add_hline(y=MAX_BET, line_dash="dash", line_color="red", annotation_text="Table Limit")
    fig2.update_layout(
        title="Bet Amounts (Red = Loss, Green = Win)",
        xaxis_title="Round",
        yaxis_title="Bet Amount ($)",
        hovermode='x'
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # History table
    st.subheader("📜 Betting History")
    st.dataframe(df, use_container_width=True)
    
    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download History", csv, "martingale_history.csv", "text/csv")

# Settings section
with st.sidebar:
    st.header("⚙️ Settings")
    new_base = st.number_input("Base Bet Amount", min_value=MIN_BET, max_value=100, value=st.session_state.base_bet, step=10)
    if new_base != st.session_state.base_bet:
        st.session_state.base_bet = new_base
        if st.session_state.consecutive_losses == 0:
            st.session_state.current_bet = new_base
    
    st.write(f"**Table Limits**")
    st.write(f"- Minimum: ${MIN_BET}")
    st.write(f"- Maximum: ${MAX_BET}")
    
    if st.button("🔄 Reset Everything"):
        st.session_state.balance = 1000
        st.session_state.current_bet = st.session_state.base_bet
        st.session_state.consecutive_losses = 0
        st.session_state.history = []
        st.session_state.total_wagered = 0
        st.session_state.peak_balance = 1000
        st.success("Game reset!")
    
    st.write("---")
    st.write("**⚠️ Disclaimer**")
    st.write("This is for educational purposes only. The Martingale strategy does not overcome the house edge and can lead to significant losses.")