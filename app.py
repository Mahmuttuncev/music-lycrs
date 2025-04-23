from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_lyrics', methods=['POST'])
def get_lyrics():
    data = request.get_json()
    artist = data.get('artist')
    song = data.get('song')
    
    try:
        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')
        if response.status_code == 200:
            return jsonify({'lyrics': response.json()['lyrics']})
        else:
            return jsonify({'error': 'Şarkı sözleri bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)