# お家でできる！ホットジャバ

Amazon Web Services (AWS) Lambdaを使った「今日も気温がホットジャバ」の実装。
気温がある一定を越えると「今日も気温がホットジャバ」とツイッターに投稿する。
Lambda化でEC2を動かし続けなくて良くなり、請求金額が下がると期待されている。

## 設定方法

* install_libs.sh を実行してpip を用いて必要なライブラリをsrc以下に展開。
* src/hotjava.py のweather_url にライブドア天気のJSON APIのURLをセット。city= 以下をお好みの都市に変える。
* src/hotjava.py のtw_*** にツイッタ〜APIキー／シークレット、他を設定する。この辺はTweepyのドキュメントに従う必要がある。

## デプロ葦方法

AWSのコンソ〜ルでLambdaを新しく作る。
アップロードするZIPはsrc のファイルとディレクトリを固めたもの(make-zip.sh)。
AWS Lambdaの流儀でzip を展開したディレクトリにhotjava.py が出てくるようにする必要がある。

* Runtime Python 2.7
* Handler hotjava.handler_hotjava
* メモリは128 MBで充分
* 現状で正常動作したときには900 msくらい。タイムアウトは10 secとかでよさそう

トリガーはCloudWatch Events - Schedule を選んで、

* Schedule expression: cron(43 21 * * ? *)

などとする。時間がUTCなので注意が必要。


