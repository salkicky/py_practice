#encoding:shift-jis

import ConfigParser

if __name__ == "__main__":
    inifile = ConfigParser.SafeConfigParser()
    inifile.read(u'sample.ini')

    print inifile.get("index1","param2")
    print inifile.get("index1","param1")
    print inifile.get("index2","param3")
    print inifile.get("index2","パラメータ４")
