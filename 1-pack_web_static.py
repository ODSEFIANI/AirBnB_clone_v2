#!/usr/bin/python3
""" compress files using gzip """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ function """
    try:
        local('mkdir -p versions')
      
        m = datetime.now().month
        n = datetime.now().minute
        s = datetime.now().second
        d = datetime.now().day
        h = datetime.now().hour
        y = datetime.now().year

        filename = 'web_static_{}{}{}{}{}{}.tgz'.format(y, m, d, h, n, s)
        local('tar -czvf versions/{} web_static/'.format(filename))
        return 'versions/{}'.format(filename)
    except:
        return None
