#!/usr/bin/env python3.6
import requests
from urllib.parse import urljoin
import os
import logging
LOG_LEVEL = logging.DEBUG
def download_file_by_curl(url, outdir, filename):
    newpath =  os.path.join('./downloads/',os.path.dirname(outdir))
    #logging.info(newpath)
    os.system('mkdir -p %s;'%newpath)
    os.system('cd %s;curl -OL %s'%(newpath,url))
def main():
    filename = "windbg.log"
    outdir = './downloads/'
    main_url = 'https://msdl.microsoft.com/'
    with open(filename, 'r', encoding='gbk') as fp:
        for rline in fp:
            line = rline.strip()
            m = None
            uri = None
            if (line.startswith('SYMSRV:  http') and line.endswith(' not found')) :
                m = line.rstrip(' not found').split(':  ')
                uri = m[1]
            elif line.startswith('SYMSRV:  HTTPGET'):
                m = line.split(':')
                uri = m[2].strip(' ')
            if uri:
                print(f'uri: {uri:s}')
                pdb_name = uri[len('/download/symbols/'):]
                logging.info("Download from {} to {}".format(url, pdb_name))
                download_file_by_curl(url, pdb_name, filename)
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s', level=LOG_LEVEL)
    main()
