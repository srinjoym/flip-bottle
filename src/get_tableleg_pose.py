#!/usr/bin/env python

from tableleg_pose.srv import *
import geometry_msgs.msg
import rospy


def handle_get_tableleg_pose(req):
    # print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    tableleg_pose = req.gripper_pose

    tableleg_pose.position.x += 5

    return TableLegPoseResponse(req.gripper_pose)


def get_tableleg_pose_server():
    rospy.init_node('get_tableleg_pose_server')
    s = rospy.Service('get_tableleg_pose', TableLegPose, handle_get_tableleg_pose)
    print "Ready to add two ints."
    rospy.spin()


if __name__ == "__main__":
    get_tableleg_pose_server()