const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.json());

// Endpoint para salvar a nota
app.post('/salvar-nota', (req, res) => {
    const nota = req.body.nota;
    fs.writeFile(path.join(__dirname, 'nota.txt'), nota, (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Erro ao salvar a nota.');
        } else {
            res.send('Nota salva com sucesso no servidor.');
        }
    });
});

// Endpoint para recuperar a nota
app.get('/recuperar-nota', (req, res) => {
    fs.readFile(path.join(__dirname, 'nota.txt'), 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('Erro ao recuperar a nota.');
        } else {
            res.send(data);
        }
    });
});

app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
