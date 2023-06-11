DELIMITER $$
USE weather_records $$
DROP PROCEDURE IF EXISTS create_basic_record $$

CREATE PROCEDURE create_basic_record(
    year INT,
    month TINYINT,
    day TINYINT,
    precip DECIMAL(5,2)
)
BEGIN
INSERT INTO basic_records (
    year,
    month,
    day,
    precip
)
VALUES (
    year,
    month,
    day,
    precip
);

END $$

DELIMITER ;