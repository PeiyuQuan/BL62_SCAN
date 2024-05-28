import math
import epics
import time
import numpy as np
import random
import matplotlib.pyplot as plt

def scan_energy_1_range(start, step, points, file_name, off_sample,exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:A.VAL")
#    Linear_Base = epics.PV("BL62:DMC01:A.VAL")
    Linear_Base = epics.PV("BL62:DMC01:A.TWV")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
#    J=[]
    k=[]
    data=[]
    bg=[]
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    f = open(file_name, "a")
#    f.write("#\toff_sample\timage_name\timage_num\tenergy\tI1(amps)\tintensity\texposure_time\tangle\n")    
    f.write("#\tabsolute_position\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for i in range(0, points):
        if i%2==0:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
        if i%2==1:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m]))
    f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
    fina_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)-1
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous',wait=True)
    x=a[0::2]
#    y=b
    y=data
    plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.scatter(x,y,marker="o", ms=6)
    plt.show()
    if points%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    print("The scan is Done!")

def scan_energy_2_ranges(start, step, points, start1, step1, points1, off_sample,file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:A.VAL")
#    Linear_Base = epics.PV("BL62:DMC01:A.VAL")
    Linear_Base = epics.PV("BL62:DMC01:A.TWV")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
#    J=[]
    k=[]
#    data=[]
#    bg=[]
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    f = open(file_name, "a")
#    f.write("#\toff_sample\timage_name\timage_num\tenergy\tI1(amps)\tintensity\texposure_time\tangle\n")
    f.write("#\tabsolute_position\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for i in range(0, points):
        if i%2==0:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
        if i%2==1:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
    if points%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    print("The 1st range is Done!")
    for i in range(0, points1):
        if i%2==0:
            mono = start1 + step1*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
        if i%2==1:
            mono = start1 + step1*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))  
    print("The 2nd range is Done!")
    if points1%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
    fina_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)-1
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous',wait=True)
    x=a[0::2]
#    y=b
    y=data
    plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.scatter(x,y,marker="o", ms=6)
    plt.show()
    print("The scan is Done!")

def scan_energy_3_ranges(start, step, points, start1 , step1, points1, start2, step2, points2, off_sample,file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:A.VAL")
    Linear_Base = epics.PV("BL62:DMC01:A.TWV")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
#    J=[]
    k=[]
#    data=[]
#    bg=[] 
 epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    f = open(file_name, "a")
#    f.write("#\toff_sample\timage_name\timage_num\tenergy\tI1(amps)\tintensity\texposure_time\tangle\n")
    f.write("#\tabsolute_position\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for i in range(0, points):
        if i%2==0:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
        if i%2==1:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))  
    if points%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    print("The 1st range is Done!")
    for i in range(0, points1):
        if i%2==0:
            mono = start1 + step1*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
        if i%2==1:
            mono = start1 + step1*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))  
    print("The 2nd range is Done!")
    if points1%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    for i in range(0, points2):    
        if i%2==0:
            mono = start2 + step2*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
        if i%2==1:
            mono = start2 + step2*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))  
    print("The 3rd range is Done!")
    if points2%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
    fina_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)-1
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous',wait=True)
    x=a[0::2]
#    y=b
    y=data
    plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.scatter(x,y,marker="o", ms=6)
    plt.show()
    print("The scan is Done!")

def scan_energy_4_ranges(start, step, points, start1 , step1, points1, start2, step2, points2, start3 , step3, points3, off_sample,file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC02:A.VAL")
    Linear_Base = epics.PV("BL62:DMC01:A.TWV")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
#    J=[]
    k=[]
#    data=[]
#    bg=[]
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    f = open(file_name, "a")
#    f.write("#\toff_sample\timage_name\timage_num\tenergy\tI1(amps)\tintensity\texposure_time\tangle\n")
    f.write("#\tabsolute_position\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
    for i in range(0, points):
        if i%2==0:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
        if i%2==1:
            mono = start + step*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*i+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m]))  
    if points%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    print("The 1st range is Done!")
    for i in range(0, points1):
        if i%2==0:
            mono = start1 + step1*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
        if i%2==1:
            mono = start1 + step1*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+points+1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m]))  
    print("The 2nd range is Done!")
    if points1%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    for i in range(0, points2):    
        if i%2==0:
            mono = start2 + step2*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m], h[m]))
        if i%2==1:
            mono = start2 + step2*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1+points+points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))                
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m])) 
    print("The 3rd range is Done!")
    if points2%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    for i in range(0, points3):
        if i%2==0:
            mono = start3 + step3*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1+points+points1+points2)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
 #           J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1+points2),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], b[m], c[m], h[m]))
            Linear_Base.put(off_sample, wait=True)
            time.sleep(0.5)
            epics.PV("BL62:DMC01:A.TWR").put(1,wait=True)
            n.append(i+1+points+points1+points2)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1+points2)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m],b[m], c[m], h[m]))
        if i%2==1:
            mono = start3 + step3*i
            m1 = 2*dspacing*mono
            crystal = math.asin(hc/m1)
            angle_crystal=float(180.0*crystal/math.pi)
            crystal_1.put(angle_crystal, wait=True)
            n.append(i+1+points+points1+points2)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1+points2),len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m],b[m], c[m], h[m]))
            epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
            n.append(i+1+points+points1+points2)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
            time.sleep(0.5)
#            J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            data.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(2*(i+points+points1+points2)+1,len(a)):
#                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m],k[m], d[m], e[m], a[m], J[m],b[m], c[m], h[m]))
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m],d[m], e[m], a[m], b[m], c[m], h[m])) 
    print("The 4th range is Done!")
    if points3%2==1:
        epics.PV("BL62:DMC01:A.TWF").put(1,wait=True)
    f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
    fina_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)-1
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous',wait=True)
    x=a[0::2]
#    y=b
    y=data
    plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('energy')
    plt.ylabel('Intensity from camera ROI')
    plt.scatter(x,y,marker="o", ms=6)
    plt.show()
    print("The scan is Done!")
