# Anaconda
    1. 查看电脑所有环境 conda env list
    2. 查看环境管理的全部命令 conda env -h
    3. 升级完成后可以用命令清理无用的包释放空间 
        conda clean -p 删除没用的包
        conda clean -t 删除保存的压缩文件.tar
    4. 新建环境
        conda create -n your_env_name python=x.x
    5. 克隆环境:
        生成的新的环境的位置在anaconda的安装路径下，一般情况在D:\Anaconda3\envs\文件夹下。
        a. 已有A，生成B：conda create -n B --clone A
        b. 已有路径D:\A，生成B: conda create -n B --clone D:\A
    6. 进入/退出环境
        a. conda activate env_name
        b. deactivate env_name
    7. 删除整个环境
        conda remove -n your_env_name --all
    8. 删除整个包
        conda remove --name $your_env_name  $package_name 
    9. 设置国内镜像
        http://Anaconda.org的服务器在国外，安装多个packages时，conda下载的速度经常很慢。清华TUNA镜像源有Anaconda仓库的镜像，将其加入conda的配置即可：
    
        a. 添加Anaconda的TUNA镜像,TUNA的help中镜像地址加有引号，需要去掉
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    
        b. 设置搜索时显示通道地址
        conda config --set show_channel_urls yes
    
        #恢复默认镜像 conda config --remove-key channels

    10. 若不设置默认镜像，就每次手动 pip install package_name   -i https://pypi.tuna.tsinghua.edu.cn/simple/  
   
    
# Git
### 账户、连接
    1. 设置邮箱  git config --global user.email xxxx

    2. 显示所有 Git 配置设置的列表以及每个设置的来源      
                git config --list --show-origin
    3. 测试连接  ssh -T git@github.com
    4. 换接口    git config --global http.proxy "http://127.0.0.1:8080"
### 仓库
先进入要操作的git仓库文件夹：


    1. 克隆仓库  git clone git@...

    2. 添加修改的文件到当前分支
        git add . 添加当前目录下的所有文件到暂存区
        git add [file1] [file2] ... 添加一个或多个到暂存区
        git add [dir] 添加指定目录及子目录到暂存区

    3. 确认修改             git commit -m "commit message"
        
    4. 把修改push到远程仓库  git push
       
    5. 查看当前所处分支及状态 git status
        
    6. 查看当前分支的日志    git log
        
    7. 版本回退到某版本号    git reset --hard 版本号
        Please be cautious when using --hard as it will permanently delete any uncommitted changes.
        文件最好放在另一个地方先备份好。
            
        回退到最新commit:     git reset --hard

    8.创建分支新分支'dev':  git checkout -b dev
        
    9. 切换当前显示的分支到 main 分支: git checkout main
        
    10. 合并分支dev到当前分支    git merge dev --no-ff 
        --no-ff: 禁用快进合并。这意味着即使当前分支可以简单地通过快进来包含 dev 分支的更改，Git 仍然会创建一个新的合并提交。 
    11. 删除分支dev             git branch --delete dev  

        
# Others
    1. 命令行输错的时候 control+c 一下，就可以重新输入了