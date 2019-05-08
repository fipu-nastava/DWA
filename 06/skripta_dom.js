function izvrsi() {
    alert("Stranica učitana!");

    // dohvat DOM elementa po ID-u
    var el = document.getElementById("dom_id")
    el.innerHTML = "<span>Evo dinamičkog teksta pomoću JS DOM API-a</span><br/><a href='http://www.facebook.com'>Dosadno mi je.</a>";

    console.log("Moj roditelj je", el.parentNode);
    console.log("Moja djeca su", el.childNodes);

    // Primjer čitanja atributa pojedinog elementa
    console.log("Link na koji vodim", el.childNodes[2].attributes["href"].value);

    // Element može biti i izvan stabla (ne prikazuje se)
    var div = document.createElement("div");
    div.innerText = "Ja sam virtualni element";
    el.appendChild(div);

    console.log("Nakon dodavanja", el.childNodes);

    // Dodavanje event listenera
    div.addEventListener("click", function() {alert("Whoa!")})
    div.addEventListener("click", function() {alert("Zar opet?!")})
}

window.onload = izvrsi;
