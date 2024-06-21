# 下記import欄
import random
import itertools

# 下記リストデータ（予備・未完）↓
killers = ["トラッパー", "レイス", "ヒルビリー", "ナース", "ハグ", "ドクター", "ハントレス", "シェイプ", "カニバル", "ナイトメア", "ピッグ", "クラウン", "スピリット", "リージョン", "プレイグ", "ゴーストフェイス", "鬼", "デススリンガー", "エクセキューショナー", "ブライト", "ツインズ", "トリックスター", "ネメシス", "セノバイト", "アーティスト", "貞子", "ドレッジ", "ウェスカー", "ナイト", "スカルマーチャント", "シンギュラリティ", "ゼノモーフ", "チャッキー"]
kill_parks_1 = ["不安の元凶", "野蛮な力", "興奮", "捕食者", "血の追跡者", "闇より出でし者", "不屈", "光より出でし者", "ガラクタいじり", "喘鳴", "死恐怖症", "看護婦の使命", "呪術：第三の封印", "呪術：破滅", "呪術：貪られる希望"]
kill_parks_2 = []


# 下記辞書型データ
dictionary_1 = {
    "トラッパー": ["不安の元凶", "野蛮な力", "興奮"]
    ,"レイス": ["捕食者", "血の追跡者", "闇より出でし者"]
    ,"ヒルビリー": ["不屈", "光より出でし者", "ガラクタいじり"]
    ,"ナース": ["喘鳴", "死恐怖症", "看護婦の使命"]
    ,"ハグ": ["呪術：第三の封印", "呪術：破滅", "呪術：貪られる希望"]
    ,"ドクター": ["圧倒的存在感", "観察＆虐待", "オーバーチャージ"]
    ,"ハントレス": ["猛獣", "縄張り意識", "呪術：女狩人の子守唄"]
    ,"シェイプ": ["最後のお楽しみ", "弄ばれる獲物", "消えゆく灯"]
    ,"カニバル": ["ノックアウト", "バーベキュー＆チリ", "フランクリンの悲劇"]
    ,"ナイトメア": ["ファイアー・アップ", "リメンバー・ミー", "血の番人"]
    ,"ピッグ": ["悶絶のフック：処刑人の妙技", "監視", "選択は君次第だ"]
    ,"クラウン": ["まやかし", "ピエロ恐怖症", "イタチが飛び出した"]
    ,"スピリット": ["怨霊の怒り", "呪術：霊障の地", "怨恨"]
    ,"リージョン": ["不協和音", "狂気の根性", "アイアンメイデン"]
    ,"プレイグ": ["堕落の介入", "伝播する怖気", "闇の信仰心"]
    ,"ゴーストフェイス": ["地獄耳", "戦慄", "隠密の追跡"]
    ,"鬼": ["残心の戦術", "血の共鳴", "天誅"]
    ,"デススリンガー": ["変速機", "死人のスイッチ", "呪術：報復"]
    ,"エクセキューショナー": ["強制苦行", "煩悶のトレイル", "デスバウンド"]
    ,"ブライト": ["ドラゴンの掌握", "呪術：不死", "呪術：血の恩恵"]
    ,"ツインズ": ["溜め込み屋", "迫害", "とどめの一撃"]
    ,"トリックスター": ["スターに憧れて", "呪術：クラウドコントロール", "袋小路"]
    ,"ネメシス": ["死を呼ぶ追跡者", "集団ヒステリー", "イラプション"]
    ,"セノバイト": ["デッドロック", "呪術：玩具", "悶絶のフック：苦痛という名の賜り物"]
    ,"アーティスト": ["不吉な包囲", "悶絶のフック：共鳴する苦痛", "呪術；ペンティメント"]
    ,"貞子": ["悶絶のフック：氾濫する憤怒", "海の呼び声", "怒涛の嵐"]
    ,"ドレッジ": ["解体", "露見する闇", "腐敗の気配"]
    ,"ウェスカー": ["人体の超越", "知覚覚醒", "終末期"]
    ,"ナイト": ["隠れ場なし", "呪術：闇との対面", "ヒュブリス"]
    ,"スカルマーチャント": ["バシッ！", "骨抜きの作用", "執拗な狩り"]
    ,"シンギュラリティ": ["遺伝的限界", "躊躇の強制", "機械学習"]
    ,"ゼノモーフ": ["究極の武器", "素早い残虐行為", "エイリアンの本能"]
    ,"チャッキー": ["呪術：二人遊び", "死ぬまで親友", "電池付き"]
}

# 1.ランダムでパークを4つ取り出す（重複なし ＆ dictionary_1から取り出す）
# 注：「list(dictionary_1.values())」のみだと辞書型から二次元リストになる
# 　　「itertools.chain.from_iterable」の部分で二次元リストを一次元リストに平坦化してる
# def R4parksMethod():
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values()))
#     r_4parks = random.sample(d_1d, 4) # d_1dの一次元リストからランダムに4つ取り出す
#     return r_4parks
# r_4parks = R4parksMethod()
# print(r_4parks)


# 2.ランダムでパークを1〜4つ取り出す（重複なし　＆　dictionary_1から取り出す）
# def R1To4parksMethod():
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values())) 
#     random_1to4num = random.randint(1, 4)
#     r_1to4parks = random.sample(d_1d, random_1to4num)
#     return r_1to4parks
# r_1to4parks = R1To4parksMethod()
# print(r_1to4parks)


# 3.指定した数だけランダムなパークを取り出す（重複なし　＆　dictionary_1から取り出す）
# def RparkSpecifyNumMethod(park_num):
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values()))
#     r_park_specify_num = random.sample(d_1d, park_num)
#     return r_park_specify_num
# print("パークの数を指定してください。")
# park_num = int(input())
# r_park_specify_num = RparkSpecifyNumMethod(park_num)
# print(r_park_specify_num)


# 4.指定したdictionary_1のkey(キャラクター)の値（パーク）を除いた状態からランダムでパークを4つ取り出す（重複なし　＆　dictionary_1から取り出す）
# def RparkSpecifyCharMethod(names): # 辞書データから指定したkeyの値を削除したデータを返すメソッド
#     for name in names:
#         del dictionary_1[name]
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values()))
#     rd_1d = random.sample(d_1d, 4)
#     return rd_1d
# r_park_specify_char = RparkSpecifyCharMethod(["トラッパー"])
# print(r_park_specify_char)


# 5.指定したdictionary_1の値（パーク）を除いた状態からランダムでパークを4つ取り出す（重複なし　＆　dictionary_1から取り出す）
# def RparkSpecifyParMethod(parks): # 引数の辞書データの値を1次元リストにし、2つ目の引数である除きたいパークのリストデータを1次元リストから除いたリストデータを返すメソッド
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values()))
#     for park in parks: # removeで消されるデータはあくまでメソッド内部のリストデータのみ
#         d_1d.remove(park)
#     rd_1d = random.sample(d_1d, 4)
#     return rd_1d #戻り値はリスト型
# r_park_specify_par = RparkSpecifyParMethod(["不安の元凶", "野蛮な力", "興奮"]) # revision関数にdictonary_1データと除く値（パーク名）を引数に挿入
# print(r_park_specify_par)


# 6.4でやったことにさらにメソッドの引数は入力でできるようにすること
# def RparkSpecifyCharMethod(names): # 辞書データから指定したkeyの値を削除したデータを返すメソッド
#     for name in names:
#         del dictionary_1[name]
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values()))
#     rd_1d = random.sample(d_1d, 4)
#     return rd_1d
# print("除外するキャラクターを入力してください。(複数選択する場合は半角区切りで入力すること)")
# excluded_characters = input().split()
# r_park_specify_char = RparkSpecifyCharMethod(excluded_characters)
# print(r_park_specify_char)


# 7.5でやったことにさらにメソッドの引数は入力でできるようにすること
# def RparkSpecifyParMethod(parks): # 引数の辞書データの値を1次元リストにし、2つ目の引数である除きたいパークのリストデータを1次元リストから除いたリストデータを返すメソッド
#     d_1d = list(itertools.chain.from_iterable(dictionary_1.values()))
#     for park in parks: # removeで消されるデータはあくまでメソッド内部のリストデータのみ
#         d_1d.remove(park)
#     rd_1d = random.sample(d_1d, 4)
#     return rd_1d #戻り値はリスト型
# print("除外するパークを入力してください。(複数選択する場合は半角区切りで入力すること)")
# excluded_parks = input().split()
# r_park_specify_par = RparkSpecifyParMethod(excluded_parks) # revision関数にdictonary_1データと除く値（パーク名）を引数に挿入
# print(r_park_specify_par)
