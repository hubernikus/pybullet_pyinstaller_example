import PyInstaller.__main__
import os
import shutil
from pathlib import Path

PyInstaller.__main__.run(['scripts/hello_pybullet.py'])


src_dir = Path("/home/lukas/Code/pybullet_pyinstaller/.venv/lib/python3.12/site-packages/pybullet_data")
dst_dir = Path("dist/hello_pybullet/pybullet_data")

# os.mkdir(dst_dir)
# 
# file = "plane.urdf"
# shutil.copyfile(src_dir/ file, dst_dir / file)
# shutil.copyfile(src_dir/ file, dst_dir / file)
# 
# file = "r2d2.urdf"
# shutil.copyfile(src_dir/ file, dst_dir / file)

# Copy full directory
shutil.copytree(src_dir, dst_dir)  
