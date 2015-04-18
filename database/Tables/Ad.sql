DROP TABLE IF EXISTS Ad;

CREATE TABLE Ad (
	AdID int auto_increment not NULL primary key,
	AdvertiserID int not NULL,
	StartDate datetime not NULL,
	EndDate datetime not NULL,
	HTML varchar(2000) not NULL,
	CreatedDate datetime not NULL);