#!/usr/bin/python3
"""Deploying"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['34.202.164.217', '100.26.230.167']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Deploy archive"""
    if not os.path.exists(archive_path):
        return (False)

    try:
        li = archive_path.split('/')
        file_name = li[-1]

        path_of_releases = f"/data/web_static/releases/{file_name[:-4]}/"
        path_of_tmp = f"/tmp/{file_name}"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {path_of_releases}")
        run(f"tar -xzf {path_of_tmp} -C {path_of_releases}")
        run(f"rm {path_of_tmp}")
        run(f"mv {path_of_releases}web_static/* {path_of_releases}")
        run(f"rm -rf {path_of_releases}web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path_of_releases} /data/web_static/current")
        print("New version deployed!")
        return (True)
    except Exception:
        return (False)
