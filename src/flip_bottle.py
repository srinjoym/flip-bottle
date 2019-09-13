#!/usr/bin/env python

from hlpr_manipulation_utils.arm_moveit2 import ArmMoveIt
from kinova_msgs.msg import JointVelocity

import rospy

class FlipBottle:
    def __init__(self):
        self.arm = ArmMoveIt()
        self.arm_velocity_pub = rospy.Publisher('j2s7s300_driver/in/joint_velocity', JointVelocity, queue_size=1)

    def throw_bottle(self):
        self.move_arm_to_init_pose()
        rate = rospy.Rate(100) # 10hz

        end_time = rospy.Time.now() + rospy.Duration(1)
        while rospy.Time.now() < end_time :
            # velocity_msg = JointVelocity(joint6=-150.0)
            velocity_msg = JointVelocity(joint4=70.0, joint6=-150)
            self.arm_velocity_pub.publish(velocity_msg)
            rate.sleep()


    def move_arm_to_init_pose(self):
        # self.move_arm([-0.8065584429967274, 3.4143445576880027, -1.151746730848438, 1.0875841228115404, 0.33927320733356275, 4.181650269903889, 7.1650202620743295])
        planTraj =  self.arm.plan_jointTargetInput([-1.57, 3.7824834351817977, 0, 1.0376508510579634, 0, 3.855092125457827, 1.57])
        self.arm.group[0].execute(planTraj)
        
    def move_arm(self,pose):
        self.old_gripper_pos = self.arm.group[0].get_current_pose().pose
        planTraj = self.arm.plan_poseTargetInput(pose)
        self.arm.group[0].execute(planTraj)
        self.gripper_pos = self.arm.group[0].get_current_pose().pose


def main():
    client = FlipBottle()
    client.throw_bottle()
    # client.move_arm_to_init_pose()

if __name__ == "__main__":
    rospy.init_node('flip_bottle_node', anonymous=True)
    main()
