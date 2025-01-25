document.getElementById("bandwidth-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const apiKey = document.getElementById("api-key").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Loading...";

    try {
        const response = await fetch("https://api.localtonet.com/api/v1/tunnels", {
            method: "GET",
            headers: {
                Authorization: `Bearer ${apiKey}`,
            },
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        const bandwidthLimitMB = (data.bandwidthLimit / 1024 / 1024).toFixed(2);
        const bandwidthUsageMB = (data.bandwidthUsage / 1024 / 1024).toFixed(2);

        resultDiv.innerHTML = `
            <h2>Result:</h2>
            <p><strong>Bandwidth Limit:</strong> ${bandwidthLimitMB} MB</p>
            <p><strong>Bandwidth Usage:</strong> ${bandwidthUsageMB} MB</p>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
});
