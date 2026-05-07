# Cloudflare Tunnel for Chat

Use this when school Wi-Fi blocks direct device-to-device access.

## What you need

- A free Cloudflare account
- `cloudflared` installed on the machine running the chat server
- The chat server running locally on port `5000`

## Start the chat server

From `CPDJ101_WebServer/chat`:

```powershell
$env:PYTHONPATH='src'
& 'C:\Users\amitr\Downloads\CPDJ101github-proj\.venv\Scripts\python.exe' -c "from chat import run; run(port=5000)"
```

## Create a tunnel

If `cloudflared` is already installed and authenticated, run:

```powershell
cloudflared tunnel --url http://127.0.0.1:5000
```

Cloudflare will print a public `https://...trycloudflare.com` link. Share that link with other people.

## Notes

- Keep the chat server running while the tunnel is active.
- If the server is restarted, restart the tunnel too.
- `127.0.0.1:5000` is only local. The tunnel is what makes it reachable from outside your network.
