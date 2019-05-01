from flask import Flask, Response, jsonify, request
from domain import Studenti, Ispiti, Kolegiji

app = Flask(__name__)

@app.route("/studenti", methods=["GET"])
def handle_studenti():
    studenti = Studenti.listaj()
    return jsonify({"data": studenti})

@app.route("/studenti", methods=["POST"])
def handle_studenti_dodaj():
    status, greske = Studenti.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/ispiti", methods=["GET"])
def handle_ispiti():
    ispiti = Ispiti.listaj()
    return jsonify({"data": ispiti})

@app.route("/ispiti", methods=["POST"])
def handle_ispiti_dodaj():
    status, greske = Ispiti.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/kolegiji", methods=["GET"])
def handle_kolegiji():
    kolegiji = Kolegiji.listaj()
    return jsonify({"data": kolegiji})

@app.route("/kolegiji", methods=["POST"])
def handle_kolegiji_dodaj():
    status, greske = Kolegiji.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r
