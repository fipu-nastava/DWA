var app = new Vue({
    el: '#app',
    data: {
        studenti: [{
            ime: "Nikola",
            prezime: "Tanković",
            jmbag: "02134234"
        }],
        novi: {
            ime: "",
            prezime: "",
            jmbag: ""
        }
    },
    computed: {
    },
    methods: {
        dodaj: function() {
            var novi_student = {
                ime: this.novi.ime,
                prezime: this.novi.prezime,
                jmbag: this.novi.jmbag
            }
            this.studenti.push(novi_student);
        },
        brisi: function(idx) {
            this.studenti.splice(idx, 1);
        }
    }
})
