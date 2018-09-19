#!/usr/bin/env python3
"""
    Purpose:
        Test Function Execution Timer. Allows for the testimg
        of function performance in Time.
    example call:
        @time_function_execution(units='ms', percision=2)
        def some_function(arg1, kwarg2='default'):
            print('Do something you want timed')
            return 'test'

        >>Do something you want timed
        >>Execution Time of func_exec_timer.py->some_function: 0.04 ms
"""

# Python Library Imports
import logging
import time
from wrapt import decorator


def time_function_execution(units='ms', percision=4):
    """
        Purpose:
            Decorator for timing the execution of a python function.
        Args:
            units (string): Time unit of measure to ouput
            percision (int): Percision in decimal places to show
                the output of the time
        Returns:
            decorator (function): function decorating another
                function. Returns a function, which times the
                execution of a function
    """

    @decorator
    def get_function_timing(wrapped, instance, args, kwargs):
        """
            Purpose:
                TIming wrapping function
            Args:
                f (function/method): function being decorated
                instance: pass in self when wraping class method.
                    default is None when wraping function.
                args (Tuple): List of arguments
                kwargs (Dict): Dictionary of named arguments
            Return:
                func_return (Object): Whatever is returned by the
                    wrapped function is passed through the timing
                    function
        """

        func_start = time.time()
        func_return = wrapped(*args, **kwargs)
        func_end = time.time()

        unit_func = {
            'ms': lambda x: x * 1000,
            's': lambda x: x,
            'm': lambda x: x / 60,
            'h': lambda x: x / 3600,
        }

        execution_time = unit_func[units](func_end - func_start)
        func_full_name = '{0}->{1}'.format(
            wrapped.__code__.co_filename, wrapped.__name__
        )
        logging.info(
            'Execution Time of {func}: {exec_time:.{percision}f} '
            '{units}'.format(
                func=func_full_name,
                exec_time=execution_time,
                units=units,
                percision=percision,
            )
        )

        return func_return

    return get_function_timing
