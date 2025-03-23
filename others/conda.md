---
title: Anaconda
icon: file
order: 2
author: Doris
category:
  - CS
tags:
  - Computer
footer: 
copyright: free
date: 2024-08-01
---
# Anaconda

1. Display all the environments
    ```cmd
    conda env list
    ```

2. Get the help for conda env
   ``` cmd
    conda env -h
   ```
   
3. Release the space
    
    3.1 Delete useless packages
    ```cmd
    conda clean -p 
   ```
   3.2 Delete the .tar files
   ```cmd
   conda clean -t 
   ```
              
4. Create a new environment
    ```cmd
    conda create -n your_env_name python=x.x
    ```
              
5. Clone an environment

    The new environment will be under the Anaconda installation path, normally under 'D:\Anaconda3\envs\'
    
    I've tried this one, and it's OK:
    ```cmd
    conda create -n B --clone A
    ```
    When having the path of A, you can also (I have not tried yet):
    ```cmd
    conda create -n B --clone D:\A
    ```
6. Enter an environment
    ```cmd
    conda activate env_name
    ```
7. Exist an environment
    ```cmd
    deactivate env_name
    ```

8. Remove a whole env
    ```cmd
    conda remove -n your_env_name --all
    ```
9. Delete a package
    ```cmd
    conda remove --name $your_env_name  $package_name 
    ```
              
9. Set the mirror (to speed up download)
    
    a.Add the mirror

    ```cmd
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    ```

    b. Show the channel urls when searching

    ```cmd
    conda config --set show_channel_urls yes
    ```
    c. Remove the settings you've made:
    ```cmd
    conda config --remove-key channels
    ```

10. Without setting a mirror, you could also add an url after the installation instruction everytime manually.
    ```cmd
    pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple/
    ```
### Export the current environment to filename.yaml
- Export the packages installed by conda
   - Non-base env, export directly
      ```cmd
      conda env export > filename.yaml
      ```
   - base env: first clone, enter the cloned env, then export.
     ```cmd
     conda create -n new_name --clone base
     ```
     You can delete the cloned env if necessary.
     ```cmd
     conda remove -n new_name --all
     ```
- Export the packages installed by pip
     ```cmd
      pip freeze > pipenv.txt
     ```
### Create a new environment using filename.yaml on the other machine
  ``` cmd
     conda env create -f filename.yaml
  ```
  ``` cmd
     pip install -r pipenv.txt
  ```

### Pip things
1.
  ``` cmd
  pip install setuptools -U
  ```
2.
  ``` cmd
  pip install setuptools -U
  ```
3. Using the Command Line to Install Packages from GitHub directly
Before running the command below, please make sure your virtual environment installed packages: git and pip.
If not, conda install git, conda install pip.
  ``` cmd
  pip install git+https://github.com/kernc/backtesting.py.git
  ```
