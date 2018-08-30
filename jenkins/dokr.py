#!/usr/bin/env python

import sys
import os


def cmdExec(str):
    return os.popen(str).read().strip()


def joinMe(stringList):
    return "".join(string for string in stringList)


def addBuildTag():
    searchPattern = sys.argv[2];
    tagName = sys.argv[3];
    print ('\nSearching pattern: *', searchPattern + '* and adding tag ' + tagName)
    imageName = cmdExec("docker images | cut -d ' '  -f1 | grep " + searchPattern + " | head -1");
    print('\nFound this image name from the given pattern ' , imageName)
    addTagCommand = joinMe(['docker tag ' , imageName , ' ' , imageName , ':', tagName ]);
    print('\nExecuting tag command : \n' + addTagCommand)
    print(cmdExec(addTagCommand));
    print('\nAdded Tag : '  + tagName + ' into the images\n')
    print(cmdExec('docker images'))
   

  
def pushImage():
    searchPattern = sys.argv[2];
    print('\nPushing images matching pattern ', searchPattern)
    
    imageName = cmdExec("docker images | cut -d ' '  -f1 | grep " + searchPattern + " | head -1");
    
    print('\nFound this image name from the given pattern ' , imageName)
    
    imageListStr = "docker image inspect -f '{{join .RepoTags \"\\n\" }}' " + imageName;
    imageList = cmdExec(imageListStr)
    
    print('\nFound Following images : \n\n' + imageList)
    
    tagList = cmdExec(imageListStr).split("\n")
    
    print('\nTotal Tags found :' , len(tagList))
    
    for tag in tagList:
        print('\n--------------------------Pushing image :' + tag + '-----------------------------------')
        print(cmdExec('docker push ' + tag))


def loginEcs():
    login = cmdExec("aws ecr get-login   | sed  's/-e none//g'")
    print('\n----------  Logining into aws  ----------  \n\n', login + '\n')
    print(cmdExec(login))
    

def cleanUp():
    searchPattern = sys.argv[2];
    print('Cleaning Old Images  matching pattern ', searchPattern)
    cleaner = cmdExec("docker images -a | grep " + searchPattern + " | awk '{print $3}' | xargs docker rmi -f")
    print(' ----------  Cleaning Old Images ---- \n', cleaner)


def helper():
    print('\n------------------------ Command Options ------------------------')
    print('\ndokr clean searchPattern # delete old images matching pattern')
    print('\ndokr lecs # ECS login')
    print('\ndokr tag searchPattern tagName # add a tag *tagName*on a image matching *searchPattern* ')
    print('\ndokr push searchPattern  # push all images matching the pattern')
    print('\n')

    
def switch(arg):
    function_dict = {
        'clean' : cleanUp,
        'lecs' :loginEcs,
        'tag': addBuildTag,
        'push': pushImage,
        'help' : helper
        }
    return function_dict[arg]


switch(sys.argv[1])()
