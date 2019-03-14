from flask import Flask, request, Response
from flask import jsonify


app = Flask(__name__)
studenti = [{"id": "0", "ime":"hrvoje", "prezime":"horvat"}]


@app.route('/studenti', methods=['POST'])
def spremi_studenta():
    s = request.get_json()
    studenti.append(s)
    return Response(status=201)

@app.route('/studenti/<id>')
def dohvati_studenta(id):
    answer = None
    for s in studenti:
        if "id" in s and s["id"] == id:
            answer = s
            break

    return jsonify({"answer": answer })

@app.route('/studenti')
def dohvati_studente():
    return jsonify({"answer":studenti})


# if __name__ == '__main__':
#     app.run()

# pokretanje: FLASK_DEBUG=1 FLASK_APP=server_dynamic_rest_flask.py flask run