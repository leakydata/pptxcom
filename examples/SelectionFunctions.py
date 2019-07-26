import win32com.client as win32

# Create/Assign an Application object from the currently active PowerPoint Instance
PPT = win32.GetActiveObject("PowerPoint.Application") 
#pres = PPT.ActivePresentation #Grab the already open powerpoint file (the active PowerPoint Presentation)
    
    
PPT.ActivePresentation.Slides(1)
