-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Client :  127.0.0.1
-- Généré le :  Mer 28 Juin 2017 à 10:31
-- Version du serveur :  5.7.14
-- Version de PHP :  5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `siteweb_python`
--

-- --------------------------------------------------------

--
-- Structure de la table `inscription`
--

CREATE TABLE `inscription` (
  `username` varchar(11) NOT NULL COMMENT 'Colonne du nom utilisateur',
  `mdp` varchar(20) NOT NULL COMMENT 'colonne du mot de passe',
  `mail` varchar(35) NOT NULL COMMENT 'colonne du mail'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Table sur l''Inscription';

--
-- Contenu de la table `inscription`
--

INSERT INTO `inscription` (`username`, `mdp`, `mail`) VALUES
('zaere', 'zrf', 'a@b.c'),
('Alex', 'alex', 'alex.lecoq@orange.com'),
('Lamyae', 'lamyae', 'lamyae.laaroussi@orange.com'),
('Maxime', 'mdp', 'maxime.rasse@orange.com'),
('Yusuf', 'yusuf', 'yusuf.makanjuola@orange.com');

-- --------------------------------------------------------

--
-- Structure de la table `pages_web`
--

CREATE TABLE `pages_web` (
  `article` varchar(65000) NOT NULL,
  `titre` varchar(100) NOT NULL,
  `chemin_image` varchar(100) NOT NULL,
  `taille_titre` varchar(1) NOT NULL,
  `numero_page` varchar(1) DEFAULT NULL,
  `user_mail` varchar(35) NOT NULL,
  `id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `pages_web`
--

INSERT INTO `pages_web` (`article`, `titre`, `chemin_image`, `taille_titre`, `numero_page`, `user_mail`, `id`) VALUES
('eses', 'Bonjour', 'image1', '4', '1', 'maxime.rasse@orange.com', 1),
('eses', 'Bonjour', 'image1', '4', '1', 'maxime.rasse@orange.com', 53),
('ok', 'Titre Page 1 test', 'image1.jpg', '3', '2', 'maxime.rasse@orange.com', 54),
('mON PREMIER ARTICLE', 'MonTitre', 'image.jpg', '1', '1', 'yusuf.makanjuola@orange.com', 55),
('iuiuiuiuiuiuu', 'Bonjour', 'image1', '2', '3', 'maxime.rasse@orange.com', 56);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `inscription`
--
ALTER TABLE `inscription`
  ADD PRIMARY KEY (`mail`),
  ADD UNIQUE KEY `mail` (`mail`);

--
-- Index pour la table `pages_web`
--
ALTER TABLE `pages_web`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `user_mail` (`user_mail`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `pages_web`
--
ALTER TABLE `pages_web`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `pages_web`
--
ALTER TABLE `pages_web`
  ADD CONSTRAINT `fk_inscription_pages_web` FOREIGN KEY (`user_mail`) REFERENCES `inscription` (`mail`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
