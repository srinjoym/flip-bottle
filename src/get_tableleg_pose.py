#!/usr/bin/env python

from tableleg_pose.srv import *
import geometry_msgs.msg
from arm_moveit import *

import rospy

class GetTableLegPose:

    def __init__(self):
        self.arm = ArmMoveIt()




    def handle_get_tableleg_pose(self,req):
        # print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))

        self.arm.group[0].set_pose_target(req.gripper_pose)

        self.arm.group[0].go()

        tableleg_pose = req.gripper_pose

        tableleg_pose.position.x += 5

        return TableLegPoseResponse(req.gripper_pose)


    def get_tableleg_pose_server(self):
        rospy.init_node('get_tableleg_pose_server')
        s = rospy.Service('get_tableleg_pose', TableLegPose, self.handle_get_tableleg_pose)
        print "Ready to output table leg pose."
        rospy.spin()


if __name__ == "__main__":
    GetTableLegPose().get_tableleg_pose_server()
