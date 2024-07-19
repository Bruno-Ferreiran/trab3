O print abaixo contem o Docker-compose.yml
![1](https://github.com/user-attachments/assets/63970c89-13bc-4083-84e8-2a91105d830c)
o print abaixo contem o Dockerfile
![2](https://github.com/user-attachments/assets/1c74e716-41d8-42d7-9abf-29b369869755)



Descrição:
Esta imagem Docker contém um aplicativo Node.js configurado para usar o Prisma ORM com um banco de dados MySQL. O aplicativo fornece uma API RESTful que permite realizar operações CRUD em um banco de dados MySQL.

Componentes:

Node.js: Versão 16, que fornece o ambiente de execução JavaScript necessário para o aplicativo.
Prisma: ORM (Object-Relational Mapping) utilizado para a conexão e manipulação do banco de dados MySQL.
MySQL: Servidor de banco de dados relacional configurado e gerenciado através do Docker Compose.
Configuração:

Variáveis de Ambiente:

DATABASE_URL: URL de conexão com o banco de dados MySQL, configurada no arquivo .env e utilizada pelo Prisma para se conectar ao banco de dados.
Portas Expostas:

3000: Porta na qual o aplicativo Node.js está em execução e disponível para acesso externo.
3306: Porta do MySQL, exposta para permitir a conexão com o banco de dados.
