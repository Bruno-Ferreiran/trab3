import { PrismaClient } from "@prisma/client";
import { Router } from "express";

const prisma = new PrismaClient();
const router = Router();

router.get("/", async (req, res) => {
  const livros = await prisma.livro.findMany(); // Altere para "livro" em vez de "filme"
  res.status(200).json(livros);
});

router.post("/", async (req, res) => {
  const { titulo, autor, genero, preco } = req.body; // Adicione "autor"

  if (!titulo || !autor || !genero || !preco) {
    res.status(400).json({ "Erro": "Informe os dados" });
    return;
  }

  const livro = await prisma.livro.create({
    data: {
      titulo,
      autor,
      genero,
      preco,
    },
  });
  res.status(201).json(livro);
});

router.delete("/:id", async (req, res) => {
  const { id } = req.params;

  const livro = await prisma.livro.delete({
    where: {
      id: Number(id),
    },
  });
  res.status(200).json(livro);
});

router.put("/:id", async (req, res) => {
  const { id } = req.params;
  const { preco } = req.body;

  const livro = await prisma.livro.update({
    where: { id: Number(id) },
    data: { preco },
  });
  res.status(200).json(livro);
});

export default router;
