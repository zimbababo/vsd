from flask import Flask, Response, request
import requests

app = Flask(__name__)

# Put your secret key mechanism here if you have one enabled
SECRET_KEY = "your_secret_key_here"  # Match whatever key you use

def fetch_fresh_stream_url():
    return "http://23.153.217.158:8080/JOSEWEBTV25*201/39*22hdkult202/55342"

@app.route('/wapa')
def proxy():
    # Optional security key check
    key = request.args.get('key')
    if SECRET_KEY and key != SECRET_KEY:
        return "Unauthorized", 403

    stream_url = fetch_fresh_stream_url()
    
    try:
        # Stream the video data chunk by chunk through Render
        req = requests.get(stream_url, stream=True, timeout=10)
        
        return Response(
            req.iter_content(chunk_size=1024),
            content_type=req.headers.get('content-type', 'video/mp2t'),
            status=req.status_code
        )
    except Exception as e:
        return f"Proxy Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
