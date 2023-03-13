USE weather_records;

CREATE TABLE IF NOT EXISTS user_records (
    id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    day TINYINT NOT NULL,
    office_id VARCHAR(10) NOT NULL,
    station_id VARCHAR(10) NOT NULL,
    prec_water DECIMAL(5,2),
    prec_snow DECIMAL(5.2),
    prec_type VARCHAR(50)
)