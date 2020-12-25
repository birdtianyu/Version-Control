# 情報収集のレポート
## 名前: Xu Hongkun  　学籍番号: 20M31378

## 1. Linuxコマンドについて
>演習1　文字‘`#`’のASCIIコードを調べよ


> Googleで検索した結果: 
>
> + [ASCII Code - Wikipedia](https://zh.wikipedia.org/wiki/ASCII)

ずっとWindowsオペレーションシステムを使っているので、Linuxコマンドについてぜんぜん知らなかった。<br>
そこで、Linuxのヘルプコマンド`help`,`man`,`info`と`tldr`の詳細を調べた。

### `help`
```bash
help <command>      # builtin commands.
```
```bash
<command> --help     # external commands.
```
```bash
type <command>      # check builtin or external
```

### `man`
```bash 
man <section> <command>
```
参考：[man command - Wikipedia](https://zh.wikipedia.org/wiki/%E6%89%8B%E5%86%8C%E9%A1%B5) 


### `info`
```bash 
info <command>
```
参考：[info command - Zhihu](https://zhuanlan.zhihu.com/p/105096446)

### `tldr`「Too long, Don't read」
面白いコマンドです。インストール必要がある。
```bash
tldr <command>
```
参考：[tldr command - Github](https://github.com/tldr-pages/tldr)

>演習2　tarでディレクトリを圧縮し、ファイルを作る

Linuxの`tar`コマンドについて
### `tar`
```bash
tar -czvf アーカイブ.tgr.gz 対象ディレクトリ
```

ディレクトリ中のファイルのアーカイブを作成しgzip形式で圧縮する

```bash 
tar -xzvf アーカイブ.tgr.gz
```
gzipで圧縮されたアーカイブを展開する


| 短いオプション    | 長いオプション    | 意味    |
| --------------- |------------------|-----|
| -c             | --create           | 新しいアーカイブを作成する            |
| -z             | --gzip             |   アーカイブをgzip形式で圧縮する、gzip形式で圧縮されたアーカイブを展開する <br>（拡張子は「.tar.gz」または「.tgz」） |
| -v             | --verbose          |   処理したファイルを詳しく出力する |
| -t             | --list             |   アーカイブの内容の一覧を表示する |
| -x             | --extract,--get    |   アーカイブからファイルを抽出する |
| -f アーカイブ  | --file=アーカイブ   |   アーカイブファイル名を指定する |

Linuxのコマンドはまだたくさんあるので、引き続き学んでいく。

## 2. コラッツの問題とコンパイラの最適化
>演習3　次のプログラムについて最適化しない場合とした場合を比べ、最適化の影響を調べよ

```C
int collatz(int n) {
    if (n == 1) return 1;
    if (n%2) return collatz(3*n + 1);
    else     return collatz(n/2);
}
```

> gccとはGNU Compiler Collectionの略で、[GNUプロジェクト](http://e-words.jp/w/GNU.html)が開発・公開しているコンパイラです。(1987年から)

gccで最適化した結果

```x86asm
collatz(int):
        mov     eax, 1
        ret
```

> Clang(クラン)とはＣ言語族(C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript)をターゲットとした新しいコンパイラです。(2005年から)

Clangで最適化した結果

```	x86asm
collatz(int):                            # @collatz(int)
        i32.const       1
        end_function
```



## 3. OSSプロダクトに関する情報収集
> オープンソースソフトウェア（英: Open Source Software、略称: OSS）とは、利用者の目的を問わずソースコードを使用、調査、再利用、修正、拡張、再配布が可能なソフトウェアの総称である

Djangoを用いて自分のウェブサイトを作りたいと思いますが、まだ決めていない状態です。<br>

> **Django**（ジャンゴ）は、Pythonで実装されたWebアプリケーションフレームワークです。
>
> 公式ホームページ：https://docs.djangoproject.com/zh-hans/3.1/

とりあえずいろいろ試してみたいです。<br>

### Django

a.  `Flying_Colors`というプロジェクトを作成する

```shell
$ django-admin startproject Flying_Colors
```

ディレクトリ構造:

```
│  db.sqlite3
│  manage.py
│  
└─Flying_Colors
    │  asgi.py
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
    │  
    └─__pycache__
```

b. 中に入って`helloworld`というアプリケーションの作成

```shell
$ python3 manage.py startapp helloworld
```

c.  実行する

```bash
$ python manage.py runserver
```



## 4. Markdownの使い方

参考：<br>
https://zhuanlan.zhihu.com/p/75286458 <br>
https://pandao.github.io/editor.md/examples/full.html <br>
https://www.jianshu.com/p/191d1e21f7ed <br>

> Typoraの使い方:

https://sspai.com/post/54912

> プログラミング言語の表示

| 言語名         | キーワード   |
| :------------- | :----------- |
| Bash           | bash         |
| CoffeeScript   | coffeescript |
| C++            | cpp          |
| C#             | cs           |
| CSS            | css          |
| Diff           | diff         |
| HTTP           | http         |
| Ini            | ini          |
| Java           | java         |
| JavaScript     | javascript   |
| JSON           | json         |
| Makefile       | makefile     |
| Markdown       | markdown     |
| Objective-C    | objectivec   |
| Perl           | perl         |
| Python         | python       |
| Ruby           | ruby         |
| SQL            | sql          |
| XML            | xml          |
| ARMアセンブリ  | armasm       |
| AVRアセンブリ  | avrasm       |
| MIPSアセンブリ | mipsasm      |
| x86アセンブリ  | x86asm       |
| Elixir         | elixir       |
| Elm            | elm          |
| Erlang         | erlang       |
| F#             | fsharp       |
| Haskell        | haskell      |
| GLSL           | glsl         |
| Clojure        | clojure      |
| Lisp           | lisp         |

## 5. cmdでディレクトリ構造を生成する方法

```shell
tree ディレクトリ /f >tree.txt
```
