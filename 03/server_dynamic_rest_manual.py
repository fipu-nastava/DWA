from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

# za pakiranje i raspakiranje JSON-a
import json

# FAKE BAZA
studenti = [{"id": 1, "name": "nikola"}]

class MojHandler(BaseHTTPRequestHandler):
    def do_POST(self):

        # Koliko imam za citati?
        content_len = int(self.headers['content-length'])

        # Procitaj
        post_body = self.rfile.read(content_len)

        # Pretvori string u dict
        s = json.loads(post_body)
        studenti += [s]

    def do_GET(self):
        adresa = self.path

        if adresa == "/studenti":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            string_odgovor = json.dumps(studenti)
            self.wfile.write(string_odgovor.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Nema nicega".encode("utf-8"))
        
port=8081

server_class = HTTPServer
handler_class = MojHandler
server_address = ('localhost', port)

httpd = server_class(server_address, handler_class)

print('Starting httpd on port %d...' % port)
httpd.serve_forever()  # 
