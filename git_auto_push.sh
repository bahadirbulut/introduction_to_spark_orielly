#!/bin/bash

# init
function pause(){
   read -p "$*"
}

echo ============================================
echo Adding Files...
echo ============================================
git add -A

echo ============================================
echo Committing...
echo ============================================
git commit -m "Auto Commit"

echo ============================================
echo Pushing...
echo ============================================
git push

## Pause it ##
pause 'Press [Enter] key to continue...'