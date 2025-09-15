# Pages Directory

Esta carpeta contiene archivos para el **sistema multi-página avanzado** de Streamlit.

⚠️ **ADVERTENCIA**: Estos archivos tienen navegación experimental que puede fallar.

## Recomendación

**Usa la app unificada en su lugar:**

```bash
streamlit run martingale_unified.py
```

## Si quieres usar el sistema multi-página

```bash
# Ejecuta cualquier archivo de esta carpeta y navega desde ahí
streamlit run pages/main_dashboard.py
```

Los archivos en esta carpeta usan `st.switch_page()` para navegación automática entre páginas.

## Estructura

- `main_dashboard.py` - Dashboard con navegación
- `coin_flip_martingale.py` - Coin flip con navegación  
- `martingale_bot.py` - Roulette con navegación

**Nota**: fibonacci_bot.py está en el directorio raíz como archivo independiente.