"""
Sensor handler
Module contains functions to control and check sensors.
"""

import time
from gpiozero import DistanceSensor


def check_distance_sensor(distance_sensor: DistanceSensor) -> bool:
    """
    Check if distance_sensor [distance_sensor] is connected.

    Args:
        distance_sensor [DistanceSensor]: sensor to check.

    Return:
        [bool] indicating if sensor is connetecd
    """

    with DistanceSensor.ECHO_LOCK:
        # Fire the trigger
        distance_sensor._trigger.pin.state = True
        time.sleep(0.00001)
        distance_sensor._trigger.pin.state = False

        # Wait up to 100ms for the echo pin to rise and fall (35ms is the
        # maximum pulse time, but the pre-rise time is unspecified in the
        # "datasheet"; 100ms seems sufficiently long to conclude something
        # has failed)
        if distance_sensor._echo.wait(0.1):
            return True

        return False


def test_distance_sensors(max_distance: int) -> None:
    """
    Procedure Test distance sensor status.

    Args:
        max_distance[int]: max distance sensor detects.

    Return: None, program execution shoud never finish.
    """

    ## -- START DISTANCE SENSORs --
    distance_sensor_1 = DistanceSensor(echo=17,
                                       trigger=4,
                                       max_distance=max_distance)
    distance_sensor_2 = DistanceSensor(echo=22,
                                       trigger=27,
                                       max_distance=max_distance)

    time.sleep(1)


    while True:

        if check_distance_sensor(distance_sensor_1):
            print("distance sensor_1̣ ", distance_sensor_1.distance)
        else:
            print("sensor 1 NOT CONECTED")

        time.sleep(0.01)
        if check_distance_sensor(distance_sensor_2):
            print("distance sensor_̣2 ", distance_sensor_2.distance)
        else:
            print("sensor 2 NOT CONECTED")


        time.sleep(2)
