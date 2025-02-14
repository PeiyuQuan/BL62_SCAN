import PySimpleGUI as sg
from scan_energy_range import scan_energy_1_range
from scan_energy_range import scan_energy_2_ranges
from scan_energy_range import scan_energy_3_ranges
from scan_energy_range import scan_energy_4_ranges
from scan_rotation_stage import scan_rotation_stage


cycle = ['1', '2', '3', '4']

layout1 = [
    [sg.Text("Start1 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start1-'),
     sg.Text("eV")],
    [sg.Text("Step1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step1-'),
     sg.Text("eV")],
    [sg.Text("Points1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points1-'),
     sg.Text("points")],
    [sg.Text("file_name", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-filename-')],
    [sg.Text("off_sample", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-off_sample-'),
     sg.Text("mm")],
    [sg.Text("exposure_time", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-exposure-'),
     sg.Text("s")]
]

layout2 = [
    [sg.Text("Start1 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start21-'),
     sg.Text("eV")],
    [sg.Text("Step1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step21-'), sg.Text("eV")],
    [sg.Text("Points1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points21-'),
     sg.Text("points")],
    [sg.Text("Start2 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start22-'),
     sg.Text("eV")],
    [sg.Text("Step2", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step22-'), sg.Text("eV")],
    [sg.Text("Points2", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points22-'),
     sg.Text("points")],
    [sg.Text("file_name", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-filename2-')],
    [sg.Text("off_sample", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-off_sample2-'),
     sg.Text("mm")],
    [sg.Text("exposure_time", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-exposure2-'),
     sg.Text("s")],
]

layout3 = [
    [sg.Text("Start1 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start31-'),
     sg.Text("eV")],
    [sg.Text("Step1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step31-'), sg.Text("eV")],
    [sg.Text("Points1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points31-'),
     sg.Text("points")],
    [sg.Text("Start2 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start32-'),
     sg.Text("eV")],
    [sg.Text("Step2", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step32-'), sg.Text("eV")],
    [sg.Text("Points2", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points32-'),
     sg.Text("points")],
    [sg.Text("Start3 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start33-'),
     sg.Text("eV")],
    [sg.Text("Step3", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step33-'), sg.Text("eV")],
    [sg.Text("Points3", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points33-'),
     sg.Text("points")],
    [sg.Text("file_name", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-filename3-')],
    [sg.Text("off_sample", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-off_sample3-'),
     sg.Text("mm")],
    [sg.Text("exposure_time", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-exposure3-'),
     sg.Text("s")]
]

layout4 = [
    [sg.Text("Start1 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start41-'),
     sg.Text("eV")],
    [sg.Text("Step1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step41-'), sg.Text("eV")],
    [sg.Text("Points1", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points41-'),
     sg.Text("points")],
    [sg.Text("Start2 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start42-'),
     sg.Text("eV")],
    [sg.Text("Step2", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step42-'), sg.Text("eV")],
    [sg.Text("Points2", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points42-'),
     sg.Text("points")],
    [sg.Text("Start3 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start43-'),
     sg.Text("eV")],
    [sg.Text("Step3", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step43-'), sg.Text("eV")],
    [sg.Text("Points3", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points43-'),
     sg.Text("points")],
    [sg.Text("Start4 energy", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start44-'),
     sg.Text("eV")],
    [sg.Text("Step4", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step44-'),
     sg.Text("eV")],
    [sg.Text("Points4", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points44-'),
     sg.Text("points")],
    [sg.Text("file_name", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-filename4-')],
    [sg.Text("off_sample", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-off_sample4-'),
     sg.Text("mm")],
    [sg.Text("exposure_time", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-exposure4-'),
     sg.Text("s")]
]

layout_E = [
    [sg.Text('Scanning Energy',font=('Calibri',14),expand_x=True,justification='center')],
    [sg.Text('scan energy range'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Text("ranges")],
    [sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'),
    sg.Column(layout3, visible=False, key='-COL3-'), sg.Column(layout4, visible=False, key='-COL4-')],
    [sg.Button('GO'), sg.Button('Close')]
]

layout_S = [
    [sg.Text('Scanning Rotation stage',font=('Calibri',14),expand_x=True,justification='center')],
    [sg.Text("Start_position", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-start5-'),
     sg.Text("eV")],
    [sg.Text("Step", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-step5-'), sg.Text("eV")],
    [sg.Text("Points", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-points5-'),
     sg.Text("points")],
    [sg.Text("Mono", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-mono5-'), sg.Text("eV")],
    [sg.Text("off_sample", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-off_sample5-'),
     sg.Text("mm")],
    [sg.Text("file_name", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-filename5-')],
    [sg.Text("Image_Num", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-image_num5-')],
    [sg.Text("Back_exp_time", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-bg_exp5-'),
     sg.Text("s")],
    [sg.Text("exp_time", size=(13, 1), justification='center'), sg.Input(size=(15, 200), key='-exp5-'), sg.Text("s")],
    [sg.Button('Run'), sg.Button('Exit')]
]

layout = [
    [sg.Button('scan energy', key='-se-'), sg.Button('scan sample', key='-ss-')],
    [sg.Column(layout_S, key='-s-', visible=True), sg.Column(layout_E, key='-e-', visible=False)]
]

window = sg.Window('Scanning Experiments', layout)

layout = 1
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-ss-':
        window['-s-'].update(visible=True)
        window['-e-'].update(visible=False)
    if event == 'Run':
        start = float(values['-start5-'])
        step = float(values['-step5-'])
        points = int(values['-points5-'])
        mono = float(values['-mono5-'])
        off_sample = float(values['-off_sample5-'])
        file_name = values['-filename5-']
        Image_Num = int(values['-image_num5-'])
        bg_exp_time = float(values['-bg_exp5-'])
        exp_time = float(values['-exp5-'])
        scan_rotation_stage(start, step, points, mono, off_sample, file_name, Image_Num, bg_exp_time, exp_time)
    if event == '-se-':
        window['-s-'].update(visible=False)
        window['-e-'].update(visible=True)

    elif event in '1234':
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'GO' and layout == 1:
        start = float(values['-start1-'])
        step = float(values['-step1-'])
        points = int(values['-points1-'])
        file_name = values['-filename-']
        off_sample = float(values['-off_sample-'])
        exposure_time = float(values['-exposure-'])
        scan_energy_1_range( start, step, points, file_name, off_sample, exposure_time)
    
    if event == 'GO' and layout == 2:
        start = float(values['-start21-'])
        step = float(values['-step21-'])
        points = int(values['-points21-'])
        start1 = float(values['-start22-'])
        step1 = float(values['-step22-'])
        points1 = int(values['-points22-'])
        file_name = values['-filename2-']
        off_sample = float(values['-off_sample2-'])
        exposure_time = float(values['-exposure2-'])
        scan_energy_2_ranges(start, step, points, start1, step1, points1, off_sample, file_name, exposure_time)

    if event == 'GO' and layout == 3:
        start = float(values['-start31-'])
        step = float(values['-step31-'])
        points = int(values['-points31-'])
        start1 = float(values['-start32-'])
        step1 = float(values['-step32-'])
        points1 = int(values['-points32-'])
        start2 = float(values['-start33-'])
        step2 = float(values['-step33-'])
        points2 = int(values['-points33-'])
        file_name = values['-filename3-']
        off_sample = float(values['-off_sample3-'])
        exposure_time = float(values['-exposure-'])
        scan_energy_3_ranges(start, step, points, start1, step1, points1, start2, step2, points2, off_sample, file_name,
                             exposure_time)

    if event == 'GO' and layout == 4:
        start = float(values['-start41-'])
        step = float(values['-step41-'])
        points = int(values['-points41-'])
        start1 = float(values['-start42-'])
        step1 = float(values['-step42-'])
        points1 = int(values['-points42-'])
        start2 = float(values['-start43-'])
        step2 = float(values['-step43-'])
        points2 = int(values['-points43-'])
        start3 = float(values['-start44-'])
        step3 = float(values['-step44-'])
        points3 = int(values['-points44-'])
        file_name = values['-filename4-']
        off_sample = float(values['-off_sample4-'])
        exposure_time = float(values['-exposure4-'])
        scan_energy_4_ranges(start, step, points, start1, step1, points1, start2, step2, points2, start3, step3,
                             points3, off_sample, file_name, exposure_time)

window.close()
