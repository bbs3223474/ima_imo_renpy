label ev0010:

scene bg2 is_ecg102_s01
with dis2
play music "bgm_m07"
pause 0.5

"上着が必要ないくらい、季節はずれの陽気に恵まれた今日。"
"俺は、人生の大きな別れ道に立っていた。"
"このまま前へ進むことができるのか、それとも別の道へ回されるのか――"

scene bg2 is_ecg02_s01
with dis2

r "「…………」"
"その結果が記された掲示板の前。"
"受験生たちが、真剣な眼差しで自分の受験番号を探している。"
"一足先に結果を知った人たちの反応。"
"笑顔……そして、涙……"
"果たして俺に訪れる結末は……"
play se "se009_001"
hide bg2 is_ecg02_s01
scene bg1 bg00b_s01
with dis
scene bg1 bg00b_s01 at top with move
"ビュウウウウウウっ！！"

voice "rikuto_10001"
r "「あっ！？」"
"突風に受験票をかすめ盗られる。"
voice "rikuto_10002"
r "「ちょ、ま、待てっ！！」"
scene bg1 bg00b_s02
with dis
"風に乗って遠ざかる受験票をあわてて追いかける。"
"でも、掲示板前は混雑していて思うように進めない。"
scene bg1 bg00b_s03
with dis
"ほどなくして受験票は人混みに紛れてしまい、どこにいったのかわからなくなってしまった。"
voice "rikuto_10003"
r "「ああぁ……」"
"こんなときに受験票をなくすなんて、我ながら不注意すぎる。"
"でも、一応番号は覚えているからないならないでも……"
"いやダメだ、確か受験票は入学手続きをするときにいるはず！"
voice "rikuto_10004"
r "「す、すいません、すいませんっ！」"
"再び人混みをかき分け、受験票が飛んでいった方向へ進む。"
"確か……あのへんに……"
voice "rikuto_10005"
r "「……ん？」"
"数メートル先にいる女の子。"
"その娘は、俺を見つめていた。"
stop music fadeout 0.5

scene cg1 is_cg01_s03
with dis2
play music "bgm_m36"
on "「…………」"
"……かわいい。"
"素直に、そう思った。"
"そのかわいい娘は、視線が合っても目を逸らさない。"
"ただ一点……じっと、俺を見つめていた。"
r "「…………」"
on "「…………」"
voice "rikuto_10006"
r "「あ、あの……」"
voice "ayumu_10018"
on "「……えっ？」"
voice "rikuto_10007"
r "「俺に、何か？」"
voice "ayumu_10019"
on "「あ……ご、ごめんなさい……」"
"ちょっと恥ずかしそうに瞳を揺らし、頬を染める女の子。"
"それから改めて、その娘はこちらに視線を戻した。"
voice "ayumu_10020"
on "「……あの、もしかして、受験票を探してますか？」"
voice "rikuto_10008"
r "「あっ、はい、さっき風に飛ばされちゃって……」"
scene cg1 is_cg01_s02
with dis
voice "ayumu_10021"
on "「やっぱりっ！！」"
voice "rikuto_10009"
r "「えっ？」"
scene cg1 is_cg01_s03
with dis
voice "ayumu_10022"
on "「い、いえ……なんでもないです、ごめんなさい」"
voice "rikuto_10010"
r "「はあ……」"
voice "ayumu_10023"
on "「それで、あなたは……三谷、陸斗さん、ですか？」"
voice "rikuto_10011"
r "「あ、はい、そうです。三谷陸斗です」"
"名前を告げるとその娘は――"
scene cg1 is_cg01_s05
with dis
voice "ayumu_10024"
on "「合格、おめでとうございます！」"
"俺がこれから進む道を教えてくれた。"
"とびきりの笑顔で――"
scene black
with dis2
stop music fadeout 1

jump ev0020