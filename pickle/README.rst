このフォルダについて
==============================
    Pythonオブジェクトをシリアライズするモジュール pickle を試したコード。

参考
--------------------
    http://diveintopython3-ja.rdy.jp/serializing.html


各ファイル
--------------------
    Event.py

        シリアライズ対象とするクラスのサンプル。
        メンバは Event._pid, Event._setting の二つ。

    write_pickle.py

        Eventクラスを生成して、それをシリアライズしたデータを
        ファイル名'event.pickle'へ書き込む。

    event.pickle

        write_pickle.pyでEventクラスを書きこんだファイル

    read_pickle.py

        event.pickleからデータを読み込んでEventクラスを取得し、
        その内容をprintする。
        write_pickle.pyで書き込んだ内容と一致することを確認する。

注意
--------------------
    Eventモジュールのimport方法は、write_pickle.pyとread_pickle.pyとで
    同じようにしておかなくてはならない。

    つまり、片方が import Event で、もう一方が from Event import * のように、
    クラスを参照する上でのパス（？）が互いに異なると、読み出し時に未定義
    クラスと言われて失敗する。
