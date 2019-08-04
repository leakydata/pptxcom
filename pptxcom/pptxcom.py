import win32com.client as win32Client
import win32com.client.gencache as win32ClientGen
from pywintypes import com_error  # pylint: disable=I0011,E0611

def PPT(visible=True):
    try:
        p = win32Client.GetActiveObject("PowerPoint.Application")
    except com_error:
        p = win32ClientGen.EnsureDispatch("PowerPoint.Application")
    p.Visible = visible
    return p
