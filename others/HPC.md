1. login
    ```cmd
   ssh ID@SERVER
    ```
### Operations
vim xx       view xx
i   insert contents
:wq   save and quit
:!q   do not save and quit
Click the right mouse button  paste.   'control v' does not work for bash??linux

### For the freshman, install Miniconda3
1. Download
    ```cmd
   wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh --no-check-certificate
    ```
2. Activate. Follow the instructions. If 'No space' error, contact with the admin.
    ```cmd
   bash Miniconda3-py38_4.8.3-Linux-x86_64.sh
    ```
   3. Add path
   ```cmd
      vim 
   ```
```cmd
      # >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/mail/YOUR_GRADE/YOUR_ID/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/mail/YOUR_GRADE/YOUR_ID/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/mail/YOUR_GRADE/YOUR_ID/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/mail/YOUR_GRADE/YOUR_ID/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```
