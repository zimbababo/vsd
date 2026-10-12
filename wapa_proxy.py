from flask import Flask, Response, stream_with_context
import requests

app = Flask(__name__)

UPSTREAM_STREAM_URL = "http://23.153.217.158:8080/JOSEWEBTV25*201/39*22hdkult202/55342"

@app.route('/playlist.m3u')
def playlist():
    m3u_content = """#EXTM3U
#EXTINF:-1 tvg-id="WapaTV" tvg-name="Wapa TV" group-title="Local",Wapa TV
https://vsd-v45s.onrender.com/wapa
"""
    return Response(m3u_content, mimetype='application/x-mpegurl')

@app.route('/wapa')
def proxy():
    headers = {
        'User-Agent': 'TiviMate/5.1.6 (Android 11)',
        'Accept': '*/*'
    }

    def generate():
        try:
            with requests.get(UPSTREAM_STREAM_URL, headers=headers, stream=True, timeout=15) as req:
                req.raise_for_status()
                for chunk in req.iter_content(chunk_size=32768):
                    if chunk:
                        yield chunk
        except Exception as e:
            print(f"Streaming error: {e}")

    return Response(stream_with_context(generate()), content_type='video/mp2t')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
