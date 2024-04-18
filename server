from http.server import *
import streamlit as st


class BlissfulMugs(BaseHTTPRequestHandler):
    st.title("BlissfulMugs")

    def do_GET(self):
        self.send_response(200)

        self.send_header('content type', 'text/html')
        self.end_headers()

port = HTTPServer(('', 888), BlissfulMugs)


port.serve_forever()
