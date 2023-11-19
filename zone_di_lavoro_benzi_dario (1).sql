-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 10:43
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_benzi_dario`
--

CREATE TABLE `zone_di_lavoro_benzi_dario` (
  `nome_zona` varchar(40) NOT NULL,
  `numero_clienti` int(11) DEFAULT NULL,
  `id_dipendente` int(11) DEFAULT NULL,
  `aperture` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_benzi_dario`
--

INSERT INTO `zone_di_lavoro_benzi_dario` (`nome_zona`, `numero_clienti`, `id_dipendente`, `aperture`) VALUES
('Officina', 30, 1, '2023-10-03'),
('reparto_tecnico', 15, 5, '2023-10-01'),
('Ufficio', 10, 2, '2023-10-26');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zone_di_lavoro_benzi_dario`
--
ALTER TABLE `zone_di_lavoro_benzi_dario`
  ADD PRIMARY KEY (`nome_zona`),
  ADD KEY `id_dipendente` (`id_dipendente`);

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zone_di_lavoro_benzi_dario`
--
ALTER TABLE `zone_di_lavoro_benzi_dario`
  ADD CONSTRAINT `zone_di_lavoro_benzi_dario_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendenti_benzi_dario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
