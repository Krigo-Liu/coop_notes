# Anaconda

1. Display all the environments
    ```python
    conda env list
    ```

2. Get the help for conda env
   ``` python
    conda env -h
   ```
   
3. Release the space
    
    3.1 Delete useless packages
    ```python
    conda clean -p 
   ```
   3.2 Delete the .tar files
   ```python
   conda clean -t 
   ```
              
4. Create a new environment
    ```python
    conda create -n your_env_name python=x.x
    ```
              
5. Clone an environment

    The new environment will be under the Anaconda installation path, normally under 'D:\Anaconda3\envs\'
    
    I've tried this one, and it's OK:
    ```python
    conda create -n B --clone A
    ```
    When having the path of A, you can also (I have not tried yet):
    ```python
    conda create -n B --clone D:\A
    ```
6. Enter an environment
    ```python
    conda activate env_name
    ```
7. Exist an environment
    ```python
    deactivate env_name
    ```

8. Remove a whole env
    ```python
    conda remove -n your_env_name --all
    ```
9. Delete a package
    ```python
    conda remove --name $your_env_name  $package_name 
    ```
              
9. Set the mirror (to speed up download)
    
    a.Add the mirror

    ```python
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    ```

    b. Show the channel urls when searching

    ```python
    conda config --set show_channel_urls yes
    ```
    c. Remove the settings you've made:
    ```python
    conda config --remove-key channels
    ```

10. Without setting a mirror, you could add an url after the install instruction everytime manually.
    ```python
    pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple/
    ```