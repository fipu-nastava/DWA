from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# emulacija baze (samo memorija)
studenti_list = [
    {
        "id": 1,
        "ime": "Hrvoje",
        "prezime": "Horvat"
    },
    {
        "id": 2,
        "ime": "Nikolina",
        "prezime": "Nikolić"
    }
]
# primjer append-a
studenti_list.append({"id":3, "ime": "Ivica", "prezime": "Ivić"})

# .. ali drzat cemo kao dict zbog vremenske složenosti pristupa
studenti_dict = { s["id"]: s for s in studenti_list }
zadnji_id = max(s["id"] for s in studenti_list)

@app.route("/")
def hendler_kako_god():
    r = Response(status=200)
    r.set_data("Hello world!")
    return r

@app.route("/studenti", methods=["PUT"])
def dodaj_novog_studenta():
    global zadnji_id  # jer želimo mijenjati vanjsku (globalnu) varijablu

    data = request.get_json()
    data["id"] = zadnji_id + 1
    zadnji_id = data["id"]

    # studenti_list.append(data)
    studenti_dict[data["id"]] = data

    response = Response(status=201)  # instancijacija odgovora
    response.headers["Location"] = f"/studenti/{zadnji_id}"
    return response

@app.route("/studenti")
def listaj_studente():
    return jsonify(list(studenti_dict.values()))

@app.route("/studenti/<id_studenta>")
def dohvati_studenta(id_studenta):

    ids = int(id_studenta)

    # for s in studenti_list:
    #     if s["id"] == ids:
    #         return jsonify(s)
    if ids in studenti_dict:
        return jsonify(studenti_dict[ids])
    else:
        return Response(status=404)

@app.route("/studenti/<id_studenta>", methods=["DELETE"])
def obrisi_studenta(id_studenta):

    ids = int(id_studenta)
    if ids in studenti_dict:
        del studenti_dict[ids]
        return Response(status=202)

    return Response(status=404)
