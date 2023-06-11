USE weather_records;

CREATE TABLE IF NOT EXISTS noaa_records (
    id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    office_id VARCHAR(10) NOT NULL,
    station_id VARCHAR(10) NOT NULL,
    temp_max INT,
    temp_min INT,
    temp_avg INT,
    temp_hdd INT,
    temp_cdd INT,
    prec_water DECIMAL(5,2),
    prec_snow DECIMAL(5.2),
    prec_snow_depth INT,
    wind_2minspeed_avg DECIMAL(5,2),
    wind_2minspeed_max INT,
    wind_dir INT,
    weather_types VARCHAR(10),
    wind_peak_speed INT,
    wind_peak_dir INT
);