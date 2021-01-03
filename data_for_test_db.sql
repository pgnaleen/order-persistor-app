--CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON * . * TO 'root'@'localhost';
FLUSH PRIVILEGES;

create database ase_assignment;

use ase_assignment;
CREATE TABLE Catalog(
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
item_name VARCHAR(30),
price FLOAT(12) UNSIGNED,
count INT(5) UNSIGNED,
updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO Catalog VALUES (null,'ToothBrush', 145.50, 20, null);
INSERT INTO Catalog VALUES (null,'soap', 45.50, 220, null);
INSERT INTO Catalog VALUES (null,'Men Wallet', 3345.50, 10, null);
