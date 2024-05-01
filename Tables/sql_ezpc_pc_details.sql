-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: sql_ezpc
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `pc_details`
--

DROP TABLE IF EXISTS `pc_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pc_details` (
  `user_id` int NOT NULL,
  `pc_id` int NOT NULL AUTO_INCREMENT,
  `pc_name` varchar(50) DEFAULT NULL,
  `case_id` int DEFAULT NULL,
  `cooler_id` int DEFAULT NULL,
  `cpu_id` int DEFAULT NULL,
  `gpu_id` int DEFAULT NULL,
  `mobo_id` int DEFAULT NULL,
  `psu_id` int DEFAULT NULL,
  `ram_id` int DEFAULT NULL,
  `storage_id` int DEFAULT NULL,
  PRIMARY KEY (`pc_id`),
  KEY `pc_details_user_details_FK` (`user_id`),
  CONSTRAINT `pc_details_user_details_FK` FOREIGN KEY (`user_id`) REFERENCES `user_details` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pc_details`
--

LOCK TABLES `pc_details` WRITE;
/*!40000 ALTER TABLE `pc_details` DISABLE KEYS */;
INSERT INTO `pc_details` VALUES (4,1,'test build',56,43,58,92,NULL,NULL,317,NULL),(11,2,'Most Expensive PC',67,8,71,286,472,111,24,77),(4,3,'Another One',12,12,12,12,12,12,12,12),(4,7,'test build (2)',43,1,32,9,32,77,88,32),(4,12,'test build (3)',NULL,48,NULL,39,NULL,332,NULL,38),(5,13,'100Computer',100,100,100,100,100,100,100,100),(5,14,'Another One',99,NULL,NULL,99,NULL,NULL,99,NULL);
/*!40000 ALTER TABLE `pc_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 16:48:53
