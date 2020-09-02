# Python ではじめる機械学習

このリポジトリは原著 [Introduction to Machine Learning with Python](https://www.oreilly.com/library/view/introduction-to-machine/9781449369880/) に付随した[リポジトリ](https://github.com/amueller/introduction_to_ml_with_python)の 2019年1月11日時点でのバージョンをもとにしている。変更点は以下の通り。

- 第1章から第5章までのノートブックの内容を一部取捨選択し、日本語に訳した（セル内の `### [5]` などのようなコメントは、そのブロックが本文中の `In[5]:` に対応していることを表す）。
- 第7章については日本語を対象とした非常に簡単な自然言語処理の例で置き換えた。
- ノートブックについては、まっさらな状態から実行できるように、実行結果を含めないようにした。
- Windows環境でスムーズに実行できるように、決定木の可視化で使われていた `graphviz` の代わりに `sklearn.tree` の `plot_tree` を使うようにした。

## リポジトリのダウンロード

ダウンロード先はどこでもよいが、以下では Windows のホームディレクトリ (`C:\Users\username`) の直下に `ds2` という名前のフォルダで保存することを前提としている。
- `git` コマンドが使える場合は Windows のホームディレクトリにてコマンドプロンプトから `git clone https://github.com/nakanolab/ds2.git` を実行。
- `git` コマンドが使えない場合は、上にある Code と書かれた緑色のボタンから "Download ZIP" を選択して、ダウンロード後に解凍する（フォルダー名は `ds2-master` から `ds2` に変更する）。

## Python 実行環境の準備

### Anaconda のインストール

[Anaconda Individual Edition](https://www.anaconda.com/products/individual) を該当する OS のインストーラーをダウンロードして、基本的にすべてデフォルトの設定でインストール。

### proxy 環境の場合

Anaconda Prompt を立ち上げ、notepad .condarc と打ち、以下をペーストして保存。

    ssl_verify: true
    channels:
      - defaults
    proxy_servers:
      http: http://wwwproxy.kanazawa-it.ac.jp:8080
      https: http://wwwproxy.kanazawa-it.ac.jp:8080

続いて「仮想環境 `ds2` の作成」を実行。

### 仮想環境 `ds2` の作成

Anaconda Prompt を起動し、次のコマンドを実行。

    cd ds2
    conda env create -f ds2_windows.yml

## ノートブックの実行

Anaconda Prompt を起動し、次のコマンドを実行。

    conda activate ds2
    cd ds2
    jupyter notebook

ブラウザが立ち上がるので、ja で始まる該当章のノートブックをシングルクリックで開く。
