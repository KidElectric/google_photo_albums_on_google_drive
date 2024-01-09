import sys
import subprocess
import pandas as pd
from pathlib import Path
rclone_gp = sys.argv[2] + ':/album'
rclone_drive = sys.argv[1] + ':/'
gp_on_drive = sys.argv[3]
print("Organize photos in %s to %s%s " % (rclone_gp,
                                                   rclone_drive,
                                                   gp_on_drive))
subprocess.check_call(['rclone','lsd','%s' % rclone_drive])
subprocess.check_call(['rclone','lsd','%s' % rclone_gp])
#subprocess.check_call(['echo','hello'])

