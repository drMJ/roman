import sys
import numpy as np
import math 
import time
import random
import os
import socket
rootdir = os.path.dirname(os.path.dirname(__file__))
os.sys.path.insert(0, rootdir)
from robot.types import *

urscripts = os.path.join(rootdir, "URScripts")
os.sys.path.insert(0, urscripts)

from robot.URScripts.interface import *

def get_arm_state_test():
    print(f"Running {__file__}::{get_arm_state_test.__name__}()")
    state = State.fromarray(get_arm_state())
    #print(state)
    print("Passed.")

def execute_arm_command_test():
    print(f"Running {__file__}::{execute_arm_command_test.__name__}()")
    cmd = Command()
    state = State.fromarray(execute_arm_command(cmd))
    cmd = Command(target_position=Joints(1,1,1,1,1,1))
    state = State.fromarray(execute_arm_command(cmd))
    #print(state)
    print("Passed.")

def run():
    get_arm_state_test()
    execute_arm_command_test()

#env_test()
if __name__ == '__main__':
    run()