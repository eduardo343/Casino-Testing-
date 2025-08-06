import streamlit as st
import random

st.title("🎰 Bot de Ruleta - Estrategia Fibonacci")

if 'saldo' not in st.session_state:
    st.session_state.saldo = 100
if 'fibo_seq' not in st.session_state:
    st.session_state.fibo_seq = [1, 1]
if 'fibo_pos' not in st.session_state:
    st.session_state.fibo_pos = 0
if 'historial' not in st.session_state:
    st.session_state.historial = []

st.write(f"💰 Saldo actual: ${st.session_state.saldo}")
st.write(f"📈 Posición en Fibonacci: {st.session_state.fibo_pos}")
apuesta_actual = st.session_state.fibo_seq[st.session_state.fibo_pos]
st.write(f"🎯 Apuesta actual: ${apuesta_actual}")

opcion = st.selectbox("¿A qué color deseas apostar?", ["Rojo", "Negro"])

if st.button("Girar ruleta"):
    if apuesta_actual > st.session_state.saldo:
        st.error("No tienes suficiente saldo para esta apuesta.")
    else:
        resultado = random.choice(["Rojo", "Negro"])
        gano = (opcion == resultado)

        if gano:
            st.success(f"✅ ¡Ganaste! La ruleta cayó en {resultado}")
            st.session_state.saldo += apuesta_actual
            st.session_state.fibo_pos = max(0, st.session_state.fibo_pos - 2)
        else:
            st.error(f"❌ Perdiste. La ruleta cayó en {resultado}")
            st.session_state.saldo -= apuesta_actual
            st.session_state.fibo_pos += 1

            if st.session_state.fibo_pos >= len(st.session_state.fibo_seq):
                nuevo = st.session_state.fibo_seq[-1] + st.session_state.fibo_seq[-2]
                st.session_state.fibo_seq.append(nuevo)

        st.session_state.historial.append({
            "Color apostado": opcion,
            "Resultado": resultado,
            "Ganó": "✅" if gano else "❌",
            "Apostado": apuesta_actual,
            "Saldo": st.session_state.saldo
        })

if st.session_state.historial:
    st.subheader("📜 Historial de apuestas")
    st.table(st.session_state.historial)

if st.button("🔄 Reiniciar todo"):
    st.session_state.saldo = 100
    st.session_state.fibo_seq = [1, 1]
    st.session_state.fibo_pos = 0
    st.session_state.historial = []
    st.success("Todo ha sido reiniciado.")
