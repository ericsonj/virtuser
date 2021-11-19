#!/usr/bin/env python3

import subprocess
import os
import sys
from pathlib import Path

shell_cmd = sys.argv[1]
home_path = sys.argv[2]
install_file = sys.argv[3]

def getPATH(env: dict) -> str:
    path_list = []
    if 'PATH' in env:
        paths = str(env['PATH']).split(':')
        for p in paths:
            path_list.append()

def getDefaultEnv(vars: list) -> dict:
    user_env = os.environ.copy()
    env = {}

    for var in vars:
        if var in user_env:
            env[var] = user_env[var]

    env["HOME"] = home_path
    env["HOME_VIRT"] = home_path
    
    return env

# SHELL=/bin/bash
# COLORTERM=truecolor
# SUDO_GID=1000
# LC_ADDRESS=es_AR.UTF-8
# LC_NAME=es_AR.UTF-8
# LC_MONETARY=es_AR.UTF-8
# SUDO_USER=ericson
# LOGNAME=melina
# XAUTHORITY=/run/user/1000/gdm/Xauthority
# LC_PAPER=es_AR.UTF-8
# LANG=en_US.UTF-8
# LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
# LESSCLOSE=/usr/bin/lesspipe %s %s
# TERM=xterm-256color
# LC_IDENTIFICATION=es_AR.UTF-8
# LESSOPEN=| /usr/bin/lesspipe %s
# DISPLAY=:0
# SHLVL=1
# LC_TELEPHONE=es_AR.UTF-8
# LC_MEASUREMENT=es_AR.UTF-8
# LC_TIME=es_AR.UTF-8
# PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
# SUDO_UID=1000
# LC_NUMERIC=es_AR.UTF-8
# OLDPWD=/home/ericson

env = getDefaultEnv([
    'SHELL',
    'COLORTERM',
    'SUDO_GID',
    'LC_ADDRESS',
    'LC_NAME',
    'LC_MONETARY',
    'SUDO_USER',
    'LOGNAME',
    'XAUTHORITY',
    'LC_PAPER',
    'LANG',
    'LS_COLORS',
    'LESSCLOSE',
    'TERM',
    'LC_IDENTIFICATION',
    'LESSOPEN',
    'DISPLAY',
    'SHLVL',
    'LC_TELEPHONE',
    'LC_MEASUREMENT',
    'LC_TIME',
    'SUDO_UID',
    'LC_NUMERIC',
    '_OLD_VIRTUAL_PATH',
    'VIRTUAL_ENV'
])

if Path(f"{home_path}/install.sh").exists():
    subprocess.call(['sh', install_file], env=env)

subprocess.call([shell_cmd], env=env)