label ev0090:
## Eyecatch
## 过场动画
scene white
with dis03
pause 0.3
scene bg2 eyecatch_s01
with dis03
pause 1.5
scene black
with dis03

scene bg2 is_ecg04b_s04
with dis2

# se001_003l
play se2 "se001_003l" loop
"……"
"…………"
"………………"
stop se2

play se "se001_002"

scene bg2 is_ecg04b_s05
with dis
play music "bgm_m02"

voice "rikuto_10193"

"陸斗" "「もしもし？」"

voice "matsuri_10110"
"奉莉" "「あ、陸斗？　いま大丈夫？」"

voice "rikuto_10194"

"陸斗" "「うん、大丈夫だけど」"

voice "matsuri_10111"
"奉莉" "「今どこ？」"

voice "rikuto_10195"

"陸斗" "「家だよ」"

voice "matsuri_10112"
"奉莉" "「そう、だったら今から昨日の寿司桶取りに行っていい？」"

voice "rikuto_10196"

"陸斗" "「いいよ」"

voice "matsuri_10113"
"奉莉" "「じゃ、今から行くからねー」"

voice "rikuto_10197"

"陸斗" "「了解」"

play se "se001_002"

scene bg1 bg13_s01
with Dis
"電話を終わらせて、時刻を確認する。"
"ええと……３時半か……"
"昼ご飯を適当に済ませた後、だらだらしてるうちにこんな時間になってしまった。"
"受験が終わったら、あれしよう、これしようなんて考えていたけど、全然できてない。"
"せいぜいやれてるのはほぼ日課にしているサッカーボールを使ってのリフティングくらい……"
"だけど、それは好きでやってるもので、奉莉のように家を手伝っているわけじゃない。"
"そう考えると、自分はなんだか怠けているようでちょっとした罪悪感を……"

voice "rikuto_10198"

"陸斗" "「んん――――――っ！！」"
"大きく伸びをした後、ベッドの上で読んでいたサッカー雑誌を閉じた。"
"俺ももうちょっと、まじめにやるか。"
"今日からはまた普通に晩ご飯も作らないとならないし。"

play se "se006_001"
"ぴんぽーん"

voice "rikuto_10199"

"陸斗" "「ん？　早いな？」"
"奉莉の家からの距離を考えると、少し到着が早いような気がする。"
"まあ、道の途中から電話してきたのかもしれないし……"

play se "se007_004"
scene black
with Dis

voice "rikuto_10200"

"陸斗" "「はーい、いま開けるよー」"

play se "se007_003"

play music "bgm_m27"

scene bg1 bg15_s01
show ch5c 08mika02m05 at c
with bomb1

voice "miku_10001"
"未玖" "「お兄ちゃぁ――――んっ！！」"
show ch5c 08mika02m05 with dis:
 xalign 0.5 yalign -0.8
 linear 0.5 yalign -0.3 zoom 1.5 alpha 0.0

voice "rikuto_10201"

"陸斗" "「うおっ！？」"

play se "se002_003"
play se "se002_003"
scene bg1 bg15_s01
with vpunch
"どすん、ばたーん！！！"

voice "rikuto_10202"

"陸斗" "「いたたたたたた……」"
hide ch5c 08mika02m05
show ch5c 08mikb02m18:
 xalign 0.5 yalign -1.8
 linear 0.3 yalign -0.8
with dis03

voice "miku_10002"
"未玖" "「大丈夫？」"

voice "rikuto_10203"

"陸斗" "「大丈夫じゃない！　とりあえず俺の上から降りてっ！」"

show ch5c 08mikb02m07 with dis:
 xalign 0.5 yalign -0.8
 pause 0.5
 linear 0.5 xalign 0.0 yalign -1.0 alpha 0.0

voice "miku_10003"
"未玖" "「はーい……よいしょっと」"

show ch5f 08mikb02s03:
 xalign 0.5 yalign -1.8
 linear 0.5 yalign -1.25
with dis

voice "miku_10004"
"未玖" "「ただいま、お兄ちゃん！」"

voice "rikuto_10204"

"陸斗" "「……お帰り、未玖」"
"我が家を訪れたのは、奉莉ではなくお隣に住む未玖だった。"
"一昨日の夜から、未玖のお父さんと北海道旅行に出てたんだけど、もう戻ってきたのか……"
# hide ch5f 08mikb02s03
show ch5f 08mikb02s04 with dis:
 xalign 0.5 yalign -1.25
 pause 0.5
 linear 0.15 yalign -1.0
 linear 0.15 yalign -1.25

voice "miku_10005"
"未玖" "「お兄ちゃん、朝岡合格おめでとーっ！！」"

voice "rikuto_10205"

"陸斗" "「あー、ありがと」"
hide ch5f 08mikb02s04
show ch5f 08mikb02s03 at c
with dis
voice "miku_10006"
"未玖" "「昨日お兄ちゃんが合格メールくれたとき、北海道の道の真ん中で万歳しちゃった」"

voice "rikuto_10206"

"陸斗" "「そっか……で、北海道はどうだった？」"

show ch5f 08mika02s04 at c
with dis
voice "miku_10007"
"未玖" "「んー、雪ばっか降ってて寒かった。でも、食べ物はおいしかったよ」"

voice "rikuto_10207"

"陸斗" "「北海道の食べ物か……確かにおいしそうだ」"

show ch5f 08mika02s21 at c
with dis
voice "miku_10008"
"未玖" "「だけど、どーせなら雪祭りが見たかったよ。なんで、終わった直後に旅行なんて……」"

voice "rikuto_10208"

"陸斗" "「おじさんの出張に合わせた旅行だから仕方がないさ」"

show ch5f 08mikb02s01 at c
with dis
voice "miku_10009"
"未玖" "「そうなんだけど、ものすごく損した気分……と、思い出したっ！」"

voice "rikuto_10209"

"陸斗" "「ん？」"
## When I use "show ch5c 08mikb02m04 at c" in here, game shows nothing on the screen,
## but when I write like above it becames normal. I don't know why.
## 当我在这里用“show ch5c 08mikb02m04 at c”时，屏幕上没有任何显示，
## 但我像下面这样写的时候，它又正常了，我不知道为什么会这样。
hide ch5f 08mikb02s01 at c
show image "ch5c/08mikb02m04.png" at c
with dis
voice "miku_10010"
"未玖" "「はいっ、おみやげっ！」"

voice "rikuto_10210"

"陸斗" "「ああ、ありがと」"
# hide image "ch5c/08mikb02m04.png" at c
show image "ch5c/08mikb02m04.png":
 xalign 0.5 yalign -1.25
 linear 0.15 yalign -1.45
 linear 0.15 yalign -1.25
 linear 0.15 yalign -1.45
 linear 0.15 yalign -1.25


voice "miku_10011"
"未玖" "「ねえねえ、開けてみて！」"

voice "rikuto_10211"

"陸斗" "「えっ？　でも、これ……あれだよね？」"
"包装紙を見るに、これは北海道でもっともポピュラーなお菓子のおみやげだと思うんだけど……"
hide image "ch5c/08mikb02m04.png"
show ch5c 08mikb02m05 at c
with dis
voice "miku_10012"
"未玖" "「いいからいいから開けてみて！」"

voice "rikuto_10212"

"陸斗" "「わかったってば」"
hide ch5c 08mikb02m05 at c
with dis
"未玖に催促されて、包装紙をむいていく。"

voice "rikuto_10213"

"陸斗" "「えーと……ああ、やっぱり」"
"予想どおり、白い箱が出てきた。"
stop music fadeout 1
"でも……あれ……？"

voice "rikuto_10214"

"陸斗" "「なんか、違う？」"

voice "miku_10013"
"未玖" "「よく見てよ」"

play music "bgm_m12"

show bg2 is_ecg14_s01 as fr
with Dis

voice "rikuto_10215"

"陸斗" "「えーと……ひどい、恋人……？」"
hide bg2 is_ecg14_s01 as fr
show ch5f 08mika02s05 at c
with dis
## Ignored a effect that shakes the character's image.
## 这里忽略了一个角色图像抖动的效果。

voice "miku_10014"
"未玖" "「あははははははははは」"

voice "rikuto_10216"

"陸斗" "「なにこれ？　類似品？」"

show ch5f 08mika02s07 at c
with dis
voice "miku_10015"
"未玖" "「もう最高でしょ！　空港で見つけたとき大爆笑しちゃった」"

voice "rikuto_10217"

"陸斗" "「こんなもの売ってるのか……」"
"それにしても……これはひどい。"
"誰がこんなデザインを……"

show ch5f 08mika02s03 at c
with dis
voice "miku_10016"
"未玖" "「あ、でも、中身は本物とだいたい同じだと思うから、おじさんと食べてね！」"

voice "rikuto_10218"

"陸斗" "「わかった……」"

show bg1 bg_dark as fr
with dis
"にしても、未玖のおみやげセンスはやっぱりどこかズレてる。"
"前に北陸へ行ったときは、マス寿司に似せたクッキーとか買ってくるし。"
"しかもあれ、クッキーと言いながら上層部に羊羹がのってたんだよな……"

play music "bgm_m27"
hide bg1 bg_black as fr
with dis

show ch5f 08mikb02s04 at c
with dis
voice "miku_10017"
"未玖" "「お兄ちゃん、ようやく受験が終わったね」"

voice "rikuto_10219"

"陸斗" "「まあね」"

show ch5f 08mikb02s03 at c
with dis
voice "miku_10018"
"未玖" "「じゃあ……いいよね？」"

voice "rikuto_10220"

"陸斗" "「何が？」"

show ch5f 08mikb02s04 at c
with dis
voice "miku_10019"
"未玖" "「わかってるくせに……えいっ！！」"
hide ch5f 08mikb02s04 at c
with dis03

show ch5c 08mika02m04 with dis03:
 xalign 0.5 yalign -1.0
 linear 0.2 yalign -1.25
"がばっと未玖が俺に抱きついてきた。"
show ch5c 08mika02m04:
 xalign 0.5 yalign -1.25
 linear 0.2 yalign -1.45
 linear 0.2 yalign -1.25
voice "rikuto_10221"

"陸斗" "「っと」"
"最初のときと違い、こちらは予想していたのできっちり受けとめる。"
"すると未玖は俺の胸に顔を寄せ、そのまま頬ずりをはじめた。"

show ch5c 08mika02m23 with dis:
 xalign 0.5 yalign -1.25
 pause 0.35
 linear 0.2 yalign -1.10
 linear 0.2 yalign -1.25

voice "miku_10020"
"未玖" "「んー……お兄ちゃん」"

"陸斗" "「…………」"
show ch5c 08mika02m23:
 xalign 0.5 yalign -1.25
 linear 0.2 yalign -1.10
 linear 0.2 yalign -1.25

voice "miku_10021"
"未玖" "「お兄ちゃん、お兄ちゃん、お兄ちゃん」"

"陸斗" "「…………」"
show ch5c 08mika02m23:
 xalign 0.5 yalign -1.25
 linear 0.2 yalign -1.10
 linear 0.2 yalign -1.25
 linear 0.2 yalign -1.10
 linear 0.2 yalign -1.25

voice "miku_10022"
"未玖" "「お兄ちゃん、お兄ちゃん、お兄ちゃん、お兄ちゃん、お兄ちゃーんっ！」"

voice "rikuto_10222"

"陸斗" "「……そろそろいい？」"
hide ch5c 08mika02m23 at c
show ch5c 08mika02m09 at c
with dis
voice "miku_10023"
"未玖" "「ダメ」"

voice "rikuto_10223"

"陸斗" "「もう十分じゃないの？」"

show ch5c 08mika02m10 at c
with dis
voice "miku_10024"
"未玖" "「足りない足りない足りないよーっ！　お兄ちゃんが受験の間、ずっとガマンしてたんだからーっ！！」"

show bg1 bg_dark as fr
with dis
"以前はほぼ毎日のようにウチへ来ていた未玖。"
"だけど、ここ半年はウチへ遊びにくる頻度をぐんと落としていた。"
"だから、未玖がその分を取り返そうとしているのはわかる。"
"わかるけど……"
hide bg1 bg_black as fr
with dis

show ch5c 08mika02m25 at c
with dis

voice "miku_10024b"
"未玖" "「んっ」"

voice "rikuto_10224"

"陸斗" "「……どうして、目を閉じて唇突き出してるの？」"

show ch5c 08mika02m24 at c
with dis
voice "miku_10025"
"未玖" "「もう、わかるでしょお兄ちゃん。女に恥かかせないでよ」"

voice "rikuto_10225"

"陸斗" "「女って……小学生がなに言ってるんだか」"

show ch5c 08mika02m19 at c
with dis
voice "miku_10026"
"未玖" "「春になったら中学生だよ！　もう大人みたいなもんじゃない」"

voice "rikuto_10226"

"陸斗" "「大人みたい……？」"
"じっと未玖の顔を見る。"
"どっからどう見ても、子供だよ。"
"ぎゅっとこちらに密着させてる身体だって、ほとんど凹凸を感じないし……"

show ch5c 08mika02m15 at c
with dis
voice "miku_10027"
"未玖" "「ね、半年もガマンしたんだよ？　このくらいご褒美があってもいいじゃない」"

voice "rikuto_10227"

"陸斗" "「ダメ」"

show ch5c 08mika02m03 at c
with dis
voice "miku_10028"
"未玖" "「じゃあ、逆に考えようよ。これはお兄ちゃんのご褒美なんだって」"

voice "rikuto_10228"

"陸斗" "「……俺の？」"

show ch5c 08mika02m04 at c
with dis
voice "miku_10029"
"未玖" "「そう、かわいいかわいい未玖ちゃんのファーストキスが、ご・ほ・う・び！」"

voice "rikuto_10229"

"陸斗" "「お気持ちだけで結構ですから」"

show ch5c 08mika02m07 at c
with dis
voice "miku_10030"
"未玖" "「そんな遠慮しなくてもいいよ、減るもんじゃないし！」"

voice "rikuto_10230"

"陸斗" "「減るってば。ファーストキスは１回しかないし」"

show ch5c 08mika02m25 at c
with dis
show ch5c 08mikb02l25:
 xalign 0.5 yalign 1.55
 zoom 0.6
with dis03
voice "miku_10031"
"未玖" "「あーもう、こうなったら強硬手段！　んんんーっ！」"

voice "rikuto_10231"

"陸斗" "「こ、こら、顔近づけてくるなっ！」"
hide ch5c 08mikb02l25
show ch5c 08mikb02l25:
 xalign 0.5 yalign -0.75
 zoom 0.7
with dis03

voice "miku_10032"
"未玖" "「んんんんん――っ！！」"

voice "matsuri_10114"
"？？" "「いけっ！　そこだっ！」"

voice "rikuto_10232"

"陸斗" "「や、やめろぉ――――――っ！！」"
show ch5c 08mikb02l25:
 xalign 0.5 yalign 0.1
 zoom 1.0
with dis03

voice "miku_10033"
"未玖" "「んんんんんんんんんんんん――――――っ！！！」"

voice "matsuri_10115"
"？？" "「もうちょっと、ほらっ、頑張れ未玖っ！！」"

voice "rikuto_10233"

"陸斗" "「ぬうううううううううっ……って、奉莉！？」"

play music "bgm_m24"
hide ch5c 08mikb02l25
with dis
show ch2f 02mata02s04 at right
with dis

voice "matsuri_10116"
"奉莉" "「やっほー、陸斗」"

voice "rikuto_10234"

"陸斗" "「い、いつの間に？」"

show ch2f 02mata02s07 at right
with dis
voice "matsuri_10117"
"奉莉" "「いや、ピンポン鳴らしても全然出てこないし、玄関に鍵も掛かってないからどうしたのかなーと思って……」"

voice "rikuto_10235"

"陸斗" "「見てたんなら助けてよ！」"

show ch5c 08mika02m06 at c
with dis
voice "miku_10034"
"未玖" "「今だっ！　隙ありぃ――――っ！！」"

show ch5c 08mika02m25 with dis03:
 xalign 0.5 yalign 0.0
 linear 0.3 yalign 0.05 zoom 1.6

voice "rikuto_10236"

"陸斗" "「うわっ！？」"
scene black
with dis

voice "miku_10035"
"未玖" "「ちゅ……っ！？」"
"未玖がキスしたのは、ギリギリのところで俺たちの顔の間に差し込まれた、奉莉の手のひらだった。"

scene bg1 bg15_s01
show ch5c 08mika02m25 at c
show ch1c 02matb02m07 at right
with dis

voice "matsuri_10118"
"奉莉" "「はーい、残念でしたー」"

show ch5c 08mika02m10 with dis03:
 xalign 0.5 yalign -1.25
 pause 0.3
 linear 0.15 yalign -0.9
 linear 0.15 yalign -1.25

voice "miku_10036"
"未玖" "「邪魔しないでよ、お祭りっ！」"
show ch1c 02mata02m23 at right
with dis
voice "matsuri_10119"
"奉莉" "「あたしも無粋だとは思ったんだけどさ、陸斗に泣いて懇願されるとねぇ」"

voice "rikuto_10237"

"陸斗" "「いや、泣いてはいないけど……」"
hide ch5c 08mika02m10
hide ch1c 02mata02m23 at right 
with dis

scene bg1 bg15_s01
with Dis
"そう言いながら、抱きつく未玖をゆっくり引きはがした。"

show ch2f 02mata02s03 at right
show ch5f 08mika02s09 at left
with dis

voice "miku_10037"
"未玖" "「もうちょっとだったのに……ちぇっ！」"

voice "matsuri_10120"
"奉莉" "「どうせなら、もう少しロマンティックにしてもらった方がいいんじゃない？」"

show ch5f 08mika02s11 at left
with dis
voice "miku_10038"
"未玖" "「大きなお世話！　だいたいなにしに来たのさ？」"

show ch2f 02mata02s02 at right
with dis
voice "matsuri_10121"
"奉莉" "「あたしは仕事。陸斗、寿司桶は？」"

voice "rikuto_10238"

"陸斗" "「あ、ちょっと待って」"
hide ch5f 08mika02s11 at left
hide ch2f 02mata02s02 at right
with dis
"キッチンの脇に立てかけてあった寿司桶を持ってきて、奉莉に渡す。"

voice "rikuto_10239"

"陸斗" "「はい、ごちそうさまでした」"

show ch2f 02mata02s02 at c
with dis
voice "matsuri_10122"
"奉莉" "「どうだった？　昨日のネタはおいしかった？」"

voice "rikuto_10240"

"陸斗" "「うん……まあ、おいしかったとは思うけど……」"

show ch2f 02mata02s17 at c
with dis
voice "matsuri_10123"
"奉莉" "「けど……？」"

voice "rikuto_10241"

"陸斗" "「ちょっと、いろいろあってね、味がよくわかんなかったというか……」"
hide ch2f 02mata02s17 at c
with dis
show ch5f 08mikb02s13 at c
with dis
voice "miku_10039"
"未玖" "「お兄ちゃん……何かあったの？」"
"心配そうに俺の様子をうかがう未玖。"
"隣の奉莉も同じような顔でこっちを見ている。"

"陸斗" "「…………」"
stop music fadeout 0.5
"一瞬迷ったけど、二人にはきちんと言うことにした。"

play music "bgm_m04"

voice "rikuto_10242"

"陸斗" "「実は……父さんが再婚することになって……」"
hide ch5f 08mikb02s13 at c 
show ch5c 08mikb02m15:
 xalign -0.15 yalign -1.25
 linear 0.3 xalign 0.12
show ch1c 02mata02m18:
 xalign 1.0 yalign 0.0
 linear 0.3 xalign 0.85
with dis

$ renpy.music.play("matsuri_10124", channel="vo2", synchro_start=True)
$ renpy.music.play("miku_10040", channel="vo3", synchro_start=True)
"奉莉·未玖" "「ええっ？　ホントにっ！？」"

voice "rikuto_10243"

"陸斗" "「こんな話で、うそなんかつかないよ……」"

hide ch1c 02mata02m18
show ch1c 02mata02m11 at right
with dis
"奉莉" "「…………」"
hide ch5c 08mikb02m15
show ch5c 08mikb02m12 at left
with dis
"未玖" "「…………」"
"二人は、なんて言っていいかわからないという感じで、俺の腰につけてある時計を見つめた。"
"奉莉も、未玖も、俺が死んだ母さんとの思い出を、すごく大事にしているって知っているから……"

voice "rikuto_10244"

"陸斗" "「ありがと、二人とも心配してくれて」"


show ch1c 02mata02m12 at right
with dis
voice "matsuri_10125"
"奉莉" "「陸斗……」"

show ch5c 08mikb02m13 at left
with dis
voice "miku_10041"
"未玖" "「お兄ちゃん……」"

voice "rikuto_10245"

"陸斗" "「でも、大丈夫だから。昨日のうちに気持ちの整理はつけたし」"


show ch1c 02mata02m11 at right
with dis
voice "matsuri_10126"
"奉莉" "「それって……」"

voice "rikuto_10246"

"陸斗" "「今のところ、反対はしないって決めた」"

show ch5c 08mikb02m15 at left
with dis
voice "miku_10042"
"未玖" "「えっ？　ホント？」"

voice "rikuto_10247"

"陸斗" "「ホントだよ。父さんが新しい奥さんをもらうだけのことだから」"


show ch1c 02mata02m06 at right
with dis
voice "matsuri_10127"
"奉莉" "「……そっか、そういう線引きか」"

show ch5c 08mikb02m18 at left
with dis
voice "miku_10043"
"未玖" "「どういうこと？　未玖よくわかんないよ」"

voice "rikuto_10248"

"陸斗" "「いいよ、わからなくて」"

show ch5c 08mikb02m20 at left
with dis
voice "miku_10044"
"未玖" "「ええー？　なんかお祭りだけわかってる顔してずるいー」"
"そう、ある意味ずるい……大人ぶったずるい決着点。"
"そんな考え、未玖はまだ知らなくたっていい。"
hide ch5c 08mikb02m20 at left
hide ch1c 02mata02m06 at righ
show ch2f 02mata02s03 at c
with dis 

voice "matsuri_10128"
"奉莉" "「で、どんな人？」"

voice "rikuto_10249"

"陸斗" "「あ、うん、それが一切情報なし」"

show ch2f 02mata02s18 at c
with dis
voice "matsuri_10129"
"奉莉" "「ええっ？」"

voice "rikuto_10250"

"陸斗" "「今度会わせるから、そのとき自分で判断しろだって」"

show ch2f 02mata02s21 at c
with dis
voice "matsuri_10130"
"奉莉" "「うわー……いかにもおじさんらしい……」"
hide ch2f 02mata02s21 at c
show ch5f 08mikb02s01 at c
with dis
voice "miku_10045"
"未玖" "「いつ？　いつ会うの？」"

voice "rikuto_10251"

"陸斗" "「まだちゃんと決まってないけど、来月の上旬あたりだってさ」"
show ch5f 08mikb02s13 at c
with dis
voice "miku_10046"
"未玖" "「来月か……き、きちんとご挨拶しないと」"
hide ch5f 08mikb02s13 at c
show ch2f 02mata02s01 at c
with dis
voice "matsuri_10131"
"奉莉" "「なに緊張してるの？」"
hide ch2f 02mata02s01 at c
show ch5f 08mika02s15 at c
with dis
voice "miku_10047"
"未玖" "「だって、未来のお姑さんだよ？　嫌われたりしたら、嫁姑戦争がはじまるんだよ？」"

voice "rikuto_10252"

"陸斗" "「なんの心配してるんだか……」"

show ch5f 08mika02s09 at c
with dis
voice "miku_10048"
"未玖" "「ダメだよお兄ちゃん。そういう夫の無関心が嫁姑関係を悪化させるんだから！」"

hide ch5f 08mika02s09 at c
show ch2f 02matb02s04 at c
with dis

voice "matsuri_10132"
"奉莉" "「あはは、そのとーりだ。もっと言ってやれ、未玖」"
hide ch2f 02matb02s04 at c
show ch5f 08mika02s11 with dis03:
 xalign 0.5 yalign -1.25
 pause 0.3
 linear 0.1 yalign -1.55
 linear 0.1 yalign -1.25

voice "miku_10049"
"未玖" "「いい？　何かあったら夫は無条件で妻の味方をするんだよ！　それが家庭円満の秘訣なんだから」"

voice "rikuto_10253"

"陸斗" "「いったいどこからそんな知識を仕入れてくるんだ……まったく……」"
"呆れながら、肩をすくめる。"
"でも、ちょっとだけありがたかった。"
"未玖の無邪気さが……"
scene black
with dis2
stop music fadeout 1
jump ev0095