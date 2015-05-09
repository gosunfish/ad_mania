DROP TABLE IF EXISTS Ad;

CREATE TABLE Ad (
	ID int auto_increment not NULL primary key,
	AdID int not NULL,
	AdvertiserID int not NULL,
  Category varchar(50) not NULL default '',
	StartDate datetime not NULL default '1900-01-01',
	EndDate datetime not NULL default '2999-12-31',
	HTML varchar(2000) not NULL,
	`DateTimeStamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);