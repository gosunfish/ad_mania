DROP TABLE IF EXISTS Affiliate;

CREATE TABLE Affiliate (
	ID int auto_increment not NULL primary key,
	AffiliateName varchar(50) not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
  
ALTER TABLE Affiliate AUTO_INCREMENT = 0;

INSERT Affiliate (AffiliateName) values ('CJ');
INSERT Affiliate (AffiliateName) values ('ShareASale');