import pdb
# breakpoint()

import pybullet as p
import time
import pybullet_data 
from pathlib import Path


def main():
    pass


physicsClient = p.connect(p.GUI) # p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)



try:
    # p.loadURDF("plane.urdf")
    pass 
# except p.error:
except:
    print('exception')
    # breakpoint()
    dir_pybullet = Path("./pybullet_data")
    p.loadURDF(str(dir_pybullet/"plane.urdf"))


cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])

try:
    robot_id = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)

except Exception as e:
    # breakpoint()
    dir_pybullet = Path("./pybullet_data")
    # robot_id = p.loadURDF(str(dir_pybullet/"r2d2.urdf"))
    robot_id = p.loadURDF(str(dir_pybullet/"r2d2.urdf"), cubeStartPos, cubeStartOrientation)


for i in range (100000):
   p.stepSimulation()
   time.sleep(1./240.)
   cubePos, cubeOrn = p.getBasePositionAndOrientation(robot_id)

print(cubePos,cubeOrn)
breakpoint()

p.disconnect()

if __name__ == "__main__":
    main()
