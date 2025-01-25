from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        api = request.form.get("api")
        id_tunnel = request.form.get("id_tunnel")

        if api and id_tunnel:
            url = f"https://localtonet.com/api/GetTunnelDetail/{id_tunnel}"
            headers = {
                'Authorization': f'Bearer {api}',
                'accept': 'application/json'
            }

            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    result = data["result"]  # Ambil detail tunnel

                    # Konversi bytes ke MB dan batasi 2 angka desimal
                    result["bandwidthLimit"] = round(result["bandwidthLimit"] / (1024 * 1024), 2)
                    result["bandwidthUsage"] = round(result["bandwidthUsage"] / (1024 * 1024), 2)
                else:
                    error = f"Error {response.status_code}: {response.text}"
            except Exception as e:
                error = f"Exception: {str(e)}"
        else:
            error = "API Token dan ID Tunnel harus diisi!"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)