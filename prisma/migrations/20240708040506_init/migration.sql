-- CreateTable
CREATE TABLE `livros` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `titulo` VARCHAR(60) NOT NULL,
    `autor` VARCHAR(60) NOT NULL,
    `genero` VARCHAR(40) NOT NULL,
    `preco` DOUBLE NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
