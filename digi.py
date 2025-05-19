import subprocess
import time
def start_blender():
    subprocess.Popen(['C:\\Program Files\\Blender Foundation\\Blender 4.0\\blender-launcher.exe', 'C:\\Users\\shayelorgelly\\OneDrive - Kaiapoi High School\\Documents\\dwad.blend'])

def open_page(page):
    subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', page])
    
print('Starting Blender')
start_blender()
print('Opening design log')
open_page('https://docs.google.com/document/d/15b5wWG3MKmA6VfGRswUkm89JRofRiJBhL3uJpnowsn4/edit?tab=t.0')
print('Opening testing log')
open_page('https://docs.google.com/document/d/1udttJF5FsiBx_S2NVo_R6gRKnp_bHwHGDJpNuCov6Jc/edit?tab=t.0')
print('Opening sprint tracking')
open_page('https://docs.google.com/document/d/1PC3lfzHIDKcee2tYETizitOSesKtt9QADUWrnmYH5RM/edit?tab=t.0')
print('Opening classroom')
open_page('https://classroom.google.com/c/NzQ3OTgxNTY4NjEy')
time.sleep(5)
