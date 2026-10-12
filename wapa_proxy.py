from flask import Flask, Response
import requests

app = Flask(__name__)

# The upstream provider URL containing their required token/path
UPSTREAM_STREAM_URL = "http://23.153.217.158:8080/JOSEWEBTV25*201/39*22hdkult202/55342"

@app.route('/wapa')
def proxy():
    try:
        # Stream the video data chunk by chunk through Render, forwarding the provider's token
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
