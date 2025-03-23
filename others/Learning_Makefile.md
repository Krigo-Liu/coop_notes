---
title: How to use the Makefile
icon: file
order: 1
author: Krigo
category:
    - CS
tag:
    - Computer Sience
    - Makefile
footer: It is a time to learn Makefile and use the stupid BNU servers
copyright: 随便用
date: 2024-05-30
---

## Introduction

`Makefile` 定义了一系列的规则来指定，哪些文件需要先编译，哪些文件需要后编译，哪些文件需要重新编译，甚至进行更复杂的操作。

`Makefile` 带来的好处 —— “自动化编译”。写好后，只需要一个make命令，整个工程完全自动编译。
    - `make` 是一个命令工具，一个解释 `Makefile` 中指令的命令工具
      - `Delphi`： `make`
      - `Visual C++`: `nmake`
      - `Linux`: GNU `make`