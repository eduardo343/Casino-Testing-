import streamlit as st
import random
import os
import time
import pandas as pd

st.set_page_config(page_title="Roulette Bot", page_icon="🎰")
st.title("🎰 Roulette Bot - Fibonacci Strategy")

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
st.write(f"💰 Current balance: ${st.session_state.balance}")
st.write(f"📈 Fibonacci position: {st.session_state.fibo_pos}")
current_bet = st.session_state.fibo_seq[st.session_state.fibo_pos]
st.write(f"🎯 Current bet: ${current_bet}")

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
            st.session_state.fibo_pos = max(0, st.session_state.fibo_pos - 2)
        else:
            st.error(f"❌ You lost. The roulette landed on {result}")
            st.session_state.balance -= current_bet
            st.session_state.fibo_pos += 1

            # Expandir secuencia Fibonacci si es necesario
            if st.session_state.fibo_pos >= len(st.session_state.fibo_seq):
                new_value = st.session_state.fibo_seq[-1] + st.session_state.fibo_seq[-2]
                st.session_state.fibo_seq.append(new_value)

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
