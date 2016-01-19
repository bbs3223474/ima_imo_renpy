## Define area. For every in-game experiences.
## 定义区域。用于任何游戏中的体验效果。
define dis = dissolve
define Dis = Dissolve(1.0)
define dis05 = Dissolve(0.5)
define dis15 = Dissolve(1.5)
define dis2 = Dissolve(2.0)
define dis3 = Dissolve(3.0)
define dis5 = Dissolve(5.0)
define dis7 = Dissolve(7.0)
define su = CropMove(1.0, mode="slidedown", startpos=(1280, 720), endpos=(1280, 1440))
define mu = MoveTransition(1.0, enter=None, leave=None, old=False, layers=['master'], time_warp=None, enter_time_warp=None, leave_time_warp=None)

image black = "#000"
image white = "#fff"
define r = Character ('陸斗')
define on = Character ('女の子')

## Add a defined character for test use.
## 添加一个定义好的角色用于测试。
# define r = Character('璃　紗', color="#ffffff")

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