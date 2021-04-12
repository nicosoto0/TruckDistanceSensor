"""
Runner handler module.
Module in charge to start procedures.
"""

from argparse import Namespace
from configparser import SectionProxy

## -- LOCAL IMPORTS --
from src.modules.proximity_switch import proximity_switch_procedure
from src.modules.sensor_handler import test_distance_sensors
#from src.modules.utils import load_json_file

def run_proximity_switch(config: SectionProxy,
                         args: Namespace) -> None:
    """
    Load all necesary variables and execute proximity_switch_procedure().

    Args:
        config[SectionProxy]: program config data.
        args [Namespace]: program arguments data.

    Return: None.
    """

    print("RUNNING proximity_switch_procedure()")

    ## -- LOAD NECESARY ARGUMENTS --
    #json_file = load_json_file(config['CONFIG_JSON_FILE'])
    #print(f"Loaded json file type: {type(json_file)}")


    ## -- RUN PROCEDURE --
    proximity_switch_procedure(args.max_distance,
                               args.threshold_distance)

def run_test_sensors(config: SectionProxy,
                     args: Namespace) -> None:
    """
    run Test distance sensor status.

    Args:
        config[SectionProxy]: program config data.
        args [Namespace]: program arguments data.

    Return: None.
    """
    print("RUNNING test_distance_sensors()")


    test_distance_sensors(args.max_distance)
