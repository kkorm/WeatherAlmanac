DELIMITER $$
USE weather_records $$
DROP PROCEDURE IF EXISTS create_noaa_record $$

CREATE PROCEDURE create_noaa_record(
    day TINYINT,
    month TINYINT,
    year INT,
    office_id VARCHAR(10),
    station_id VARCHAR(10),
    temp_max SMALLINT,
    temp_min SMALLINT,
    temp_avg SMALLINT,
    temp_hdd SMALLINT,
    temp_cdd SMALLINT,
    prec_water DECIMAL(5,2),
    prec_snow DECIMAL(5.2),
    prec_snow_depth TINYINT,
    wind_2minspeed_avg DECIMAL(5,2),
    wind_2minspeed_max SMALLINT,
    wind_dir TINYINT UNSIGNED,
    weather_types VARCHAR(10),
    wind_peak_speed TINYINT UNSIGNED,
    wind_peak_dir SMALLINT
)
BEGIN
    INSERT INTO noaa_records (
        day,
        month,
        year,
        office_id,
        station_id,
        temp_max,
        temp_min,
        temp_avg,
        temp_hdd,
        temp_cdd,
        prec_water,
        prec_snow,
        prec_snow_depth,
        wind_2minspeed_avg,
        wind_2minspeed_max,
        wind_dir,
        weather_types,
        wind_peak_speed,
        wind_peak_dir
    )
    VALUES (
        day,
        month,
        year,
        office_id,
        station_id,
        temp_max,
        temp_min,
        temp_avg,
        temp_hdd,
        temp_cdd,
        prec_water,
        prec_snow,
        prec_snow_depth,
        wind_2minspeed_avg,
        wind_2minspeed_max,
        wind_dir,
        weather_types,
        wind_peak_speed,
        wind_peak_dir
    ) ;
END  $$

DELIMITER ;