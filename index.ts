import express from 'express';
const app = express();
const port = 3000;

import livrosRoutes from './routes/livros'; // Renomeie para "livrosRoutes"

app.use(express.json());
app.use("/livros", livrosRoutes); // Altere para "/livros"

app.get('/', (req, res) => {
  res.send('API de Livros: Clube de Leitura'); // Altere para "Livros" e "Clube de Leitura"
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta: ${port}`);
});
