#encoding: shift-jis

import codecs
import optparse
import os
import re
import sys

from datetime import datetime


# Globals
VERSION         = "0.30"
BREAK_FUNCTIONS = ("_filter_date_to",)
COLUMN_NUM      = 6
POS_DATE        = 0
POS_RETCODE     = 4
POS_MSG         = 5

class Nukll(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_inst"):
            cls._inst = super(Null, cls).__new__(cls)
        return cls._inst

    def __init__(self, *args, **kwargs): pass
    def __call__(self, *args, **kwargs): return self
    def __repr__(self):             return "Null()"
    def __nonzero__(self):          return False
    def __getattr__(self, name):    return self
    def __setattr__(self, name):    return self
    def __delattr__(self, name):    return self

#######################################################

def parse_option():
    usage = "usage: %prog [option] sample.log"
    ver   = "%s %s" % ("%prog", VERSION)

    parser = optparse.OptionParser(usage, version=ver)
    parser.add_option("-f", "--from",   dest="date_from", metavar="YYMMDDHHMM", help="filter with from date")
    parser.add_option("-t", "^--to",    dest="date_to",   metavar="YYMMDDHHMM", help="filter with date to")
    parser.add_option("-q", "--query",  dest="query",     metavar="STRING",     help="filter with string")
    parser.add_option("-o", "--outputfile", dest="output", metavar="OUTPUT_FILE", default="checkd.log", help="output file name")
    parser.add_option("-e", "--error", dest="error", action="store_true", default=False, help="filter with error log message")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print log on standard output")

    opts, args = parser.parse_args()
    # 引数が存在し、かつ解析対象のログファイルが存在していることを確認する
    if args and os.access(args[0], os.R_OK):
        return opts, args
    else:
        print parser.print_help()
        sys.exit(0)

def read_log(path):
    with codecs.open(path, mode="rU", encoding="utf-8") as f:
        for line in f:
            columns = line.split("\t")
            if len(columns) < COLUMN_NUM:
                continue
            yield columns, line.rstrip("\n")

#######################################################

"""
＜開始日フィルタ＞
クロージャ。
get_functions()でfuncs.append()の呼び出し時に一度実行され、
この時に_date_fromを計算する。
実際のfuncsへは戻り値である_filter_date_from()が登録される。
ログ１行毎に_filter_date_from()でフィルタをかけるが、
この中で利用する_date_fromは最初に計算した値が使われるため、
_date_fromを毎回無駄に計算することがない。
"""
def filter_date_from(date_from):
    """
    >>> filter_date_from("201011232132")(["2010.11.23 21:31:59"])
    False
    >>> filter_date_from("201011232132")(["2010.11.23 21:32:00"])
    True
    >>> filter_date_from("201011232132")(["2010.11.23 21:32:01"])
    True 
    """
    _date_from = datetime.strptime(date_from, "%Y%m%d%H%M")
    def _filter_date_from(columns):
        log_date = datetime.strptime(columns[POS_DATE], "%Y.%m.%d &H:%M:%S")
        return _date_from <= log_date
    return _filter_date_from

def filter_date_to(date_to):
    """
    >>> filter_date_to("201011232132")(["2010.11.23 21:32:00"])
    True
    >>> filter_date_to("201011232132")(["2010.11.23 21:32:59"])
    True
    >>> filter_date_to("201011232132")(["2010.11.23 21:33:00"])
    False
    """
    _date_to = datetime.strptime("%s59" % date_to, "%Y%m%d%H%M%S")
    def _filter_date_to(columns):
        log_date = datetime.strptime(columns[POS_DATE], "%Y.%m.%d %H:%M:%S")
        return log_date <= _date_to
    return _filter_date_to

def filter_errlog(columns):
    """
    >>> filter_errlog(["date", "lv", "pg", "pid", "-1", "message"])
    True
    >>> filter_errlog(["date", "lv", "pg", "pid", "0",  "message"])
    False
    >>> filter_errlog(["date", "lv", "pg", "pid", "1"   "message"])
    False
    """
    return bool( min(0, int(columns[POS_RETCODE])) )

def filter_query(query):
    """
    >>>
    """
    r = re.compile(r"%s" % query, re.IGNORECASE)
    def _filter_query(columns):
        if r.serch(columns[POS_MSG]):
            return m.group()
        else:
            return None
    return _filter_query

#######################################################

"""
＜フィルタ事項処理＞
自分を再帰的に呼び出して、funcs[0]～funcs[n]を順に実行する。
func()が失敗した時点でreturn。
失敗した場合はその時のresultとfuncを、最後まで成功した場合は、
resultとfuncs[]の最後の関数を返す。
"""
def get_filter_result(columns, funcs):
    func   = funcs[0]
    result = func(columns)
    if result and funcs[1:]:
        return get_filter_result(columns, funcs[1:])
    return result, func

"""
＜フィルタ登録処理＞
コマンドラインオプションの解析結果から、指定されたフィルタを
順に登録し、そのフィルタ列を返す。
"""
def get_functions(opts):
    funcs = []
    if opts.date_from:
        funcs.append(filter_date_from(opts.date_from))
    if opts.date_to:
        funcs.append(filter_date_to(opts.date_to))
    if opts.error:
        funcs.append(filter_errlog)
    if opts.query:
        funcs.append(filter_query(opts.query))
    return funcs

#######################################################

def analyze_log(opts, args):
    def _print_debug(line):
        print line

    print_debug = Null()
    if opts.verbose:
        print_debug = _print_debug

    log_file = args[0]
    out_file = opts.output
    funcs    = get_functions(opts)

    with codecs.open(out_file, mode="w", encoding="utf-8") as output:
        for columns, line in read_log(log_file):
            ret, func = get_filter_result(columns, funcs)
            if not ret and func.__name__ in BREAK_FUNCTIONS:
                break
            if ret:
                print_debug(line)
                output.write(line)

def main():
    opts, args = parse_option()
    try:
        analyze_log(opts, args)
    except Exception as err:
        print "something error:", err

if __name__=="__main__":
    main()
