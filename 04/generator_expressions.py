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

# definicija generatora
generator = (s["prezime"][::-1] for s in studenti_list if "a" in s["ime"])

# korištenje generatora u petlji
for s in generator:
    print(s)

# pretvordba generatora u listu
rezultat = list(s["prezime"] for s in studenti_list if "o" in s["ime"])
print(rezultat)

# sintaksa 

iterabilno = studenti_list  # može i string, set, tuple, dict ...

def nesto(x):
    return x["prezime"]

def uvjet(x):
    return "o" in x["ime"]

print(list( nesto(x) for x in iterabilno if uvjet(x) ))