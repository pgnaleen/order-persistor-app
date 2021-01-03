--CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON * . * TO 'root'@'localhost';
FLUSH PRIVILEGES;

create database ase_assignment;

use ase_assignment;
CREATE TABLE Orders(
order_id VARCHAR(10),
user_id VARCHAR(10),
items VARCHAR(1000),
total_price FLOAT(12) UNSIGNED,
updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
