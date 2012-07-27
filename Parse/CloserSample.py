#encoding: shift-jis

from datetime import datetime
import sys


def filter_date_from(date_from):
    _date_from = datetime.strptime(date_from, "%Y%m%d%H%M%S")
    def _filter_date_from(date_str):
        log_date = datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
        return _date_from <= log_date
    return _filter_date_from

"""
単体テストだけ実行
  > python -m hoge.py
テスト結果詳細も表示
  > python -m hoge.py -v
"""
def filter_date_to(date_to):
    """
    >>> (filter_date_to("20120727010203"))("2012/07/27 01:02:03")
    True
    >>> (filter_date_to("20120727010203"))("2012/07/27 01:01:59")
    True
    >>> (filter_date_to("20120727010203"))("2012/07/27 01:02:04")
    False
    """
    _date_to = datetime.strptime(date_to, "%Y%m%d%H%M%S")
    def _filter_date_to(date_str):
        log_date = datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
        return log_date <= _date_to
    return _filter_date_to


if __name__=='__main__':
    argvs = sys.argv

    is_from = filter_date_from(argvs[1])
    is_to   = filter_date_to(argvs[2])

    for date in argvs[3:]:
        print "\ndate =", date
        if is_from(date):
            pass
        else:
            print "   date < from"

        if is_to(date):
            pass
        else:
            print "   to < date"


