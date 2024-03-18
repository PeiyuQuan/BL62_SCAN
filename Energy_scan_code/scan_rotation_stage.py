import math
import epics
import time
import numpy as np
import matplotlib.pyplot as plt

def scan_rotation_stage(start, step, points, mono, file_name):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:iXI4:m1.VAL")
    m1 = 2*dspacing*mono
    crystal = math.asin(hc/m1)
    angle_crystal=int((180.0*crystal/math.pi) * 1000)/1000.0
    crystal_1.put(angle_crystal, wait=True)
    rotation_stage = epics.PV("BL62:iXI4:m4.VAL")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("BL62:ANDOR3:HDF1:FileNumber_RBV").get(as_numpy=True)
    for i in range(0, points):
        stage_position = start + step*i
        a.append(stage_position)
        n.append(i+1)
        rotation_stage.put(stage_position, wait=True)
        c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
        d.append(epics.PV("BL62:ANDOR3:HDF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("BL62:ANDOR3:HDF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
        time.sleep(.5)
        b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(mono)
    f = open(file_name, "a")
    f.write("#\timage_name\timage_number\trotation_angle\tintensity\texposure_time\renergy\n")
    for m in range(0,len(a)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], a[m], b[m], c[m], h[m]))
    fina_image_number= epics.PV("BL62:ANDOR3:HDF1:FileNumber_RBV").get(as_numpy=True)-1
    time.sleep(1)
    x=a
    y=b
    plt.plot(x,y,marker="o", ms=6)
    plt.title(epics.PV("BL62:ANDOR3:HDF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('rotation_angle')
    plt.ylabel('Intensity from camera ROI')
    plt.show()
    rotation_stage.put(0, wait=True)

