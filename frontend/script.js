async function predict() {

    const news = document.getElementById("news").value.trim();
    const result = document.getElementById("result");

    if (news === "") {
        result.innerHTML = `
            <div class="card">
                <h2> Please enter a news article.</h2>
            </div>
        `;
        return;
    }

   
    result.innerHTML = `
        <div class="card">
            <h2>⏳ Classifying...</h2>
        </div>
    `;

    try {

        const response = await fetch("http://127.0.0.1:8000/classify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                news: news
            })
        });

        const data = await response.json();

        if (response.ok && data.success) {

            result.innerHTML = `
                <div class="card">
                    <h2>${data.icon} ${data.category}</h2>
                </div>
            `;

        } else {

            result.innerHTML = `
                <div class="card">
                    <h2> ${data.detail}</h2>
                </div>
            `;
        }

    } catch (error) {

        result.innerHTML = `
            <div class="card">
                <h2> Unable to connect to the server.</h2>
                <p>Please make sure the FastAPI server is running.</p>
            </div>
        `;
    }
}