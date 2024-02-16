import numpy as np
import pybullet as p
import pybullet_data  # pybullet自带的一些模型


def get_jointIds_Names( id_robot):
    jointNamesAll = []
    jointIdsAll = []
    jointNames = []
    jointIds = []
    for j in range(p.getNumJoints(id_robot)):
        info = p.getJointInfo(id_robot, j)
        p.changeDynamics(id_robot, j, linearDamping=0, angularDamping=0)
        jointName = info[1]
        jointType = info[2]
        jointIdsAll.append(j)
        jointNamesAll.append(jointName)
        if (jointType == p.JOINT_PRISMATIC or jointType == p.JOINT_REVOLUTE):
            jointIds.append(j)
            jointNames.append(jointName)
    return jointIdsAll, jointNamesAll, jointIds, jointNames

p.connect(p.GUI)  # 连接到仿真环境，p.DIREACT是不显示仿真界面,p.GUI则为显示仿真界面
p.setGravity(0, 0, -9.81)  # 设定重力
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.resetSimulation()  # 重置仿真环境
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # 添加pybullet的额外数据地址，使程序可以直接调用到内部的一些模型
planeId = p.loadURDF("plane.urdf")  # 加载外部平台模型
idrobot = p.loadURDF("urdf/manual.urdf", basePosition=[1, -1, 1], globalScaling=1,useFixedBase = True)
#objects = p.loadURDF("humanoid.urdf")  # 加载机械臂，flags=9代表取消自碰撞，详细教程可以参考pybullet的官方说明文档
jointIdsAll, jointNamesAll, jointIds, jointNames = get_jointIds_Names(idrobot)
print(jointNamesAll)
print((len(jointNames)))

while 1:
    p.stepSimulation()