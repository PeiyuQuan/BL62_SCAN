import math
import epics
import time
import numpy as np
import random
import matplotlib.pyplot as plt

def set_zero():
    epics.PV("BL62:DMC01:A.SET").put('Set',wait=True)
    time.sleep(0.5)
    epics.PV("BL62:DMC01:A.VAL").put(0, wait=True)
    epics.PV("BL62:DMC01:A.SET").put('Use',wait=True)
    time.sleep(0.5)

