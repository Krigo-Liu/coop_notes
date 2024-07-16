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