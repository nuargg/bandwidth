from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Mengatasi masalah CORS jika diakses dari domain eksternal

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil input dari form
        api_key = request.form.get('api_key')

        # Contoh data hasil pengecekan bandwidth
        result = {
            "title": "Bandwidth Usage Report",
            "bandwidthLimit": 1000,  # Contoh limit dalam MB
            "bandwidthUsage": 750   # Contoh penggunaan dalam MB
        }
        return render_template('index.html', result=result)
    
    # GET request untuk tampilan awal
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
