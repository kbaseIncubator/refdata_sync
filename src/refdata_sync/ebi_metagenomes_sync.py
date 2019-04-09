"""
Manually download all ebi metagenomes directly from http.
"""
import sys
import os
import requests
from .utils.cli import fatal

def run(dest_path, overwrite=False):
    # check if dest_path exits, if not, create it
    if not os.path.isdir(dest_path):
        os.mkdir(dest_path)

    with open("data/ebi_metagenome_dl_urls.txt") as fid:
        urls = [line.strip() for line in fid.readlines()]

    for url in urls:
        resp = requests.get(url, stream=True)
        if resp.status_code == requests.codes.ok:
            file_path = os.path.join(dest_path, url.split("/")[-3] + "_" + url.split("/")[-1])

            if os.path.isfile(file_path):
                if overwrite:
                    # remove existing file
                    os.remove(file_path)
                else:
                    #existing file is not overwritten
                    continue
            with open(file_path, "ab") as fd:
                for chunk in resp.iter_content(chunk_size=2048):
                    fd.write(chunk)
        else:
            with open("failed_queries.txt", "a") as fid:
                fid.write(url+"\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # error here
        fatal("Pass in the destination path as the first argument")
    dest_path = sys.argv[1]
    run(dest_path)
