#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
"""Packing"""


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None
