"""
TODO: Specify parameters
    human-readable
    1033 bytes in size
    not executable
"""

import os
start_path = '.' # current directory
for path,dirs,files in os.walk(start_path):
    for filename in files:
        print os.path.join(path,filename)