#!/usr/bin/env python3.6
import requests
from urllib.parse import urljoin
import os
import logging
LOG_LEVEL = logging.DEBUG
def download_file_by_curl(url, outdir, filename):
    newpath =  os.path.join('./downloads/',os.path.dirname(outdir))
    logging.info(newpath)
    os.system('mkdir -p %s;'%newpath)
    os.system('cd %s;curl -OL %s'%(newpath,url))
def main():
    filename = "windbg.log"
    outdir = './downloads/'
    main_url = 'https://msdl.microsoft.com/'
    with open(filename, 'r') as fp:
        content = fp.readlines()
        for rline in content:
            line = rline.strip()
            if line.startswith('SYMSRV:  http'):
                m = line.rstrip(' not found').split(':  ')
                url =urljoin(main_url, m[1])
                pdb_name = m[1][len('/download/symbols/'):]
                logging.info("{} {}".format(url, pdb_name))
                download_file_by_curl(url, pdb_name, filename)
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s', level=LOG_LEVEL)
    main()
