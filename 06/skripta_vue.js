var app = new Vue({
    el: "#app",
    data: {
        message: "Hello vue! (a dynamic thing)",
        title_varijabla: "Wee hoo!",
        prikazi: true,
        zadaci: [
            { tekst: "Naučiti Javascript!" },
            { tekst: "Naučiti Vue.js!" },
            { tekst: "Napraviti projekt" }
        ],
        poruka: "Stisni to dugme"
    },
    methods: {
        hendlerFunkcija: function() {
            this.poruka = this.poruka + ".";
        }
    }
})
