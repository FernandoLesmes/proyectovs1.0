-- MySQL dump 10.13  Distrib 9.1.0, for Linux (x86_64)
--
-- Host: localhost    Database: proyecto1
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Actividades`
--

DROP TABLE IF EXISTS `Actividades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actividades` (
  `id_actividad` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `id_proyecto` int DEFAULT NULL,
  `visibilidad` enum('Publica','Privada','Limitada') NOT NULL,
  `id_colaborador` int DEFAULT NULL,
  PRIMARY KEY (`id_actividad`),
  KEY `id_proyecto` (`id_proyecto`),
  KEY `id_colaborador` (`id_colaborador`),
  CONSTRAINT `Actividades_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `Proyectos` (`id_proyecto`) ON DELETE CASCADE,
  CONSTRAINT `Actividades_ibfk_2` FOREIGN KEY (`id_colaborador`) REFERENCES `Colaborador` (`id_colaborador`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actividades`
--

LOCK TABLES `Actividades` WRITE;
/*!40000 ALTER TABLE `Actividades` DISABLE KEYS */;
INSERT INTO `Actividades` VALUES (8,'Presentar proyecto el 14 noviembre','hola, esto lo hago por un error q ha pasado, debo de verificar la base de datos, el codigo ','2024-12-27','2024-12-31',2,'Privada',2),(9,'Verificar las actas de entrega ','Debos dscargar las actas  de bajas de actulización, guardalas en le servidor ','2024-12-28','2024-12-28',3,'Publica',3),(10,'verificar el menu que sea igual para todos','verificar el ligi de cada uno de los usuarios por q al ingresar se esta viendo diferente menu ','2024-12-28','2024-12-31',4,'Publica',6);
/*!40000 ALTER TABLE `Actividades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Colaborador`
--

DROP TABLE IF EXISTS `Colaborador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Colaborador` (
  `id_colaborador` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `area` varchar(100) DEFAULT NULL,
  `cargo` varchar(100) DEFAULT NULL,
  `usuario` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `codigo_sap` varchar(50) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `id_rol` int DEFAULT NULL,
  `session_token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_colaborador`),
  UNIQUE KEY `usuario` (`usuario`),
  UNIQUE KEY `correo` (`correo`),
  UNIQUE KEY `codigo_sap` (`codigo_sap`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `Colaborador_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `Roles` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Colaborador`
--

LOCK TABLES `Colaborador` WRITE;
/*!40000 ALTER TABLE `Colaborador` DISABLE KEYS */;
INSERT INTO `Colaborador` VALUES (2,'Fernando','Lesmes','Sistemas','Tecnico','flesmes','correo@example.com','123','scrypt:32768:8:1$QlC5TtVTbeSsjj1G$af91dacca26a2d8753a920810e842023122603506294389fa2146743e3d94c4e2e08a92885868a7a9c43d47bb7b5b4ccfdcfde3f71eb27627ddacc4dc478e305',1,'5f33ba2c-1234-4d42-bf94-59e39b9dff73'),(3,'Jorge','lopez','contabilidad','analista','jlopez','a.ejemplo@example.com','110813','scrypt:32768:8:1$QB8ImfW8wlnjjlLY$4a515181ef64b47a6ac31859b687b852eea68943aad6883706350e03527278f00af04233a909953b64192ecdaf45cda5b44bdab6c268569b681b5990f54d885c',2,'5080d31f-8bea-4dfb-b8df-2a1d5207ed4c'),(6,'Edwars','Diaz','Costos','Director','ediaz','e.diaz@prueva.edu.co','110814','scrypt:32768:8:1$vMwujPDAmBtUhsaR$067a6349ba2e638dfbdcc1963c6d98262a0a2bc514b088c622428646b6d37a52eb9f255feb853491dd797db6b99069718fe7bedfb184edbcf6151f9beaa76ae4',3,'9b3465ee-f2a2-45da-bdf5-2d1611dabb71');
/*!40000 ALTER TABLE `Colaborador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Colaborador_Proyectos_Roles`
--

DROP TABLE IF EXISTS `Colaborador_Proyectos_Roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Colaborador_Proyectos_Roles` (
  `id_colaborador` int NOT NULL,
  `id_proyecto` int NOT NULL,
  `id_rol` int NOT NULL,
  PRIMARY KEY (`id_colaborador`,`id_proyecto`,`id_rol`),
  KEY `id_proyecto` (`id_proyecto`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `Colaborador_Proyectos_Roles_ibfk_1` FOREIGN KEY (`id_colaborador`) REFERENCES `Colaborador` (`id_colaborador`) ON DELETE CASCADE,
  CONSTRAINT `Colaborador_Proyectos_Roles_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `Proyectos` (`id_proyecto`) ON DELETE CASCADE,
  CONSTRAINT `Colaborador_Proyectos_Roles_ibfk_3` FOREIGN KEY (`id_rol`) REFERENCES `Roles` (`id_rol`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Colaborador_Proyectos_Roles`
--

LOCK TABLES `Colaborador_Proyectos_Roles` WRITE;
/*!40000 ALTER TABLE `Colaborador_Proyectos_Roles` DISABLE KEYS */;
INSERT INTO `Colaborador_Proyectos_Roles` VALUES (2,2,1),(2,2,2),(2,2,3),(2,3,1),(2,3,2),(2,3,3),(2,4,1),(2,4,2),(2,4,3);
/*!40000 ALTER TABLE `Colaborador_Proyectos_Roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Permisos`
--

DROP TABLE IF EXISTS `Permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Permisos` (
  `id_permiso` int NOT NULL AUTO_INCREMENT,
  `id_rol` int DEFAULT NULL,
  `nombre_permiso` varchar(100) NOT NULL,
  PRIMARY KEY (`id_permiso`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `Permisos_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `Roles` (`id_rol`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Permisos`
--

LOCK TABLES `Permisos` WRITE;
/*!40000 ALTER TABLE `Permisos` DISABLE KEYS */;
INSERT INTO `Permisos` VALUES (1,3,'Crear proyectos'),(2,3,'Asignar tareas'),(3,3,'Ver progreso'),(4,2,'Ver tareas'),(5,2,'Actualizar progreso'),(6,1,'Administrar usuarios'),(7,1,'Administrar proyectos'),(8,1,'Ver todo');
/*!40000 ALTER TABLE `Permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proyectos`
--

DROP TABLE IF EXISTS `Proyectos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Proyectos` (
  `id_proyecto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `id_lider` int DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `avance` float DEFAULT '0',
  PRIMARY KEY (`id_proyecto`),
  KEY `id_lider` (`id_lider`),
  CONSTRAINT `Proyectos_ibfk_1` FOREIGN KEY (`id_lider`) REFERENCES `Colaborador` (`id_colaborador`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proyectos`
--

LOCK TABLES `Proyectos` WRITE;
/*!40000 ALTER TABLE `Proyectos` DISABLE KEYS */;
INSERT INTO `Proyectos` VALUES (2,'Entrega total','Para el jueves debo realizar la entraga ',2,'2024-11-11','2024-11-14',0),(3,'inventario','relizar inventario de tosos los equipos de cga ',3,'2024-11-13','2024-11-22',0),(4,'Session','Debemos de verificar el por que no me esta cargando las diferentes inicios de sesion de  de cada uno ¿de los usuarios ',6,'2024-12-04','2024-12-05',0);
/*!40000 ALTER TABLE `Proyectos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Roles`
--

DROP TABLE IF EXISTS `Roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Roles` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(50) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Roles`
--

LOCK TABLES `Roles` WRITE;
/*!40000 ALTER TABLE `Roles` DISABLE KEYS */;
INSERT INTO `Roles` VALUES (1,'Admin'),(2,'Usuario'),(3,'Líder de Proyecto');
/*!40000 ALTER TABLE `Roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-27 13:03:19
