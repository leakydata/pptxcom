# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:00:36 2019

@author: Nathan Jones
"""

import win32com.client as win32Client
import win32com.client.gencache as win32ClientGen
from win32com.client import constants as constants
from pywintypes import com_error  # pylint: disable=I0011,E0611

def grab_active(visible=True):
    """
    @visible: Set PowerPoint application window to visible
    
    Grabs the active PowerPoint application and creates a COM object
    representing the application.
    """
    
    try:
        p = win32Client.GetActiveObject("PowerPoint.Application")
    except com_error:
        p = win32ClientGen.EnsureDispatch("PowerPoint.Application")
    
    # If Visible = False we will get a COM error since an Open Applivation window will always be visible
    # Visible is set here to avoid vagueness, but it is basically optional in this specific case
    p.Visible = visible 

    return p
