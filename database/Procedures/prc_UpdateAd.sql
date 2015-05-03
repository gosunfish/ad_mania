DELIMITER ;;

DROP PROCEDURE IF EXISTS prc_UpdateAd;;

CREATE PROCEDURE prc_UpdateAd (
	paramAdID INT, 
	paramAdvertiserID INT, 
	paramStartDate datetime, 
	paramEndDate datetime, 
	paramHTML varchar(2000))
BEGIN
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

