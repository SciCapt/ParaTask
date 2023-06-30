import time as t
import mcnets as mc
import numpy as np
import random as rn
from os import system
import os
import inspect
import multiprocessing.shared_memory as sm

class Task:
    def __init__(self, targetFunction, functionArgs:list = [], requiredModules:list = []):
        """
        Create a task object that has the information to create/run a file of the given function.

        targetFunction
            - The function name that is to be used for the task
            - Note: all package definitions should not be abreviated unless using the secondary notion for the required modules below.

        functionArgs
            - List of seperate arguments to be placed in the function when ran. 
            - Note: The arguments should be given in the correct amount and order according to the target function

        requiredModules
            - Complete list of the seperate modules required to run the given function
            - Primary Notation: (no abbreviations used in function)
                - requiredModules = ["time", "numpy", "matplotlib.pyplot", ...]
            - Secondary Notation: (allows for abbreviations in function)
                - requiredModules = ["time as t", "numpy as np", ...]
            - NOTE: The notation you should use should reflect how packages are referenced in
              the target function. (i.e. if using time.sleep(), just import "time", but if doing
              something like t.sleep(), you have to write "time as t" instead)
        """

        # Setup task variables
        self.id = id(targetFunction)
        self.func = targetFunction
        self.args = functionArgs
        self.mods = requiredModules

    def __str__(self):
        return f"ID: {self.id}\nFunction: {self.func.__name__}\nArguments: {self.args}\nModules: {self.mods}"
    
    def generate(self):
        """
        Creates the executable file for the given function/task to run from.
        The file is located at \ paratasks \ (function id) \ (function id).py.
        Also generates the shared memory to transfer information from the main
        python end to the task and back
        """

        ## Create executable file for task ##
        # Import modules
        self.mods += ["os"]
        moduleLines = ''
        if self.mods != None:
            for mod in self.mods: # Required modules
                moduleLines += f"import {mod}\n"

        # Setup function
        definition = f"{inspect.getsource(self.func)}"

        # Setup command to run
        command = f"out = {self.func.__name__}("
        if self.args != None:
            for i, arg in enumerate(self.args):
                if i != len(self.args) - 1:
                    command += f"{arg}, "
                else:
                    command += f"{arg}"
        command += ")"

        # Compile to one bit
        self.tempCode = moduleLines + '\n' + definition + '\n' + command

        # Save output to seperate file
        path = f"\paratasks\{self.id}\{self.id}.py"
        fullpath = os.getcwd() + path
        os.makedirs(os.path.dirname(fullpath), exist_ok=True)
        with open(fullpath, "w") as f:
            f.write(self.tempCode)

    def run(self, n:int):
        """
        Runs the given task n # of times. The outputs (if any) are stored along with the file under the names
        id_1, id_2, ... id_n.
        """

        # Function to get outputs when done
        def gather(self, n):
            # Maybe check time for 60% to be done, and wait 2-3 times that much
            pass

        # Load and organize outputs