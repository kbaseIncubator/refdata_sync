"""
Rsync data from NCBI's refseq
"""
import sys
import subprocess
from .utils.cli import fatal

_FTP_URL = "rsync://ftp.ncbi.nlm.nih.gov/genomes/refseq/"


def run(dest_path):
    proc = subprocess.Popen(
        [
            'rsync',
            '--copy-links',
            '--recursive',
            '--times',
            '--verbose',
            _FTP_URL,
            dest_path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    for line in proc.stdout:
        print(line)
    proc.wait()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        fatal('Pass in the destination path as the first argument.')
    dest_path = sys.argv[1]
    run(dest_path)
