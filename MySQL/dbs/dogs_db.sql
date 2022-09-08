-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema users_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `users_schema` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema world
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema world
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `world` DEFAULT CHARACTER SET latin1 ;
-- -----------------------------------------------------
-- Schema dogs
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dogs
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dogs` DEFAULT CHARACTER SET utf8mb3 ;
USE `users_schema` ;

-- -----------------------------------------------------
-- Table `users_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

USE `world` ;

-- -----------------------------------------------------
-- Table `world`.`countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `world`.`countries` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `code` CHAR(3) NOT NULL DEFAULT '',
  `name` CHAR(52) NOT NULL DEFAULT '',
  `continent` ENUM('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America') NOT NULL DEFAULT 'Asia',
  `region` CHAR(26) NOT NULL DEFAULT '',
  `surface_area` FLOAT(10,2) NOT NULL DEFAULT '0.00',
  `indep_year` SMALLINT NULL DEFAULT NULL,
  `population` INT NOT NULL DEFAULT '0',
  `life_expectancy` FLOAT(3,1) NULL DEFAULT NULL,
  `gnp` FLOAT(10,2) NULL DEFAULT NULL,
  `gnp_old` FLOAT(10,2) NULL DEFAULT NULL,
  `local_name` CHAR(45) NOT NULL DEFAULT '',
  `government_form` CHAR(45) NOT NULL DEFAULT '',
  `head_of_state` CHAR(60) NULL DEFAULT NULL,
  `capital` INT NULL DEFAULT NULL,
  `code2` CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 240
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `world`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `world`.`cities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` CHAR(35) NOT NULL DEFAULT '',
  `country_code` CHAR(3) NOT NULL DEFAULT '',
  `district` CHAR(20) NOT NULL DEFAULT '',
  `population` INT NOT NULL DEFAULT '0',
  `country_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cities_countries1_idx` (`country_id` ASC) VISIBLE,
  CONSTRAINT `fk_cities_countries1`
    FOREIGN KEY (`country_id`)
    REFERENCES `world`.`countries` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4080
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `world`.`languages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `world`.`languages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `country_code` CHAR(3) NOT NULL DEFAULT '',
  `language` CHAR(30) NOT NULL DEFAULT '',
  `is_official` ENUM('T', 'F') NOT NULL DEFAULT 'F',
  `percentage` FLOAT(4,1) NOT NULL DEFAULT '0.0',
  `country_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_languages_countries_idx` (`country_id` ASC) VISIBLE,
  CONSTRAINT `fk_languages_countries`
    FOREIGN KEY (`country_id`)
    REFERENCES `world`.`countries` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 985
DEFAULT CHARACTER SET = latin1;

USE `dogs` ;

-- -----------------------------------------------------
-- Table `dogs`.`dogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dogs`.`dogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `breed` VARCHAR(45) NULL DEFAULT NULL,
  `color` VARCHAR(45) NULL DEFAULT NULL,
  `age` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `dogs`.`awards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dogs`.`awards` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `dog_id` INT NOT NULL,
  PRIMARY KEY (`id`, `dog_id`),
  INDEX `fk_awards_dogs_idx` (`dog_id` ASC) VISIBLE,
  CONSTRAINT `fk_awards_dogs`
    FOREIGN KEY (`dog_id`)
    REFERENCES `dogs`.`dogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
