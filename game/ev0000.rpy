
label ev0000:

## This is the solution of sound waiting statement.
## Using these python scripts and then "$ waitsound("{file}")", so the images can wait for the voices.
## 这是官方给出的等待声音播放的解决方案。
## 通过下列python代码并在脚本中使用“$ waitsound("{文件}")”命令，即可实现图片等待声音播放。
init python:
    def waitsound():
        ui.soundstopbehavior("sound")
        renpy.pause()

# stop music fadeout 1.0
pause 0.5
$ _skipping = True
$ _dismiss_pause = False

play music "bgm_m36"

scene bg2 is_ecg01a_s01
# with Fade(0.5, 1.0, 0.5)
show bg2 is_ecg01a_s27 as bot
with Dis

## 『「おにいちゃんがほしいです」』
play sound "vo1/ayumu_10001.ogg"
show bg2 is_ecg01a_s02 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s02 as top
with Dis

## 『小さい頃、何回そうやって神様にお願いしたかな？』
play sound "vo1/ayumu_10002.ogg"
show bg2 is_ecg01a_s03 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s03 as top
with Dis

## 『いつしか神様にお願いするのはやめてしまったけど、』
play sound "vo1/ayumu_10003a.ogg"
show bg2 is_ecg01a_s04 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s04 as top
with Dis

## 『おにいちゃんがほしいって気持ちは心の中にずっとあったの。』
play sound "vo1/ayumu_10003b.ogg"
show bg2 is_ecg01a_s05 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s05 as top
with Dis

## 『そして、そのお願いが今になって叶うこと』
play sound "vo1/ayumu_10004a.ogg"
show bg2 is_ecg01a_s06 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s06 as top
with Dis

## 『突然、お母さんから知らされた。』
play sound "vo1/ayumu_10004b.ogg"
show bg2 is_ecg01a_s07 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s07 as top
with Dis

## 『いきなりだったから最初はビックリしたけれど、』
play sound "vo1/ayumu_10005a.ogg"
show bg2 is_ecg01a_s08 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s08 as top
with Dis

## 『だんだんうれしくなってきて……』
play sound "vo1/ayumu_10005b.ogg"
show bg2 is_ecg01a_s09 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s09 as top
with Dis

## 『今は、どうしたらいいのかわからないくらい喜んでる。』
play sound "vo1/ayumu_10006.ogg"
show bg2 is_ecg01a_s10 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s10 as top
with Dis

## 『だって……ホントにおにいちゃんが、』
play sound "vo1/ayumu_10007a.ogg"
show bg2 is_ecg01a_s11 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s11 as top
with Dis

## 『わたしにおにいちゃんができるんだよ？』
play sound "vo1/ayumu_10007b.ogg"
show bg2 is_ecg01a_s12 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s12 as top
with Dis

## 『夢以外でも逢える、』
play sound "vo1/ayumu_10008a.ogg"
show bg2 is_ecg01a_s13 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s13 as top
with Dis

## 『現実の、本物のおにいちゃんができるんだよ？』
play sound "vo1/ayumu_10008b.ogg"
show bg2 is_ecg01a_s14 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s14 as top
with Dis

## 『なんだか、夢みたい。』
play sound "vo1/ayumu_10009.ogg"
show bg2 is_ecg01a_s15 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s15 as top
with Dis

## 『でも、ちょっぴり不安もあるの。』
play sound "vo1/ayumu_10010.ogg"
show bg2 is_ecg01a_s16 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s16 as top
with Dis

## 『だって、どんな人なのか、まだわからないし。』
play sound "vo1/ayumu_10011.ogg"
show bg2 is_ecg01a_s17 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s17 as top
with Dis

## 『夢のおにいちゃんみたいに、優しかったらいいんだけど、』
play sound "vo1/ayumu_10012a.ogg"
show bg2 is_ecg01a_s18 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s18 as top
with Dis

## 『もしそうじゃなかったら。』
play sound "vo1/ayumu_10012b.ogg"
show bg2 is_ecg01a_s19 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s19 as top
with Dis

## 『ううん、きっと優しい人だよ。』
play sound "vo1/ayumu_10013a.ogg"
show bg2 is_ecg01a_s20 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s20 as top
with Dis

## 『だって、お母さんが選んだ人の子供だもん。』
play sound "vo1/ayumu_10013b.ogg"
show bg2 is_ecg01a_s21 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s21 as top
with Dis

## 『絶対……優しい人だよ……。』
play sound "vo1/ayumu_10014a.ogg"
show bg2 is_ecg01a_s22 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s22 as top
with Dis

## 『わたしのおにいちゃんになる人だもん。』
play sound "vo1/ayumu_10014b.ogg"
show bg2 is_ecg01a_s23 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s23 as top
with Dis

## 『だから……早く会ってみたい……。』
play sound "vo1/ayumu_10015.ogg"
show bg2 is_ecg01a_s24 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s24 as top
with Dis

## 『そして、会ったらおにいちゃんに言いたい。』
play sound "vo1/ayumu_10016.ogg"
show bg2 is_ecg01a_s25 as top
with Dis
$ waitsound()
pause 0.5
hide bg2 is_ecg01a_s25 as top
with Dis

## 『「わたしが、妹の歩夢です」って。』
play sound "vo1/ayumu_10017.ogg"
show bg2 is_ecg01a_s26 as top
with Dis
$ waitsound()
pause 0.5
scene white
with Dis
stop music fadeout 1
scene black
with dis2

jump ev0010