-- task 7 is about creatin cities table in the already made hbtn_0d_usa db
-- wil be using create cyane cyane
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES state(id));
