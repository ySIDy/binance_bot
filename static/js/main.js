

document.addEventListener("DOMContentLoaded", function () {
    // Функция для обновления данных
    function fetchDataAndRender() {
        // Загрузка данных из файла data.json
        fetch("data_json")
            .then(response => response.json())
            .then(data => {
                
                const orderBookContainer = document.getElementById("orderBook");
                orderBookContainer.innerHTML = `
                    <p><strong>Last Update ID:</strong> ${data.lastUpdateId}</p>
                    <h2 class="table_title">Bids</h2>
                    <ul class="table_row">
                        ${data.bids.map(bid => `<li class="table_ellement">Price: ${bid[0]}, Quantity: ${bid[1]}</li>`).join('')}
                    </ul>
                    <h2 class="table_title">Asks</h2>
                    <ul class="table_row">
                        ${data.asks.map(ask => `<li class="table_ellement">Price: ${ask[0]}, Quantity: ${ask[1]}</li>`).join('')}
                    </ul>
                `;
                
            })
            .catch(error => console.error("Error fetching data:", error));
    }

    // Запускаем функцию сразу и устанавливаем таймер на обновление каждые 5 секунд (5000 миллисекунд)
    fetchDataAndRender();
    // setInterval(fetchDataAndRender, 50);
});