"""
Input Arguments Handler Module.
"""


from configparser import ConfigParser
from argparse import (
    ArgumentParser,
    Namespace
)


def get_arguments(config_init: ConfigParser,
                  env: str='DEFAULT') -> Namespace:
    """
    Get ArgParser input arguments.
    Args:
        config_init [ConfigParser]: Initailization configuration file.
        env [str]: Name of environment from where to load initialization variables.

    Return:
        [Namespace] with arguments.
    """


    parser = ArgumentParser()

    ## -- [function] ARGUMENT --
    parser.add_argument('--function', type=int, required=False,
                        default=config_init[env]['FUNCTION'],
                        help="Number of function too execute.")


    if env == 'DEFAULT':
        ## -- [max_distance] ARGUMENT --
        parser.add_argument('--max_distance', type=int, required=False,
                            default=config_init[env].getfloat('MAX_DISTANCE'),
                            help="Distance to activate switch.")


        ## -- [threshold_distance] ARGUMENT --
        parser.add_argument('--threshold_distance', type=int, required=False,
                            default=config_init[env].getfloat('THRESHOLD_DISTANCE'),
                            help="Distance to activate switch.")

        ## -- [max_time_on] ARGUMENT --
        parser.add_argument('--max_time_on', type=int, required=False,
                            default=config_init[env].getfloat('MAX_TIME_ON'),
                            help="Max time switch ON")



    return parser.parse_args()
