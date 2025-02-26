import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Конфигурация страницы
st.set_page_config(
    page_title="RockCOIN - Cryptocurrency for Rock Music",
    page_icon="🎸",
    layout="wide"
)

# Загрузка CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Генерация тестовых данных
def generate_mock_data():
    dates = pd.date_range(start='2023-01-01', end=datetime.now(), freq='D')
    beats_sold = np.cumsum(np.random.randint(5, 50, size=len(dates)))
    coin_price = 10 + (beats_sold / 1000) + np.random.normal(0, 1, size=len(dates))
    return pd.DataFrame({
        'Date': dates,
        'Beats_Sold': beats_sold,
        'Coin_Price': coin_price
    })

# Создание тестовых данных
df = generate_mock_data()

# Шапка сайта с логотипом и статистикой
st.image("assets/logo.svg", width=200)
st.title("RockCOIN (ROCK)")
st.markdown("### 🎸 Революция в Мире Рок-Музыки и Криптовалют")

# Текущая статистика рынка
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Текущая цена", value="$ROCK 12.50", delta="+15.2%")
with col2:
    st.metric(label="Объем торгов 24ч", value="$25M", delta="+5.8%")
with col3:
    st.metric(label="Рыночная капитализация", value="$125M", delta="+12.3%")

# Ключевые показатели
st.subheader("💎 Ключевые показатели")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("**Общее предложение**\n\n100M ROCK")
with col2:
    st.info("**Активных пользователей**\n\n10K+")
with col3:
    st.info("**Проданных битов**\n\n50K+")

# О проекте
st.subheader("💫 О проекте RockCOIN")
st.write("""
RockCOIN (ROCK) — революционная криптовалюта, созданная для поддержки и развития рок-музыки. 
Наша миссия — создать децентрализованную экосистему, где музыканты и фанаты могут взаимодействовать напрямую.
""")

# Миссия проекта
st.subheader("🎯 Наша миссия")
mission_col1, mission_col2 = st.columns(2)
with mission_col1:
    st.write("""
    - Создание справедливой системы монетизации для музыкантов
    - Прямое взаимодействие артистов с фанатами
    - Развитие инновационной музыкальной экосистемы
    """)
with mission_col2:
    st.write("""
    - Поддержка начинающих рок-музыкантов
    - Создание глобального сообщества рок-культуры
    - Внедрение блокчейн-технологий в музыкальную индустрию
    """)

# Технические характеристики
with st.expander("💡 Технические характеристики"):
    st.write("""
    - **Тип токена:** ERC-20
    - **Блокчейн:** Ethereum
    - **Общее предложение:** 100,000,000 ROCK
    - **Циркулирующее предложение:** 45,000,000 ROCK
    - **Механизм консенсуса:** Proof of Stake (PoS)
    - **Смарт-контракт:** Проверен и аудирован Certik
    - **Минимальная сумма стейкинга:** 1000 ROCK
    - **Годовая доходность стейкинга:** до 12% APY
    """)

# Графики в две колонки
st.subheader("📊 Аналитика")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.write("### Продажи битов")
    fig_beats = go.Figure()
    fig_beats.add_trace(go.Scatter(
        x=df['Date'],
        y=df['Beats_Sold'],
        mode='lines',
        name='Beats Sold',
        line=dict(color='#ff69b4', width=2)
    ))
    fig_beats.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#4a4a4a'),
        yaxis=dict(gridcolor='#4a4a4a'),
        margin=dict(t=0, b=0)
    )
    st.plotly_chart(fig_beats, use_container_width=True)

with chart_col2:
    st.write("### Цена RockCOIN")
    # Подготовка данных для свечного графика
    df['Open'] = df['Coin_Price'].shift(1)
    df['High'] = df['Coin_Price'] * (1 + np.random.uniform(0, 0.03, len(df)))
    df['Low'] = df['Coin_Price'] * (1 - np.random.uniform(0, 0.03, len(df)))
    df['Close'] = df['Coin_Price']
    
    fig_price = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        increasing_line_color='#26df8b',  # Зеленый цвет для роста
        decreasing_line_color='#df264d'   # Красный цвет для падения
    )])
    fig_price.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='#4a4a4a'),
        yaxis=dict(gridcolor='#4a4a4a'),
        margin=dict(t=0, b=0)
    )
    st.plotly_chart(fig_price, use_container_width=True)

# Токеномика
st.subheader("📊 Токеномика")
tokenomics_col1, tokenomics_col2 = st.columns(2)

with tokenomics_col1:
    st.write("""
    - **Команда и советники:** 15% (15M ROCK)
    - **Маркетинг и партнерства:** 20% (20M ROCK)
    - **Экосистемный фонд:** 25% (25M ROCK)
    """)

with tokenomics_col2:
    st.write("""
    - **Публичная продажа:** 30% (30M ROCK)
    - **Ликвидность:** 10% (10M ROCK)
    """)

# Безопасность
with st.expander("🔒 Безопасность и аудит"):
    st.write("""
    - Смарт-контракты прошли полный аудит Certik
    - Мультисиг кошелек для управления токенами команды
    - Постепенное разблокирование токенов (vesting)
    - Регулярные проверки безопасности
    - Страхование средств пользователей
    - Защита от атак типа front-running
    """)

# Как это работает
st.subheader("⚡ Как это работает")
st.write("""
1. **Покупка RockCOIN:**
   - Приобретайте ROCK токены через поддерживаемые биржи
   - Минимальная сумма покупки: 100 ROCK
   - Поддержка основных криптовалют для обмена

2. **Доступ к контенту:**
   - Используйте ROCK для покупки битов
   - Получайте эксклюзивный контент
   - Участвуйте в премьерах новых треков

3. **Поддержка артистов:**
   - Прямые донаты любимым музыкантам
   - Участие в финансировании новых проектов
   - Получение процента от будущих продаж

4. **Получение наград:**
   - Стейкинг токенов
   - Участие в управлении платформой
   - Эксклюзивные NFT и мерч
""")

# Присоединяйтесь к сообществу
st.subheader("🤘 Присоединяйтесь к сообществу")
st.write("Станьте частью растущего сообщества RockCOIN!")
st.link_button("Присоединиться к Telegram", "https://t.me/rockcoin123")

# Подвал
st.markdown("---")
st.caption("© 2023 RockCOIN. All rights reserved. 🎸")
