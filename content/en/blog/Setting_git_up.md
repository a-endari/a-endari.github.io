---
title: Setting git up!
author: Abbas Endari
date: 2024-08-20
description: How to setup git after installation. (concise version)
tags:
  - Admin
  - git
  - windows
  - mac
  - linux
  - tutorial
thumbnail: /git_banner.jpeg
_build:
  render: true
  list: true
  publishResources: true
---
# To Config git

### take the steps bellow and your basic git setup is done in minutes

## There are 3 levels of configurations

**Commands to edit each Settings level:**

``` shell
git config --sytem <setting to edit> <setting value> 

git config --global <setting to edit> <setting value> 

git config --local <setting to edit> <setting value> 
```

**Scope**

*SYSTEM* : All Users of current computer

*GLOBAL*: All repositories of current user

*LOCAL*: The current Repository

## The Settings

### Line Endings

- Configure Git to ensure line endings in files you checkout are correct for Windows.
- For compatibility, line endings are converted to Unix style when you commit files.

- For Windows = true

``` shell
git config --global core.autocrlf true
```

- For Mac or Linux = input

```shell
git config --global core.autocrlf input
```

### The User Name

- Double quotes are present because we have space in our name!

``` shell
git congif --global user.name "<user's name>" 
```

### The Email address

```shell
git config --global user.email name@domain.com 
```

### The Default Editor (Editor must be added to path)

- --wait makes the terminal wait for the edit to finish

```shell
git config --global core.editor "code --wait" 
```

## To open settings in the editor

```shell
git config --global -e 
```

### My Prettified git log

```shell
    git config --global alias.glog "log --pretty=format:'%C(yellow)%h %C(blue)%ad %C(cyan)| %Creset%s%C(red)%d%Creset [%C(green)%an%Creset]' --graph --date=short"
```

### To list all settings and their origin

```shell
git config --list --show-origin
```

### To Disable pager for a specific command

```shell
git config --global pager.log false
# or pager.diff  for diff, and ...
```
