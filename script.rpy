define dis = dissolve
define Dis = Dissolve(1.0)


label splashscreen:
$ _skipping = False
$ _dismiss_pause = False
scene bg "bg1/f_logo02_s01.png"
pause 3
scene bg "bg1/f_logo01_s01.png"
pause 3
with Dis
$ _skipping = True
$ _dismiss_pause = True
$ renpy.movie_cutscene('movie/00a_grop.mpg')
return