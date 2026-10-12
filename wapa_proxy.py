from flask import Flask, Response
import requests

app = Flask(__name__)

UPSTREAM_STREAM_URL = "http://23.153.217.158:8080/JOSEWEBTV25*201/39*22hdkult202/55342"

# Endpoint 1: Serves the M3U Playlist file that TiviMate expects
@app.route('/playlist.m3u')
def playlist():
    m3u_content = """#EXTM3U
#EXTINF:-1 tvg-id="WapaTV" tvg-name="Wapa TV" group-title="Local",Wapa TV
https://vsd-v45s.onrender.com/wapa
"""
    return Response(m3u_content, mimetype='application/x-mpegurl')

# Endpoint 2: The actual video stream proxy
@app.route('/wapa')
def proxy():
    try:
        req = requests.get(UPSTREAM_STREAM_URL, stream=True, timeout=15)
        return Response(
            req.iter_content(chunk_size=1024),
            content_type=req.headers.get('content-type', 'video/mp2t'),
            status=req.status_code
        )
    except Exception as e:
        return f"Proxy Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
