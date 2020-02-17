CREATE DATABASE test;
use test

create table users (
	id int AUTO_INCREMENT,
	name varchar(50) NOT NULL, 
	address varchar(100),
	tel varchar(20),
	mail varchar(100),
	PRIMARY KEY(id)
);

GRANT ALL PRIVILEGES ON test.* TO 'user'@'%';

FLUSH PRIVILEGES;

