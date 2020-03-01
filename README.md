# Python ではじめる機械学習

## ノートブックのダウンロード

Anaconda Prompt を起動し、次のコマンドを実行。

    git clone https://github.com/nakanolab/ds2.git

教材に更新があった場合には、その都度次のコマンドを実行。

    cd ds2
    git pull

もし上記コマンドが、あるファイルのコンフリクトのため失敗したら、次のコマンドを実行してから再度 `git pull` する。

    git checkout -- 該当ファイル名

## 仮想環境の構築 (初回のみ)

Anaconda Prompt を起動し、次のコマンドを実行。

    cd ds2
    conda env create -f ds2_windows.yml

## ノートブックの実行

Anaconda Prompt を起動し、次のコマンドを実行。プロキシサーバーを指定している `set` の2行は、学内LANを使っている場合にのみ必要。

    conda activate ds2
    set http_proxy=http://wwwproxy.kanazawa-it.ac.jp:8080
    set https_proxy=http://wwwproxy.kanazawa-it.ac.jp:8080
    cd ds2
    jupyter notebook

ブラウザが立ち上がるので、ja で始まる該当章のノートブックをシングルクリックで開く。
