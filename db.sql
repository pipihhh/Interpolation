-- MySQL dump 10.13  Distrib 5.7.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: interpolation
-- ------------------------------------------------------
-- Server version	5.7.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `calculation_log`
--

DROP TABLE IF EXISTS `calculation_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calculation_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `host` varchar(50) NOT NULL,
  `file_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COMMENT='计算记录表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calculation_log`
--

LOCK TABLES `calculation_log` WRITE;
/*!40000 ALTER TABLE `calculation_log` DISABLE KEYS */;
INSERT INTO `calculation_log` VALUES (1,'2020-03-28 13:23:17','127.0.0.1:5000','calculated_1585401797.png'),(2,'2020-03-28 13:27:48','127.0.0.1:5000','calculated_1585402068.png'),(3,'2020-03-28 13:29:00','127.0.0.1:5000','calculated_1585402139.png'),(4,'2020-03-28 13:33:45','127.0.0.1:5000','calculated_1585402139.png'),(8,'2020-03-30 08:52:42','127.0.0.1:5000','calculated_1585558362.png'),(9,'2020-03-30 08:52:54','127.0.0.1:5000','calculated_1585558374.png');
/*!40000 ALTER TABLE `calculation_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plot_log`
--

DROP TABLE IF EXISTS `plot_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plot_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` varchar(255) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `file_name` varchar(50) NOT NULL,
  `download_times` int(11) NOT NULL DEFAULT '0',
  `plot_md5` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `plot_log_plot_md5_uindex` (`plot_md5`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COMMENT='画图的记录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plot_log`
--

LOCK TABLES `plot_log` WRITE;
/*!40000 ALTER TABLE `plot_log` DISABLE KEYS */;
INSERT INTO `plot_log` VALUES (7,'127.0.0.1:5000','2020-03-28 13:23:17','calculated_1585401797.png',1,'b\'\\x7f\\xbbP\\xd8TD\\x96\\xe8&*\\xbe\\xcc\\xb7Lje\''),(8,'127.0.0.1:5000','2020-03-28 13:27:48','calculated_1585402068.png',0,'b\'\\xe0\\xf4i\\x9e&\\x13\\x92\\x00\\x8fZ\\x8a\\xa0r\\xdc\\x8c7\''),(9,'127.0.0.1:5000','2020-03-28 13:28:59','calculated_1585402139.png',2,'b\'_(G^\\xd9\\xbcc\\xf3\\x9e\\xd8\\x13\\x9f\\xce\\xf3\\xb2D\''),(12,'127.0.0.1:5000','2020-03-30 08:52:42','calculated_1585558362.png',0,'b\'\\x04e};ch\\x9eL\\xa6d\\x0e\\xb9@E*\\xec\''),(13,'127.0.0.1:5000','2020-03-30 08:52:54','calculated_1585558374.png',0,'b\'\\x9ff\\x1c\\xabE-Oh\\x98z\\x80\\xd2W\\xda\\xb0w\'');
/*!40000 ALTER TABLE `plot_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-06 11:55:14
