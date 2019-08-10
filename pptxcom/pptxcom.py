# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:00:36 2019

@author: Nathan Jones
"""

import os

import win32com.client as win32Client
import win32com.client.gencache as win32ClientGen

from pywintypes import com_error  # pylint: disable=I0011,E0611

def active_app():
	"""
	@visible: Set PowerPoint application window to visible
	
	Grabs the active PowerPoint application and creates a COM object
	representing the active application.
	"""
	
	try:
		p = win32Client.GetActiveObject("PowerPoint.Application")
	except com_error:
		p = win32ClientGen.EnsureDispatch("PowerPoint.Application")
		
	return p


def active_pres():
	"""
	@visible: Set PowerPoint application window to visible
	
	Grabs the active PowerPoint application and creates a COM object
	representing the active presentation.
	"""
	
	try:
		p = win32Client.GetActiveObject("PowerPoint.Application")
	except com_error:
		p = win32ClientGen.EnsureDispatch("PowerPoint.Application")
		
	return p.ActivePresentation


def open_pres(filepath, visible=True):
	"""
	@filepath: raw text file path r'C:\path\to\the\powerpoint_file.pptx'
	@visible: Set PowerPoint application window to visible
	
	Opens a PowerPoint file creates a COM object representing the presentation.
	"""

	try:
		os.path.isfile(filepath)
	except ValueError:
		print("File does not exist.")
		return False
	
	try:
		p = win32Client.Dispatch("PowerPoint.Application")
	except com_error:
		print("File not available.")   
		return False
		
	p.Visible = visible
	pres = p.Presentations.Open(filepath) 
	
	return pres

# Convert standard RGB colors to PowerPoint color integer values
def rgb_to_hex(rgb): # color uses bgr in hex
    bgr = (rgb[2], rgb[1], rgb[0]) # convert rgb into bgr
    str_value = '%02x%02x%02x' % bgr # convert bgr in hex
    int_value = int(str_value, 16) # convert hex to integer
    return int_value
