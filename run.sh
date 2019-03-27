#!/bin/sh

# Docker container entrypoint script
# When you run `docker run my-app xyz`, then this script is run

set -e

if [ "${1}" = "refseq" ] ; then
  python -m src.refdata_sync.refseq_sync $2
fi
