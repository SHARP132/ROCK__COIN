
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RockCOIN - Revolutionary Music Cryptocurrency</title>
    <link href="styles.css" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header>
            <img src="assets/logo.svg" alt="RockCOIN Logo" width="300">
            <h1>RockCOIN (ROCK)</h1>
            <p class="header-subtitle">🎸 Революция в Мире Рок-Музыки и Криптовалют</p>
        </header>

        <!-- Market Stats -->
        <div class="market-stats">
            <div class="market-stat">
                <div class="market-stat-value">$ROCK 12.50</div>
                <div class="market-stat-label">Текущая цена</div>
            </div>
            <div class="market-stat">
                <div class="market-stat-value">+15.2%</div>
                <div class="market-stat-label">24ч изменение</div>
            </div>
            <div class="market-stat">
                <div class="market-stat-value">$25M</div>
                <div class="market-stat-label">Объем торгов 24ч</div>
            </div>
        </div>

        <!-- Key Metrics -->
        <h2 class="section-header">💎 Ключевые показатели</h2>
        <div class="metrics-grid">
            <div class="stat-item">
                <div class="stat-value">100M</div>
                <div class="stat-label">Общее предложение ROCK</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">10K+</div>
                <div class="stat-label">Активных пользователей</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">50K+</div>
                <div class="stat-label">Проданных битов</div>
            </div>
        </div>

        <!-- About Project -->
        <h2 class="section-header">💫 О проекте RockCOIN</h2>
        <div class="info-card">
            <p>RockCOIN (ROCK) — революционная криптовалюта, созданная для поддержки и развития рок-музыки. 
            Наша миссия — создать децентрализованную экосистему, где музыканты и фанаты могут взаимодействовать напрямую.</p>
            
            <h3>🎯 Наша миссия:</h3>
            <ul>
                <li>Создание справедливой системы монетизации для музыкантов</li>
                <li>Прямое взаимодействие артистов с фанатами</li>
                <li>Развитие инновационной музыкальной экосистемы</li>
                <li>Поддержка начинающих рок-музыкантов</li>
            </ul>
        </div>

        <!-- Analytics -->
        <h2 class="section-header">📊 Аналитика</h2>
        <div class="charts-grid">
            <div class="chart-container">
                <div id="beatsChart"></div>
            </div>
            <div class="chart-container">
                <div id="priceChart"></div>
            </div>
        </div>

        <!-- Community -->
        <h2 class="section-header">🤘 Присоединяйтесь к сообществу</h2>
        <div class="info-card">
            <p>Станьте частью растущего сообщества RockCOIN!</p>
            <a href="https://t.me/rockcoin123" target="_blank" class="custom-link">
                Присоединиться к Telegram
            </a>
        </div>

        <!-- Footer -->
        <footer>
            <p>© 2023 RockCOIN. All rights reserved. 🎸</p>
        </footer>
    </div>

    <script>
        // Generate mock data for charts
        function generateMockData() {
            const dates = [];
            const beatsSold = [];
            const coinPrice = [];
            let beats = 0;

            for(let i = 0; i < 365; i++) {
                const date = new Date();
                date.setDate(date.getDate() - (365 - i));
                dates.push(date);
                
                beats += Math.floor(Math.random() * 45) + 5;
                beatsSold.push(beats);
                
                const price = 10 + (beats / 1000) + (Math.random() * 2 - 1);
                coinPrice.push(price);
            }

            return { dates, beatsSold, coinPrice };
        }

        // Create charts
        const data = generateMockData();

        // Beats chart
        const beatsTrace = {
            x: data.dates,
            y: data.beatsSold,
            type: 'scatter',
            mode: 'lines',
            name: 'Продажи битов',
            line: {
                color: '#ff69b4',
                width: 2
            }
        };

        const beatsLayout = {
            title: 'Продажи битов',
            plot_bgcolor: 'rgba(0,0,0,0)',
            paper_bgcolor: 'rgba(0,0,0,0)',
            font: {
                color: 'white'
            },
            xaxis: {
                gridcolor: '#4a4a4a'
            },
            yaxis: {
                gridcolor: '#4a4a4a'
            }
        };

        Plotly.newPlot('beatsChart', [beatsTrace], beatsLayout);

        // Price chart
        const priceTrace = {
            x: data.dates,
            y: data.coinPrice,
            type: 'scatter',
            mode: 'lines',
            name: 'Цена ROCK',
            line: {
                color: '#ff69b4',
                width: 2
            }
        };

        const priceLayout = {
            title: 'Цена RockCOIN',
            plot_bgcolor: 'rgba(0,0,0,0)',
            paper_bgcolor: 'rgba(0,0,0,0)',
            font: {
                color: 'white'
            },
            xaxis: {
                gridcolor: '#4a4a4a'
            },
            yaxis: {
                gridcolor: '#4a4a4a'
            }
        };

        Plotly.newPlot('priceChart', [priceTrace], priceLayout);
    </script>
</body>
</html>
