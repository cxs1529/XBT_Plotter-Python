# from xbtFunctions import *

class LauncherClass:
    def __init__(self, code, name):
        self.name = name
        self.code = code

class ProbeClass:
    def __init__(self, coefA, coefB, maxDepth, name, code):
        self.coefA = coefA
        self.coefB = coefB
        self.maxDepth = maxDepth
        self.name = name
        self.code = code

class RecorderClass:
    def __init__(self, name, frequency, code):
        self.name = name
        self.frequency = frequency
        self.code = code


def get_launcher(code):
    if code == 0:
        launcherName = "unknown"
    elif code == 1:
        launcherName = "LM-2A Deck-mounted"
    elif code == 2:
        launcherName = "LM-3A Hand-Held"
    elif code == 3:
        launcherName = "LM-4A Thru-Hull"
    elif code == 10:
        launcherName = "AL-12 TSK Autolauncher (up to 12 Probes)"
    elif code == 20:
        launcherName = "SIO XBT Autolauncher (up to 6 probes)"
    elif code == 30:
        launcherName = "AOML XBT V6 Autolauncher (up to 6 Deep Blue probes)"
    elif code == 31:
        launcherName = "AOML XBT V8.0 Autolauncher (up to 8 Deep Blue probes)"
    elif code == 32:
        launcherName = "AOML XBT V8.1 Autolauncher (up to 8 Deep Blue and Fast Deep probes)"
    elif code == 90:
        launcherName = "CSIRO Devil Autolauncher"
    elif code == 91:
        launcherName = "TURO/CSIRO Quoll Autolauncher"
    elif code == 100:
        launcherName = "MFSTEP Autolauncher (Mediterranean)"
    elif code == 255:
        launcherName = "Missing"

    return launcherName


def get_probe(code):
    probe = ProbeClass(-99.9, -99.9, -999, "unknown",code)

    if code == 1:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 460
        probe.name = "Sippican T-4"
    elif code == 2:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 460
        probe.name = "Sippican T-4"
    elif code == 11:
        probe.coefA = 6.828
        probe.coefB = -1.82
        probe.maxDepth = 1830
        probe.name = "Sippican T-5"
    elif code == 21:
        probe.coefA = 6.390
        probe.coefB = -1.82
        probe.maxDepth = 1000
        probe.name =  "Sippican Fast Deep"
    elif code == 31:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 460
        probe.name =  "Sippican T-6"
    elif code == 32:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 460
        probe.name =  "Sippican T-6"
    elif code == 41:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 760
        probe.name =  "Sippican T-7"
    elif code == 42:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 760
        probe.name =  "Sippican T-7"
    elif code == 51:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 760
        probe.name =  "Sippican Deep Blue"
    elif code == 52:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 760
        probe.name =  "Sippican Deep Blue"        
    elif code == 61:
        probe.coefA = 6.301
        probe.coefB = -2.16
        probe.maxDepth = 200
        probe.name =  "Sippican T-10"    
    elif code == 71:
        probe.coefA = 1.779
        probe.coefB = -0.255
        probe.maxDepth = 460
        probe.name =  "Sippican T-11"        
    elif code == 81:
        probe.coefA = 1.52
        probe.coefB = 0.0
        probe.maxDepth = 460
        probe.name =  "Sippican AXBT"
    elif code == 201:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 460
        probe.name =  "TSK T-4"
    elif code == 202:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 460
        probe.name =  "TSK T-4"
    elif code == 211:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 460
        probe.name =  "TSK T-6"
    elif code == 212:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 460
        probe.name =  "TSK T-6"
    elif code == 221:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 760
        probe.name =  "TSK T-7"
    elif code == 222:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 760
        probe.name =  "TSK T-7"
    elif code == 231:
        probe.coefA = 6.828
        probe.coefB = -1.82
        probe.maxDepth = 1830
        probe.name =  "TSK T-5"
    elif code == 241:
        probe.coefA = 6.301
        probe.coefB = -2.16
        probe.maxDepth = 200
        probe.name =  "TSK T-10"
    elif code == 251:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 760
        probe.name =  "TSK Deep Blue"
    elif code == 252:
        probe.coefA = 6.691
        probe.coefB = -2.25
        probe.maxDepth = 760
        probe.name =  "TSK Deep Blue"
    elif code == 261:
        probe.coefA = -1
        probe.coefB = -1
        probe.maxDepth = 4000
        probe.name =  "TSK AXBT"
    elif code == 401:
        probe.coefA = 6.301
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-1"
    elif code == 411:
        probe.coefA = 5.861
        probe.coefB = -0.0904
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-3"        
    elif code == 421:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-4"  
    elif code == 431:
        probe.coefA = 6.828
        probe.coefB = -1.82
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-5"       
    elif code == 441:
        probe.coefA = 6.828
        probe.coefB = -1.82
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-5DB"      
    elif code == 451:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-6"      
    elif code == 461:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-7" 
    elif code == 462:
        probe.coefA = 6.705
        probe.coefB = -2.28
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-7" 
    elif code == 471:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-7DB"      
    elif code == 481:
        probe.coefA = 6.301
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-10"  
    elif code == 491:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-20"  
    elif code == 501:
        probe.coefA = 6.472
        probe.coefB = -2.16
        probe.maxDepth = 4000
        probe.name =  "Sparton XBT-20DB"     
    elif code == 510:
        probe.coefA = 1.524
        probe.coefB = 0.0
        probe.maxDepth = 4000
        probe.name =  "Sparton 536 AXBT-7"   
    elif code == 900:
        probe.coefA = 9.727
        probe.coefB = -0.0000473
        probe.maxDepth = 2000
        probe.name =  "Sippican T-12 (LMP5-T1)"  

    return probe      


def get_recorder(code):
    recorder = RecorderClass("unknown", -99,code)

    if code == 1:
        recorder.frequency = 10.0
        recorder.name = "Sippican Strip Chart Recorder"
    elif code == 2:
        recorder.frequency = 10.0
        recorder.name = "Sippican MK2A/SSQ-61"  
    elif code == 3:
        recorder.frequency = 10.0
        recorder.name = "Sippican MK-9"
    elif code == 4:
        recorder.frequency = 10.0
        recorder.name = "Sippican AN/BHQ-7/MK8"
    elif code == 5:
        recorder.frequency = 10.0
        recorder.name = "Sippican MK-12"
    elif code == 6:
        recorder.frequency = 10.0
        recorder.name = "Sippican MK-21"       
    elif code == 10:
        recorder.frequency = 10.0
        recorder.name = "Sparton SOC BT/SV Processor Model 10"
    elif code == 11:
        recorder.frequency = 10.0
        recorder.name = "Lockheed-Sanders Model QL5005"
    elif code == 20:
        recorder.frequency = 10.0
        recorder.name = "ARGOS XBT-ST"      
    elif code == 21:
        recorder.frequency = 10.0
        recorder.name = "CLS-ARGOS/Protecno XBT-ST Model-1"
    elif code == 22:
        recorder.frequency = 10.0
        recorder.name = "CLS-ARGOS/Protecno XBT-ST Model-2"
    elif code == 30:
        recorder.frequency = 10.0
        recorder.name = "Bathy Systems SA-810"
    elif code == 31:
        recorder.frequency = 10.0
        recorder.name = "Scripps Metrobyte Controller"
    elif code == 32:
        recorder.frequency = 10.0
        recorder.name = "Murayama Denki Z-60-16 III"
    elif code == 33:
        recorder.frequency = 10.0
        recorder.name = "Murayama Denki Z-60-16 II"
    elif code == 34:
        recorder.frequency = 10.0
        recorder.name = "Protecno ETSM2"
    elif code == 35:
        recorder.frequency = 10.0
        recorder.name = "Nautilus Marine Service NMS-XBT"
    elif code == 40:
        recorder.frequency = 10.0
        recorder.name = "TSK MK-2A"
    elif code == 41:
        recorder.frequency = 10.0
        recorder.name = "TSK MK-2S"
    elif code == 42:
        recorder.frequency = 10.0
        recorder.name = "SK MK-30"
    elif code == 43:
        recorder.frequency = 10.0
        recorder.name = "TSK MK-30N"
    elif code == 45:
        recorder.frequency = 10.0
        recorder.name = "TSK MK-100"
    elif code == 46:
        recorder.frequency = 10.0
        recorder.name = "TSK MK-130"
    elif code == 48:
        recorder.frequency = 10.0
        recorder.name = "TSK AXBT Receiver MK-300"
    elif code == 50:
        recorder.frequency = 10.0
        recorder.name = "JMA ASTOS"
    elif code == 60:
        recorder.frequency = 10.0
        recorder.name = "ARGOS Communications, Sampling on up transit"
    elif code == 61:
        recorder.frequency = 10.0
        recorder.name = "ARGOS Communications, Sampling on down transit"
    elif code == 62:
        recorder.frequency = 10.0
        recorder.name = "Orbcomm Communications, Sampling on up transit"
    elif code == 63:
        recorder.frequency = 10.0
        recorder.name = "Orbcomm Communications, Sampling on down transit"
    elif code == 70:
        recorder.frequency = 10.0
        recorder.name = "CSIRO Devil-1"
    elif code == 71:
        recorder.frequency = 10.0
        recorder.name = "CSIRO Devil-2"
    elif code == 99:
        recorder.frequency = 10.0
        recorder.name = "Unknown"

    return recorder