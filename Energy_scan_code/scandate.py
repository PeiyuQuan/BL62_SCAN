import PySimpleGUI as sg
from scan_energy_range import scan_energy_1_range 
from scan_energy_range import scan_energy_2_ranges 
from scan_energy_range import scan_energy_3_ranges 
from scan_energy_range import scan_energy_4_ranges 



cycle=['1','2','3','4']

layout1=[
	[sg.Text("Start1 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start1'),sg.Text("eV")],
	[sg.Text("Step1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step1')],
	[sg.Text("Points1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points1')],
	[sg.Text("file_name",size=(13,1),justification='center'),sg.Input(size=(15,200),key='filename')],
	[sg.Text("off_sample",size=(13,1),justification='center'),sg.Input(size=(15,200),key='offsample')],
	[sg.Text("exposure_time",size=(13,1),justification='center'),sg.Input(size=(15,200),key='exposure')],
]

layout2=[
	[sg.Text("Start1 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start1')],
	[sg.Text("Step1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step1')],
	[sg.Text("Points1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points1')],
	[sg.Text("Start2 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start2')],
	[sg.Text("Step2",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step2')],
	[sg.Text("Points2",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points2')],
	[sg.Text("file_name",size=(13,1),justification='center'),sg.Input(size=(15,200),key='filename')],
	[sg.Text("off_sample",size=(13,1),justification='center'),sg.Input(size=(15,200),key='offsample')],
	[sg.Text("exposure_time",size=(13,1),justification='center'),sg.Input(size=(15,200),key='exposure')],
]

layout3=[
	[sg.Text("Start1 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start1')],
	[sg.Text("Step1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step1')],
	[sg.Text("Points1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points1')],
	[sg.Text("Start2 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start2')],
	[sg.Text("Step2",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step2')],
	[sg.Text("Points2",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points2')],
	[sg.Text("Start3 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start3')],
	[sg.Text("Step3",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step3')],
	[sg.Text("Points3",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points3')],
	[sg.Text("file_name",size=(13,1),justification='center'),sg.Input(size=(15,200),key='filename')],
	[sg.Text("off_sample",size=(13,1),justification='center'),sg.Input(size=(15,200),key='offsample')],
	[sg.Text("exposure_time",size=(13,1),justification='center'),sg.Input(size=(15,200),key='exposure')],
]

layout4=[
	[sg.Text("Start1 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start1')],
	[sg.Text("Step1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step1')],
	[sg.Text("Points1",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points1')],
	[sg.Text("Start2 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start2')],
	[sg.Text("Step2",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step2')],
	[sg.Text("Points2",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points2')],
	[sg.Text("Start3 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start3')],
	[sg.Text("Step3",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step3')],
	[sg.Text("Points3",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points3')],
	[sg.Text("Start4 energy",size=(13,1),justification='center'),sg.Input(size=(15,200),key='start4')],
	[sg.Text("Step4",size=(13,1),justification='center'),sg.Input(size=(15,200),key='step4')],
	[sg.Text("Points4",size=(13,1),justification='center'),sg.Input(size=(15,200),key='points4')],
	[sg.Text("file_name",size=(13,1),justification='center'),sg.Input(size=(15,200),key='filename')],
	[sg.Text("off_sample",size=(13,1),justification='center'),sg.Input(size=(15,200),key='offsample')],
	[sg.Text("exposure_time",size=(13,1),justification='center'),sg.Input(size=(15,200),key='exposure')],
]

layout=[
	[sg.Text("Scan Energy", font=("calbri",15),justification='left')],
	[sg.Text('scan energy range'),sg.Button('1'), sg.Button('2'), sg.Button('3'),sg.Button('4')],
	[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), 
	sg.Column(layout3, visible=False, key='-COL3-'),sg.Column(layout4, visible=False, key='-COL4-')],
	[sg.Button('GO'), sg.Button('Exit')]
	]

window=sg.Window('Scanning Experiments',layout)
layout=1
while True:
    event,values = window.read()
    print(event,values)
    
    if event == sg.WIN_CLOSED or event=='Exit':
        break
    elif event in '1234':
        window[f'-COL{layout}-'].update(visible=False)
        layout=int(event)
        window[f'-COL{layout}-'].update(visible=True)
    
    if event=='GO' and layout==1:
        start=float(values['start1'])
        step=float(values['step1'])
        points=int(values['points1'])
        file_name=values['filename']
        off_sample=float(values['offsample'])
        exposure_time=float(values['exposure'])
        scan_energy_1_range(start, step, points, file_name, off_sample,exposure_time)
    
    if event=='GO' and layout==2:
        start=float(values['start1'])
        step=float(values['step1'])
        points=int(values['points1'])
        start1=float(values['start2'])
        step1=float(values['step2'])
        points1=int(values['points2'])
        file_name=values['filename']
        off_sample=float(values['offsample'])
        exposure_time=float(values['exposure'])
        scan_energy_2_ranges(start, step, points, start1, step1, points1, off_sample,file_name, exposure_time)

    if event=='GO'and layout==3:
        start=float(values['start1'])
        step=float(values['step1'])
        points=int(values['points1'])
        start1=float(values['start2'])
        step1=float(values['step2'])
        points1=int(values['points2'])
        start2=float(values['start3'])
        step2=float(values['step3'])
        points2=values['points3']
        file_name=values['filename']
        off_sample=float(values['offsample']0
        exposure_time=float(values['exposure'])
        scan_energy_3_ranges(start, step, points, start1 , step1, points1, start2, step2, points2, off_sample,file_name, exposure_time)
    
    if event=='GO' and layout==4:
        start=float(values['start1'])
        step=float(values['step1'])
        points=int(values['points1'])
        start1=float(values['start2'])
        step1=float(values['step2'])
        points1=int(values['points2'])
        start2=float(values['start3'])
        step2=float(values['step3'])
        points2=int(values['points3'])
        start3=float(values['start4'])
        step3=float(values['step4'])
        points3=int(values['points4'])
        file_name=values['filename']
        off_sample=float(values['offsample'])
        exposure_time=float(values['exposure'])
        scan_energy_4_ranges(start, step, points, start1 , step1, points1, start2, step2, points2, start3 , step3, points3, off_sample,file_name, exposure_time)  
		
window.close()
