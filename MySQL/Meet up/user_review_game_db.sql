-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema user_review_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema user_review_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `user_review_db` DEFAULT CHARACTER SET utf8 ;
USE `user_review_db` ;

-- -----------------------------------------------------
-- Table `user_review_db`.`reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_review_db`.`reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `review_comment` VARCHAR(45) NULL,
  `rating` INT(10) NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_reviews_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_reviews_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_review_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_review_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_review_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `review_id` INT NOT NULL,
  `review_user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `review_id`, `review_user_id`),
  INDEX `fk_users_reviews1_idx` (`review_id` ASC, `review_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_reviews1`
    FOREIGN KEY (`review_id` , `review_user_id`)
    REFERENCES `user_review_db`.`reviews` (`id` , `user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_review_db`.`requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_review_db`.`requests` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `game` VARCHAR(45) NULL,
  `players_req` INT NULL,
  `rating_min` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_requests_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_requests_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `user_review_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
