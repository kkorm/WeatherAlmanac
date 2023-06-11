USE weather_records;

CREATE TABLE IF NOT EXISTS user_records (
    id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    user_site_id INT NOT NULL,
    prec_water DECIMAL(5,2),
    prec_snow DECIMAL(5.2),
    prec_type VARCHAR(50)
);