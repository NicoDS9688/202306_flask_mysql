CREATE DATABASE  IF NOT EXISTS `recipes_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `recipes_schema`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recipes_schema
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `instructions` text NOT NULL,
  `more_than_30` varchar(45) DEFAULT NULL,
  `made_at` datetime NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,'Banana Banana Bread','This banana bread recipe creates the most delicious, moist loaf with loads of banana flavor. Why compromise the banana flavor? Friends and family love my recipe and say it\'s by far the best! It tastes wonderful toasted. Enjoy!','You\'ll find the full, step-by-step recipe below — but here\'s a brief overview of what you can expect when you make this simple banana bread:\r\n\r\n1. Combine the dry ingredients in one bowl.\r\n2. Beat the butter and sugar in another bowl. Add the eggs and mashed bananas.\r\n3. Add the wet mixture to the dry mixture.\r\n4. Pour the batter into a loaf pan and bake in a preheated oven.','No','2023-08-08 00:00:00',1,'2023-08-30 19:20:52','2023-08-30 19:20:52'),(2,'Philly Cheesesteak Sloppy Joes','Take the best of two classic sandwiches—sloppy joes and Philly cheesesteaks—to make these cheesy, meaty, and saucy cheesesteak sloppy joes!','Cook the vegetables:\r\nIn a large skillet set over medium heat, melt the butter. Add the onions and bell peppers. Cook until soften, 6 to 7 minutes, stirring frequently. The vegetables shouldn’t brown at this point, just soften.\r\nCook the beef:  \r\nAdd the ground beef and use a wooden spoon to break it up into small pieces as it cooks. Cook until the meat is browned, 5 to 6 minutes.\r\nMake it saucy:\r\nStir in the stock, ketchup, Worcestershire sauce, garlic powder, salt, and black pepper. Turn the heat down to low and simmer for 4 to 5 minutes until the mixture thickens.\r\n\r\nStack 6 slices provolone cheese on a cutting board and use a chef’s knife to cut them into 1/2-inch pieces. Right before serving, stir in the cut cheese.\r\nAssemble the sloppy joes: \r\nToast the brioche buns in a toaster oven or toaster. Lay the remaining 6 slices provolone cheese on each brioche bun half. Top the cheese with heaping spoonfuls of the sloppy joe mixture and the top bun. Serve warm.\r\n\r\nIf you have leftover sloppy joe mixture, good news! It keeps beautifully in the fridge for 4 to 5 days and reheats well in the microwave or in a skillet with a splash of water or stock. \r\n\r\nYou can freeze the mixture in freezer-safe container for 3 months. Thaw it before reheating. If you need to thaw it quickly, you can do so in the microwave.','No','2023-05-31 00:00:00',1,'2023-08-30 19:39:06','2023-08-30 19:39:06'),(3,'Air Fryer Hot Dogs','Making a few hot dogs for a quick meal? Reach for your air fryer! Great for kids’ lunches and easy to upgrade for grownups.','Spray the basket of an air fryer with nonstick spray.\r\nAir fry the hot dogs:\r\nAdd your 4 hot dogs to the air fryer basket, leaving some space between each hot dog. \r\n\r\nAir fry at 350˚F for 5 minutes. When the hot dogs are done, they should be glistening hot and slightly browned in spots.\r\nToast the buns in the air fryer: \r\nRemove hot dogs from air fryer basket using tongs or a fork and place each hot dog in a bun. \r\nPlace 2 assembled hot dogs in the air fryer and cook for 90 seconds to toast the bun. The finished toasted bun will have a light toast on it and be slightly crispy on the edges.\r\n\r\nIf you are adding cheese to your hot dogs—add a slice of cheese in the middle each bun and top with hot dog. Air fry for 90 seconds and cheese will be melted, and the buns toasted.\r\n\r\nRepeat with remaining hot dogs.\r\nTo serve: \r\nServe hot dogs immediately topped with your favorite hot dog toppings including mustard, ketchup, and pickles. ','Yes','2022-06-16 00:00:00',2,'2023-08-30 19:47:43','2023-08-30 19:47:43');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-30 20:38:27
