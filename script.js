function salvarNota() {
    var nota = document.getElementById("noteText").value;
    localStorage.setItem("nota", nota);
    alert("Nota salva com sucesso!");
}

window.onload = function() {
    var notaSalva = localStorage.getItem("nota");
    if (notaSalva !== null) {
        document.getElementById("noteText").value = notaSalva;
    }
}
