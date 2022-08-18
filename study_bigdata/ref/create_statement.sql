CREATE DATABASE `crawling_data`;

CREATE TABLE `tourist_sumary` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `nat_cd` int NOT NULL,
  `nat_name` varchar(45) NOT NULL,
  `visit_cnt` int NOT NULL,
  `yyyymm` char(6) NOT NULL,
  PRIMARY KEY (`idx`)
);

