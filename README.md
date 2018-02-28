# RTC-RobotARM

ロボットアームに関するレポジトリです。

(ここにロボットアームの写真が入る)

このロボットアームはサーボを3個使用し、実際にものをつかむこともできるものとなります。

# How to install

### python version

必要なpython環境は `python2.7.*`系統ですので

```
$ python -V
> Python 2.7.9
```

などが返ってくることを確認し。もしバージョンが合っていない場合は

```
$ pyenv local 2.7.*
```
でpyenvを用いてバージョンを合わせるか

```
$ pyenv virtualenv 2.7.* RobotARM
```
でvirtualenv環境を構築してpythonのバージョンを合わせてください。

### Install
このリポジトリをcloneします。
```
$ git clone https://github.com/FaBoPlatform/RTC-RobotARM.git
```

ディレクトリ構造が以下のようになっているのを確認します。

```
$ tree -d

.
├── RobotARMRTC
│   ├── cmake
│   ├── cmake_modules
│   ├── cpack_resources
│   ├── doc
│   │   └── content
│   ├── idl
│   ├── include
│   │   └── RobotARM_RTC
│   └── src
└── lib
```

必要になるpythonライブラリはlibのところに固まっているので、そこで` pip install `

```
$ cd lib
$ pip install -r requirements.txt
```

このインストールが終了すると実際に使うことができます。

### OpenRTM
ロボットアームを使用するためには[OpenRTM](https://www.openrtm.org/openrtm/ja/content/openrtm-aist-official-website)をインストールする必要があります。

今回は事前にインストールしてあるということを想定してインストールを書きましたが、もしインストールがされていない場合は以下を参照のことインストールをお願いします。

[fabo OpenRTM docs / OpenRTMのインストール](http://docs.fabo.io/openrtm/install.html)

## 実行

実際にサーボを動かします。

### 使用するもの
- Raspberry pi 3
- [#502 OUT/IN Shield for Raspberry Pi](http://fabo.io/502.html)
- ロボットアーム(サーボ3個)
- 電源(モバイルバッテリー)

### 接続
ロボットアームに搭載しているサーボをシールドに接続します。

接続するのはPWMポート、ロボットアームを立てた際に、上から順に
PWM0 -> PWM1 -> PWM2 というようにPWMポートに接続します。

ここでサーボの配線を間違ってしまうとサーボの故障だけではなく最悪の場合Raspberry piも故障する場合があるので注意してください。

