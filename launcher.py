"""
Program Main Launcher

"""

import os
import sys
import configparser

if __name__ == "__main__":

    import argparse


    ## -- LOCAL IMPORTS --
    from src.modules.arguments_handler import get_arguments
    from src.modules.runner_handler import (
        run_proximity_switch,
        run_test_sensors
    )

    ## -- LOAD CONFIG FILE --
    CONFIG = configparser.ConfigParser()
    CONFIG.read('config.ini')
    ENV = 'DEFAULT'

    ## -- GET ARGUMENTS --
    ARGS = get_arguments(CONFIG)

    FUNCTION = ARGS.function

    if FUNCTION == 1:
        run_proximity_switch(CONFIG[ENV], ARGS)

    elif FUNCTION == 2:
        run_test_sensors(CONFIG[ENV], ARGS)

    else:
        print("Add --function [func_num] with a valid number of function to be use.")


    print("\n -- Finish! --")
