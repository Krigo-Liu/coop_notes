---
title: Git
icon: file
order: 1
author: Doris
category:
  - CS
tags:
  - Computer
footer: 
copyright: free
date: 2024-08-01
---
# Git

#### Self-learning link: https://nulab.com/zh-cn/learn/software-development/git-tutorial/

## Account & Connection
1. Initialize your folder as the local repo
   ```git
   git init
   ```
2. Setting the mailbox
    ```git
   git config --global user.email xxxx
    ```
3. Display all the Git setting lists and their origins
   ```git
   git config --list --show-origin
   ```
4. Test the connection
   ```git
   ssh -T git@github.com
   ```
5. Change an interface
   ```git
   git config --global http.proxy "http://127.0.0.1:8080"
   ```
##  Repository 
(already entered in the folder of your local repository)
1. Clone a repository
   ```git
   git clone git@...
   ```
2. Add modified files to current branch
   * Add all files in current directory into the buffer.
   ```git
   git add . 
   ```
   * Add certain files
   ```git 
   git add [file1] [file2]
   ```
   * Add certain directories
   ```git 
   git add [dir]
   ```
3. Commit the modification
   ```git
   git commit -m "commit message"
   ```
4. Push the modification to the remote repository
   ```git
   git push
   ```
5. Branch
   * Check current branch and the status
   ```git
   git status
   ```
   * Check the log of current branch
   ```git
   git log
   ```
   * Switch to the main branch
   ```git
   git checkout main
   ```
   * Create a new branch "dev"
   ```git
   git checkout -b dev
   ```
   * Merge "dev" to the current branch\
   The **--no-ff** option disables fast-forward merging. This means that even if the current branch can simply fast-forward to include changes from the dev branch, Git will still create a new merge commit.
   ```git
   git merge dev --no-ff
   ```
   * Delete the branch "dev"
   ```git
   git branch --delete dev 
   ```
6. Trace back\
Please be cautious when using **--hard** as it will **PERMANENTLY delete any uncommitted changes.**\
It's best to back up a file somewhere else first. This is based on my painful experience.
   * To a certain version(versionNumber).
   ```git
   git reset --hard versionNumber
   ```
   * To the latest version.
   ```git
   git reset --hard
   ```