#!/usr/bin/env python

import sys
import os
from curses.ascii import NUL


def cmdExec(str):
    return os.popen(str).read().strip()


def joinMe(stringList):
    return "".join(string for string in stringList)


def addBuildTag():
    throwException(sys.argv[2], 'Cannot push image. Search pattern is missing')
    throwException(sys.argv[3], 'Cannot push image. Tag Name  is missing')
    searchPattern = sys.argv[2];
    tagName = sys.argv[3];
    print ('Searching pattern:', searchPattern + 'adding tag ' + tagName)
    imageName = cmdExec("docker images | cut -d ' '  -f1 | grep " + searchPattern + " | head -1");
    print('image name is ' , imageName)
    addTagCommand = joinMe(['docker tag ' , imageName , ' ' , imageName , ':', tagName ]);
    cmdExec(addTagCommand);
    print('tag command ' + addTagCommand)


def throwException(inputString, message):
    if not inputString.strip():
        raise Exception(message + 'Use dokr help option')

  
def pushAll():
    searchPattern = sys.argv[2];
    throwException(searchPattern, 'Cannot push image. Search pattern is missing')
    imageName = cmdExec("docker images | cut -d ' '  -f1 | grep " + searchPattern + " | head -1");
    print('image name is ' , imageName)
    imageListStr = "docker image inspect -f '{{join .RepoTags \"\\n\" }}' " + imageName;
    imageList = cmdExec(imageListStr)
    print('tag imageListStr ' + imageList)
    tagList = cmdExec(imageListStr).split("\n")
    for tag in tagList:
        print('--------------------------Pushing image :' + tag + '-----------------------------------')
        cmdExec('docker push ' + tag)


def loginEcs():
    login = cmdExec("eval $(aws ecr get-login   | sed  's/-e none//g')")
    print('Logining into aws ', login)


def cleanUp():
    searchPattern = sys.argv[2];
    throwException(searchPattern, 'Cannot delete images. Search pattern is missing')
    login = cmdExec("docker images -a | grep " + searchPattern + " | awk '{print $3}' | xargs docker rmi -f")
    print('Logining into aws ', login)


def validateCliArgs(index, message):
    if index < len(sys.argv):
        raise Exception(message + 'Use dokr help option')


def switch(arg):
    function_dict = {
        'clean' : cleanUp,
        'lecs' :loginEcs,
        'tag': addBuildTag,
        'pa': pushAll
        }
    return function_dict[arg]


print(len(sys.argv))
throwException(sys.argv[1], 'Please enter a valid command.')
arg1 = sys.argv[1]
switch(sys.argv[1])()