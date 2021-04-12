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
                               threshold_distance: int) -> None:
    """
    Procedure of activation switch with distance information.
    
    Args:
        max_distance[int]: max distance sensor detects.
        threshold_distance [int]: threshold distance to activate switch.
        
    Return: None, program execution shoud never finish.
    """

    ## -- START FUNCTION VARIABLES --
    switch_state = False
    distance = 0
    state_queue = [False]*5
    sensor_1_status = False
    sensor_2_status = False
    
    
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

    
    while True:
        
        ## -- CHECK SENSORs STATUS --
        sensor_1_status = check_distance_sensor(distance_sensor_1)
        time.sleep(0.01)
        sensor_2_status = check_distance_sensor(distance_sensor_2)
        
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
        print(state_queue)
        
        ## -- UPDATE [switch_state] --
        if (not switch_state) and (all(state_queue)):
            print("Switch ON")
            switch_state = True
            switch.off()
        
        if (switch_state) and (not any(state_queue)):
            print("Switch OFF")
            switch_state = False
            switch.on()
            
        
        time.sleep(0.25)
