このフォルダについて
==============================
    Pythonオブジェクトをシリアライズするモジュール pickle を試したコード。


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
