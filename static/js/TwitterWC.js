window.onload = function () {
    drawWorldCloud();
    // グラフ描画
    $('#redraw').on('click', function () {
        drawWorldCloud();
    });
}




function drawWorldCloud() {
    // アニメーションテーマを使う
    am4core.useTheme(am4themes_animated);

    var chart = am4core.create("chartdiv", am4plugins_wordCloud.WordCloud);
    chart.width = am4core.percent(100);


    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

    series.data = [{"count":1614,"word":"課題"},{"count":989,"word":"バイト"},{"count":817,"word":"コミュ"},{"count":446,"word":"ゲーム"},{"count":389,"word":"人間"},{"count":362,"word":"コード"},{"count":332,"word":"ライブ"},{"count":331,"word":"すき"},{"count":321,"word":"世界"},{"count":274,"word":"ぺこ"},{"count":264,"word":"人生"},{"count":261,"word":"数学"},{"count":290,"word":"アルゴ"},{"count":244,"word":"お腹すいた"},{"count":234,"word":"オンライン"},{"count":233,"word":"未来"},{"count":233,"word":"問題"},{"count":218,"word":"確率"},{"count":216,"word":"技術"},{"count":216,"word":"ラーメン"},{"count":210,"word":"ライタス"},{"count":201,"word":"東方"},{"count":201,"word":"PC"},{"count":188,"word":"あわ"},{"count":158,"word":"コロナ"},{"count":157,"word":"レベル"},{"count":155,"word":"イベント"},{"count":154,"word":"バグ"},{"count":149,"word":"レジ"},{"count":145,"word":"単位"},{"count":145,"word":"基礎"},{"count":142,"word":"投稿"},{"count":141,"word":"プロジェクト"},{"count":134,"word":"コーヒー"},{"count":133,"word":"オタク"},{"count":131,"word":"ポケモン"},{"count":130,"word":"布団"},{"count":128,"word":"カレー"},{"count":127,"word":"キーボード"},{"count":127,"word":"アニメ"},{"count":125,"word":"ネット"},{"count":122,"word":"カラオケ"},{"count":121,"word":"線形"},{"count":120,"word":"研究"},{"count":118,"word":"函館"},{"count":117,"word":"サークル"},{"count":115,"word":"論文"},{"count":115,"word":"アプリ"},{"count":115,"word":"スライド"},{"count":115,"word":"イベ"},{"count":111,"word":"中間"},{"count":111,"word":"ハッカソン"},{"count":110,"word":"応数"},{"count":108,"word":"2020"},{"count":106,"word":"彼氏"},{"count":105,"word":"寿司"},{"count":103,"word":"アホ"},{"count":102,"word":"おじさん"},{"count":102,"word":"クリスマス"},{"count":98,"word":"バカ"},{"count":97,"word":"プロセカ"},{"count":97,"word":"解析"},{"count":97,"word":"天才"},{"count":96,"word":"ピザ"},{"count":96,"word":"ストーリー"},{"count":95,"word":"アドカレ"},{"count":94,"word":"女の子"},{"count":94,"word":"英語"},{"count":93,"word":"工学"},{"count":93,"word":"演習"},{"count":93,"word":"発表"},{"count":90,"word":"パスタ"},{"count":87,"word":"微分方程式"},{"count":86,"word":"麻雀"},{"count":86,"word":"マスク"},{"count":83,"word":"ハード"},{"count":83,"word":"OR"},{"count":83,"word":"焼肉"},{"count":83,"word":"HI"},{"count":103,"word":"SQL"},{"count":81,"word":"LINE"},{"count":81,"word":"#質問箱"},{"count":81,"word":"虚無"},{"count":80,"word":"レポート"},{"count":79,"word":"大学生"},{"count":77,"word":"LT"},{"count":75,"word":"応用"},{"count":75,"word":"ねこ"},{"count":75,"word":"ソフトウェア"},{"count":73,"word":"バレー"},{"count":72,"word":"クワタン"},{"count":71,"word":"ラッピ"},{"count":70,"word":"#ジャパンコーラ"},{"count":69,"word":"実装"},{"count":69,"word":"ぺこら"},{"count":68,"word":"#本田圭佑"},{"count":68,"word":"#本田とじゃんけん2020"},{"count":67,"word":"リモート"},{"count":66,"word":"フリート"},{"count":66,"word":"#FunBlock2020"},{"count":66,"word":"カメラ"},{"count":66,"word":"開発"},{"count":66,"word":"プログラミング"},{"count":65,"word":"餃子"},{"count":65,"word":"ファミリーマート"},{"count":65,"word":"アイドル"},{"count":65,"word":"ビール"},{"count":64,"word":"統計"},{"count":63,"word":"温泉"},{"count":63,"word":"人工知能基礎"},{"count":62,"word":"インスタ"},{"count":60,"word":"公立"},{"count":60,"word":"CD"},{"count":60,"word":"案件"},{"count":60,"word":"仕様"},{"count":60,"word":"ソース"},{"count":60,"word":"サーバ"},{"count":60,"word":"進捗"},{"count":60,"word":"お嬢様"},{"count":59,"word":"ぎゆしの"},{"count":58,"word":"たつお"},{"count":57,"word":"CV"},{"count":57,"word":"企業"},{"count":57,"word":"お菓子"},{"count":57,"word":"AC"},{"count":56,"word":"就活"},{"count":56,"word":"ぶり"},{"count":56,"word":"地震"},{"count":55,"word":"コンテナ"},{"count":55,"word":"出勤"},{"count":55,"word":"殺意"},{"count":54,"word":"胡蝶"},{"count":53,"word":"通話"},{"count":53,"word":"クイユニ"},{"count":53,"word":"ストレス"},{"count":53,"word":"デザイン"},{"count":53,"word":"札幌"},{"count":53,"word":"コミュニケーション"},{"count":52,"word":"自転車"},{"count":52,"word":"エンジニア"},{"count":51,"word":"チャリ"},{"count":50,"word":"DB"},{"count":50,"word":"ビーコン"},{"count":50,"word":"情報表現"},{"count":50,"word":"IVE"},{"count":50,"word":"非同期"},{"count":49,"word":"ぴえん"},{"count":49,"word":"ハードウェア"},{"count":49,"word":"甘露"},{"count":49,"word":"人知"},{"count":48,"word":"ライブラリ"},{"count":48,"word":"OS"},{"count":48,"word":"フォント"},{"count":47,"word":"産業"},{"count":84,"word":"ドンキ"},{"count":46,"word":"オフ"},{"count":46,"word":"彼女"},{"count":45,"word":"コマンド"},{"count":44,"word":"サーバー"},{"count":44,"word":"AI"},{"count":44,"word":"アーカイブ"},{"count":43,"word":"同窓会"},{"count":43,"word":"情報処理演習"},{"count":43,"word":"FUN"},{"count":43,"word":"バイク"},{"count":43,"word":"ウイルス"},{"count":42,"word":"カービィ"},{"count":42,"word":"データベース"},{"count":42,"word":"線形代数"},{"count":42,"word":"VEP"},{"count":41,"word":"落単"},{"count":40,"word":"ストーブ"},{"count":40,"word":"ポインタ"},{"count":40,"word":"ハイボール"},{"count":40,"word":"リポジトリ"},{"count":39,"word":"令嬢"},{"count":39,"word":"メモリ"},{"count":39,"word":"ミスド"},{"count":38,"word":"ボス"},{"count":38,"word":"ガン"},{"count":38,"word":"ピカチュウ"},{"count":38,"word":"スシロー"},{"count":37,"word":"機械学習"},{"count":37,"word":"試験"},{"count":37,"word":"インターン"},{"count":37,"word":"ラボ"},{"count":36,"word":"ハンバーグ"},{"count":35,"word":"#本田にグーで勝つ"},{"count":35,"word":"コンテスト"},{"count":35,"word":"北海道"},{"count":34,"word":"#osc20do"},{"count":34,"word":"スタバ"},{"count":33,"word":"メソッド"},{"count":33,"word":"深層学習"},{"count":33,"word":"煉獄"},{"count":33,"word":"シャニマス"},{"count":32,"word":"おっぱい"},{"count":32,"word":"イケメン"},{"count":31,"word":"スプラ"},{"count":31,"word":"ディスコ"},{"count":31,"word":"認知"},{"count":31,"word":"コート"},{"count":30,"word":"JK"},{"count":30,"word":"ひぐらし"},{"count":30,"word":"飯テロ"},{"count":30,"word":"メンヘラ"},{"count":30,"word":"ICT"},{"count":30,"word":"マック"},{"count":29,"word":"快活"},{"count":29,"word":"#ニコニコ動画"},{"count":29,"word":"クソリプ"},{"count":29,"word":"ミーティング"},{"count":29,"word":"怪文書"},{"count":29,"word":"ドライブ"},{"count":29,"word":"LOL"},{"count":29,"word":"財布"},{"count":29,"word":"ピアレビュー"},{"count":29,"word":"ブランチ"},{"count":28,"word":"#shindanmaker"},{"count":28,"word":"ドキュメント"},{"count":28,"word":"APEX"},{"count":27,"word":"MSSP"},{"count":27,"word":"仮説"},{"count":26,"word":"微分"},{"count":26,"word":"アリュージョニスト"},{"count":26,"word":"アップデート"},{"count":26,"word":"FUNAC"},{"count":26,"word":"コピペ"},{"count":26,"word":"セントラル"},{"count":26,"word":"生放送"},{"count":25,"word":"UI"},{"count":25,"word":"プリン"},{"count":25,"word":"出前"},{"count":25,"word":"パンダ"},{"count":25,"word":"たこ焼き"},{"count":24,"word":"オートマトン"},{"count":24,"word":"スプラトゥーン"},{"count":24,"word":"バーチャル"},{"count":24,"word":"VSC"},{"count":24,"word":"オブジェクト"},{"count":24,"word":"アイマス"},{"count":24,"word":"フロント"},{"count":24,"word":"筋肉"},{"count":24,"word":"期末"},{"count":23,"word":"コミュニティ"},{"count":23,"word":"ガチャ"},{"count":23,"word":"ばあちゃん"},{"count":23,"word":"プロダクト"},{"count":22,"word":"#技育祭"},{"count":22,"word":"履修"},{"count":22,"word":"ケース"},{"count":22,"word":"メガ"},{"count":22,"word":"LIVE"},{"count":22,"word":"CSS"},{"count":22,"word":"アート"},{"count":22,"word":"ニート"},{"count":22,"word":"赤川"},{"count":22,"word":"やまむらはる"},{"count":22,"word":"積分"},{"count":22,"word":"ブレイクアウトルーム"},{"count":21,"word":"山岡家"},{"count":21,"word":"ジムニー"},{"count":21,"word":"API"},{"count":21,"word":"アルコール"},{"count":21,"word":"たばこ"},{"count":21,"word":"グラブル"}];
    // 文字列を渡すだけ
    series.dataFields.word = "word";
    series.dataFields.value = "count";

    //series.maxCount = 1;

    series.heatRules.push({
        "target": series.labels.template,
        "property": "fill",
        "min": am4core.color("#52262a"),
        "max": am4core.color("#ff7d88"),
        "dataField": "value"
    });

    series.labels.template.url = "https://twitter.com/search?q={word.urlEncode()}&src=typed_query&pf=on";
    series.labels.template.urlTarget = "_blank";

    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";

    var subtitle = chart.titles.create();
    subtitle.text = "(click to open)";

    var title = chart.titles.create();
    title.text = "2020 Twitter Trend";
    title.fontSize = 30;
    title.fontWeight = "800";
    title.paddingTop = 20;

    // カラフルになる。
    series.colors = new am4core.ColorSet();
    series.colors.passOptions = {}; // makes it loop

    // 配置が動くようになる
    setInterval(function () {
        series.dataItems.getIndex(series.dataItems.length - 1).setValue("value", Math.round(Math.random() * 10));
       }, 10000);
}

