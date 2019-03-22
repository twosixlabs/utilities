#!/usr/bin/env bash
#
# Push TwoSix Labs Python2.x Utilities Library To Repository
#
# Example Call:
#    ./push.sh --repository=http://localhost:8081/repository/pypi/
#

REPOSITORY="http://xd3-node-a.twosix.local:8081/repository/mw-pip/"
USERNAME=""
PASSWORD=""
BUILD_DIR="./dist/*"

# Parse CLI Arguments
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -R|-r|--repo|--repository)
        REPOSITORY="$2"
        shift
        shift
        ;;
        --repo=*|--repository=*)
        REPOSITORY="${1#*=}"
        shift
        ;;
        -B|-b|--build_dir)
        BUILD_DIR="$2"
        shift
        shift
        ;;
        --build_dir=*)
        BUILD_DIR="${1#*=}"
        shift
        ;;
        -U|-u|--username)
        USERNAME="$2"
        shift
        shift
        ;;
        --username=*)
        USERNAME="${1#*=}"
        shift
        ;;
        -P|-p|--password)
        PASSWORD="$2"
        shift
        shift
        ;;
        --password=*)
        PASSWORD="${1#*=}"
        shift
        ;;
        *)
        shift
        ;;
    esac
done

if [ -z "${REPOSITORY}" ]
then
  echo "$(date +%c): No Repository Specified, Exiting"
  exit 1
fi

if [ -z "$(ls -A ${BUILD_DIR})" ]; then
   echo "$(date +%c): Build Dir is Empty, Nothing to Push. Maybe need to Build First?"
   exit 1
fi

echo "$(date +%c): Pushing Pushing TwoSix Labs Python3.x Utilities i(${BUILD_DIR}) to ${REPOSITORY}"
if ([ -z "${USERNAME}" ] || [ -z "${PASSWORD}" ])
then
  echo "$(date +%c): No Username, Pushing without"
  twine upload --repository-url=${REPOSITORY} ${BUILD_DIR}
else
  echo "$(date +%c): Pushing with Specified User: ${USERNAME}"
  twine upload --username=${USERNAME} --password=${PASSWORD} --repository-url=${REPOSITORY} ${BUILD_DIR}
fi
