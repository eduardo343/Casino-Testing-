import streamlit as st
import random
import os
import time
import pandas as pd

st.set_page_config(page_title="Roulette Bot", page_icon="🎰")
st.title("🎰 Roulette Bot - Fibonacci Strategy")

# Explanation of Fibonacci Strategy
with st.expander("📚 How does the Fibonacci Strategy work?"):
    st.write("""
    **The Fibonacci betting strategy** uses the famous Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21...) 
    where each number is the sum of the two preceding ones.
    
    **How it works:**
    - Start betting with the first number in the sequence ($1)
    - When you **lose**: Move one step forward in the sequence (increase bet)
    - When you **win**: Move two steps back in the sequence (decrease bet)
    - The goal is to recover losses gradually while minimizing risk
    
    **Example:**
    - Bet $1 and lose → Next bet: $1 (move to position 1)
    - Bet $1 and lose → Next bet: $2 (move to position 2)
    - Bet $2 and win → Next bet: $1 (move back to position 0)
    """)

# Inicializar el estado
if 'balance' not in st.session_state:
    st.session_state.balance = 20
if 'fibo_seq' not in st.session_state:
    st.session_state.fibo_seq = [1, 1]
if 'fibo_pos' not in st.session_state:
    st.session_state.fibo_pos = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# Mostrar información actual
st.subheader("📊 Current Status")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Balance", f"${st.session_state.balance}")
with col2:
    st.metric("📈 Fibonacci Position", st.session_state.fibo_pos)
with col3:
    current_bet = st.session_state.fibo_seq[st.session_state.fibo_pos]
    st.metric("🎯 Current Bet", f"${current_bet}")

# Show Fibonacci sequence visualization
st.write("**Current Fibonacci Sequence:**")
sequence_display = ""
for i, num in enumerate(st.session_state.fibo_seq[:min(len(st.session_state.fibo_seq), 10)]):
    if i == st.session_state.fibo_pos:
        sequence_display += f"**[${num}]** "
    else:
        sequence_display += f"${num} "
if len(st.session_state.fibo_seq) > 10:
    sequence_display += "..."
st.write(sequence_display)

# Explain current position
if st.session_state.fibo_pos == 0:
    st.info("🎯 You're at the beginning of the sequence. This is the minimum bet.")
elif st.session_state.fibo_pos >= len(st.session_state.fibo_seq) - 1:
    st.warning(f"⚠️ You're at position {st.session_state.fibo_pos}. The sequence will expand if you lose again.")
else:
    st.info(f"📍 You're at position {st.session_state.fibo_pos} in the Fibonacci sequence.")

# Elegir color
option = st.selectbox("Which color do you want to bet on?", ["Red", "Black", "Green"], key="color_select")

# Botón de girar ruleta
if st.button("🎲 Spin the roulette", key="spin_btn"):
    if current_bet > st.session_state.balance:
        st.error("🚫 You don't have enough balance for this bet.")
    else:
        if os.path.exists("roulette.gif"):
            st.image("roulette.gif", use_container_width=True)
            time.sleep(3)
        else:
            st.warning("⚠️ Gif not found, spinning without animation.")

        # Probabilidades realistas: rojo 47%, negro 47%, verde 6%
        result = random.choices(
            population=["Red", "Black", "Green"],
            weights=[47, 47, 6],
            k=1
        )[0]

        win = (option == result)

        if win:
            if result == "Green":
                payout = current_bet * 14  # paga más por verde
            else:
                payout = current_bet

            st.success(f"✅ You won! The roulette landed on {result}")
            st.session_state.balance += payout
            
            # Fibonacci strategy explanation for win
            old_pos = st.session_state.fibo_pos
            st.session_state.fibo_pos = max(0, st.session_state.fibo_pos - 2)
            new_pos = st.session_state.fibo_pos
            
            with st.container():
                st.write("**🎲 Fibonacci Strategy Action:**")
                st.write(f"✅ Since you won, moving back 2 positions: Position {old_pos} → Position {new_pos}")
                next_bet = st.session_state.fibo_seq[new_pos]
                st.write(f"💡 Your next bet will be: ${next_bet}")
                if new_pos == 0:
                    st.success("🎉 You're back at the minimum bet!")
        else:
            st.error(f"❌ You lost. The roulette landed on {result}")
            st.session_state.balance -= current_bet
            
            # Fibonacci strategy explanation for loss
            old_pos = st.session_state.fibo_pos
            st.session_state.fibo_pos += 1
            new_pos = st.session_state.fibo_pos

            # Expandir secuencia Fibonacci si es necesario
            if st.session_state.fibo_pos >= len(st.session_state.fibo_seq):
                new_value = st.session_state.fibo_seq[-1] + st.session_state.fibo_seq[-2]
                st.session_state.fibo_seq.append(new_value)
                st.warning(f"📈 Fibonacci sequence expanded! New value added: ${new_value}")
                st.write(f"Calculation: ${st.session_state.fibo_seq[-3]} + ${st.session_state.fibo_seq[-2]} = ${new_value}")
            
            with st.container():
                st.write("**🎲 Fibonacci Strategy Action:**")
                st.write(f"❌ Since you lost, moving forward 1 position: Position {old_pos} → Position {new_pos}")
                next_bet = st.session_state.fibo_seq[new_pos]
                st.write(f"💡 Your next bet will be: ${next_bet}")
                st.write(f"📊 This follows the Fibonacci progression to help recover losses gradually.")

        # Guardar historial
        st.session_state.history.append({
            "Bet Color": option,
            "Result": result,
            "Win": "✅" if win else "❌",
            "Bet": current_bet,
            "Balance": st.session_state.balance
        })

# Mostrar historial de apuestas
if st.session_state.history:
    st.subheader("📜 History of bets")
    df = pd.DataFrame(st.session_state.history)
    
    # Add statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        total_bets = len(df)
        st.metric("Total Bets", total_bets)
    with col2:
        wins = df[df['Win'] == '✅'].shape[0]
        win_rate = (wins / total_bets * 100) if total_bets > 0 else 0
        st.metric("Win Rate", f"{win_rate:.1f}%")
    with col3:
        total_wagered = df['Bet'].sum()
        st.metric("Total Wagered", f"${total_wagered}")
    with col4:
        profit_loss = st.session_state.balance - 20  # Initial balance was 20
        st.metric("Profit/Loss", f"${profit_loss:+.0f}")
    
    st.table(df)

    # Botón para descargar historial
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download history", csv, "roulette_history.csv", "text/csv")

# Botón para reiniciar
if st.button("🔄 Reboot all", key="reset_btn"):
    st.session_state.balance = 20
    st.session_state.fibo_seq = [1, 1]
    st.session_state.fibo_pos = 0
    st.session_state.history = []
    st.success("🔁 Game reset successfully.")
