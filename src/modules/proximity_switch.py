"""
Proximity switch control functions

"""


import time
from gpiozero import (
    DistanceSensor,
    LED
)

## -- LOCAL IMPORTS --
from src.modules.utils import queue_add
from src.modules.sensor_handler import check_distance_sensor


def proximity_switch_procedure(max_distance: int,
                               threshold_distance: int,
                               max_time_on: int) -> None:
    """
    Procedure of activation switch with distance information.

    Args:
        max_distance[int]: max distance sensor detects.
        threshold_distance [int]: threshold distance to activate switch.

    Return: None, program execution shoud never finish.
    """

    ## -- START FUNCTION VARIABLES --

    truck_in = False
    ## [truck_in]: Truck start out of sensor range

    switch_state = False
    ## [switch_state]: Indicates that switch has (or not) been activated for the
    ## Truck that is now in the sensor range. Switch is turn OFF after 120 seconds,
    ## and will should not turn on until next Truck

    state_queue = [False]*5
    ## [state_queue]: Consolidation of last 5 distance threshold.

    sensor_1_status = False
    sensor_2_status = False
    ## [sensor_N_status]: Indicates status of conexión of sensor N.

    distance = 0
    ## [distance]: Min Sensor Distance measure

    time_in = 0
    ## [time_in]: Timestamp in which Truck began to be in sensor range

    ## -- START 2 DISTANCE SENSOR --
    distance_sensor_1 = DistanceSensor(echo=17,
                                       trigger=4,
                                       max_distance=max_distance)

    distance_sensor_2 = DistanceSensor(echo=22,
                                       trigger=27,
                                       max_distance=max_distance)

    ## -- START SWITCH --
    switch = LED(13)
    switch.on()
    ## PS: because of conextion to plac, on() function turns OFF switch and
    ## off() turn ON the switch.


    while True:

        ## -- CHECK SENSORs STATUS --
        sensor_1_status = check_distance_sensor(distance_sensor_1)
        time.sleep(0.01)
        sensor_2_status = check_distance_sensor(distance_sensor_2)

        time_now = time.time()


        ## -- GET DISTANCE --
        if sensor_1_status and sensor_2_status:
            distance = min(distance_sensor_1.distance,
                           distance_sensor_2.distance)

        elif sensor_1_status:
            distance = distance_sensor_1.distance

        elif sensor_2_status:
            distance = distance_sensor_2.distance

        else:
            distance = None

        ## -- UPDATE [state_queue] --
        if bool(distance):
            queue_add(state_queue, distance < threshold_distance)
        else:
            queue_add(state_queue, False)

        ## -- UPDATE [truck_in] --
        if not truck_in and all(state_queue):
            truck_in = True
        if truck_in and not any(state_queue):
            truck_in = False

        # print("truck_in ", truck_in)
        # print("switch_state ", switch_state, "-- time_in ", time_in)
        # print("state_queue ", state_queue)
        # print("\n")

        ## -- UPDATE [switch_state] --
        ## TRUCK IN SENSOR RANGE
        if truck_in:

            ## IF SWITCH OFF AND TIME NULL
            if not switch_state and time_in == 0:
                print("Switch ON")
                switch_state = True
                time_in = time.time()
                switch.off()

            elif switch_state:
                time_diff = time_now - time_in

                if (time_diff > max_time_on):
                    switch_state = False
                    print("Timer Pass, Switch off")
                    switch.on()

        ## TRUCK OUT OF SENSOR RANGE
        else:

            ## IF TURN-ON, THEN TURN-OFF
            if switch_state:
                print("Switch OFF")
                switch_state = False
                switch.on()

            time_in = 0


        time.sleep(0.25)
