import epics

def filter(0):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(1):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(2):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(3):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)

def filter(4):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(5):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(6):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(7):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("Out", wait=True)
	
def filter(8):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(9):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(10):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(11):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(12):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(13):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(14):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("Out", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
	
def filter(15):
	epics.PV("BL62:E1608_2:Bo1").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd1").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo2").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd2").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo3").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd3").put("In", wait=True)
	epics.PV("BL62:E1608_2:Bo4").put("Low", wait=True)
	epics.PV("BL62:E1608_2:Bd4").put("In", wait=True)
