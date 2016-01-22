label ev0030:
init python:
    def waitsound():
        ui.soundstopbehavior("se")
        renpy.pause()

"………………"

scene bg2 is_ecg04_s02
with dis2

voice "rikuto_10030"
r "「うん、わかった……じゃ、切るよ」"
play se "se001_002"
scene bg1 bg06_s07
with dis
"父さんとの電話が終わり、ケータイをポケットに入れた。"
play music "bgm_m08"
play se2 "se009_002l" loop
voice "rikuto_10031"
r "「おまたせ」"
show ch2f 02mata02s02 at c
with dis
voice "matsuri_10019"
m "「合格報告は無事済んだ？」"
voice "rikuto_10032"
r "「おかげさまで。それじゃいこっか」"
"奉莉と横並びになって、駅に向かって歩き出す。"
"この後、中学校へ戻って担任に合格報告をしなければならない。"
voice "matsuri_10020"
m "「で、おじさんの反応はどう？」"
voice "rikuto_10033"
r "「普通に喜んでたけど」"
show ch2f 02mata02s17 at c
with dis
voice "matsuri_10021"
m "「普通って……『合格、コングラッチュレーションだっ！！』とか？」"
voice "rikuto_10034"
r "「いや、普段の父さんはそんなんじゃないから。もっと普通に『よくやった』って」"
show ch2f 02mata02s12 at c
with dis
voice "matsuri_10022"
m "「そうなの？　イチゴを語るときはあんなにテンションあがるのに……つまり、おじさんにとって陸斗はイチゴ以下の存在……？」"
voice "rikuto_10035"
r "「イチゴと比べられてもなぁ……」"
stop se2 fadeout 0.5
hide ch2f 02mata02s12 at c
with dis
show ch1c 02matb02m18 at c
with dis
voice "matsuri_10023"
m "「どうして勝負を放棄するようなことを言うの？　諦めちゃダメだってば、もっと理想を高く持とうよ、イチゴ以上になってやろうよ！」"
voice "rikuto_10036"
r "「めちゃめちゃ情熱的に煽ってるけど意味がわからないよ。そもそもイチゴ以上の存在ってなに？」"
hide ch1c 02matb02m18 at c
with dis
show ch2f 02mata02s04 at c
with dis
voice "matsuri_10024"
m "「うーん……ニゴ？」"
voice "rikuto_10037"
r "「ニゴ……？　なにそれ？」"
show ch2f 02mata02s03 at c
with dis
voice "matsuri_10025"
m "「１より２の方が確実に上だと思わない？」"
voice "rikuto_10038"
r "「そりゃそうだけど、イチゴのイチは数字じゃないし。だいたいニゴってなに？　実在するの？」"
show ch2f 02mata02s20 at c
with dis
voice "matsuri_10026"
m "「細かいこと気にするわね」"
voice "rikuto_10039"
r "「なんだ、奉莉の想像上のシロモノか……」"
show ch2f 02mata02s02 at c
with dis
voice "matsuri_10027"
m "「うーん……じゃあ、サンゴでどう？　実在するし、ニゴよりさらに上！」"
voice "rikuto_10040"
r "「いや、サンゴのサンも数字じゃないし……ってか、いつまでこの話続くの？」"
voice "matsuri_10028"
m "「えーと、少なくとも１００年以上」"
voice "rikuto_10041"
r "「１００年って、死ぬまで続くってこと？」"
voice "matsuri_10029"
m "「ううん、もっと続くわ」"
voice "rikuto_10042"
r "「もっと？　いつまで？」"
show ch2f 02mata02s04 at c
with dis
voice "matsuri_10030"
m "「そうね……シゴの世界まで」"
play se "se005_003"
$ waitsound()
voice "rikuto_10043"
r "「……おお！」"
"思わず感心して手をポンと叩いた。"
voice "matsuri_10031"
m "「どうどう？　結構綺麗にオチがついたと思わない？」"
voice "rikuto_10044"
r "「そうだね。で、話を元に戻してもいいかな？」"
show ch2f 02mata02s03 at c
with dis
voice "matsuri_10032"
m "「いいわよ、イチゴの話ね」"
voice "rikuto_10045"
r "「いや、それよりもっと前……っても、ゼロゴの話じゃないからね」"
show ch2f 02mata02s20 at c
with dis
voice "matsuri_10033"
m "「ちっ、先回りされたか」"
voice "rikuto_10046"
r "「で、父さんから伝言があるんだ」"
show ch2f 02mata02s17 at c
with dis
voice "matsuri_10034"
m "「おじさんから？　あたしに？」"
voice "rikuto_10047"
r "「奉莉っていうか、七勢寿司さんに」"
show ch2f 02mata02s02 at c
with dis
voice "matsuri_10035"
m "「あ、もしかして出前？」"
voice "rikuto_10048"
r "「うん。合格祝いってことで」"
show ch2f 02matb02s04:
 xalign 0.5 yalign 0.0
 linear 0.2 yalign -0.15
 linear 0.2 yalign 0.0
voice "matsuri_10036"
m "「まいどありー。で、ご注文は？」"
voice "rikuto_10049"
r "「特上３人前。いつものパターンで」"
hide ch2f 02matb02s04
show ch2f 02mata02s03 at c
with dis
voice "matsuri_10037"
m "「１ネタ２貫にして、バリエーションを増やせばいいのね？」"
voice "rikuto_10050"
r "「そんな感じでお願い」"
show ch2f 02mata02s04 at c
with dis
voice "matsuri_10038"
m "「了解。じゃあ、家に帰ったらお父さんに伝えておくから」"
scene black
with Dis
stop music fadeout 1
"話が一段落したところで、駅が見えてきた。"
"改札に繋がる階段を登っていくと……"
voice "matsuri_10039"
m "「……ん？　なんか騒がしくない？」"
voice "rikuto_10051"
r "「確かに……」"
"改札に近づくほど、ざわめきが大きくなっていく。"
scene bg1 bg07_s01
with Dis
play se2 "se002_021l" loop
voice "rikuto_10052"
r "「向こうに人だかりが……」"
voice "matsuri_10040"
m "「なんだろ？　芸能人でもいるのかな？」"
voice "rikuto_10053"
r "「そういう雰囲気じゃないみたいだけど……」"
"なんというか、色めきだってる感じじゃない。"
play music "bgm_m13"
"もっとこう、張り詰めた雰囲気で……"
stop se2 fadeout 1
voice "moba001_10001"
"絡む男A" "「おい、なんとか言えっ！！」"
"輪の中心から怒鳴り声が聞こえてきた。"
voice "matsuri_10041"
m "「っ、なに？」"
voice "rikuto_10054"
r "「ケ、ケンカかな？」"
"さらに近づき、人垣の合間から騒ぎの中心部を覗くと――"
voice "moba001_10002"
"絡む男A" "「てめぇ……っざけんなぁ！！」"
"今まさに殴られようとしている女の子の姿が目に飛び込んできた。"
"あ、あぶないっ！！！"
play se "se002_001"
play se "se002_001"
"乾いた打撃音に続いてあたりに響いたのは――"
scene bg1 bg07_s01
with vpunch
voice "moba001_10003"
"絡む男A" "「ぐあっ！！」"
"予想外にも殴りかかった男の叫び声だった。"
## Now way can deal with the original zoom in and out effect, so replaced with simple dissolve.
## 原游戏的放大缩小效果无法实现，只好用简单的dissolve效果代替了。
scene cg1 is_cg03_s01
with Dis
voice "rikuto_10055"
r "「あ……」"
"どうやら、女の子は木刀で男の拳を受けとめたらしい。"
"ほっとするが、女の子はピンチを脱したわけじゃない。"
voice "moba002_10001"
"絡む男B" "「ぼ、木刀なんて卑怯じゃねーか！！」"
voice "moba003_10001"
"絡む男C" "「そうだっ！　こっちは素手だぞっ！」"
"やられた男の仲間が女の子ににじり寄る。"
voice "mao_10001"
"女の子" "「……では、三人で一人を囲むのは卑怯ではないと？」"
voice "moba002_10002"
"絡む男B" "「なんだとっ？」"
voice "moba003_10002"
"絡む男C" "「だいたい、そっちが先に絡んできたんだろっ！」"
voice "mao_10002"
"女の子" "「違う。目の前に立っているお年寄りに優先席を譲る気配がなかったから声をかけただけだ」"
voice "moba002_10003"
"絡む男B" "「はあ？　そんなことくらいで声をかける奴なんかいないぞ？」"
voice "mao_10003"
"女の子" "「ここにいるじゃないか」"
voice "moba003_10003"
"絡む男C" "「バ、バカにしてるのかっ！！」"
voice "moba002_10004"
"絡む男B" "「泣いて謝れば許してやったのに……もう女だからって手加減しねーぞっ！！」"
voice "moba001_10004"
"絡む男A" "「待てっ、一人で突っ込むな！」"
voice "moba003_10004"
"絡む男C" "「おっ？　もう大丈夫なのか？」"
voice "moba001_10005"
"絡む男A" "「まだ痛ぇよ」"
voice "moba002_10005"
"絡む男B" "「だったら、３倍にして返してやろうぜ」"
voice "moba001_10006"
"絡む男A" "「おう……まずは囲んで逃げられないようにしろ」"
"女の子" "「…………」"
scene bg1 bg07_s01
with Dis
"ふたたび、男達は女の子を三方から囲んだ。"
show ch2f 02mata02s08 at c
with dis
voice "matsuri_10042"
m "「どう見てもあの男達が悪いわよね？」"
voice "rikuto_10056"
r "「うん、助けないとっ！」"
show ch2f 02matb02s18 at c
with dis
voice "matsuri_10043"
m "「ちょっと陸斗っ！？」"
hide ch2f 02matb02s18 at c
with dis
"なんとか女の子の方へ行こうとするけど、人が邪魔でなかなか前へ進めない。"
hide ch2f 02matb02s18 at c
show ch1c 02mata02m18 at c
with dis
voice "matsuri_10044"
m "「陸斗待ってっ！」"
"そして、奉莉が俺に追いついたところで――"
scene cg1 is_cg03_s01
with Dis
## Since Ren'py cannot play multiple voices at the same time by voice statement but can define multiple sound channels,
## multiple voices playing can be realized by this way and absolutely have to register the sound channels in options.rpy first.
## 因为Ren'py不能通过voice语句同时播放多个语音，但是可以注册多个声音通道，
## 因此多语音同时播放就可以通过以下方式实现，当然首先也要在options.rpy里注册好声音通道。
$ renpy.music.play("moba001_10007", channel="vo2", synchro_start=True)
$ renpy.music.play("moba002_10006", channel="vo3", synchro_start=True)
$ renpy.music.play("moba003_10005", channel="vo4", synchro_start=True)
"絡む男ABC" "「うおおおおぉっ！！」"
play se "se002_010"
"一斉に男達が女の子に殴りかかった。"
"瞬間、真ん中にいた女の子は――"
stop se
voice "mao_10004"
"女の子" "「ふっ……」"
"男達の包囲網からするっと身をかわした。"
$ renpy.music.play("moba001_10008", channel="vo2", synchro_start=True)
$ renpy.music.play("moba002_10007", channel="vo3", synchro_start=True)
$ renpy.music.play("moba003_10006", channel="vo4", synchro_start=True)
"絡む男ABC" "「おおぉっ！？」"
"あやうく同士討ちになりそうになった男達。"
"あわてて女の子の方へ向き直り――"
voice "moba002_10008"
"絡む男B" "「このやろおおぉっ！！」"
"一番近くにいた男がすぐさま殴りかかった。"
play se "se002_017"
$ waitsound()
voice "mao_10005"
"女の子" "「ふ……」"
voice "moba003_10007"
"絡む男C" "「うおおおおっ！！」"
play se "se002_018"
$ waitsound()
voice "mao_10006"
"女の子" "「と……」"
voice "moba001_10009"
"絡む男A" "「りゃあああぁっ！！」"
play se "se002_017"
$ waitsound ()
voice "mao_10007"
"女の子" "「ふ……」"
"次々に殴りかかってくる男達を、女の子は軽くかわしていく。"
"しかも、ただかわしてるわけじゃない。"
"かわした先は、必ず相手が一人しか攻撃できない場所になっている。"
"これなら相手が何人いても、不利にならない――"
voice "rikuto_10057"
r "「……あの子すごいね」"
voice "matsuri_10045"
m "「うん。剣道か何かの有段者じゃないかな？」"
voice "rikuto_10058"
r "「で、どうする？」"
voice "matsuri_10046"
m "「たぶんあたしたちが割って入るより、駅員さんを呼んできたほうがこの場を収められると思う」"
voice "rikuto_10059"
r "「わかった、そうしよう」"
"振り返って駅員を呼びにいこうとした瞬間――"
voice "mobb001_10001"
"女の人" "「え、駅員さんっ！　こっちですこっちでーすっ！」"
voice "mao_10008"
"女の子" "「っ！？」"
"野次馬の中から大きな声があがって、わずかに動揺する女の子。"
"一方、男達は……"
voice "moba002_10009"
"絡む男B" "「ま、まずいっ！」"
voice "moba001_10010"
"絡む男A" "「くそ……」"
voice "moba003_10008"
"絡む男C" "「さっさと逃げるぞっ！！」"
play se "se002_010b"
"あっという間に逃げ支度を整えて、全員輪の中心から離れていった。"
stop music fadeout 1
scene bg1 bg07_s01
with Dis
show ch2f 02mata02s21 at c
with dis
voice "rikuto_10060"
r "「な、なんという逃げ足の速さ……」"
voice "matsuri_10047"
m "「逃げ足だけは一流だわ」"
"奉莉と二人呆れていると、男達のかわりに複数の駅員が女の子を取り囲む。"
hide ch2f 02mata02s21 at c
show ch3f 03maoa04s01 at c
with dis
voice "moba004_10001"
"駅員A" "「キミ、駅構内でケンカは困るよっ！」"
voice "mao_10009"
"女の子" "「申し訳ありません。しかし、自分は手を出していません」"
voice "moba005_10001"
"駅員B" "「うん、まあ、とりあえず話は奥で聞くから」"
voice "mao_10010"
"女の子" "「……奥とは？」"
voice "moba004_10002"
"駅員A" "「だから、駅の事務所」"
voice "mao_10011"
"女の子" "「いや、しかし……」"
"どうも雲行きが怪しい。"
"なんとか、あの子が無実だってことを証明しないと……"
voice "matsuri_10048"
m "「……行くよ、陸斗」"
voice "rikuto_10061"
r "「……うん、わかった」"
"奉莉も同じことを考えていたようだ。"
"先行する奉莉の後についていく。"
voice "moba004_10003"
"駅員A" "「とにかく、話は聞かせてもらわないと……」"
play music "bgm_m24"
show ch3f 03maoa04s01 at sleft with move03
show ch1c 02matb02m18 at cu with dis03
voice "matsuri_10049"
m "「待って待ってっ！」"
show ch3f 03maoa04s16 at sleft
voice "mao_10012"
"女の子" "「っ！？」"
"駅員が女の子を強引に引っ張っていこうとしたところに、奉莉と一緒に割って入る。"
show ch1c 02matb02m09 at cu
with dis
voice "matsuri_10050"
m "「その子、ケンカなんかしてませんでしたよ！」"
voice "rikuto_10062"
r "「そうです、男三人組に一方的に絡まれてました。どう見てもこの人は被害者だと思います」"
voice "moba004_10004"
"駅員A" "「だけどね、木刀を振り回してたわけだし……」"
voice "rikuto_10063"
r "「振り回したりなんかしてませんでしたよ。木刀は自分を守るのに使っただけで、ただの一度も相手を攻撃なんかしてないです」"
show ch1c 02mata02m02 at cu
with dis
voice "matsuri_10051"
m "「そうそう、周りのみなさんもこの子が一切手を出してないの、見てましたよね？」"
"まだ残っている野次馬に奉莉が訴えかけた。"
"すると、複数の人がうんうんと頷いてくれる。"
voice "rikuto_10064"
r "「ほら、目撃者の賛同もこんなにたくさんありますよ？　駅員さん」"
voice "moba004_10005"
"駅員A" "「う、うーん……」"
voice "moba005_10002"
"駅員B" "「しかしなぁ……」"
hide ch1c 02mata02m02 at cu with dis
show ch2f 02mata02s05 at c with dis
"俺が駅員と話している隙に奉莉が女の子に近づき、その両肩に手をぽんと置いた。"
voice "matsuri_10052"
m "「ね、あなたも騒ぎを起こしたって点では、悪いと思ってるんだよね？」"
show ch3f 03maoa04s01 at sleft
with dis
voice "mao_10013"
"女の子" "「当然申し訳ないと思っている」"
voice "matsuri_10053"
m "「だったら、そこは駅員さんに謝って、ほら」"
"そう言って奉莉は女の子の肩をそっと押し、駅員と少し距離を取らせた。"
"駅員たちと向かい合う状態になったところで、女の子は素直に頭を下げる。"
hide ch3f 03maoa04s01 at sleft
hide ch2f 02mata02s05 at c
with dis
show ch1c 03maoc04m10:
 xalign 0.5 yalign 0.12
 linear 0.5 yalign 0.0
 linear 0.5 yalign 0.12
with dis
voice "mao_10014"
on "「……騒ぎを起こして、申し訳ありませんでした」"
hide ch1c 03mao04m10
with dis
"すると、駅員たちは互いに顔を見合わせて……"
voice "moba005_10003"
"駅員B" "「まあ……今回は目撃者の多くがキミを擁護しているようなので……」"
voice "moba004_10006"
"駅員A" "「とりあえず厳重注意ということで、今後はこういう真似はしないようお願いします」"
show ch1c 03maoc04m10:
 xalign 0.5 yalign 0.12
 linear 0.25 yalign 0.0
 linear 0.25 yalign 0.12
with dis
voice "mao_10015"
on "「……お騒がせしたことを、重ね重ねお詫びいたします。申し訳ありませんでした」"
voice "moba004_10007"
"駅員A" "「はい、これからは気をつけてね」"
hide ch1c 03maoc04m10
with dis
"もう一度頭を下げた女の子にそう言って、駅員たちは立ち去った。"
stop music fadeout 1
"なんとか、女の子は罪に問われないで済んだようだ。"
show ch2f 02mata02s04 at right
show ch3f 03maoa04s02 at left
with dis
voice "matsuri_10054"
m "「よかったわね」"
voice "rikuto_10065"
r "「ほっとしたよ」"
play music "bgm_m25"
show ch3f 03maoa04s02:
 yalign 0.0
 linear 0.25 yalign -0.25
 linear 0.25 yalign 0.0
voice "mao_10016"
on "「このたびは本当に助かりました。ありがとうございます」"
voice "rikuto_10066"
r "「頭あげてよ。当然のことをしただけだし」"
show ch2f 02mata02s03 at right
with dis
voice "matsuri_10055"
m "「でもホントよかったわね、余計な時間取られなくて。これから朝岡の合格発表見に行くんでしょ？」"
hide ch3f 03maoa04s02
show ch3f 03maoa04s17 at left
with dis
voice "mao_10017"
on "「えっ？　何故それを？」"
show ch2f 02mata02s02 at right
with dis
voice "matsuri_10056"
m "「ほら、カバンにつけてるお守り、『合格祈願』って書いてあるからきっと受験生なんだろうなって思ってね」"
show ch3f 03maoa04s16 at left
with dis
voice "mao_10018"
on "「あ……ああ……そういうことか……」"
"奉莉のやつ、よく見てるなぁ。"
"俺は全然気づかなかった。"
"でも、朝岡の受験生ってことは、春からこの娘と同じクラスになる可能性もあるってことか。"
"何かの縁で知り合ったんだし、できればそうなってほしい……"
hide ch3f 03maoa04s16 at left
hide ch2f 02mata02s02 at right
with dis
show ch1c 02mata02m17 at c
with dis
voice "matsuri_10057"
m "「っと、陸斗、そろそろ電車が来るわよ」"
voice "rikuto_10067"
r "「え？　あ、ホントだ」"
"かすかに到着予告のアナウンスが耳に届いた。"
show ch1c 02mata02m04 at c
with dis
voice "matsuri_10058"
m "「じゃあ、春に会えるの楽しみにしとくね」"
hide ch1c 02mata02m04 at c
show ch1c 03maoa04m17 at c
with dis
voice "mao_10019"
on "「えっ？　春……もしかして、お二人も朝岡を？」"
hide ch1c 03maoa04m17 at c
show ch1c 02matb02m02 at c
with dis
voice "matsuri_10059"
m "「おかげさまで、朝岡学園次期新入生になることが決まりましたっ！」"
"笑顔でぐっと親指を立てる奉莉。"
"つられるように、俺も親指を立てる。"
hide ch1c 02matb02m02 at c
with dis03
show ch1c 03maoa04m04:
 xalign 0.5 yalign 0.0
 linear 0.2 yalign -0.25
 linear 0.2 yalign 0.0
with dis
voice "mao_10020"
on "「お二人とも、おめでとうございます！」"
hide ch1c 03maoa04m04
with dis03
show ch1c 02matb02m04:
 xalign 0.5 yalign 0.0
 linear 0.15 yalign 0.15
 linear 0.15 yalign 0.0
 linear 0.15 yalign 0.15
 linear 0.15 yalign 0.0
with dis
voice "matsuri_10060"
m "「ありがと、それじゃねっ！」"
hide ch1c 02matb02m04
show ch1c 03maoa04m02 at c
with dis
voice "rikuto_10068"
r "「一緒のクラスになれたらいいねっ！」"
"さっき思ったことをそのまま口にして、俺は女の子に手を振った。"
"そしてそのまま、奉莉と一緒に改札へ向かった。"
scene black
with dis2
stop music fadeout 1
jump ev0035