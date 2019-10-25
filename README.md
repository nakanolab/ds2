# Python ではじめる機械学習

## 仮想環境の構築 (初回のみ)

Anaconda Prompt を起動し、次のコマンドを実行。

    conda create -n ds2 python=3.6 numpy scipy=1.1.0 scikit-learn matplotlib pandas pillow
    activate ds2
    conda install jupyter
    conda install seaborn

## ノートブックのダウンロード

Anaconda Prompt を起動し、次のコマンドを実行。

    git clone https://github.com/nakanolab/ds2.git

教材に更新があった場合には、その都度次のコマンドを実行。

    cd ds2
    git pull

もし上記コマンドが、あるファイルのコンフリクトのため失敗したら、次のコマンドを実行してから再度 `git pull` する。

    git checkout -- 該当ファイル名

## ノートブックの実行

Anaconda Prompt を起動し、次のコマンドを実行。プロキシサーバーを指定している `set` の2行は、学内LANを使っている場合にのみ必要。

    activate ds2
    set http_proxy=http://wwwproxy.kanazawa-it.ac.jp:8080
    set https_proxy=http://wwwproxy.kanazawa-it.ac.jp:8080
    cd ds2
    jupyter notebook

ブラウザが立ち上がるので、ja で始まる該当章のノートブックをシングルクリックで開く。
