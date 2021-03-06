﻿## Define area. For every in-game experiences.
## 定义区域。用于任何游戏中的体验效果。
define dis = dissolve
define Dis = Dissolve(1.0)
define dis03 = Dissolve(0.3)
define dis05 = Dissolve(0.5)
define dis15 = Dissolve(1.5)
define dis2 = Dissolve(2.0)
define dis3 = Dissolve(3.0)
define dis5 = Dissolve(5.0)
define dis7 = Dissolve(7.0)
define su = CropMove(1.0, mode="slidedown", startpos=(1280, 720), endpos=(1280, 1440))
define mu = MoveTransition(0.2)
define move03 = MoveTransition(0.3)
define eyeclose = ImageDissolve("tr/eyeopen.png", 1.0)
define eyeopen = ImageDissolve("tr/eyeclose.png", 1.0)
define bomb1 = ImageDissolve("tr/bomb2.png", 0.5)

image black = "#000"
image white = "#fff"
define r = Character ('陸斗')
define on = Character ('女の子')
define x = Character ('？？')
define m = Character ('奉莉')
define a = Character ('歩夢')
# 尽管上面定义了一些常见角色的名称，但实际上在使用buriko2rpy工具转换脚本的时候，
# 角色名称已经直接准备好，因此不如直接使用而非使用define去从头定义。
# Though some define statements was presented above, but when we're using buriko2rpy tool
# to convert scripts, the characters' name has already been prepared. So it will be easier
# to use them directly rather than use define statement.

## Add a defined character for test use.
## 添加一个定义好的角色用于测试。
# define r = Character('璃　紗', color="#ffffff")

## Add transitions contain in original game.
## 添加原游戏中的转场特效。
# init:
#  $ eyeclose = ImageDissolve("tr/eyeclose.png", 2.0)

###############################################################
## Scripts below are for splash screen.
## 以下代码用于启动界面。

## Add splashscreen ahead of main menu.
## 在主菜单前加入启动画面与动画。
label splashscreen:
 scene black
 $ _skipping = True
 $ _dismiss_pause = False
 scene bg1 f_logo02_s01
 with dis15
 pause 4
 scene white
 with Dis

 ## It's very interesting when using "voice" statement, the system voice can only play when movie shows,
 ## but I want it to play when "f_logo01_s01" appears. Finally I found "play" argument can solve this problem.
 ## 当使用“voice”命令时，发生了很有趣的事情。系统语音只会在视频播放时出现，而我希望它在“f_logo01_s01”时就播放，
 ## 最终我发现“play”命令解决了这个问题。
 $ _skipping = False
 $ _dismiss_pause = False
 scene bg1 f_logo01_s01
 with Dis
 play sound "vo1/sys_00001.ogg"
 pause 1.5

 $ _skipping = True
 $ _dismiss_pause = True
 scene white
 with Dis
 $ renpy.movie_cutscene('movie/00a_grop.avi')

 ## Simply added voice when entering the main menu. This can play when movie finished playing or beeing skipped.
 ## 简单地添加了进入主菜单时的语音。它能够在视频播放完毕或被跳过时播放。
 play sound "vo1/sys_00002.ogg"
 return

## This is the end of splash screen scripts.
## 这是启动界面代码的结束点。
###############################################################

label start:
scene black
stop music fadeout 1
with Fade(0.5, 1.0, 0.5)
jump ev0000
