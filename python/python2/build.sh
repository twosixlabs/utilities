#!/usr/bin/env bash
#
# Build TwoSix Labs Python3.x Utilities Package For Pushing to Repository
#
# Example Call:
#    ./build.sh
#

SETUP_FILE="./setup.py"

# Parse CLI Arguments
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -S|-s|--setup)
        SETUP_FILE="$2"
        shift
        shift
        ;;
        --setup=*)
        SETUP_FILE="${1#*=}"
        shift
        ;;
        -F|-f|--file|--filename)
        SETUP_FILE="$2"
        shift
        shift
        ;;
        --file=*|--filename=*)
        SETUP_FILE="${1#*=}"
        shift
        ;;
        *)
        shift
        ;;
    esac
done

echo "$(date +%c): Building TwoSix Labs Python3.x (Setup File = ${SETUP_FILE})"
python2 ${SETUP_FILE} sdist bdist_wheel
