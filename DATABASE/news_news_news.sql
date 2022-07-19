-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: news
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `news_news`
--

DROP TABLE IF EXISTS `news_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news_news` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `heading` varchar(300) NOT NULL,
  `details` longtext NOT NULL,
  `photo` varchar(100) NOT NULL,
  `reporter_id` int NOT NULL,
  `category_id` int DEFAULT NULL,
  `recent` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `news_news_category_id_f060a768_fk_news_category_id` (`category_id`),
  KEY `news_news_reporter_id_7b387abd` (`reporter_id`),
  CONSTRAINT `news_news_category_id_f060a768_fk_news_category_id` FOREIGN KEY (`category_id`) REFERENCES `news_category` (`id`),
  CONSTRAINT `news_news_reporter_id_7b387abd_fk_news_reporter_id` FOREIGN KEY (`reporter_id`) REFERENCES `news_reporter` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_news`
--

LOCK TABLES `news_news` WRITE;
/*!40000 ALTER TABLE `news_news` DISABLE KEYS */;
INSERT INTO `news_news` VALUES (1,'2021-04-18','Two Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar Prasad','Two Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar PrasadTwo Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar Prasad','news_photos/hhh_PETsPdF.jpg',1,1,1),(2,'2021-04-18','Two Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar Prasad','Two Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar PrasadTwo Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar PrasadTwo Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar PrasadTwo Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar PrasadTwo Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar PrasadTwo Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar Prasad','news_photos/bs.jpg',1,2,1),(3,'2021-04-18','iot exhibition  in softwarica clg','on 23rd march IOT EXHIBITION TAKES PLACE IN SOFTWARICA. MANY STUDENTS COME FROM DIFFERENT SCHOOL OR COLLEGES TO TAKE PATTICIPATE','news_photos/hhh_9FhNtI7.jpg',1,1,1),(4,'2021-04-18','Two Lakh Jobs Added In IT Sector Since 2019: Ravi Shankar Prasad','two lakhs provide to the IT best hacker\r\nof the world','news_photos/hhh_Bx8ThOO.jpg',1,2,1);
/*!40000 ALTER TABLE `news_news` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-20 12:04:23
