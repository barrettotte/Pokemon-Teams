#!/bin/sh
# A lazy script for running Vue app from base directory => ./scripts/app.sh
fp="$(pwd)/app/"
npm run --prefix $fp serve