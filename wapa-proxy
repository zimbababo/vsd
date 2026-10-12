

app = Flask(__name__)

# Cache variables to hold the active stream URL and its fetch time
cached_stream_url = None
last_fetched_time = 0
TOKEN_VALIDITY_SECONDS = 3600  # Refresh every 1 hour (adjust as needed)

def fetch_fresh_stream_url():
    return "http://23.153.217.158:8080/JOSEWEBTV25*201/39*22hdkult202/55342"
 

def get_active_url():
    global cached_stream_url, last_fetched_time
    current_time = time.time()
    
    # If the token is older than our validity window, fetch a new one
    if not cached_stream_url or (current_time - last_fetched_time) > TOKEN_VALIDITY_SECONDS:
        print("[-] Token expired or missing. Fetching a fresh stream URL...")
        try:
            cached_stream_url = fetch_fresh_stream_url()
            last_fetched_time = current_time
            print("[+] Successfully acquired fresh stream URL.")
        except Exception as e:
            print(f"[!] Error fetching fresh token: {e}")

    return cached_stream_url

@app.route('/wapa')
def proxy_stream():
    stream_url = get_active_url()
    if not stream_url:
        return "Could not fetch active stream", 500
    
    # Redirect your IPTV player straight to the freshly authenticated stream URL
    return redirect(stream_url, code=302)

if __name__ == '__main__':
    # Runs locally on port 8080
    app.run(host='0.0.0.0', port=8080)
 
