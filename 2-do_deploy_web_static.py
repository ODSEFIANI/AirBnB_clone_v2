#!/usr/bin/python3
""" module"""
from fabric.api import env, put, run, local, task
from os import path
from datetime import datetime

env.hosts = ['34.204.101.175', '35.153.192.118']
env.user = "ubuntu"

@task
def do_pack():
    """ ffabric """
    try:
        local('mkdir -p versions')
        dt = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'web_static_{}.tgz'.format(dt)
        local('tar -czvf versions/{} web_static/'.format(filename))
        return 'versions/{}'.format(filename)
    except:
        return None


def do_deploy(archive_path):
    """ fabric """
    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp")
        name = archive_path.split('/')[-1].split('.')[0]
        folder = "/data/web_static/releases/{}".format(name)
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(name, folder))
        run("rm /tmp/{}.tgz".format(name))
        run("rm -rf {}/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")
        return True
    except:
        return False
