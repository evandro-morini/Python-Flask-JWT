CREATE DATABASE  IF NOT EXISTS `testeb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `testeb`;
-- MySQL dump 10.13  Distrib 8.0.18, for Linux (x86_64)
--
-- Host: localhost    Database: testeb
-- ------------------------------------------------------
-- Server version	5.7.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valor` float NOT NULL,
  `data` datetime DEFAULT NULL,
  `revendedor_id` int(11) NOT NULL,
  `cashback` float NOT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `revendedor_id` (`revendedor_id`),
  CONSTRAINT `compra_ibfk_1` FOREIGN KEY (`revendedor_id`) REFERENCES `revendedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (2,2500,'2019-12-19 15:15:56',1,500,1),(3,1000,'2019-12-19 15:15:56',5,150,1),(4,1250,'2019-12-19 15:15:56',1,187.5,1),(5,975,'2019-12-19 15:15:56',1,97.5,1),(6,5012.1,'2019-12-19 15:15:56',1,1002.42,1),(7,10425.9,'2019-12-19 15:15:56',8,2085.18,1),(8,500.5,'2019-12-19 18:06:46',5,50.05,1);
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `revendedor`
--

DROP TABLE IF EXISTS `revendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `revendedor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(60) NOT NULL,
  `email` varchar(50) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `senha` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `cpf` (`cpf`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `revendedor`
--

LOCK TABLES `revendedor` WRITE;
/*!40000 ALTER TABLE `revendedor` DISABLE KEYS */;
INSERT INTO `revendedor` VALUES (1,'Carlos Silva','carlos.silva@testeb.com.br','08364021036','pbkdf2:sha256:150000$pgPNge7G$8c2ab2fffb4219fd1c203e678e05358adc8c89cd462c155eb8925551f0ce268a'),(5,'Pedro Pereira','pedro.pereira@testeb.com.br','36919411091','pbkdf2:sha256:150000$AmxarxvX$aecd6c42d267e2b0cb69b16ac45cd01c306e94047e8e0f748856d0f845666317'),(8,'Augusto Santos','augusto.santos@testeb.com.br','26571885085','pbkdf2:sha256:150000$lyeuDMjg$2bfa81c4a4b1a9fa3f17da9081e8312884a5132614c6bdf0c022faa999f4c703');
/*!40000 ALTER TABLE `revendedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'testeb'
--

--
-- Dumping routines for database 'testeb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-19 18:17:54
