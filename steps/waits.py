from behave import *
import time



@step('I wait for {sec} seconds')
def step_impl(context, sec):
    """
    Waits for 2 seconds during test execution.
    
    Args:
        sec:
        context (behave.runner.Context): Behave context object
    """
    time.sleep(float(sec))
