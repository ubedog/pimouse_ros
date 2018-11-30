<<<<<<< HEAD
#!/usr/bin/env python
=======
<<<<<<< HEAD
#!/usr/bin/env python

import rospy, unittest, rostest
import rosnode
import time
from std_msgs.msg import UInt16

class BuzzerTest(unittest.TestCase):
    def test_node_exist(self):
        nodes =  rosnode.get_node_names()
        self.assertIn('/buzzer', nodes, "node does not exist")

    def test_put_value(self):
        pub = rospy.Publisher('/buzzer', UInt16)
        for i in range(10):
            pub.publish(1234)
            time.sleep(0.1)

        with open("/dev/rtbuzzer0", "r") as f:
            data = f.readline()
            self.assertEqual(data, "1234\n", "value does not written to rtbuzzer0")
=======
#!/usr/bin/nev python
>>>>>>> fbcc8cde3659e41f9a02b5e0ef984aadd093d2a7
import rospy, unittest, rostest
import rosnode
import time

class BuzzerTest(unittest.TestCase):
    def test_node_exist(self):
	nodes = rosnode.get_node_names()
	self.assertIn('/buzzer',nodes, "node does not exist")
>>>>>>> 90787d43ca79531b39d727e19463fa0425eb4b83

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_buzzer')
<<<<<<< HEAD
    rostest.rosrun('pimouse_ros', 'travis_test_buzzer', BuzzerTest)
=======
    rostest.rosrun('pimouse_ros','travis_test_buzzer',BuzzerTest)
>>>>>>> 90787d43ca79531b39d727e19463fa0425eb4b83
