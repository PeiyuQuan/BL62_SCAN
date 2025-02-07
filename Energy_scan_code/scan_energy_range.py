import math
import epics
import time
import numpy as np
import random
import matplotlib.pyplot as plt


def scan_energy_1_range(start, step, points, file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC01:B.VAL")
    linear_Base = epics.PV("BL62:DMC01:A.VAL")
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    n = []
    k = []
    x = a
    y = b
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes', wait=True)
    init_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    with open(file_name, "a") as f:
        f.write("#\toff_sample\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
        for i in range(0, points):
            mono = start + step * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(i, len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + " ~ " + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        f.write("-----------------------------------------------------------------------------------------------\n")
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous', wait=True)
    linear_Base.put(0, wait=True)
    plt.show()


def scan_energy_2_ranges(start, step, points, start1, step1, points1, file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC01:B.VAL")
    linear_Base = epics.PV("BL62:DMC01:A.VAL")
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    n = []
    k = []
    x = a
    y = b
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes', wait=True)
    init_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    with open(file_name, "a") as f:
        f.write("#\toff_sample\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
        for i in range(0, points):
            mono = start + step * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(i, len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        for i in range(0, points1):
            mono = start1 + step1 * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + points + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range((i + points), len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        f.write("----------------------------------------------------------------------------------------------\n")
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous', wait=True)
    linear_Base.put(0, wait=True)
    plt.show()


def scan_energy_3_ranges(start, step, points, start1, step1, points1, start2, step2, points2, file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC01:B.VAL")
    linear_Base = epics.PV("BL62:DMC01:A.VAL")
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    n = []
    k = []
    x = a
    y = b
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes', wait=True)
    init_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    with open(file_name, "a") as f:
        f.write("#\toff_sample\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
        for i in range(0, points):
            mono = start + step * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(i, len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        for i in range(0, points1):
            mono = start1 + step1 * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + points + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range((i + points), len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        for i in range(0, points2):
            mono = start2 + step2 * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1 + points + points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range((i + points + points1), len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        f.write("-------------------------------------------------------------------------------------------------\n")
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous', wait=True)
    linear_Base.put(0, wait=True)
    plt.show()

def scan_energy_4_ranges(start, step, points, start1, step1, points1, start2, step2, points2, start3, step3, points3,
                         file_name, exposure_time):
    hc = 12398.4244
    dspacing = 3.1356
    crystal_1 = epics.PV("BL62:DMC01:B.VAL")
    linear_Base = epics.PV("BL62:DMC01:A.VAL")
    a = []
    b = []
    c = []
    d = []
    e = []
    h = []
    n = []
    k = []
    x = a
    y = b
    epics.PV("BL62:ANDOR3:cam1:AcquireTime").put(exposure_time, wait=True)
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Fixed', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:EnableCallbacks").put('Enable', wait=True)
    epics.PV("BL62:ANDOR3:ROIStat1:1:Use").put('Yes', wait=True)
    init_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True)
    with open(file_name, "a") as f:
        f.write("#\toff_sample\timage_name\timage_num\tenergy\tintensity\texposure_time\tangle\n")
        for i in range(0, points):
            mono = start + step * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range(i, len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        for i in range(0, points1):
            mono = start1 + step1 * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + points + 1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range((i + points), len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        for i in range(0, points2):
            mono = start2 + step2 * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1 + points + points1)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range((i + points + points1), len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        for i in range(0, points3):
            mono = start3 + step3 * i
            m1 = 2 * dspacing * mono
            crystal = math.asin(hc / m1)
            angle_crystal = float(180.0 * crystal / math.pi)
            crystal_1.put(angle_crystal, wait=True)
            linear_Base.put(0, wait=True)
            n.append(i + 1 + points + points1 + points2)
            a.append(mono)
            c.append(epics.PV("BL62:ANDOR3:cam1:AcquireTime_RBV").get(as_numpy=True))
            d.append(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True))
            e.append(epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True))
            epics.PV("BL62:ANDOR3:cam1:Acquire").put('Acquire', wait=True)
            time.sleep(0.5)
            b.append(epics.PV("BL62:ANDOR3:ROIStat1:1:Total_RBV").get(as_numpy=True))
            h.append(epics.PV("BL62:DMC01:D.RBV").get(as_numpy=True))
            k.append(epics.PV("BL62:DMC01:A.RBV").get(as_numpy=True))
            for m in range((i + points + points1 + points2), len(a)):
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(n[m], k[m], d[m], e[m], a[m], b[m], c[m],
                                                                  h[m]))
                fina_image_number = epics.PV("BL62:ANDOR3:TIFF1:FileNumber_RBV").get(as_numpy=True) - 1
                plt.plot(x, y, marker="o", ms=6)
                plt.pause(0.05)
                plt.title(epics.PV("BL62:ANDOR3:TIFF1:FileName_RBV").get(as_string=True) + " " + "scan #" +
                          str(init_image_number) + "~" + str(fina_image_number))
                plt.xlabel('energy')
                plt.ylabel('Intensity from camera ROI')
        f.write("--------------------------------------------------------------------------------------------------\n")
    epics.PV("BL62:ANDOR3:TIFF1:EnableCallbacks").put('Disable', wait=True)
    epics.PV("BL62:ANDOR3:cam1:ImageMode").put('Continuous', wait=True)
    linear_Base.put(0, wait=True)
    plt.show()
                             
