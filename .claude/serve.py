#!/usr/bin/env python3
"""Kleiner Vorschau-Server für die Timo-Blunck-Website.
Start:  python3 .claude/serve.py   →   http://127.0.0.1:4321
"""
import http.server
import os
import socketserver

PORT = 4321
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Vorschau läuft auf http://127.0.0.1:{PORT}  (Strg+C zum Beenden)")
    httpd.serve_forever()
