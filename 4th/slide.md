---
marp: true
---

<!-- page_number: true -->
<!-- $theme: defalut -->
<!-- $size: 16:9 -->

FY19 VORTEX FUNトレーニング
Pythonスキルアップチーム勉強会
==

## 第4回
2019.12.19

---

本日のアジェンダ
==
- webアプリケーションとRESTAPI
- djangoを使ってみよう
- デプロイについて
- AWS Lambda簡易講座
- 企画アドバイスコーナー

---

webアプリケーションとRESTAPI
==

---

HTTPおさらい
==
- Hyper Text Tranfer Protocol
- サーバ・クライアントモデル
- 他文書へのリンクを持つハイパーテキストの仕様と、クライアントとサーバの間でそれをやりとりする仕様を決めたもの
- URL(Uniform Resource Locater) で、ハイパーテキストの場所を指定する
```
http://hoge.com/document/sugoi/yabai.html
```
- 現在はテキストの転送だけでなく、パケット通信の基盤になったり（websocket)、ブラウザがアプリケーションの基盤になる（webassembly)など、進化の目覚ましいプロトコルのひとつ

---


HTTPメソッドおさらい
==
### GET
- HTTPサーバからコンテンツを取得する
### POST
- HTTPサーバにコンテンツを配置する
### PUT/PATCH
- HTTPサーバに配置済みのコンテンツの一部を変更する
### DELETE
- HTTPサーバに配置されたコンテンツを削除する

---

webアプリケーションとは
==
- webブラウザで利用できるアプリケーションのこと
- 何かを入力してその結果が反映されるようなwebサイトはwebアプリと呼べる
  - webメール、ECサイト、ブログ（の管理画面）、クラウド家計簿、などなど
- コンテンツ（文章、写真など動きのないもの）が置いてあるだけのwebサイトはwebアプリとは呼ばない
- 構成は大体こんな感じになっている
```
webブラウザ - Internet - webサーバ - webアプリケーションサーバ - データベース
```
---

webアプリケーションの歴史
==
### 動きのない時代
- HTMLを読み込んで表示するだけ
- 文字と絵を表示するだけのwebページが主流
- ハイパーリンクが登場。テキストをクリックすると次のテキストが表示され、コンピュータ上でのドキュメント閲覧が劇的に進化した
##### 構成
```
webブラウザ - Internet - webサーバ
```

---

webアプリケーションの歴史
==

### CGIの時代
- インターネット普及前夜ごろ
  - Windows95 Plus!、第1次ブラウザ戦争勃発
- webサーバ内でPerlスクリプトを動かして、表示するたびに変化のあるwebページが出来るように進化した
  - アクセスカウンター、掲示板などが流行
- JavaScriptは存在したが、互換性が低かったり機能が低く、ページの装飾程度にしか使われていなかった
##### 構成
```
webブラウザ - Internet - webサーバ(スクリプトが動く) (- データベース)
```

---

webアプリケーションの歴史
==
### アプリケーションサーバの時代
- データベースを利用して、動的にHTMLを生成できるアプリケーションサーバが登場
  - ユーザーの入力や指示に応じてページ内容を変更できるようになった
    - データベースから商品一覧を取得して表のHTMLを生成するなど
  - Javaが一気に時代の表舞台に
- 業務アプリやECサイトなどが劇的に発展した
##### 構成
```
webブラウザ - Internet - webサーバ - アプリケーションサーバ - データベース
```

---

webアプリケーションの歴史
==

### モダンwebアプリの時代
- Ajaxが登場、ページの表示とサーバアクセスが別タイミングに
- JavaScriptが、ブラウザ側でコンテンツを生成するようになった
- webサーバは、静的ファイルとデータベースだけを提供するように　
  - 静的ファイル・・・HTML/CSS、JavaScript、メディア関連など
- 従来のアプリケーションサーバでのHTML生成と併用もある
##### 構成
```
webブラウザ - Internet - webサーバ - APサーバ(DBアクセス用サーバ) - データベース
```

---

データベースにwebからアクセスする需要が生まれた
==
- 通常のデータベースはインターネット経由でアクセスされることは想定されていない
  - ブラウザとインターネットの間のFWがHTTP(S)しか許可してないことがある
  - プロキシがいたりもする
  - SQLは自由度が高く、意図しないデータにアクセスされる危険がある
  - そもそもセキュリティ対策をするより、データベースとしてやることがいっぱいるある
- HTTPを使ってデータベースに安全にアクセスする仕組みが登場 -> RESTAPI誕生
> RESTAPIの利用はデータベースだけに限定されません。今回は話を簡略化するためにだいぶ端折っていますm(_ _)m)

--- 

RESTAPIとは
==
- データベース構造をURLで表現し、HTTPでアクセするための仕組み
> くどいですが本当はもっと細かい話があるのですが今回は割愛します
- HTTPメソッドで、データの読み書き・更新・削除（CRUD)を実現する 
  - GETで読み出し、POSTで書き込み、PUTで更新、DELETEで削除
- HTTPでアクセスできるので、認証や暗号化にHTTPSを使える

---

RESTAPIの例
==
- こんな感じの名言データベース（のテーブル）があったとする

| id   | quote                                                              | author       |
| :--- | :----------------------------------------------------------------- | :----------- |
| 1    | 明日死ぬかのように生きよ。永遠に生きるかのように学べ               | ガンジー     |
| 2    | 10%の才能と20%の努力、30%の臆病さと、残る40%は、運、だろうな。。。 | デューク東郷 |
| 3    | 自分で薪を割れ、二重に温まる                                       | フォード     |

---

RESTAPIの例
==
### RESTAPIのURLが http://kakugen.com だった場合

- idが1の格言を読み込みたい場合
```
curl http://kaugen.com/quote/1
```

- 格言を追加したい場合
```
curl -X POST -d '{"quote":"talk is cheap.show me the code.","author":"トーバルズ"}' http://kaugen.com/quote/1
```
- なお、以下のようなAPIはRESTAPIとは言わない
```
http://kakugen.com/getquote
```
- getという動作をAPI名に入れてしまっている。RESTでは、動作はHTTPメソッドで決める

---

（ちょっと余談）webAPIいろいろ
==
- webサービスの持っているデータをプログラムから利用するために、いろいろなAPIが存在する
	- 天気予報、為替、飲食店情報、などなど
- webAPIが提供されていない、あるいは利用者を制限しているような場合は、HTMLソースを解析して情報を抜き出す**スクレイピング**をする必要がある
- webAPIを利用して新たなwebサービスを開発することを、マッシュアップという
  - クラウド家計簿、SNS統合サイトなど

---

djangoを使ってみよう
==

---

ちゃんとしたwebアプリを作るのは結構大変
==
#### 入力された文字をチェックしないといけない
- フリガナの欄にちゃんとカタカナを使っているか
- メアドや電話番号のフォーマットは正しいか、などなど
#### セキュリティの問題
- 存在しないURLを叩かれたときに弾く処理がいる
- フォームの文字列を使ってSQLを叩く場合、SQLインジェクションされる可能性がある
#### 定形処理
- 〇〇一覧表示など、よく使う処理を何度も書くのか
- ログインしてるかどうかの確認も定形処理の一つ

---

webアプリケーションフレームワークとは
==
- 最小限の労力でwebアプリを開発できるようにする仕組み
### 「当たり前のこと」を全部勝手にやってくれる
- URLの定義と、そこへアクセスされたときの処理
- フォームに入力された文字の書式チェック
- ログインしていない場合、自動でログイン画面にリダイレクト
- 一覧表のページをDBのテーブルから自動生成
- 存在しないURLへのアクセスに404を返す
- データベースの管理画面はフレームワークに組み込み済み

---

Python製webフレームワーク
==
### bottle
- 一本のPythonコードだけでできた、超軽量フレームワーク
- データベース機能は持っていないのでSQLを使う必要がある
### flask
- bottleより高機能なフレームワーク
- 最低限の機能だけ持ち、必要になった機能は跡から追加するスタイル
- githubでのPython webフレームワーク人気度No.1
- Netflixなどで利用されている

---

django（ジャンゴ）の紹介
==
- webアプリに必要な機能をほぼ全て盛り込んだ、重量級フレームワーク
- 簡易的なwebサーバを持っていて、開発物をすぐにテストできる
- ユーザー認証機能を組み込んでいるので、ログインが必要なアプリも割とすぐ書ける
- データベースは組み込み済み。もちろん、MySQLなども使える
- データベースをPythonのオブジェクトとして扱える、ORマッパーを持つ
  - データベースの定義にも取り扱いにもSQLを一切使わない
- URLと処理の紐付けが非常に簡単
- HTMLの生成を単純化する強力なテンプレート機能がある
- YouTubeやInstagramなどで利用されている

---

django rest frameworkの紹介
==
- djangoにRESTAPI機能を追加するフレームワーク 
- 略してDRF
- djangoに追加しているだけなので、通常のサイトの作成ももちろん可能
  - というか、通常のwebサイトにRESTAPIを追加するイメージ
- djnago同様、pipで簡単にインストール可能
- 通常のdjangoと変わらず利用できるので学習コストが低い
  - 単純なCRUDだけなら、30分ほどで新規APIが実装できる
- APIのテスト画面が提供されるので、APIをすぐに試すことができる

---

djangoでのアプリ開発の流れ
==
- djangoのインストール
- プロジェクトとアプリケーション作成
- モデル作成
  - データベースを定義する
- ビュー作成
  - URLにアクセスされたときの、返すレスポンスを決める
- ルーティング設定
  - URLと、ビューを紐付ける
- django起動

---

djangoでのwebアプリケーション構成図
==

![80%](./django_structure.png)
> https://djangobrothers.com/tutorials/memo_app/mtv/ 


---

djangoのインストール
==
- cloud9を起動して、Terminal起動
- djangoテスト用ディレクトリ作成
```
mkdir drftest
```
- テスト用ディレクトリに移動
```
cd drftest
``` 
- Python仮想環境を作成
```
python3 -m venv venv
``` 
- 仮想環境内に移動
```
source venv/bin/activate
```

---

djangoのインストール
==
- djangoのインストール
```
pip3 install django 
```
- django rest frameworkのインストール
```
pip3 install djangorestframework
```
- インストール確認
```
pip3 list
```

---

プロジェクトとアプリケーションの作成
==
- プロジェクト作成
```
django-admin startproject hogebot 
```
- アプリケーション作成
```
cd hogebot
python3 manage.py startapp api
```
- アプリケーション「api」のディレクトリに移動
```
cd api 
```

---
プロジェクトとアプリケーションとは
==
- 例えばECサイトを作るとき、ECサイト全体をプロジェクトと呼ぶ
- ECサイト内の、商品一覧、決済画面、ユーザー情報など個々の機能のことをアプリケーションと呼ぶ
- 最低、1プロジェクトと１アプリケーションが必要
- 大規模でなければ、１アプリケーションで十分
- 今回は、hogebotプロジェクトを作成、apiというアプリケーションを作成

---

ディレクトリ構成
==
```
drftest/hogebot/
├── api　（python manage.py startapp apiで作ったやつ）
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── hogebot　（django-admin startproject hogebotで作ったやつ）
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```




---

初期設定
==
- pwdコマンドでカレントディレクトリを確認
```
/home/enviroment/drftest/hogebot
```
- 以下のファイルをcloud9で開く
```
hogebot/settings.py
```

---

初期設定
==
- 以下の項目を編集する
  - ALLOWED_HOSTSを以下に変更
  ```
  ALLOWED_HOSTS = ['*']
  ```
  > アクセス元ではなく、自分のwebサイト名を書く設定なので注意
  - INSTALLED_APPSリストに以下を追加
  ```
  'api',
  ```
  > 最後のカンマをお忘れなく

--- 

初期設定
==
- settings.py続き
  - LANGUAGE_CODEを編集
  ```
  LANGUAGE_CODE='ja'
  ```
- TIME_ZONEを編集
  ```
  TIME_ZONE='Asia/Tokyo'
  ```

---

モデルの作成
==
### モデルとは
- djangoにおけるデータベース
- djangoでは、データベースはPythonオブジェクトとして扱う
  - ObjectとRelationalDBを紐付けるのでORマッパーと呼ばれる
  - SQLを扱わないのでセキュリティレベルが上がる
  - テーブルの定義をPythonコードで行う
  - テーブル名.objects.all()とかすると全レコードが取れたりとか、直感的にデータベースを扱うことができる

---

モデルの作成
==
- アプリケーション「api」で使用するデータベースを作成する
  - 名言（Quote）を保存するQuoteテーブルを作成
- api/models.pyを編集して以下を追加して、保存
```python
class Quote(models.Model):
    quote = models.TextField()
```
- 今回はdjangoに組み込みのsqlite3を使用するため、データベースサーバの設定は不要
  - もしMySQLやPostgresSQLを使いたい場合はsettings.pyに設定する（ので興味ある方はやってみてください）

---

マイグレーションの実行
==
- マイグレーションとは、モデルのPythonコードからデータベースを作成すること
- 以下を実行する
  - migrationファイルという、データベースの構成を書いたファイルが生成される
```
python3 manage.py makemigrate
```
- 続けて以下も実行する
  - この作業で、データベースがsqlite3に作成される
```
python3 manage.py migrate
```

---

django管理用ユーザーの作成
==
- djangoの管理者ユーザーを作成する
  - ユーザー名を聞かれるので、忘れない名前を入力する
  - メアドは体をなしていれば適当でOK
  - パスワードは忘れないものを入れる。簡単な場合は、簡単だけどいい？って聞かれるのでYを選ぶ
```
python3 manage.py createsuperuser
```

---

django起動！
==
- 以下を実行してdjangoを起動する
```
python3 manage.py runserver
```
- 起動結果確認
```
(snip)
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
- ↑の状態で停止すればOK。djangoが起動してHTTPアクセスを待ち受けている状態

---

djangoに接続！
==
- webブラウザで以下URLに接続
```
http://localhost:8000/
```
- ロケットが飛んでいる画面になればdjango起動成功！
### と、なればよいのですが、残念ながら〇〇（自主規制）な情シスの仕様により、手元のブラウザからcloud9のweb画面に接続することはできません（図解）
##### すぐ実施できる回避方法は以下の通り
- aptもしくはyumで、lynx（テキストベースwebブラウザ）をインストールする
- 講師の実演を指をくわえて見る

---

django 管理画面に接続！
==
- webブラウザで以下URLに接続
```
http://localhost:8000/admin/
```
- createsuperuserで作成したユーザー名とパスワードを入力

---

管理画面にQuoteモデルがない？
==
- モデルを作っただけでは、管理画面には表示されない
  - 管理画面はあくまでおまけ？という意図？
- api/admin.py以下を追加する
```python
from .models import Quote

@admin.register(Quote)
class Quote(admin.ModelAdmin):
    pass
```
- djangoが自動で再起動し、コードが読み込まれる
- 管理画面にQuotesが表示される
> Quotes になっているところに注目

---

django rest frameworkの組み込み
==
- pipでインストールしただけで、DRFはまだdjangoに組み込まれていない
- hogepj/settings.pyを開いて以下を追加
```
INSTALLED_APPS = (
  ...
  'api',
  'rest_framework',
)
```
> 最後のカンマをお忘れなく
- これだけです。簡単！
  
---

シリアライザーの設定
==
### シリアライズとは
- ハードウェア・OS・言語などのアプリケーション基盤に依存したデータを、XMLやJSONなどの基盤に依存しない形式に変換すること
  - webは様々なOSやハードウェアで利用されるため、特定の基盤に依存したデータでは通信が成り立たない
- Pythonのオブジェクトなど、言語に依存したデータ形式をファイル保存やネットワーク転送ができるバイト列にするという意味でも使われる
 
---

シリアライザーの設定
==
- ファイルは存在しないので新規に作成する
- api/serializer.py
```Python
from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quote',)
```
> 最後のカンマをお忘れなく

---

ビューの設定
==
### ビューとは
- djangoの、いわば本体。djangoで処理したい内容を書くところ
- APIへのリクエストを受け取り、データベースからデータを取得し、しかるべき処理を行い、レスポンスを生成する
- 関数、クラス＆メソッドのどちらで書いてもよい
  - 処理の数が増えるとクラスにしたほうが管理がしやすい

---

ビューの設定
==
- api/views.pyに以下を記載する
```python
from rest_framework import viewsets
from .models import Quote
from .serializer import QuoteSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
```
- データベースの値を何も加工しないのであれば、これだけでCRUDを実現できる

---

authentication_classes = []について
==
- djangoはデフォルトでCSRF対策が入っているので、それを解除する設定
- セキュリティレベルが下がるので本来はむやみに設定してはならない
### CSRFとは
- Cross Site Request Forgery攻撃のこと
- 掲示板などに、自分の意図しない書き込みをされてしまうweb攻撃
- webサイト側から乱数をブラウザに渡し、その乱数が帰ってこない場合はPOSTをさせないことで対策する
- localhostからPOSTする場合は気にしなくてよいが、APIとして公開する場合は意識する必要がある
    - DRF使ってみた的なサイトはlocalhostからしかアクセスしていないので気づきにくい

---

ルーティングの設定
==
### ルーティングとは
- URLとビューを紐付ける設定
- ネットワークのルーティングとは違います
- プロジェクトと、アプリケーションでそれぞれ設定する
    - どのアプリケーション向けかを、プロジェクト側で設定
    - アプリケーション内のどのビュー向けかを、アプリケーション側で設定

---

ルーティングの設定
==
- まずプロジェクト側に設定
- hogebot/urls.pyに以下を追加
```python
from django.conf.urls import url, include
from api.urls import router as api_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include(api_router.urls)),
]
```

---

ルーティングの設定
==
- 次にアプリケーション側を設定する
- api/urls.pyを新規に作成
```python
from rest_framework import routers
from .views import QuoteViewSet

router = routers.DefaultRouter()
router.register('quotes', QuoteViewSet)
```

---

完成したので動かしてみる
==
- お疲れさまでした！動かしてみましょう
- 以下を実行してdjangoを起動
```
python3 manage.py runserver
```
- GETしてみる
```
curl http://localhost:8000/api/quotes/
```
- データが何も入ってないので空のレスポンスが返ってくる（と思う

---

完成したので動かしてみる
==
- POSTでデータを追加
```
curl -X POST -H "Content-Type: application/json" -d '{"quote":"fugafuga"}' localhost:8000/api/quotes/
```
- エラーが出なければOK
- 再度、GET
```
curl http://localhost:8000/api/quotes/
```
- 入れた文字が帰ってくる
```
[{"quote":"fugafuga"}]
```

---

デプロイについて
==

---

デプロイの話
==
- djangoのwebサーバは開発用の簡易的なサーバのため、アプリケーションの運用には向いていない
  > django公式では禁止されています
  - 大量のトラフィックをさばくだけの性能を持っていない
  - セキュリティ対策がされていない
  - SSL/TLSのトラフィックに対応していない
- そもそも、実際にサービスを提供するときにcloud9上で実行するわけにはいかない
- 実際にサービスする際は、インターネットとdjangoの間にwebサーバを配置すること

---

デプロイの方法（webサーバなし版）
==
1. djangoアプリケーションのディレクトリ（今回の例では、hogepj以下）をzipなりで圧縮する。
> gitで管理している場合はこの手順は不要
2. インターネットからアクセスできるところにEC2でVMを構築する
3. djangoとdjango rest frameworkをpipでインストールする
4. 上記VMにSSHでログインし、zipを展開するか、git cloneしてdjangoアプリをVMに展開する
5. djangoアプリをrunserverコマンドで起動する
#### cloud9でやってたことをVMでやるだけなので楽ですが、webサーバを使っていないので、本来この方式はだめです

---

デプロイの方法（webサーバあり版）
==
1. インターネットからアクセスできるところにEC2でVMを構築する
2. 上記VMに、nginx（webサーバ）をaptやyumなどでインストールする
3. 以下の例を参考にnginx.confを作成する
  https://github.com/JinKanai/tocaro-bot-framework/blob/feature/frameworking/example/webserver/harukabot.conf
4. 上記設定ファイルを、インストールしたnginxの設定ファイルのディレクトリに置く　
5. webサーバなし版と同じ手順で、djangoアプリを展開する

---
デプロイの方法（webサーバあり版）
==
6. Python仮想環境内で、uswgiをインストールする
   ```
   pip install uwsgi
   ``` 
7. 以下の例を参考にuwsgi.iniを作成する
https://github.com/JinKanai/tocaro-bot-framework/blob/feature/frameworking/example/harukabot/uwsgi.ini
8. uswgiを起動する
9. nginxを起動する
10. http://VM:8080/にアクセスできればOK！

---

uwsgiについて
==
- 前ページで触れたとおり、「めんどくさい」です
## こんなめんどくさいをしないといけないのも、AWS API GatewayでAPIを作れないtocaroの〇〇（自主規制）仕様のせいです。
> コマンドを受け付けない場合はAPIGWでも作れます
- uwsgiの使い方は「django uwsgi」とかでググるとたくさん出てきます
- dockerを勉強する気概のある方は、tocaro-bot-frameworkのコンテナ構成をそのまま使ってもOKです

---

AWS Lambda簡易講座
==

---

AWS Lambdaとは
==
- サーバを構築せずに、アプリケーションコードを実行出来る仕組み
  - サーバのサイジングや構築など、サーバ周りの作業が一切不要
 - アプリケーション作成者が、アプリのロジックだけに専念できる
 - Lambdaファンクションを直接動かすことはAWSコンソールからしかできないため、利用するにはトリガーの設定が必要
   - タイマー、AWSの各種イベント、webAPIへのアクセス、など
 - 実行された回数と実行時間に対してのみ課金される
   - 月100万回の呼び出しまでは無料
   - 月40万秒までの実行時間に対しては無料（デフォルト設定の場合）

---

Lambdaの利用例
==
### チャットボットへの定期投稿
- タイマーをトリガーにして、定期的にtocaroなどに投稿する
### AWSリソースの異常通知
- cloudwatchイベントをトリガーにして、異常状態がしきい値を超えたらメール通知するなど
### ログの整形と保存処理
- AWS kinesisと組み合わせて、受信したログを整形してデータベースなどに配置する

---

Lambdaへのコードの配置とテスト方法
==

### 実演しますので、試してみたい方は手元の環境でやってみてください


---

企画アドバイスコーナー
==
- 各チームの企画についてアドバイスさせていただきます
> 資料を手抜きしたかったわけではありません

---

本日は以上です。
お疲れさまでした
==
- コンテストがんばってください！
