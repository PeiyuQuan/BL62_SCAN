import epics

def filter_number(n):
    epics.PV("BL62:E1608_1:Bo1").put("Low", wait=True)
    epics.PV("BL62:E1608_1:Bo2").put("Low", wait=True)
    epics.PV("BL62:E1608_1:Bo3").put("Low", wait=True)
    epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)

    if n < 16:
        if n == 0:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 1:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 2:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 3:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 4:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 5:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 6:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 7:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("In", wait=True)
        elif n == 8:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        elif n == 9:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        elif n == 10:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        elif n == 11:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        elif n == 12:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        elif n == 13:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        elif n == 14:
            epics.PV("BL62:E1608_1:Bd1").put("In", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
        else:
            epics.PV("BL62:E1608_1:Bd1").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd2").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd3").put("Out", wait=True)
            epics.PV("BL62:E1608_1:Bd4").put("Out", wait=True)
    else:
        print("You typed a wrong filter number")

filter_number(sys.argv)
