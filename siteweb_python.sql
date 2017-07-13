-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Client :  127.0.0.1
-- Généré le :  Ven 07 Juillet 2017 à 13:07
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
('Max', 'DODO', 'jean.laposte@orange.com'),
('Lamyae', 'lamyae', 'lamyae.laaroussi@orange.com'),
('Maxime', '1234', 'maxime.rasse@orange.com'),
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
('ok', 'Bonjour', '19478388_10209578052830497_940280311_o.jpg', '1', '1', 'maxime.rasse@orange.com', 1),
('rzevzervzerzrzrzrvz', 'Bonjour', 'A_crane_lifts_a_metal_shipping_container_RGB_White.png', '3', '2', 'maxime.rasse@orange.com', 61),
('Le bg du 14', 'Yusuf ', 'gettyimages-82149805_super.jpg', '4', '3', 'maxime.rasse@orange.com', 62),
('Je cherche qqc au microscope', 'Bonjour', 'stocksy_txpb0c57a47do5100_original_564527.jpg', '1', '1', 'alex.lecoq@orange.com', 63),
('Depuis peu je suis devenu papa, m\'occuper de mon fils est devenu ma passion numéro 1. Je lui transmet mon savoir de la CoopNet, pour qu\'il puisse à son tour devenir un expert de la CoopNet.\r\n\r\nJe suis fier de lui, il est devenu fort dans ce monde dangereux.\r\n', 'Mon fiston', 'u160308_en.jpg', '1', '1', 'yusuf.makanjuola@orange.com', 64),
('Mon sport favori est l\'escalade, j\'escalade souvent de grand bâtiments, j\'aime prendre du risque dans la vie, j\'aime la vie, j\'aime la nature, j\'aime les fleurs, j\'aime le CO2, j\'aime les gaz à effet de serre, j\'aime monter le long des échelles...', 'Mon sport favori', 'orange_1146189_16092016.jpg', '1', '2', 'yusuf.makanjuola@orange.com', 65),
('Moi c\'est Yusuf MAKANJUOLA, sur cette photo j\'avais dix ans,  je suis né d\'une famille italienne, avec une mère Coréenne, et un père italien. \r\nJ\'ai eu un accident étant petit, ma tête ne va plus très bien mais j\'arrive à être moi même, ce qui est le principal dans la vie.\r\n\r\nJe suis un grand fan de RASSE Maxime, je trouve que c\'est vraiment le meilleur dans son domaine, il me transmet son savoir et m\'inculque les bonnes manières. \r\n\r\nC\'est le meilleur, je suis vraiment heureux de pouvoir lui servir son café tous les matins.\r\n', 'Moi', 'gettyimages-82149805_super.jpg', '1', '3', 'yusuf.makanjuola@orange.com', 66);

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
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
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
