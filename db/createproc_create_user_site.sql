DELIMITER $$
USE weather_records $$
DROP PROCEDURE IF EXISTS create_user_site $$

CREATE PROCEDURE create_user_site(
    id INT,
    description VARCHAR(50)
)
BEGIN
INSERT INTO basic_records (
    id,
    description
)
VALUES (
    id,
    description
);

END $$

DELIMITER ;