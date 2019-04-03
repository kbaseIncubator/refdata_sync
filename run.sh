#!/bin/sh

# Docker container entrypoint script
# When you run `docker run my-app xyz`, then this script is run

set -e

if [ "${1}" = "refseq" ] ; then
  ftp_url="rsync://ftp.ncbi.nlm.nih.gov/genomes/refseq/"
  rsync --copy-links --recursive --times --verbose $ftp_url $2
fi

if [ "${1}" = "ebi_metagenomes"] ; then
  lftp -e "mirror --continue /vol1/ $2 --parallel=8" ftp.sra.ebi.ac.uk
fi

