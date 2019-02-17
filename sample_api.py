import subprocess
import win32com.client  # todo rm. pres is initialized in ppexe
import time
from ppsuite import PPAPI

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True
pres = Application.ActivePresentation

time.sleep(5)

api = PPAPI(pres)
# api.load_ppasm("./ppasm/test.ppasm")

api.mem_write(5, 11001111)
val = api.mem_read(5)
api.tape_write_raw(4, str(val))
api.execute()
res = api.tape_read_raw()
# api.teardown()