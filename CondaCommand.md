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