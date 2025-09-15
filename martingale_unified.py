import streamlit as st
import random
import time
import pandas as pd
import plotly.graph_objects as go
import os

# Page configuration
st.set_page_config(
    page_title="Martingale Strategy Hub", 
    page_icon="🎰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session states for all games
def initialize_session_states():
    # Common states
    if 'current_game' not in st.session_state:
        st.session_state.current_game = "Dashboard"
    
    # Coin flip states
    if 'coin_balance' not in st.session_state:
        st.session_state.coin_balance = 500
    if 'coin_base_bet' not in st.session_state:
        st.session_state.coin_base_bet = 5
    if 'coin_current_bet' not in st.session_state:
        st.session_state.coin_current_bet = 5
    if 'coin_consecutive_losses' not in st.session_state:
        st.session_state.coin_consecutive_losses = 0
    if 'coin_history' not in st.session_state:
        st.session_state.coin_history = []
    if 'coin_total_wagered' not in st.session_state:
        st.session_state.coin_total_wagered = 0
    if 'coin_peak_balance' not in st.session_state:
        st.session_state.coin_peak_balance = 500
    if 'coin_total_flips' not in st.session_state:
        st.session_state.coin_total_flips = 0
    
    # Roulette states
    if 'roulette_balance' not in st.session_state:
        st.session_state.roulette_balance = 1000
    if 'roulette_base_bet' not in st.session_state:
        st.session_state.roulette_base_bet = 10
    if 'roulette_current_bet' not in st.session_state:
        st.session_state.roulette_current_bet = 10
    if 'roulette_consecutive_losses' not in st.session_state:
        st.session_state.roulette_consecutive_losses = 0
    if 'roulette_history' not in st.session_state:
        st.session_state.roulette_history = []
    if 'roulette_total_wagered' not in st.session_state:
        st.session_state.roulette_total_wagered = 0
    if 'roulette_peak_balance' not in st.session_state:
        st.session_state.roulette_peak_balance = 1000
    
    # Fibonacci states
    if 'fib_balance' not in st.session_state:
        st.session_state.fib_balance = 20
    if 'fib_seq' not in st.session_state:
        st.session_state.fib_seq = [1, 1]
    if 'fib_pos' not in st.session_state:
        st.session_state.fib_pos = 0
    if 'fib_history' not in st.session_state:
        st.session_state.fib_history = []

initialize_session_states()

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
    
    st.session_state.current_game = games[selected_game]
    
    st.write("---")
    
    # Quick game info based on selection
    if st.session_state.current_game == "Coin Flip":
        st.write("🪙 **Coin Flip Martingale**")
        st.write(f"💰 Balance: ${st.session_state.coin_balance}")
        st.write(f"🎯 Bet: ${st.session_state.coin_current_bet}")
        st.write(f"📉 Streak: {st.session_state.coin_consecutive_losses}")
        
        if st.button("🔄 Reset Coin Game"):
            st.session_state.coin_balance = 500
            st.session_state.coin_current_bet = st.session_state.coin_base_bet
            st.session_state.coin_consecutive_losses = 0
            st.session_state.coin_history = []
            st.session_state.coin_total_wagered = 0
            st.session_state.coin_peak_balance = 500
            st.session_state.coin_total_flips = 0
            st.success("Coin game reset!")
    
    elif st.session_state.current_game == "Roulette":
        st.write("🎲 **Roulette Martingale**")
        st.write(f"💰 Balance: ${st.session_state.roulette_balance}")
        st.write(f"🎯 Bet: ${st.session_state.roulette_current_bet}")
        st.write(f"📉 Streak: {st.session_state.roulette_consecutive_losses}")
        
        if st.button("🔄 Reset Roulette Game"):
            st.session_state.roulette_balance = 1000
            st.session_state.roulette_current_bet = st.session_state.roulette_base_bet
            st.session_state.roulette_consecutive_losses = 0
            st.session_state.roulette_history = []
            st.session_state.roulette_total_wagered = 0
            st.session_state.roulette_peak_balance = 1000
            st.success("Roulette game reset!")
    
    elif st.session_state.current_game == "Fibonacci":
        st.write("📈 **Fibonacci Strategy**")
        st.write(f"💰 Balance: ${st.session_state.fib_balance}")
        current_fib_bet = st.session_state.fib_seq[st.session_state.fib_pos]
        st.write(f"🎯 Bet: ${current_fib_bet}")
        st.write(f"📍 Position: {st.session_state.fib_pos}")
        
        if st.button("🔄 Reset Fibonacci Game"):
            st.session_state.fib_balance = 20
            st.session_state.fib_seq = [1, 1]
            st.session_state.fib_pos = 0
            st.session_state.fib_history = []
            st.success("Fibonacci game reset!")
    
    st.write("---")
    st.write("**⚠️ Educacional Solamente**")
    st.write("Estos juegos demuestran por qué las estrategias progresivas fallan.")

# Main content area
if st.session_state.current_game == "Dashboard":
    st.title("🎰 Centro Educativo Martingale")
    
    st.write("""
    Bienvenido al **Centro Educativo de Estrategia Martingale**! Esta colección demuestra 
    el famoso sistema de apuestas martingale en diferentes juegos de casino.
    
    ⚠️ **Importante**: Todas las simulaciones son únicamente educativas. La estrategia martingale, 
    aunque matemáticamente sólida en teoría, falla en la práctica debido a límites de bankroll, 
    límites de mesa, y la realidad de las rachas perdedoras.
    """)
    
    # Game overview cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🪙 Coin Flip Martingale
        **Perfecto para principiantes**
        
        - Probabilidades perfectas 50/50
        - Demostración pura de martingale
        - Sin complicaciones de ventaja de casa
        - Cálculos de probabilidad de rachas
        - Análisis de riesgo/recompensa
        """)
        if st.button("🪙 Jugar Coin Flip", key="goto_coin"):
            st.session_state.current_game = "Coin Flip"
            st.rerun()
    
    with col2:
        st.markdown("""
        ### 🎲 Roulette Martingale
        **Experiencia realista de casino**
        
        - Simulación de ruleta europea
        - Apuestas Rojo/Negro/Verde
        - Límites de mesa ($10-$500)
        - Ventaja de la casa real
        - Seguimiento detallado de progresión
        """)
        if st.button("🎲 Jugar Roulette", key="goto_roulette"):
            st.session_state.current_game = "Roulette"
            st.rerun()
    
    with col3:
        st.markdown("""
        ### 📈 Fibonacci Strategy
        **Sistema alternativo**
        
        - Secuencia de Fibonacci
        - Avanzar en pérdida, retroceder en ganancia
        - Crecimiento más lento de apuestas
        - Perfil de riesgo menos agresivo
        - Comparación con martingale
        """)
        if st.button("📈 Jugar Fibonacci", key="goto_fib"):
            st.session_state.current_game = "Fibonacci"
            st.rerun()
    
    # Educational content
    st.write("---")
    st.subheader("📚 Resumen de Estrategia Martingale")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### ✅ Cómo "Funciona" Martingale
        1. **Empezar con apuesta base** (ej. $10)
        2. **Doblar después de cada pérdida** ($10 → $20 → $40...)
        3. **Volver a apuesta base después de ganar**
        4. **Cada ciclo garantiza ganancia de apuesta base**
        """)
    
    with col2:
        st.markdown("""
        #### ❌ Por Qué Falla Martingale
        1. **Crecimiento exponencial**: Las apuestas se doblan cada pérdida
        2. **Límites de mesa**: Los casinos limitan apuestas máximas
        3. **Límites de bankroll**: Los jugadores se quedan sin dinero
        4. **Ventaja de casa**: Incluso apuestas "50/50" favorecen al casino
        """)

elif st.session_state.current_game == "Coin Flip":
    st.title("🪙 Coin Flip Martingale")
    
    # Educational expander
    with st.expander("📚 Estrategia Martingale Pura Explicada"):
        st.write("""
        **Coin Flip Martingale** es la forma más simple de la estrategia martingale.
        
        **Cómo funciona:**
        - Elige Cara o Cruz
        - Empieza con apuesta base (ej. $5)
        - **Cuando pierdes**: Dobla tu apuesta
        - **Cuando ganas**: Vuelve a apuesta base
        - **Meta**: Cada ciclo ganador recupera todas las pérdidas + ganancia de apuesta base
        """)
    
    # Current status
    st.subheader("📊 Estado Actual")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Balance", f"${st.session_state.coin_balance}")
    with col2:
        st.metric("🎯 Apuesta Actual", f"${st.session_state.coin_current_bet}")
    with col3:
        st.metric("📉 Racha Perdedora", st.session_state.coin_consecutive_losses)
    with col4:
        st.metric("🪙 Total Lanzamientos", st.session_state.coin_total_flips)
    
    # Martingale progression
    st.write("**Progresión Martingale:**")
    progression = []
    bet = st.session_state.coin_base_bet
    for i in range(8):
        if i == st.session_state.coin_consecutive_losses:
            progression.append(f"**→ ${bet}**")
        else:
            progression.append(f"${bet}")
        bet *= 2
        if bet > st.session_state.coin_balance * 2:
            progression.append("🚫 LÍMITE BANKROLL")
            break
    st.write(" → ".join(progression))
    
    # Risk analysis
    if st.session_state.coin_consecutive_losses > 0:
        total_at_risk = sum([st.session_state.coin_base_bet * (2**i) for i in range(st.session_state.coin_consecutive_losses + 1)])
        potential_profit = st.session_state.coin_base_bet
        risk_ratio = total_at_risk / potential_profit
        
        if st.session_state.coin_consecutive_losses >= 4:
            st.error(f"""
            🚨 **ADVERTENCIA DE RIESGO EXTREMO**
            - Total invertido en secuencia: ${total_at_risk - st.session_state.coin_current_bet}
            - Apuesta actual requerida: ${st.session_state.coin_current_bet}
            - Total en riesgo: ${total_at_risk}
            - Ganancia potencial: ${potential_profit}
            - Ratio Riesgo/Recompensa: **{risk_ratio:.1f}:1**
            """)
        elif st.session_state.coin_consecutive_losses >= 2:
            st.warning(f"""
            ⚠️ **Análisis de Riesgo**
            - Inversión de secuencia: ${total_at_risk - st.session_state.coin_current_bet}
            - Próxima apuesta: ${st.session_state.coin_current_bet}
            - Riesgo/Recompensa: {risk_ratio:.1f}:1
            """)
    
    # Coin selection and flip
    st.write("### 🪙 Elige Tu Lado")
    choice = st.radio("Llámalo:", ["Cara", "Cruz"], horizontal=True)
    
    # Check if can afford current bet
    can_afford = st.session_state.coin_current_bet <= st.session_state.coin_balance
    
    if not can_afford:
        st.error(f"""
        💸 **FONDOS INSUFICIENTES!**
        Necesitas: ${st.session_state.coin_current_bet}
        Tienes: ${st.session_state.coin_balance}
        """)
    
    # Flip button
    if st.button("🪙 ¡Lanzar la Moneda!", disabled=not can_afford):
        # Animation
        with st.spinner("Lanzando moneda..."):
            time.sleep(1.5)
        
        # Perfect 50/50 coin flip
        result = random.choice(["Cara", "Cruz"])
        
        # Display result
        coin_emoji = "👑" if result == "Cara" else "⚡"
        st.write(f"## {coin_emoji} {result}!")
        
        win = (choice == result)
        bet_amount = st.session_state.coin_current_bet
        
        # Update counters
        st.session_state.coin_total_wagered += bet_amount
        st.session_state.coin_total_flips += 1
        
        if win:
            # Won the bet
            st.success(f"🎉 **¡GANASTE!** Elegiste {choice} y salió {result}")
            st.session_state.coin_balance += bet_amount
            
            # Martingale win explanation
            if st.session_state.coin_consecutive_losses > 0:
                total_recovered = sum([st.session_state.coin_base_bet * (2**i) for i in range(st.session_state.coin_consecutive_losses)])
                st.balloons()
                st.success(f"""
                🎊 **¡ÉXITO MARTINGALE!**
                - Racha perdedora: {st.session_state.coin_consecutive_losses} lanzamientos
                - Total recuperado: ${total_recovered}
                - Ganancia: ${st.session_state.coin_base_bet}
                """)
            
            # Reset to base bet
            st.session_state.coin_current_bet = st.session_state.coin_base_bet
            st.session_state.coin_consecutive_losses = 0
            
        else:
            # Lost the bet
            st.error(f"💸 **¡PERDISTE!** Elegiste {choice} pero salió {result}")
            st.session_state.coin_balance -= bet_amount
            st.session_state.coin_consecutive_losses += 1
            
            # Calculate next bet
            next_bet = bet_amount * 2
            
            # Check if we can continue
            if next_bet > st.session_state.coin_balance:
                st.error(f"""
                🚫 **FALLA MARTINGALE - BANKROLL AGOTADO!**
                - Próxima apuesta requerida: ${next_bet}
                - Tu balance: ${st.session_state.coin_balance}
                - ¡No puedes seguir doblando!
                """)
                st.session_state.coin_current_bet = min(st.session_state.coin_base_bet, st.session_state.coin_balance)
                st.session_state.coin_consecutive_losses = 0
            else:
                st.session_state.coin_current_bet = next_bet
                st.warning(f"""
                📈 **Progresión Martingale**
                - Apuesta anterior: ${bet_amount} → Próxima apuesta: ${next_bet}
                - Racha perdedora: {st.session_state.coin_consecutive_losses}
                """)
        
        # Update peak balance
        if st.session_state.coin_balance > st.session_state.coin_peak_balance:
            st.session_state.coin_peak_balance = st.session_state.coin_balance
        
        # Save to history
        st.session_state.coin_history.append({
            "Lanzamiento": st.session_state.coin_total_flips,
            "Elegiste": choice,
            "Resultado": result,
            "Ganó": "✅" if win else "❌",
            "Apuesta": bet_amount,
            "Balance": st.session_state.coin_balance,
            "Racha": st.session_state.coin_consecutive_losses if not win else 0
        })
    
    # Statistics display
    if st.session_state.coin_history:
        st.subheader("📊 Estadísticas")
        
        df = pd.DataFrame(st.session_state.coin_history)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Lanzamientos", len(df))
        with col2:
            wins = df[df['Ganó'] == '✅'].shape[0]
            win_rate = (wins / len(df) * 100) if len(df) > 0 else 0
            st.metric("Tasa de Éxito", f"{win_rate:.1f}%")
        with col3:
            st.metric("Total Apostado", f"${st.session_state.coin_total_wagered}")
        with col4:
            profit_loss = st.session_state.coin_balance - 500
            st.metric("Ganancia/Pérdida", f"${profit_loss:+}")
        
        # Recent history
        st.subheader("📋 Historial Reciente")
        recent_df = df.tail(10)
        st.dataframe(recent_df, use_container_width=True)

elif st.session_state.current_game == "Roulette":
    st.title("🎲 Roulette Martingale")
    
    # Educational expander
    with st.expander("📚 ¿Cómo funciona la Estrategia Martingale?"):
        st.write("""
        **La estrategia de apuestas Martingale** es el sistema de apuestas de casino más famoso, 
        basado en doblar tu apuesta después de cada pérdida.
        
        **Principio Central:**
        - Empezar con apuesta base (ej. $10)
        - **Cuando pierdes**: Doblar tu apuesta (2x)
        - **Cuando ganas**: Volver a apuesta base
        - **Meta**: Una ganancia recupera todas las pérdidas + ganancia igual a apuesta base
        """)
    
    # Current status
    MAX_BET = 500
    MIN_BET = 10
    
    st.subheader("📊 Estado Actual")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Balance", f"${st.session_state.roulette_balance}")
    with col2:
        st.metric("🎯 Apuesta Actual", f"${st.session_state.roulette_current_bet}")
    with col3:
        st.metric("📉 Racha Perdedora", st.session_state.roulette_consecutive_losses)
    with col4:
        doubles_left = 0
        temp_bet = st.session_state.roulette_current_bet
        while temp_bet * 2 <= MAX_BET and temp_bet * 2 <= st.session_state.roulette_balance:
            doubles_left += 1
            temp_bet *= 2
        st.metric("🔄 Doblamientos Restantes", doubles_left)
    
    # Martingale progression
    st.write("**Progresión Martingale:**")
    progression = []
    bet = st.session_state.roulette_base_bet
    for i in range(8):
        if i == st.session_state.roulette_consecutive_losses:
            progression.append(f"**→ ${bet}**")
        else:
            progression.append(f"${bet}")
        bet *= 2
        if bet > MAX_BET:
            progression.append("🚫 LÍMITE DE MESA")
            break
    st.write(" → ".join(progression))
    
    # Risk warning
    if st.session_state.roulette_consecutive_losses > 0:
        total_at_risk = sum([st.session_state.roulette_base_bet * (2**i) for i in range(st.session_state.roulette_consecutive_losses + 1)])
        potential_profit = st.session_state.roulette_base_bet
        risk_ratio = total_at_risk / potential_profit
        
        if st.session_state.roulette_consecutive_losses >= 3:
            st.error(f"""
            ⚠️ **ADVERTENCIA DE ALTO RIESGO**
            - Total invertido en esta secuencia: ${total_at_risk - st.session_state.roulette_current_bet}
            - Apuesta actual requerida: ${st.session_state.roulette_current_bet}
            - Total en riesgo: ${total_at_risk}
            - Ganancia potencial si ganas: ${potential_profit}
            - Ratio Riesgo/Recompensa: {risk_ratio:.1f}:1
            """)
    
    # Color selection
    option = st.selectbox("¿En qué color quieres apostar?", ["Rojo", "Negro", "Verde"])
    
    # Check constraints
    can_afford = st.session_state.roulette_current_bet <= st.session_state.roulette_balance
    hit_table_limit = st.session_state.roulette_current_bet > MAX_BET
    
    if hit_table_limit:
        st.error(f"🚫 ¡LÍMITE DE MESA ALCANZADO! La apuesta máxima es ${MAX_BET}")
    elif not can_afford:
        st.error(f"💸 ¡FONDOS INSUFICIENTES! Necesitas ${st.session_state.roulette_current_bet} pero solo tienes ${st.session_state.roulette_balance}")
    
    # Spin button
    if st.button("🎲 Girar la ruleta", disabled=(not can_afford or hit_table_limit)):
        with st.spinner("Girando la rueda..."):
            time.sleep(2)
        
        # Realistic roulette probabilities (European roulette)
        result = random.choices(
            population=["Rojo", "Negro", "Verde"],
            weights=[18, 18, 2],  # Single zero European roulette
            k=1
        )[0]
        
        win = (option == result)
        bet_amount = st.session_state.roulette_current_bet
        
        st.session_state.roulette_total_wagered += bet_amount
        
        if win:
            # Calculate winnings
            if result == "Verde":
                payout = bet_amount * 35  # Green pays 35:1
            else:
                payout = bet_amount  # Red/Black pays 1:1
            
            st.success(f"✅ **¡GANASTE!** La bola cayó en {result}")
            st.session_state.roulette_balance += payout
            
            # Martingale explanation for win
            if st.session_state.roulette_consecutive_losses > 0:
                total_recovered = sum([st.session_state.roulette_base_bet * (2**i) for i in range(st.session_state.roulette_consecutive_losses)])
                st.balloons()
                st.success(f"""
                🎊 **¡ÉXITO MARTINGALE!**
                - Recuperaste ${total_recovered} en pérdidas
                - Más ${st.session_state.roulette_base_bet} de ganancia
                - ¡Racha de {st.session_state.roulette_consecutive_losses} pérdidas terminó!
                """)
            
            # Reset to base bet
            st.session_state.roulette_current_bet = st.session_state.roulette_base_bet
            st.session_state.roulette_consecutive_losses = 0
            
        else:
            # Lost the bet
            st.error(f"❌ **¡PERDISTE!** La bola cayó en {result}")
            st.session_state.roulette_balance -= bet_amount
            st.session_state.roulette_consecutive_losses += 1
            
            # Calculate next Martingale bet
            next_bet = bet_amount * 2
            
            # Check if we can continue Martingale
            if next_bet > MAX_BET:
                st.error(f"""
                🚫 **FALLA MARTINGALE - ¡LÍMITE DE MESA!**
                - Próxima apuesta requerida: ${next_bet}
                - Máximo de mesa: ${MAX_BET}
                - ¡No puedes seguir doblando!
                """)
                st.session_state.roulette_current_bet = st.session_state.roulette_base_bet
                st.session_state.roulette_consecutive_losses = 0
            elif next_bet > st.session_state.roulette_balance:
                st.error(f"""
                💸 **FALLA MARTINGALE - ¡FONDOS INSUFICIENTES!**
                - Próxima apuesta requerida: ${next_bet}
                - Tu balance: ${st.session_state.roulette_balance}
                - ¡No puedes seguir doblando!
                """)
                st.session_state.roulette_current_bet = st.session_state.roulette_base_bet
                st.session_state.roulette_consecutive_losses = 0
            else:
                st.session_state.roulette_current_bet = next_bet
                st.warning(f"""
                📈 **Acción Martingale**: Doblando apuesta
                - Apuesta anterior: ${bet_amount}
                - Próxima apuesta: ${next_bet}
                - Pérdidas consecutivas: {st.session_state.roulette_consecutive_losses}
                """)
        
        # Update peak balance
        if st.session_state.roulette_balance > st.session_state.roulette_peak_balance:
            st.session_state.roulette_peak_balance = st.session_state.roulette_balance
        
        # Save to history
        st.session_state.roulette_history.append({
            "Ronda": len(st.session_state.roulette_history) + 1,
            "Apuesta Color": option,
            "Resultado": result,
            "Ganó": "✅" if win else "❌",
            "Cantidad Apuesta": bet_amount,
            "Balance": st.session_state.roulette_balance,
            "Racha": st.session_state.roulette_consecutive_losses if not win else 0
        })
    
    # Statistics display
    if st.session_state.roulette_history:
        st.subheader("📈 Estadísticas")
        
        df = pd.DataFrame(st.session_state.roulette_history)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_bets = len(df)
            st.metric("Total Giros", total_bets)
        with col2:
            wins = df[df['Ganó'] == '✅'].shape[0]
            win_rate = (wins / total_bets * 100) if total_bets > 0 else 0
            st.metric("Tasa de Éxito", f"{win_rate:.1f}%")
        with col3:
            st.metric("Total Apostado", f"${st.session_state.roulette_total_wagered}")
        with col4:
            profit_loss = st.session_state.roulette_balance - 1000
            st.metric("Ganancia/Pérdida", f"${profit_loss:+}")
        
        # Recent history
        st.subheader("📜 Historial de Apuestas")
        recent_df = df.tail(10)
        st.dataframe(recent_df, use_container_width=True)

elif st.session_state.current_game == "Fibonacci":
    st.title("📈 Fibonacci Strategy")
    
    # Educational expander
    with st.expander("📚 ¿Cómo funciona la Estrategia Fibonacci?"):
        st.write("""
        **La estrategia de apuestas Fibonacci** usa la famosa secuencia de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21...) 
        donde cada número es la suma de los dos precedentes.
        
        **Cómo funciona:**
        - Empezar apostando el primer número de la secuencia ($1)
        - Cuando **pierdes**: Avanzar un paso en la secuencia (aumentar apuesta)
        - Cuando **ganas**: Retroceder dos pasos en la secuencia (disminuir apuesta)
        - El objetivo es recuperar pérdidas gradualmente minimizando el riesgo
        """)
    
    # Current status
    st.subheader("📊 Estado Actual")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("💰 Balance", f"${st.session_state.fib_balance}")
    with col2:
        st.metric("📈 Posición Fibonacci", st.session_state.fib_pos)
    with col3:
        current_bet = st.session_state.fib_seq[st.session_state.fib_pos]
        st.metric("🎯 Apuesta Actual", f"${current_bet}")
    
    # Show Fibonacci sequence
    st.write("**Secuencia Fibonacci Actual:**")
    sequence_display = ""
    for i, num in enumerate(st.session_state.fib_seq[:min(len(st.session_state.fib_seq), 10)]):
        if i == st.session_state.fib_pos:
            sequence_display += f"**[${num}]** "
        else:
            sequence_display += f"${num} "
    if len(st.session_state.fib_seq) > 10:
        sequence_display += "..."
    st.write(sequence_display)
    
    # Explain position
    if st.session_state.fib_pos == 0:
        st.info("🎯 Estás al comienzo de la secuencia. Esta es la apuesta mínima.")
    elif st.session_state.fib_pos >= len(st.session_state.fib_seq) - 1:
        st.warning(f"⚠️ Estás en la posición {st.session_state.fib_pos}. La secuencia se expandirá si pierdes de nuevo.")
    else:
        st.info(f"📍 Estás en la posición {st.session_state.fib_pos} en la secuencia Fibonacci.")
    
    # Color selection
    option = st.selectbox("¿En qué color quieres apostar?", ["Rojo", "Negro", "Verde"])
    
    # Spin button
    if st.button("🎲 Girar la ruleta"):
        if current_bet > st.session_state.fib_balance:
            st.error("🚫 No tienes suficiente balance para esta apuesta.")
        else:
            with st.spinner("Girando la rueda..."):
                time.sleep(2)
            
            # Realistic probabilities
            result = random.choices(
                population=["Rojo", "Negro", "Verde"],
                weights=[47, 47, 6],
                k=1
            )[0]
            
            win = (option == result)
            
            if win:
                if result == "Verde":
                    payout = current_bet * 14  # Green pays more
                else:
                    payout = current_bet
                
                st.success(f"✅ ¡Ganaste! La ruleta cayó en {result}")
                st.session_state.fib_balance += payout
                
                # Fibonacci strategy explanation for win
                old_pos = st.session_state.fib_pos
                st.session_state.fib_pos = max(0, st.session_state.fib_pos - 2)
                new_pos = st.session_state.fib_pos
                
                with st.container():
                    st.write("**🎲 Acción Estrategia Fibonacci:**")
                    st.write(f"✅ Como ganaste, retrocedes 2 posiciones: Posición {old_pos} → Posición {new_pos}")
                    next_bet = st.session_state.fib_seq[new_pos]
                    st.write(f"💡 Tu próxima apuesta será: ${next_bet}")
                    if new_pos == 0:
                        st.success("🎉 ¡Estás de vuelta en la apuesta mínima!")
            else:
                st.error(f"❌ Perdiste. La ruleta cayó en {result}")
                st.session_state.fib_balance -= current_bet
                
                # Fibonacci strategy explanation for loss
                old_pos = st.session_state.fib_pos
                st.session_state.fib_pos += 1
                new_pos = st.session_state.fib_pos
                
                # Expand Fibonacci sequence if necessary
                if st.session_state.fib_pos >= len(st.session_state.fib_seq):
                    new_value = st.session_state.fib_seq[-1] + st.session_state.fib_seq[-2]
                    st.session_state.fib_seq.append(new_value)
                    st.warning(f"📈 ¡Secuencia Fibonacci expandida! Nuevo valor agregado: ${new_value}")
                    st.write(f"Cálculo: ${st.session_state.fib_seq[-3]} + ${st.session_state.fib_seq[-2]} = ${new_value}")
                
                with st.container():
                    st.write("**🎲 Acción Estrategia Fibonacci:**")
                    st.write(f"❌ Como perdiste, avanzas 1 posición: Posición {old_pos} → Posición {new_pos}")
                    next_bet = st.session_state.fib_seq[new_pos]
                    st.write(f"💡 Tu próxima apuesta será: ${next_bet}")
                    st.write("📊 Esto sigue la progresión Fibonacci para ayudar a recuperar pérdidas gradualmente.")
            
            # Save to history
            st.session_state.fib_history.append({
                "Color Apuesta": option,
                "Resultado": result,
                "Ganó": "✅" if win else "❌",
                "Apuesta": current_bet,
                "Balance": st.session_state.fib_balance
            })
    
    # Show history
    if st.session_state.fib_history:
        st.subheader("📜 Historial de Apuestas")
        df = pd.DataFrame(st.session_state.fib_history)
        
        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_bets = len(df)
            st.metric("Total Apuestas", total_bets)
        with col2:
            wins = df[df['Ganó'] == '✅'].shape[0]
            win_rate = (wins / total_bets * 100) if total_bets > 0 else 0
            st.metric("Tasa de Éxito", f"{win_rate:.1f}%")
        with col3:
            total_wagered = df['Apuesta'].sum()
            st.metric("Total Apostado", f"${total_wagered}")
        with col4:
            profit_loss = st.session_state.fib_balance - 20
            st.metric("Ganancia/Pérdida", f"${profit_loss:+}")
        
        # Recent history table
        recent_df = df.tail(10)
        st.dataframe(recent_df, use_container_width=True)

# Footer
st.write("---")
st.write("**⚠️ Únicamente Educacional** - Estos juegos demuestran por qué las estrategias progresivas fallan en situaciones reales de casino.")