import math
import epics
import time
import numpy as np
import matplotlib.pyplot as plt


def scan_rotation_stage(start, step, points, mono, off_sample, file_name, image_Num, bg_exp_time, exp_time):
    hc = 12398.4244
    dspacing = 3.1356
    m1 = 2 * dspacing * mono
    crystal = math.asin(hc / m1)
    angle_crystal = float(180.0 * crystal / math.pi)
    crystal_1 = epics.PV("BL62:DMC01:B.VAL")
    crystal_1.put(angle_crystal, wait=True)
    linear_Base = epics.PV("BL62:DMC01:A.VAL")
    rotation_stage = epics.PV("BL62:DMC01:D.VAL")
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    n = []
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed', wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes', wait=True)
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    linear_Base.put(off_sample, wait=True)
    x2.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(image_Num, wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(bg_exp_time, wait=True)
    time.sleep(0.2)
    epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
    with open(file_name, "a") as f:
        f.write("image_name\timage_number\toff_sample\tImage_Num\tintensity\texposure_time\tenergy\n")
        x1.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
        x3.append(off_sample)
        x4.append(epics.PV("BL62:ANDOR3:cam1:NumImages_RBV").get(as_numpy=True))
        x5.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
        x6.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
        x7.append(mono)
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1[0], x2[0], x3[0], x4[0], x5[0], x6[0], x7[0]))
    linear_Base.put(0, wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exp_time, wait=True)
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(1, wait=True)
    f = open(file_name, "a")
    f.write("#\timage_name\timage_number\trotation_angle\tintensity\texposure_time\tenergy\n")
    for i in range(0, points):
        stage_position = start + step * i
        a.append(stage_position)
        n.append(i + 1)
        rotation_stage.put(stage_position, wait=True)
        c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
        b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(mono)
        for m in range(i, len(a)):
            f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    rotation_stage.put(0, wait=True)
    x2.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
    linear_Base.put(off_sample, wait=True)
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(image_Num, wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(bg_exp_time, wait=True)
    time.sleep(0.2)
    epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
    with open(file_name, "a") as f:
        f.write("image_name\timage_number\toff_sample\tImage_Num\tintensity\texposure_time\tenergy\n")
        x1.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
        x3.append(off_sample)
        x4.append(epics.PV("BL62:ANDOR3:cam1:NumImages_RBV").get(as_numpy=True))
        x5.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
        x6.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
        x7.append(mono)
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1[1], x2[1], x3[1], x4[1], x5[1], x6[1], x7[1]))
        f.write("--------------------------------------------------------------------------------------------------\n")
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(1, wait=True)
    linear_Base.put(0, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous', wait=True)
    
