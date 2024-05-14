import math
import epics
import time
import numpy as np
import matplotlib.pyplot as plt

def scan_rotation_stage(start, step, points, mono, left_center,right_center,file_name,Image_Num,bg_exp_time,exp_time):
    hc = 12398.4244
    dspacing = 3.1356
    m1 = 2*dspacing*mono
    crystal = math.asin(hc/m1)
    angle_crystal=float(180.0*crystal/math.pi)
    crystal_1 = epics.PV("BL62:DMC02:A.VAL")
    crystal_1.put(angle_crystal,wait=True)
    Linear_Base = epics.PV("BL62:DMC01:A.VAL")
    rotation_stage = epics.PV("BL62:DMC01:D.VAL")
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    h=[]
    n=[]
#    J=[]
    k=[]
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed',wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable',wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes',wait=True)
    init_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    x1=[]
    x2=[]
    x3=[]
    x4=[]
    x5=[]
    x6=[]
    x7=[]
    x2.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
    Linear_Base.put(left_center, wait=True)
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(Image_Num,wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(bg_exp_time, as_numpy=True)
    epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
    f = open(file_name, "a")
    f.write("image_name\timage_number\tlinear_position\tImage_Num\tintensity\texposure_time\tenergy\n")
    x1.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
    x3.append(left_center)
    x4.append(epics.PV("BL62:ANDOR3:cam1:NumImages_RBV").get(as_numpy=True))
    x5.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
    x6.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
    x7.append(mono)
    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1[0], x2[0], x3[0], x4[0], x5[0],x6[0],x7[0]))
    x2.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
    Linear_Base.put(right_center, wait=True)
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(Image_Num,wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(bg_exp_time, as_numpy=True)
    epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
    f = open(file_name, "a")
    f.write("image_name\timage_number\tlinear_position\tImage_Num\tintensity\texposure_time\tenergy\n")
    x1.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
    x3.append(left_center)
    x4.append(epics.PV("BL62:ANDOR3:cam1:NumImages_RBV").get(as_numpy=True))
    x5.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
    x6.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
    x7.append(mono)
    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1[1], x2[1], x3[1], x4[1], x5[1],x6[1],x7[1]))
    Linear_Base.put(0, wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exp_time, as_numpy=True)
    f = open(file_name, "a")
    f.write("#\timage_name\timage_number\tI1(amps)\trotation_angle\tintensity\texposure_time\tenergy\n")
    for i in range(0, points):
        stage_position = start + step*i
        a.append(stage_position)
        n.append(i+1)
        rotation_stage.put(stage_position, wait=True)
        c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
        epics.PV("BL62:ANDOR3:cam1:NumImages").put(1,wait=True)
        d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
        e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
        epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
        time.sleep(.5)
#        J.append(epics.PV("BL62:K6487:1:Measure").get(as_numpy=True))
        b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
        h.append(mono)
        for m in range(i,len(a)):
            f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], d[m], e[m], J[m],a[m], b[m], c[m], h[m]))    
    fina_image_number= epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)-1
    x=a
    y=b
    plt.plot(x,y,marker="o")
    plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True)+" "+"scan #"+str(init_image_number)+"~"+str(fina_image_number))
    plt.xlabel('rotation_angle')
    plt.ylabel('Intensity from camera ROI')
    plt.show()
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable',wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous',wait=True)
    rotation_stage.put(0, wait=True)
    Linear_Base.put(left_center, wait=True)
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(Image_Num,wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(bg_exp_time, as_numpy=True)
    epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
    f = open(file_name, "a")
    f.write("image_name\timage_number\tlinear_position\tImage_Num\tintensity\texposure_time\tenergy\n")
    x1.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
    x3.append(left_center)
    x4.append(epics.PV("BL62:ANDOR3:cam1:NumImages_RBV").get(as_numpy=True))
    x5.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
    x6.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
    x7.append(mono)
    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1[2], x2[2], x3[2], x4[2], x5[2],x6[2],x7[2]))
    x2.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
    Linear_Base.put(right_center, wait=True)
    epics.PV("BL62:ANDOR3:cam1:NumImages").put(Image_Num,wait=True)
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(bg_exp_time, as_numpy=True)
    epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire',wait=True)
    f = open(file_name, "a")
    f.write("image_name\timage_number\tlinear_position\tImage_Num\tintensity\texposure_time\tenergy\n")
    x1.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
    x3.append(left_center)
    x4.append(epics.PV("BL62:ANDOR3:cam1:NumImages_RBV").get(as_numpy=True))
    x5.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
    x6.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
    x7.append(mono)
    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(x1[3], x2[3], x3[3], x4[3], x5[3],x6[3],x7[3]))
    Linear_Base.put(0, wait=True)
