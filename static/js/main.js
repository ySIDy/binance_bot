// main.js

console.log("11");
        // Загрузка данных из файла data.json



fetch("data.json")
    .then(response => response.json())
    .then(data => {
                // Отображение данных на HTML странице
        const orderBookContainer = document.getElementById("orderBook");
        orderBookContainer.innerHTML = `
            <p><strong>Last Update ID:</strong> ${data.lastUpdateId}</p>
            <h2>Bids</h2>
            <ul>
                ${data.bids.map(bid => `<li>Price: ${bid[0]}, Quantity: ${bid[1]}</li>`).join('')}
            </ul>
            <h2>Asks</h2>
            <ul>
                ${data.asks.map(ask => `<li>Price: ${ask[0]}, Quantity: ${ask[1]}</li>`).join('')}
            </ul>
        `;
    })
.catch(error => console.error("Error fetching data:", error));
