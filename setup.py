from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.

setup(name = "rosbag_extract",
    version = "0.1",
    description = "Tool to extract rosbag messages",
    author = "Toni Gabas",
    author_email = "a.gabas@aist.go.jp",
    url = "",
    packages = ['rosbag_extract'],
    #'package' package must contain files (see list above)
    long_description = 
        """
        Tool to extract rosbag messages.
        In the current version 2 type of image message
        can be extracted: 1-channel images (e.g. depth images)
        and 3-channel images (e.g. rgb images)
        """ 
) 

