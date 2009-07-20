#!/usr/bin/python
# Backups all zope instances (any versions)
#
# Depends : zope_instance.py
# Copyright (C) 2007-2009 Guillaume Pellerin

import os
import sys
from zope_instance import *

version = '0.2'
info = 'zope_backup v'+version+'\n'+ \
       """Copyright (C) 2007-2009 Guillaume Pellerin
       Usage: zope_backup DIRECTORY
       where DIRECTORY is the directory where you want to backup 
       the instances of the different versions of zope."""
print info

backup_dir = sys.argv[-1]
if not os.path.exists(backup_dir):
    sys.exit('This backup directory does not exists !')

z = ZopeInstall()
instances = z.get_instances()

def backup_all():
    for version in instances:
    	for instance in instances[version]:
            z = ZopeInstance(version, instance, backup_dir)
            print 'Backuping : ' + z.get_instance_dir() + '...'
            z.backup()
            print version + ': ' + instance + ' backuped !'

if __name__ == '__main__':
    backup_all()
    print "Backup_all Zopes done !"

