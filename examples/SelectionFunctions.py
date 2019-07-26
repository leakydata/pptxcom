import win32com.client as win32

# Create/Assign an Application object from the currently active PowerPoint Instance
PPT = win32.GetActiveObject("PowerPoint.Application") 
    
# Goto a specific slide number (slide view)
PPT.ActiveWindow.View.GotoSlide(1)

# Select a shape on a slide by it's number (the slide must be the current active slide)
PPT.ActivePresentation.Slides(1).Shapes(2).Select(-1)

# Select a shape it's Name (the slide must be the current active slide)
PPT.ActivePresentation.Slides(1).Shapes('Rectangle 1').Select(-1)


# Print out the Type number/constant value, of every Shape on the active slide numbered 1 
for s in PPT.ActivePresentation.Slides(1).Shapes:
    print(s.Type)
