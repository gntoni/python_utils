#!/usr/bin/env python
"""Summary

Attributes:
    out (TYPE): Description

"""

import rosbag
import numpy as np
from cv_bridge import CvBridge
from sys import argv, exit
from cv2 import imwrite
from os import path

_IMAGE_FORMATS = {'image1C': ".tiff",
                             'image3C': ".png"}


def extractMessageFromBag(bagname, topicname, msgtype, outputdir=".",
                          save_ims=False):
    """
    Function to extract the message information in a rosbag topic
    to a numpy array.

    Args:
        bagname (str): Path to the rosbag file

        topicname (str): Name of the rosbag topic that contains the images

        msgtype (str): Topic data type. Can be one of the following:
            - "image1C" : One channel image.
            -  "image3C": Three channel image.

        outputdir (str, optional): Directory where the output files will be
            stored (if any).
            Default: current directory

        save_ims (bool, optional): For image type messages, saves each
            image in "ouputdir".


    Yields:
        numpy.ndarray: Message image

    Examples:
        Extract rgb images in a message:
        >>> print(image) #TODO
    """

    bag = rosbag.Bag(bagname)
    bridge = CvBridge()
    ctr = 0
    for topic, msg, t in bag.read_messages(topics=[topicname]):
        if msgtype[0:5] == 'image':
            cvimg = bridge.imgmsg_to_cv2(msg)
            if save_ims:
                imwrite(path.join(outputdir, "img_"+str(ctr)+_IMAGE_FORMATS[msgtype]), cvimg)
                ctr += 1
            yield cvimg


if __name__ == '__main__':
    if len(argv) != 5:
        print "ERROR: wrong number of parameters: " + str(len(argv)-1)
        print "usage: "+argv[0] + " [BagFilename] [OutputDir] [TopicName] [TopicType:s image1C/image3C/pcl]"
        exit()
    else:
        bagname = argv[1]
        topicname = argv[2]
        topictype = argv[3]
        outdir = argv[4]

        out = extractMessageFromBag(bagname, topicname, topictype, outdir)
        np.save("output", out)
