import random
import itertools

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


adjective = ["不安の", "野蛮な", "血の", "闇より出でし", "光より出でし", "看護婦の", "呪術：", "第三の", "貪られる", "圧倒的", "観察＆", "女狩人の", "最後の", "弄ばれる", "消えゆく", "バーベキュー＆", "フランクリンの", "ファイアー・", "リメンバー・", "悶絶の", "処刑人の", "選択は", "イタチが", "怨霊の", "霊障の", "狂気の", "堕落の", "伝染する", "闇の", "隠密の", "残心の" ,"死人の", "強制", "煩悶の", "デス", "ドラゴンの", "とどめの", "スターに", "死を呼ぶ", "集団", "苦痛という名の", "不吉な", "共鳴する", "氾濫する", "海の", "怒涛の", "露見する", "腐敗の", "人体の", "闇との", "骨抜きの", "執拗な", "遺伝的", "躊躇の", "究極の", "素早い", "エイリアンの", "死ぬまで", "髙橋基陽"]
noun = ["元凶", "力", "興奮", "捕食者", "追跡者", "者", "不屈", "ガラクタ", "喘鳴", "死恐怖症", "使命", "封印", "破滅", "希望", "存在感", "虐待", "オーバーチャージ", "猛獣", "意識", "子守唄", "お楽しみ", "獲物", "灯", "ノックアウト", "悲鳴", "番人", "フック", "妙技", "監視", "君次第だ", "まやかし", "ピエロ恐怖症", "飛び出した", "怒り", "地", "怨恨", "不協和音", "根性", "介入", "怖気", "信仰心", "地獄耳", "戦慄", "追跡", "戦術", "共鳴", "天誅", "変速機", "スイッチ", "報復", "苦行", "トレイル", "バウンド", "掌握", "不死", "恩恵", "溜め込み屋", "迫害", "一撃", "憧れて", "コントロール", "袋小路", "追跡者", "ヒステリー", "イラプション", "ロック", "玩具", "フック", "賜り物", "包囲", "苦痛", "ペンティメント", "憤怒", "呼び声", "嵐", "解体", "闇", "気配", "超越", "覚醒", "終末期", "なし", "対面", "ヒュブリス", "バシッ！", "作用", "狩り", "限界", "強制", "学習", "武器", "残虐行為", "本能", "二人遊び", "親友", "付き"]
print(random.choice(adjective) + random.choice(noun))