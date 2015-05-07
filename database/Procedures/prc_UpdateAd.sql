DELIMITER ;;
DROP PROCEDURE IF EXISTS prc_UpdateAd;;

CREATE PROCEDURE prc_UpdateAd (
	paramAdID INT, 
	paramAdvertiserID INT, 
	paramStartDate varchar(50), 
	paramEndDate varchar(50), 
	paramHTML varchar(2000))
BEGIN
	DECLARE a,b INT;
	IF paramStartDate = 'None' THEN SET paramStartDate = NULL; END IF;
	IF paramEndDate = 'None' THEN SET paramEndDate = NULL; END IF;

set a = cast(rand() * 100000 as unsigned);
set b = cast(rand() * 100000 as unsigned);
INSERT Ad (AdID, AdvertiserID, StartDate, EndDate, HTML)
VALUES (a,b,'2010-01-01','2020-01-01','HTML');
	IF EXISTS (SELECT 1	FROM Ad WHERE AdID = paramAdID AND AdvertiserID = paramAdvertiserID LIMIT 1) THEN
		UPDATE Ad
		SET StartDate = coalesce(paramStartDate, '1900-01-01'),
			EndDate = coalesce(paramEndDate, '2999-12-31'),
			HTML = paramHTML
		WHERE AdID = paramAdID AND AdvertiserID = paramAdvertiserID;
	ELSE
		INSERT Ad (
			AdID, 
			AdvertiserID, 
			StartDate, 
			EndDate, 
			HTML)
		VALUES (
			paramAdID, 
			paramAdvertiserID, 
			coalesce(paramStartDate, '1900-01-01'), 
			coalesce(paramEndDate, '2999-12-31'),
			paramHTML);
	END IF;
END;;

GRANT EXECUTE ON PROCEDURE AdMania.prc_UpdateAd to 'adservicer'@'%';;

call prc_UpdateAd(123213,3213213,'None','None','html');
select * from Ad;


