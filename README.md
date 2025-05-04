サーバレスアプリケーション作成練習用ディレクトリ

#2025.04.29
githubにリポジトリ作成。環境構築を開始。
書籍では仮想環境にpipenvを使用しているが、pyenvかvenvで検討中。
-> pyenvはpythonのバージョン管理用のツールでvirtualenvの間違いであった。
  結局、書籍通りにPipenvを使用することとする。
  PipenvはPipfileとPipfile.lockを使用してプロジェクトの依存関係を管理する。

Pipenvの使い方：
プロジェクトディレクトリ内で"pipenv install"を実行すると、
仮想環境が作成されPipfileが自動的に作成される。
書籍では、"pipenv --python 3.8"でpythonバージョンを指定する手順があったが、
仮想環境作成の手順を実行してからでないとエラーとなる。

その他のコマンド
"pipenv install パッケージ"   仮想環境にパッケージをインストールする。プロジェクトの依存関係がPipfileに追加される。
"pipenv install パッケージ --dev"  開発中にのみ必要なパッケージを--devを付けてインストールする。
"pipenv shell"  仮想環境のアクティベート
"exit"  仮想環境の終了
"pipenv uninstall パッケージ"  パッケージのアンインストール
"pipenv lock"  依存関係のロック

その他の使い方
・pythonのバージョン指定  "pipenv --python 3.8"
・スクリプトの実行  Pipfileにスクリプトを定義できる。
  [scripts]
  test = "pytest"
  
  実行コマンド
  pipenv run test
・パッケージのセキュリティチェック  "pipenv check"
・グラフ表示  "pipenv graph"でパッケージ感の関係を視覚的に表現できる。
・本番環境でのパッケージインストール  "pipenv install --ignore-pipfile"コマンドを実行することで、
Pipfile.lockに基づいてパッケージインストールが行われる。
開発環境と本番環境の一貫性を保つのに有効。

pipenvで仮想環境を構築しようとしたが、Flaskのインストール時にPipfile.lockのロックを失敗する事象が発生。
pipやpyenvのPATHがアナコンダとかと競合しあっているようであった。
そのため、Pipenvを一旦アンインストールし、anacondaのPATHを消去してインストールし直した。
その際Pythonのパスがシステム由来のPATHとなったことでインストールできない旨のエラーが発生するようになった。
PythonをPyenv環境のPython3.8を使用してインストールすることで正常に動作するようになった。
Flaskのインストールまで行った。



#2025.04.30
Flaskによるページの雛形作成
pythonでHello Worldを実行したが、標準モジュールの欠如で実行できなかった。
必要なモジュールをaptでインストールした後、Pyenvでpython3.8.20の再インストールを行った。
再インストール後は正常にブラウザに表示された。
一つのファイルでページ表示を行っていたが徐々に分割し、設定ファイルであるconfig.pyと表示専用のvewディレクトリに分割された。


#2025.05.01
CSSライブラリとしてBootstraoを使用し、記事閲覧ページのビュー作成を行った。
Bootstrapの機能として、ブラウザサイズに合わせてナビゲーションバーがハンバーガーメニューに変わる。


#2025.05.03
トップページの記事一覧表示ページを作成。
htmlファイルの共通部分をまとめたレイアウトファイルを作成。
新規投稿画面作成。
編集画面作成。
DBとしてDynamoDBを用意する。ORMとしてPynamoDBをインストールする。
ビュー内の仮データをDynamoDBから取得するように変更。
ローカルにDynamoDBを導入するために色々準備。
Java SE Development Kit 24.0.1 downloads
DynamoDBをターミナル上で実行できた。

#2025.05.04
Flask-Scriptを用いて、PynamoDBモデル定義をデータベースに反映させてテーブル作成する。
Flask-Scriptを使用しようとしたが、現在ではサポートされていなかったためFlask-CLIを使用する構成に変更した。

DynamoDB-local起動コマンド：
java "-Djava.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb

DynamoDB-localブラウザ管理画面起動コマンド：dynamodb-admin

ここまでをGithubにプッシュする。以降はブランチ戦略も合わせて勧めていく。
次はログイン機能の作成である。

flask_loginの機能で以下の文を実行することでセッションを付与することができる。
login_user(User(request.form['username']))

アプリケーションがログインセッションを受け取ったとき、セッションに含まれるユーザーIDからユーザ情報を取得してチェックすることをユーザローダという。

