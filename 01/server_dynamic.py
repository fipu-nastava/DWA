from http.server import BaseHTTPRequestHandler, HTTPServer


def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


class MojHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        adresa = self.path  # /fibonaci/10, /favicon.ico

        if "/fibo" in adresa:
            n = int(adresa.split("/")[-1])
            odgovor = fib(n)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(odgovor).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("Nema nicega".encode("utf-8"))


port = 8081

server_class = HTTPServer
handler_class = MojHandler
server_address = ('localhost', port)

httpd = server_class(server_address, handler_class)

print('Starting httpd on port %d...' % port)
httpd.serve_forever()
