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
-- Table structure for table `cpu_data`
--

DROP TABLE IF EXISTS `cpu_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cpu_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `price` decimal(10,2) DEFAULT NULL,
  `core_count` int DEFAULT NULL,
  `core_clock` decimal(2,1) DEFAULT NULL,
  `boost_clock` decimal(2,1) DEFAULT NULL,
  `tdp` int DEFAULT NULL,
  `graphics` text,
  `smt` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpu_data`
--

LOCK TABLES `cpu_data` WRITE;
/*!40000 ALTER TABLE `cpu_data` DISABLE KEYS */;
INSERT INTO `cpu_data` VALUES (1,'Intel Core i7-13700K',18999.99,16,3.4,5.4,125,'Intel UHD Graphics 770',1),(2,'Intel Core i9-13900K',27999.99,24,3.0,5.8,125,'Intel UHD Graphics 770',1),(3,'AMD Ryzen 7 7800X3D',21499.99,8,4.2,5.0,120,'Radeon',1),(4,'Intel Core i5-13600K',14999.99,14,3.5,5.1,125,'Intel UHD Graphics 770',1),(5,'AMD Ryzen 7 7700X',14499.99,8,4.5,5.4,105,'Radeon',1),(6,'AMD Ryzen 5 7600X',10999.99,6,4.7,5.3,105,'Radeon',1),(7,'Intel Core i7-12700K',11999.99,12,3.6,5.0,125,'Intel UHD Graphics 770',1),(8,'AMD Ryzen 5 7600',10499.99,6,3.8,5.1,65,'Radeon',1),(9,'Intel Core i5-12600K',8999.99,10,3.7,4.9,125,'Intel UHD Graphics 770',1),(10,'AMD Ryzen 5 5600G',6499.99,6,3.9,4.4,65,'Radeon Vega 7',1),(11,'AMD Ryzen 9 7900X',20499.99,12,4.7,5.6,170,'Radeon',1),(12,'AMD Ryzen 9 7950X3D',27499.99,16,4.2,5.7,120,'Radeon',1),(13,'AMD Ryzen 7 5700G',7999.99,8,3.8,4.6,65,'Radeon Vega 8',1),(14,'AMD Ryzen 9 7950X',28999.99,16,4.5,5.7,170,'Radeon',1),(15,'Intel Core i9-12900K',16999.99,16,3.2,5.2,125,'Intel UHD Graphics 770',1),(16,'Intel Core i5-13500',11999.99,14,2.5,4.8,65,'Intel UHD Graphics 770',1),(17,'AMD Ryzen 7 7700',14499.99,8,3.6,5.3,65,'Radeon',1),(18,'AMD Ryzen 5 4600G',4999.99,6,3.7,4.2,65,'Radeon Vega 7',1),(19,'Intel Core i5-12400',8499.99,6,2.5,4.4,65,'Intel UHD Graphics 730',1),(20,'Intel Core i5-13400',10999.99,10,2.5,4.6,65,'Intel UHD Graphics 730',1),(21,'AMD Ryzen 9 7900',19499.99,12,3.6,5.4,65,'Radeon',1),(22,'AMD Ryzen 9 7900X3D',25999.99,12,4.4,5.6,120,'Radeon',1),(23,'Intel Core i7-9700K',16499.99,8,3.6,4.9,95,'Intel UHD Graphics 630',0),(24,'Intel Core i7-11700K',13499.99,8,3.6,5.0,125,'Intel UHD Graphics 750',1),(25,'AMD Ryzen 3 3200G',3499.99,4,3.6,4.0,65,'Radeon Vega 8',0),(26,'Intel Core i7-10700K',13999.99,8,3.8,5.1,125,'Intel UHD Graphics 630',1),(27,'Intel Core i9-9900K',27999.99,8,3.6,5.0,95,'Intel UHD Graphics 630',1),(28,'Intel Core i5-11600K',8999.99,6,3.9,4.9,125,'Intel UHD Graphics 750',1),(29,'Intel Core i7-8700K',13499.99,6,3.7,4.7,95,'Intel UHD Graphics 630',1),(30,'Intel Core i7-13700',18499.99,16,2.1,5.2,65,'Intel UHD Graphics 770',1),(31,'Intel Core i3-12100',5499.99,4,3.3,4.3,60,'Intel UHD Graphics 730',1),(32,'Intel Core i7-7700K',15499.99,4,4.2,4.5,91,'Intel HD Graphics 630',1),(33,'Intel Core i3-13100',6499.99,4,3.4,4.5,60,'Intel UHD Graphics 730',1),(34,'Intel Core i9-11900K',14499.99,8,3.5,5.3,125,'Intel UHD Graphics 750',1),(35,'Intel Core i5-10400',6499.99,6,2.9,4.3,65,'Intel UHD Graphics 630',1),(36,'Intel Core i9-10900K',16999.99,10,3.7,5.3,125,'Intel UHD Graphics 630',1),(37,'Intel Core i7-6700K',10999.99,4,4.0,4.2,91,'Intel HD Graphics 530',1),(38,'Intel Core i5-9600K',10499.99,6,3.7,4.6,95,'Intel UHD Graphics 630',0),(39,'AMD Ryzen 5 3400G',5999.99,4,3.7,4.2,65,'Radeon Vega 11',1),(40,'Intel Core i5-10600K',8499.99,6,4.1,4.8,125,'Intel UHD Graphics 630',1),(41,'Intel Core i9-10850K',11999.99,10,3.6,5.2,125,'Intel UHD Graphics 630',1),(42,'Intel Core i5-11400',6999.99,6,2.6,4.4,65,'Intel UHD Graphics 730',1),(43,'Intel Core i7-11700',9499.99,8,2.5,4.9,65,'Intel UHD Graphics 750',1),(44,'Intel Core i9-13900',27499.99,24,2.0,5.6,65,'Intel UHD Graphics 770',1),(45,'Intel Core i7-8700',15499.99,6,3.2,4.6,65,'Intel UHD Graphics 630',1),(46,'Intel Core i5-8400',8999.99,6,2.8,4.0,65,'Intel UHD Graphics 630',0),(47,'Intel Core i7-12700',15499.99,12,2.1,4.9,65,'Intel UHD Graphics 770',1),(48,'Intel Core i5-6600K',8999.99,4,3.5,3.9,91,'Intel HD Graphics 530',0),(49,'Intel Core i9-12900KS',18999.99,16,3.4,5.5,150,'Intel UHD Graphics 770',1),(50,'Intel Core i5-6500',6999.99,4,3.2,3.6,65,'Intel HD Graphics 530',0),(51,'Intel Core i7-7700',11999.99,4,3.6,4.2,65,'Intel HD Graphics 630',1),(52,'Intel Core i3-10100',4999.99,4,3.6,4.3,65,'Intel UHD Graphics 630',1),(53,'Intel Core i5-4690K',4499.99,4,3.5,3.9,88,'Intel HD Graphics 4600',0),(54,'Intel Core i7-6700',11499.99,4,3.4,4.0,65,'Intel HD Graphics 530',1),(55,'Intel Core i7-10700',11499.99,8,2.9,4.8,65,'Intel UHD Graphics 630',1),(56,'Intel Core i5-8600K',11999.99,6,3.6,4.3,95,'Intel UHD Graphics 630',0),(57,'AMD Ryzen 3 2200G',7499.99,4,3.5,3.7,65,'Radeon Vega 8',0),(58,'Intel Core i7-4770',5999.99,4,3.4,3.9,84,'Intel HD Graphics 4600',1),(59,'Intel Core i5-12500',11499.99,6,3.0,4.6,65,'Intel UHD Graphics 770',1),(60,'Intel Core i5-7500',6499.99,4,3.4,3.8,65,'Intel HD Graphics 630',0),(61,'Intel Core i7-9700',16999.99,8,3.0,4.7,65,'Intel HD Graphics 630',0),(62,'Intel Core i5-7600K',10499.99,4,3.8,4.2,91,'Intel HD Graphics 630',0),(63,'AMD Ryzen 5 2400G',6499.99,4,3.6,3.9,65,'Radeon Vega 11',1),(64,'Intel Core i5-7400',7499.99,4,3.0,3.5,65,'Intel HD Graphics 630',0),(65,'Intel Core i5-4460',3999.99,4,3.2,3.4,84,'Intel HD Graphics 4600',0),(66,'Intel Core i3-10105',4999.99,4,3.7,4.4,65,'Intel UHD Graphics 630',1),(67,'Intel Core i7-4790',15499.99,4,3.6,4.0,84,'Intel HD Graphics 4600',1),(68,'Intel Core i7-4770K',9499.99,4,3.5,3.9,84,'Intel HD Graphics 4600',1),(69,'Intel Core i5-12600',12499.99,6,3.3,4.8,65,'Intel UHD Graphics 770',1),(70,'Intel Core i5-9400',10499.99,6,2.9,4.1,65,'Intel UHD Graphics 630',0),(71,'Intel Core i9-9900KS',98999.99,8,4.0,5.0,127,'Intel UHD Graphics 630',1),(72,'Intel Core i5-8500',12499.99,6,3.0,4.1,65,'Intel UHD Graphics 630',0),(73,'Intel Core i7-8700K',17499.99,6,3.7,4.7,95,'Intel UHD Graphics 630',1),(74,'Intel Core i5-4690',4999.99,4,3.5,3.9,84,'Intel HD Graphics 4600',0),(75,'Intel Core i5-10500',10499.99,6,3.1,4.5,65,'Intel UHD Graphics 630',1),(76,'Intel Core i7-4790K',9999.99,4,4.0,4.4,88,'Intel HD Graphics 4600',1),(77,'Intel Core i9-12900',22499.99,16,2.4,5.1,65,'Intel UHD Graphics 770',1),(78,'Intel Core i5-7600',6499.99,4,3.5,4.1,65,'Intel HD Graphics 630',0),(79,'Intel Core i3-9100',6999.99,4,3.6,4.2,65,'Intel UHD Graphics 630',0),(80,'Intel Core i9-9900K (Standard Folding Box)',25499.99,8,3.6,5.0,95,'Intel UHD Graphics 630',1),(81,'Intel Core i7-8700',16999.99,6,3.2,4.6,65,'Intel UHD Graphics 630',1),(82,'Intel Core i9-10900',15499.99,10,2.8,5.2,65,'Intel UHD Graphics 630',1),(83,'Intel Core i7-8086K',23499.99,6,4.0,5.0,95,'Intel UHD Graphics 630',1),(84,'Intel Core i7-7700',14999.99,4,3.6,4.2,65,'Intel HD Graphics 630',1),(85,'Intel Core i5-8400',14499.99,6,2.8,4.0,65,'Intel UHD Graphics 630',0),(86,'Intel Core i5-4440',5999.99,4,3.1,3.3,84,'Intel HD Graphics 4600',0),(87,'Intel Core i9-11900',17999.99,8,2.5,5.2,65,'Intel UHD Graphics 750',1),(88,'Intel Core i9-9900K',44999.99,8,3.6,5.0,95,'Intel UHD Graphics 630',1),(89,'Intel Core i5-11500',10999.99,6,2.7,4.6,65,'Intel UHD Graphics 750',1),(90,'Intel Core i5-9500',10499.99,6,3.0,4.4,65,'Intel UHD Graphics 630',0),(91,'Intel Core i5-10600',9999.99,6,3.3,4.8,65,'Intel UHD Graphics 630',1),(92,'Intel Core i5-8600',11499.99,6,3.1,4.3,65,'Intel UHD Graphics 630',0),(93,'Intel Core i9-9900',29499.99,8,3.1,5.0,65,'Intel UHD Graphics 630',1),(94,'AMD A6-7400K',4999.99,2,3.5,3.9,65,'Radeon R5 (on die)',0),(95,'Intel Core i7-9700',16999.99,8,3.0,4.7,65,'Intel HD Graphics 630',0),(96,'Intel Core i7-7700T',23999.99,4,2.9,3.8,35,'Intel HD Graphics 630',1),(97,'Intel Xeon E-2176G',53499.99,6,3.7,4.7,80,'Intel HD Graphics P630',1),(98,'AMD A4-6300',1999.99,2,3.7,3.9,65,'Radeon HD 8370D',0),(99,'Intel Core i5-6402P',4999.99,4,2.8,3.4,65,'Intel HD Graphics 510',0),(100,'Intel Core i5-11600',11999.99,6,2.8,4.8,65,'Intel UHD Graphics 750',1),(101,'Intel Core i7-6700',11999.99,4,3.4,4.0,65,'Intel HD Graphics 530',1),(102,'Intel Core i9-10900K',24499.99,10,3.7,5.3,125,'Intel UHD Graphics 630',1),(103,'AMD A10-9700',5999.99,4,3.5,3.8,65,'Radeon R7 (on-die)',0),(104,'Intel Core i3-10305',4999.99,4,3.8,4.5,65,'Intel UHD Graphics 630',1),(105,'Intel Core i3-10300',8499.99,4,3.7,4.4,65,'Intel UHD Graphics 630',1),(106,'AMD A10-7850K',6499.99,4,3.7,4.0,95,'Radeon R7 (on-die)',0),(107,'Intel Core i5-7400',7499.99,4,3.0,3.5,65,'Intel HD Graphics 630',0),(108,'AMD A6-9500',3999.99,2,3.5,3.8,65,'Radeon R5 (on die)',0),(109,'Intel Core i5-9600',11499.99,6,3.1,4.6,65,'Intel UHD Graphics 630',0),(110,'Intel Core i7-8700T',15999.99,6,2.4,4.0,35,'Intel UHD Graphics 630',1),(111,'AMD A12-9800',7999.99,4,3.8,4.2,65,'Radeon R7 (on-die)',0),(112,'Intel Core i5-4690K',7999.99,4,3.5,3.9,88,'Intel HD Graphics 4600',0),(113,'Intel Core i7-10700K Avengers Collector\'s Edition',18999.99,8,3.8,5.1,125,'Intel UHD Graphics 630',1),(114,'Intel Core i7-4770K',11999.99,4,3.5,3.9,84,'Intel HD Graphics 4600',1),(115,'Intel Core i7-5775C',10999.99,4,3.3,3.7,65,'Iris Pro Graphics 6200',1),(116,'Intel Core i3-10320',7499.99,4,3.8,4.6,65,'Intel UHD Graphics 630',1),(117,'Intel Core i5-7500T',9499.99,4,2.7,3.3,35,'Intel HD Graphics 630',0),(118,'Intel Core i3-9300',11999.99,4,3.7,4.3,62,'Intel UHD Graphics 630',0),(119,'Intel Core i7-4770K',9999.99,4,3.5,3.9,84,'Intel HD Graphics 4600',1),(120,'Intel Core i5-4440S',5999.99,4,2.8,3.3,65,'Intel HD Graphics 4600',0),(121,'AMD A10-7700K',6499.99,4,3.4,3.8,95,'Radeon R7 (on-die)',0),(122,'AMD A10-7870K',15999.99,4,3.9,4.1,95,'Radeon R7 (on-die)',0),(123,'Intel Core i5-3340',13499.99,4,3.1,3.3,77,'Intel HD Graphics 2500',0),(124,'Intel Core i7-7700T',18999.99,4,2.9,3.8,35,'Intel HD Graphics 630',1),(125,'AMD A12-9800E',6499.99,4,3.1,3.8,35,'Radeon R7 (on-die)',0),(126,'AMD A6-7470K',3999.99,2,3.7,4.0,65,'Radeon R5 (on die)',0),(127,'Intel Core i5-6600T',14499.99,4,2.7,3.5,35,'Intel HD Graphics 530',0),(128,'Intel Core i5-4690',6999.99,4,3.5,3.9,84,'Intel HD Graphics 4600',0),(129,'Intel Core i7-5775C',44999.99,4,3.3,3.7,65,'Iris Pro Graphics 6200',1),(130,'Intel Core i5-7600T',6999.99,4,2.8,3.7,35,'Intel HD Graphics 630',0),(131,'Intel Core i5-8500',12499.99,6,3.0,4.1,65,'Intel UHD Graphics 630',0),(132,'Intel Core i5-8600',13999.99,6,3.1,4.3,65,'Intel UHD Graphics 630',0),(133,'Intel Xeon E3-1225 V3',18999.99,4,3.2,3.6,84,'Intel HD Graphics P4600',0),(134,'Intel Core i5-7400T',8999.99,4,2.4,3.0,35,'Intel HD Graphics 630',0),(135,'Intel Xeon E3-1265L V3',19499.99,4,2.5,3.7,45,'Intel HD Graphics',1),(136,'AMD A4-6300B',1999.99,2,3.7,3.9,65,'Radeon HD 8370D',0),(137,'Intel Xeon E3-1245 V6',30999.99,4,3.7,4.1,73,'Intel HD Graphics P630',1),(138,'Intel Xeon E-2286G',70999.99,6,4.0,4.9,95,'Intel HD Graphics P630',1),(139,'Intel Core i5-3330S',10999.99,4,2.7,3.2,65,'Intel HD Graphics 2500',0),(140,'Intel Xeon E-2274G',27999.99,4,4.0,4.9,83,'Intel HD Graphics P630',1),(141,'Intel Xeon E3-1225 V5',14499.99,4,3.3,3.7,80,'Intel HD Graphics P530',0),(142,'Intel Core i5-7600T',10999.99,4,2.8,3.7,35,'Intel HD Graphics 630',0),(143,'Intel Core i5-4670S',26499.99,4,3.1,3.8,65,'Intel HD Graphics 4600',0),(144,'Intel Xeon E3-1275 V6',17499.99,4,3.8,4.2,73,'Intel HD Graphics P630',1),(145,'AMD A4-7300',12999.99,2,3.8,4.0,65,'Radeon HD 8470D',0),(146,'Intel Xeon E3-1285 V6',46999.99,4,4.1,4.5,79,'Intel HD Graphics 630',1),(147,'AMD Pro A10-7850B',6999.99,4,3.7,4.0,95,'Radeon R7 (on-die)',0),(148,'Intel Xeon E-2146G',45499.99,6,3.5,4.5,80,'Intel HD Graphics P630',1),(149,'Intel Xeon E-2174G',26999.99,4,3.8,4.7,71,'Intel HD Graphics P630',1),(150,'Intel Xeon E3-1245 V6',28999.99,4,3.7,4.1,73,'Intel HD Graphics P630',1),(151,'Intel Xeon E-2174G',26499.99,4,3.8,4.7,71,'Intel HD Graphics P630',1),(152,'Intel Xeon E-2126G',41999.99,6,3.3,4.5,80,'Intel HD Graphics P630',0),(153,'Intel Xeon E-2124G',31999.99,4,3.4,4.5,71,'Intel HD Graphics P630',0),(154,'Intel Xeon E3-1245 V5',19499.99,4,3.5,3.9,80,'Intel HD Graphics P530',1),(155,'Intel Xeon E3-1225 V6',24499.99,4,3.3,3.7,73,'Intel HD Graphics P630',0),(156,'Intel Xeon E3-1225 V6',19999.99,4,3.3,3.7,73,'Intel HD Graphics P630',0);
/*!40000 ALTER TABLE `cpu_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 16:46:18