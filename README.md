# Python ではじめる機械学習

## 仮想環境の構築 (初回のみ)

Anaconda Prompt を起動し、次のコマンドを実行。

    conda create -n ds2 numpy scipy=1.1.0 scikit-learn matplotlib pandas pillow
    activate ds2
    conda install jupyter

## ノートブック教材のダウンロード

Anaconda Prompt を起動し、次のコマンドを実行。

    git clone https://github.com/nakanolab/ds2.git

教材に更新があった場合には、その都度次のコマンドを実行。

    cd ds2
    git pull

## ノートブックの実行 (次回以降)

Anaconda Prompt を起動し、次のコマンドを実行。

    activate ds2
    set http_proxy=http://wwwproxy.kanazawa-it.ac.jp:8080
    set https_proxy=http://wwwproxy.kanazawa-it.ac.jp:8080
    cd ds2
    jupyter notebook

ブラウザが立ち上がるので、ja で始まる該当章のノートブックをシングルクリックで開く。
