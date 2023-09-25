-- Copiando estrutura para tabela vrp.discord_config
CREATE TABLE IF NOT EXISTS `discord_config` (
  `id` int(11) DEFAULT NULL,
  `cargo` varchar(255) NOT NULL,
  `chat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Copiando dados para a tabela vrp.discord_config: ~1 rows (aproximadamente)
INSERT INTO `discord_config` (`id`, `cargo`, `chat`) VALUES
	(0, '', '');