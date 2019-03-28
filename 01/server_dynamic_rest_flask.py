from flask import Flask, jsonify, request, Response
from flask import jsonify


app = Flask(__name__)  # __name__ sadrži naziv trenutnog fajla
studenti = [
    {"id": 1, "ime": "Hrvoje", "prezime": "Horvat"},
    {"id": 2, "ime": "Mirko", "prezime": "Mirkić"}
]


@app.route('/studenti')  # dekorator koji navodi Flasku koji URL obrađuje metoda
def dohvati_studente():
    return jsonify({"answer": studenti})


@app.route('/studenti', methods=['POST'])
def spremi_studenta():
    s = request.get_json()
    # ovdje bi trebalo provjeriti jel sve OK
    print("Dobio sam studenta: ", s)
    studenti.append(s)
    r = Response(status=201)
    r.set_data("Created.")
    return r


@app.route('/studenti/<id_studenta>')
def dohvati_studenta(id_studenta):
    answer = None
    for s in studenti:
        # može li bolje?
        if "id" in s and s["id"] == int(id_studenta):
            answer = s
            break

    return jsonify({"answer": answer})


# if __name__ == '__main__':
#     app.run()

# pokretanje: FLASK_DEBUG=1 FLASK_APP=server_dynamic_rest_flask.py flask run
