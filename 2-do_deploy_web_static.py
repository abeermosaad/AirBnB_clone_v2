#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os
"""Deploying"""


env.hosts = ['34.202.164.217', '100.26.230.167']


def do_deploy(archive_path):
    """Deploy web_static"""
    if not os.path.exists(archive_path):
        return (False)
    try:
        put(archive_path, '/tmp/')
        li = archive_path.split('/')
        file_name = li[-1]
        run(f'mkdir -p /data/web_static/releases/{file_name[:-4]}')
        run(f'tar -xzf /tmp/{file_name} -C \
            /data/web_static/releases/{file_name[:-4]}')
        run(f'rm /tmp/{file_name}')
        run(f'mv /data/web_static/releases/{file_name[:-4]}/web_static/* \
                /data/web_static/releases/{file_name[:-4]}/')
        run(f'rm -rf /data/web_static/releases/{file_name[:-4]}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{file_name[:-4]}/ \
                /data/web_static/current')
        print('New version deployed!')
        return (True)
    except Exception:
        return (False)
