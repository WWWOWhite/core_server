-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 192.168.19.129    Database: django_db
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add manager table',7,'add_managertable'),(26,'Can change manager table',7,'change_managertable'),(27,'Can delete manager table',7,'delete_managertable'),(28,'Can view manager table',7,'view_managertable'),(29,'Can add register table',8,'add_registertable'),(30,'Can change register table',8,'change_registertable'),(31,'Can delete register table',8,'delete_registertable'),(32,'Can view register table',8,'view_registertable'),(33,'Can add user table',9,'add_usertable'),(34,'Can change user table',9,'change_usertable'),(35,'Can delete user table',9,'delete_usertable'),(36,'Can view user table',9,'view_usertable'),(37,'Can add node table',10,'add_nodetable'),(38,'Can change node table',10,'change_nodetable'),(39,'Can delete node table',10,'delete_nodetable'),(40,'Can view node table',10,'view_nodetable'),(41,'Can add log table',11,'add_logtable'),(42,'Can change log table',11,'change_logtable'),(43,'Can delete log table',11,'delete_logtable'),(44,'Can view log table',11,'view_logtable'),(45,'Can add software table',12,'add_softwaretable'),(46,'Can change software table',12,'change_softwaretable'),(47,'Can delete software table',12,'delete_softwaretable'),(48,'Can view software table',12,'view_softwaretable'),(49,'Can add software location',13,'add_softwarelocation'),(50,'Can change software location',13,'change_softwarelocation'),(51,'Can delete software location',13,'delete_softwarelocation'),(52,'Can view software location',13,'view_softwarelocation'),(53,'Can add regist software table',14,'add_registsoftwaretable'),(54,'Can change regist software table',14,'change_registsoftwaretable'),(55,'Can delete regist software table',14,'delete_registsoftwaretable'),(56,'Can view regist software table',14,'view_registsoftwaretable'),(57,'Can add enity table',15,'add_enitytable'),(58,'Can change enity table',15,'change_enitytable'),(59,'Can delete enity table',15,'delete_enitytable'),(60,'Can view enity table',15,'view_enitytable'),(61,'Can add register software location table',16,'add_registersoftwarelocationtable'),(62,'Can change register software location table',16,'change_registersoftwarelocationtable'),(63,'Can delete register software location table',16,'delete_registersoftwarelocationtable'),(64,'Can view register software location table',16,'view_registersoftwarelocationtable'),(65,'Can add register software table',17,'add_registersoftwaretable'),(66,'Can change register software table',17,'change_registersoftwaretable'),(67,'Can delete register software table',17,'delete_registersoftwaretable'),(68,'Can view register software table',17,'view_registersoftwaretable'),(69,'Can add kgc paramter table',18,'add_kgcparamtertable'),(70,'Can change kgc paramter table',18,'change_kgcparamtertable'),(71,'Can delete kgc paramter table',18,'delete_kgcparamtertable'),(72,'Can view kgc paramter table',18,'view_kgcparamtertable');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(15,'entitymanage','enitytable'),(18,'entitymanage','kgcparamtertable'),(11,'nodemanage','logtable'),(10,'nodemanage','nodetable'),(6,'sessions','session'),(16,'softwaremanage','registersoftwarelocationtable'),(17,'softwaremanage','registersoftwaretable'),(14,'softwaremanage','registsoftwaretable'),(13,'softwaremanage','softwarelocation'),(12,'softwaremanage','softwaretable'),(7,'usermanage','managertable'),(8,'usermanage','registertable'),(9,'usermanage','usertable');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-08 10:14:44.073684'),(2,'auth','0001_initial','2024-04-08 10:14:44.963868'),(3,'admin','0001_initial','2024-04-08 10:14:45.142430'),(4,'admin','0002_logentry_remove_auto_add','2024-04-08 10:14:45.166654'),(5,'admin','0003_logentry_add_action_flag_choices','2024-04-08 10:14:45.190204'),(6,'contenttypes','0002_remove_content_type_name','2024-04-08 10:14:45.317864'),(7,'auth','0002_alter_permission_name_max_length','2024-04-08 10:14:45.395666'),(8,'auth','0003_alter_user_email_max_length','2024-04-08 10:14:45.452107'),(9,'auth','0004_alter_user_username_opts','2024-04-08 10:14:45.474830'),(10,'auth','0005_alter_user_last_login_null','2024-04-08 10:14:45.554174'),(11,'auth','0006_require_contenttypes_0002','2024-04-08 10:14:45.561473'),(12,'auth','0007_alter_validators_add_error_messages','2024-04-08 10:14:45.585741'),(13,'auth','0008_alter_user_username_max_length','2024-04-08 10:14:45.697043'),(14,'auth','0009_alter_user_last_name_max_length','2024-04-08 10:14:45.790945'),(15,'auth','0010_alter_group_name_max_length','2024-04-08 10:14:45.837279'),(16,'auth','0011_update_proxy_permissions','2024-04-08 10:14:45.860987'),(17,'auth','0012_alter_user_first_name_max_length','2024-04-08 10:14:45.948921'),(18,'usermanage','0001_initial','2024-04-08 10:14:46.028517'),(19,'softwaremanage','0001_initial','2024-04-08 10:14:46.276143'),(20,'nodemanage','0001_initial','2024-04-08 10:14:46.381597'),(21,'entitymanage','0001_initial','2024-04-08 10:14:46.608503'),(22,'sessions','0001_initial','2024-04-08 10:14:46.664457'),(23,'nodemanage','0002_nodetable_node_port','2024-04-09 08:18:40.188203'),(24,'entitymanage','0002_kgcparamtertable','2024-04-12 03:55:36.373626'),(25,'softwaremanage','0002_registersoftwarelocationtable_registersoftwaretable_and_more','2024-04-12 03:55:36.713814'),(26,'entitymanage','0003_remove_kgcparamtertable_id_and_more','2024-04-12 03:56:24.470039'),(27,'entitymanage','0004_remove_enitytable_entity_port_and_more','2024-05-05 07:29:44.269911'),(28,'nodemanage','0003_nodetable_node_is_alive_alter_nodetable_node_ip','2024-05-05 07:29:44.663679'),(29,'softwaremanage','0003_alter_registersoftwarelocationtable_entity_ip_and_more','2024-05-05 07:29:45.052993'),(30,'softwaremanage','0004_alter_softwaretable_software_hash','2024-05-17 11:30:40.621516'),(31,'entitymanage','0005_enitytable_software_name','2024-05-17 11:46:20.191575');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodemanage_guidtable`
--

DROP TABLE IF EXISTS `nodemanage_guidtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nodemanage_guidtable` (
  `ip` varchar(100) NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  `guid` varchar(100) NOT NULL,
  `topic` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nodemanage_guidtable_id_IDX` (`id`) USING BTREE,
  UNIQUE KEY `nodemanage_guidtable_guid_IDX` (`guid`,`ip`,`topic`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1200 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodemanage_guidtable`
--

LOCK TABLES `nodemanage_guidtable` WRITE;
/*!40000 ALTER TABLE `nodemanage_guidtable` DISABLE KEYS */;
/*!40000 ALTER TABLE `nodemanage_guidtable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodemanage_logtable`
--

DROP TABLE IF EXISTS `nodemanage_logtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nodemanage_logtable` (
  `log_id` bigint NOT NULL AUTO_INCREMENT,
  `log_type` varchar(20) NOT NULL,
  `log_desc` longtext,
  `create_time` datetime(6) NOT NULL,
  `node_ip` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41976 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodemanage_logtable`
--

LOCK TABLES `nodemanage_logtable` WRITE;
/*!40000 ALTER TABLE `nodemanage_logtable` DISABLE KEYS */;
/*!40000 ALTER TABLE `nodemanage_logtable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nodemanage_nodetable`
--

DROP TABLE IF EXISTS `nodemanage_nodetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nodemanage_nodetable` (
  `node_id` varchar(32) NOT NULL,
  `node_ip` char(39) NOT NULL,
  `node_desc` longtext,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `node_port` int NOT NULL,
  `node_is_alive` tinyint(1) NOT NULL,
  `node_sub` varchar(100) DEFAULT NULL,
  `node_pub` varchar(100) DEFAULT NULL,
  `node_is_config` tinyint DEFAULT NULL,
  `white_guid` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `node_local_white` mediumtext,
  PRIMARY KEY (`node_id`),
  UNIQUE KEY `nodemanage_nodetable_node_ip_IDX` (`node_ip`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nodemanage_nodetable`
--

LOCK TABLES `nodemanage_nodetable` WRITE;
/*!40000 ALTER TABLE `nodemanage_nodetable` DISABLE KEYS */;
/*!40000 ALTER TABLE `nodemanage_nodetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usermanage_managertable`
--

DROP TABLE IF EXISTS `usermanage_managertable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usermanage_managertable` (
  `manager_id` varchar(32) NOT NULL,
  `manager_name` varchar(20) NOT NULL,
  `manager_pwd` varchar(20) NOT NULL,
  `manager_phone` varchar(11) DEFAULT NULL,
  `manager_email` varchar(254) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`manager_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usermanage_managertable`
--

LOCK TABLES `usermanage_managertable` WRITE;
/*!40000 ALTER TABLE `usermanage_managertable` DISABLE KEYS */;
/*!40000 ALTER TABLE `usermanage_managertable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usermanage_registertable`
--

DROP TABLE IF EXISTS `usermanage_registertable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usermanage_registertable` (
  `user_id` varchar(32) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_pwd` varchar(20) NOT NULL,
  `user_phone` varchar(11) DEFAULT NULL,
  `user_email` varchar(254) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usermanage_registertable`
--

LOCK TABLES `usermanage_registertable` WRITE;
/*!40000 ALTER TABLE `usermanage_registertable` DISABLE KEYS */;
/*!40000 ALTER TABLE `usermanage_registertable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usermanage_usertable`
--

DROP TABLE IF EXISTS `usermanage_usertable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usermanage_usertable` (
  `user_id` varchar(32) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `user_row` varchar(20) NOT NULL,
  `user_pwd` varchar(16) NOT NULL,
  `user_phone` varchar(11) DEFAULT NULL,
  `user_email` varchar(254) DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usermanage_usertable`
--

LOCK TABLES `usermanage_usertable` WRITE;
/*!40000 ALTER TABLE `usermanage_usertable` DISABLE KEYS */;
INSERT INTO `usermanage_usertable` VALUES ('0ad9e30ca539f968e662b6d505fcd276','Plant_Manager','admin','user_pwd','17899012894','PlantManager@nav.com','2024-05-16 08:04:47.644295','2024-07-04 08:45:10.228584'),('2b0246eaa2073b1a4a374d251a3a2965','Nav_Operator01','editor','user_pwd','15099783221','NavOperator@nav.com','2024-07-04 08:43:29.131256','2024-07-04 08:44:02.216097');
/*!40000 ALTER TABLE `usermanage_usertable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'django_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-11 17:27:25
