#Use uma imagem base oficial do Node.js
FROM node:16

#Defina o diretório de trabalho no contêiner
WORKDIR /usr/src/app

#Copie os arquivos package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

#Instale as dependências do aplicativo
RUN npm install

#Copie o restante do código do aplicativo para o diretório de trabalho
COPY . .

#Gere o Prisma Client
RUN npx prisma generate

#Exponha a porta que o aplicativo usará
EXPOSE 3000

#Comando para iniciar o aplicativo
CMD ["npm", "start"]