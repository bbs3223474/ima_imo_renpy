label ev0020:

"……"
"…………"
"………………"

scene bg1 bg04_s07
with dis2

"自分の手に戻った受験票の番号を確認してから、掲示板を見上げる。"
"あの子から合格しているとは言われてたけど、やっぱり自分の目で確認しないと……"
scene bg2 is_ecg02_s01
with Dis
voice "rikuto_10012"
r "「……あった」"

play music "bgm_m01"
"俺……朝岡に合格したんだな……"
"次第に、合格したという実感が湧いてくる。"
"朝岡を第一志望に決めてから、今日までの受験勉強の日々……"
"いろいろ大変でプレッシャーも感じてたけど、すべてが報われた。"
"なんかこう、全身に絡んでた重たい鎖が全部はずれたような気分。"
"そう、俺は自由だ！"
"未来は、無限だ！！"
"なんだか、春からの学園生活がすごく楽しみになってきた。"
"瞬間、脳裏に浮かんだのは……"

## There's a transition "_DrawFilmSx" in the original game have but Ren'py doesn't, so I decided to ignore it.
## 原游戏里有一个“_DrawFilmSx”的转场特效，但Ren'py里没有，所以我决定不管它了。
scene cg1 is_cg01_s04
with Dis
voice "ayumu_10025"
on "「ふふっ……」"
"印象的なあの子の笑顔――"
"でも、それ以外はなにも知らない。"
"あの子は俺の合格を告げると、すぐにどこかへ行ってしまったから……"
"だけど、ここにいたということは朝岡を受けたんだと思う。"
"あの笑顔から考えると、たぶん合格したんじゃないかな？"
"とすれば、春からはきっと同級生……"

stop music fadeout 0.5
voice "matsuri_10001"
x "「おーい、陸斗ぉーっ！！」"
scene bg1 bg04_s07
with Dis
voice "rikuto_10013"
r "「んっ？」"
"声がした方へ視線を向けると――"

play music "bgm_m24"

show image "ch1c/02matb02m18.png":
 xalign 0.5 yalign 0.0
 linear 0.2 yalign -0.15
 linear 0.2 yalign 0.0
with dis

voice "matsuri_10002"
x "「ちょっと、黙っていなくならないでよ」"
"同じクラスの奈々瀬奉莉がこちらへ駆け寄ってきた。"
"クラスで朝岡を受けたのが俺と奉莉の二人だけだったので、一緒に合格発表を見に来たんだけど……"
voice "rikuto_10014"
r "「あーごめん、受験票が風に飛ばされちゃってさ」"
hide image "ch1c/02matb02m18.png"

## This character image's filename is begin with numbers, Ren'py doesn't support it until 1/21/16 nightly build.
## 这个游戏的立绘文件名以数字开头，Ren'py直到2016年1月21日的每夜版才支持这种图片文件名。
show ch2f 02mata02s17 at c
with dis
voice "matsuri_10003"
m "「飛ばされたって……それで、受験票は見つかったの？」"
voice "rikuto_10015"
r "「うん、親切な女の子が拾ってくれたんだ」"
show ch2f 02mata02s07 at c
with dis
voice "matsuri_10004"
m "「……なるほど」"
voice "rikuto_10016"
r "「ん？」"
voice "matsuri_10005"
m "「いや……そのだらしないニヤけ顔の理由」"
voice "rikuto_10017"
r "「えっ？　そ、そんなにニヤけてた？」"
voice "matsuri_10006"
m "「デレデレ。その娘、よっぽどかわいかったのね」"
voice "rikuto_10018"
r "「んー……」"
scene cg1 is_cg01_s04
with Dis
voice "ayumu_10026"
on "「合格、おめでとうございます！」"
r "「…………」"
voice "matsuri_10007"
m "「うわ、またニヤけた」"
scene bg1 bg04_s07
with Dis
show ch2f 02mata02s07 at c
with dis
voice "rikuto_10019"
r "「えっ？」"
voice "matsuri_10008"
m "「これはもう好きになっちゃったかな？　その娘のこと」"
voice "rikuto_10020"
r "「そ、それはないと思うけど……」"
show ch2f 02mata02s17 at c
with dis
voice "matsuri_10009"
m "「どうして？」"
voice "rikuto_10021"
r "「その娘はあっという間にいなくなったから、好きとか嫌いとか考える時間もなかったし……」"
show ch2f 02mata02s03 at c
with dis
voice "matsuri_10010"
m "「時間は関係ないんじゃない？　世の中には一目惚れなんて言葉もあるわよ？」"
voice "rikuto_10022"
r "「一目惚れってしたことないからよくわからないけど……」"
show ch2f 02mata02s17 at c
with dis
voice "matsuri_10011"
m "「……けど？」"
voice "rikuto_10023"
r "「もう一度会いたい。会って話がしたいとは思う」"
show ch2f 02mata02s20 at c
with dis
voice "matsuri_10012"
m "「ふーん……相当気に入ったみたいね……」"
voice "rikuto_10024"
r "「んっ？」"
show ch2f 02mata02s23 at c
with dis
voice "matsuri_10013"
m "「んーん、なんでもない。その娘とまた会えるといいわね」"
voice "rikuto_10025"
r "「うん。たぶん、会えるんじゃないかと思ってる」"
show ch2f 02mata02s17 at c
with dis
voice "matsuri_10014"
m "「……どうして？」"
voice "rikuto_10026"
r "「ここにいたって事は、あの子も朝岡の受験生だと思うんだ。そして、きっとあの感じからすると受かってるはず……」"
show ch2f 02mata02s03 at c
with dis
voice "matsuri_10015"
m "「なるほど……ということは、あたしも会えるってわけだ」"
voice "rikuto_10027"
r "「えっ？　それって……」"
show ch2f 02matb02s04:
 xalign 0.5 yalign 0.0
 linear 0.2 yalign -0.15
 linear 0.2 yalign 0.0
voice "matsuri_10016"
m "「へへー、合格したぞっ！」"
"特徴的な人なつっこい笑顔にＶサイン。"
"奉莉の喜びが伝わって、俺も嬉しくなる。"
voice "rikuto_10028"
r "「おめでとう、奉莉！」"
hide ch2f 02matb02s04
show ch2f 02mata02s02 at c
with dis
voice "matsuri_10017"
m "「ありがと。一応確認だけど陸斗も……だよね？」"
voice "rikuto_10029"
r "「うん……大丈夫だった」"
"奉莉に笑顔とＶサインを返す。"
"すると奉莉は、満面の笑顔で――"
show ch2f 02mata02s02:
 xalign 0.5 yalign 0.0
 linear 0.2 yalign 0.15
hide ch2f 02mata02s02 at ju with Dissolve(0.2)
show ch1c 02matb02m04:
 xalign 0.5 yalign 0.15
 linear 0.2 yalign 0.0
with dis
voice "matsuri_10018"
m "「陸斗っ！　合格おめでとっ！！」"
play se "se002_008"
"ぎゅっと、俺をハグした。"
"反射的に俺も奉莉をハグする。"
"お互いに照れはない。"
"なぜなら、俺たちは性別を越えた盟友だから。"
scene black
with dis2
stop music fadeout 1

jump ev0030