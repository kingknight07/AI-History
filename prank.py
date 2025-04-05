import http.server
import socketserver
import os

# HTML content for the prank page
prank_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Alert</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #000;
            color: #0f0;
            font-family: monospace;
            font-size: 20px;
            text-align: center;
        }
        #message {
            transition: opacity 1s;
        }
        .blink {
            animation: blink 1s infinite;
        }
        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
</head>
<body>
    <div id="message">Uploading data...</div>
    <script>
        setTimeout(() => {
            document.getElementById('message').innerHTML = 'DEVICE HACKED!<br>';
            document.getElementById('message').classList.add('blink');
        }, 3000);
        // Prevent reuse by "deactivating" after one view
        if (localStorage.getItem('prankViewed')) {
            document.body.innerHTML = 'Link expired.';
        } else {
            localStorage.setItem('prankViewed', 'true');
        }
    </script>
</body>
</html>
"""

# Step 1: Write the HTML to a file
with open("prank.html", "w") as f:
    f.write(prank_html)

# Step 2: Serve it locally for testing
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Test the prank at http://localhost:{PORT}/prank.html")
    print("Press Ctrl+C to stop the server after testing.")
    httpd.serve_forever()
