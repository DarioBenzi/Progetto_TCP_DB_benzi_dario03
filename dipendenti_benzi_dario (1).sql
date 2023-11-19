-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 19, 2023 alle 10:42
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
-- Struttura della tabella `dipendenti_benzi_dario`
--

CREATE TABLE `dipendenti_benzi_dario` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(40) NOT NULL,
  `posizione_lavorativa` varchar(50) NOT NULL,
  `data_assunzione` date NOT NULL,
  `data_nascita` date NOT NULL,
  `turno` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `dipendenti_benzi_dario`
--

INSERT INTO `dipendenti_benzi_dario` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_assunzione`, `data_nascita`, `turno`) VALUES
(1, 'mario', 'rossi', 'dipendente', '2023-10-04', '2023-10-25', '2023-09-13'),
(2, 'ugo', 'paciugo', 'capo_officina', '2023-10-10', '2023-10-26', '2023-09-13'),
(3, 'andrea', 'bianchi', 'capo_reparto', '2023-10-26', '2017-10-20', '2023-10-04'),
(4, 'walter', 'verdi', 'dipendente', '2019-10-11', '2014-10-09', '2023-10-19'),
(5, 'sara', 'esposito', 'dipendente', '2020-10-01', '2013-10-03', '2023-10-04');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_benzi_dario`
--
ALTER TABLE `dipendenti_benzi_dario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_benzi_dario`
--
ALTER TABLE `dipendenti_benzi_dario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
