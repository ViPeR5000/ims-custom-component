"""Consts for the OpenWeatherMap."""
from __future__ import annotations
from datetime import timedelta

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.components.weather import (
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_EXCEPTIONAL,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
    ATTR_CONDITION_WINDY_VARIANT,
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    ATTR_FORECAST_PRESSURE,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
)
from homeassistant.const import (
    DEGREE,
    LENGTH_MILLIMETERS,
    PERCENTAGE,
    PRESSURE_HPA,
    SPEED_METERS_PER_SECOND,
    TEMP_CELSIUS,
    UV_INDEX,
    Platform,
)

DOMAIN = "ims"
DEFAULT_NAME = "IMSWeather"
DEFAULT_LANGUAGE = "en"
DEFAULT_SCAN_INTERVAL = 10
DEFAULT_IMAGE_PATH = "/tmp"
ATTRIBUTION = "Data provided by Israel Meteorological Service"
MANUFACTURER = "IMS"
CONF_UPDATE_INTERVAL = "update_interval"
CONF_CITY = "city"
CONF_LANGUAGE = "language"
CONF_MODE = "mode"
CONF_IMAGES_PATH = "images_path"
CONFIG_FLOW_VERSION = 2
ENTRY_NAME = "name"
ENTRY_WEATHER_COORDINATOR = "weather_coordinator"
ATTR_API_PRECIPITATION = "precipitation"
ATTR_API_FORECAST_TIME = "forecast_time"
ATTR_API_DEW_POINT = "due_point_Temp"
ATTR_API_TEMPERATURE = "temperature"
ATTR_API_FEELS_LIKE_TEMPERATURE = "feels_like"
ATTR_API_WIND_SPEED = "wind_speed"
ATTR_API_WIND_BEARING = "wind_direction_id"
ATTR_API_WIND_CHILL = "wind_chill"
ATTR_API_RELATIVE_HUMIDITY = "relative_humidity"
ATTR_API_RAIN = "rain"
ATTR_API_UV_INDEX = "u_v_index"
ATTR_API_UV_LEVEL = "u_v_level"
ATTR_API_WEATHER_CODE = "weather_code"
ATTR_API_HEAT_STRESS = "heat_stress"
ATTR_API_HEAT_STRESS_LEVEL = "heat_stress_level"
ATTR_API_FORECAST_DATE = "forecast_date"
ATTR_API_MAXIMUM_TEMPERATURE = "maximum_temperature"
ATTR_API_MINIMUM_TEMPERATURE = "minimum_temperature"
ATTR_API_MAXIMUM_UV_INDEX = "maximum_uvi"
UPDATE_LISTENER = "update_listener"

FORECAST_MODE_HOURLY = "hourly"
FORECAST_MODE_DAILY = "daily"

LANGUAGES = ["en", "he"]

WIND_DIRECTIONS = {
    "1": "180",
    "2": "203",
    "3": "225",
    "4": "248",
    "5": "270",
    "6": "293",
    "7": "315",
    "8": "338",
    "9": "360",
    "10": "23",
    "11": "45",
    "12": "68",
    "13": "90",
    "14": "113",
    "15": "135",
    "16": "158",
    "17": "180"
}

WEATHER_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=ATTR_API_DEW_POINT,
        name="Dew Point Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_TEMPERATURE,
        name="Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_RELATIVE_HUMIDITY,
        name="Relative humidity",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_FEELS_LIKE_TEMPERATURE,
        name="Feels like temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_SPEED,
        name="Wind speed",
        native_unit_of_measurement=SPEED_METERS_PER_SECOND,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_BEARING,
        name="Wind bearing",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_CHILL,
        name="Wind chill",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_RAIN,
        name="Rain",
        native_unit_of_measurement=LENGTH_MILLIMETERS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_UV_INDEX,
        name="UV Index",
        native_unit_of_measurement=UV_INDEX,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_UV_LEVEL,
        name="UV level",
        native_unit_of_measurement=UV_INDEX,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_CONDITION,
        name="Condition",
    ),
    SensorEntityDescription(
        key=ATTR_API_WEATHER_CODE,
        name="Weather Code",
    ),
    SensorEntityDescription(
        key=ATTR_API_HEAT_STRESS,
        name="Heat Stress",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_HEAT_STRESS_LEVEL,
        name="Heat Stress Level",
        state_class=SensorStateClass.MEASUREMENT,
    ),
)
FORECAST_HOURLY_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=ATTR_FORECAST_TEMP,
        name="Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key=ATTR_API_WEATHER_CODE,
        name="Weather Code",
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_TIME,
        name="Forecast Time",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
)
FORECAST_DAILY_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=ATTR_API_MAXIMUM_TEMPERATURE,
        name="Maximum temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key=ATTR_API_MINIMUM_TEMPERATURE,
        name="Minimum temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key=ATTR_API_MAXIMUM_UV_INDEX,
        name="Miximum UV index",
        native_unit_of_measurement=UV_INDEX
    ),
    SensorEntityDescription(
        key=ATTR_API_WEATHER_CODE,
        name="Weather Code",
    ),
    SensorEntityDescription(
        key=ATTR_API_FORECAST_DATE,
        name="Forecast date",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
)