#!/usr/bin/python
# Create thumbs of webpages from a list of URLs

# depends : webthumb, imagemagick

import os
import sys
from webthumb import get_thumbnail

img_dir = '/var/www/files/img/webthumbs'
site_list_file = '/var/www/files/img/webthumbs/webthumb_list.txt'

def main(site_list_file, img_dir):
    site_list = open(site_list_file,'r')
    for site in site_list.readlines():
        site = site[0:len(site)-1]
        if site:
	    print site
            file = site.replace('/','_')
            file = img_dir+os.sep+file+'.png'
            print file
            get_thumbnail('http://'+site, file,'large')
    site_list.close()
    print 'Webthumbs created !'

if __name__ == '__main__':
    main(site_list_file, img_dir)
