���̃t�H���_�ɂ���
==============================
    Python�I�u�W�F�N�g���V���A���C�Y���郂�W���[�� pickle ���������R�[�h�B

�Q�l
--------------------
    http://diveintopython3-ja.rdy.jp/serializing.html


�e�t�@�C��
--------------------
    Event.py

        �V���A���C�Y�ΏۂƂ���N���X�̃T���v���B
        �����o�� Event._pid, Event._setting �̓�B

    write_pickle.py

        Event�N���X�𐶐����āA������V���A���C�Y�����f�[�^��
        �t�@�C����'event.pickle'�֏������ށB

    event.pickle

        write_pickle.py��Event�N���X���������񂾃t�@�C��

    read_pickle.py

        event.pickle����f�[�^��ǂݍ����Event�N���X���擾���A
        ���̓��e��print����B
        write_pickle.py�ŏ������񂾓��e�ƈ�v���邱�Ƃ��m�F����B

����
--------------------
    Event���W���[����import���@�́Awrite_pickle.py��read_pickle.py�Ƃ�
    �����悤�ɂ��Ă����Ȃ��Ă͂Ȃ�Ȃ��B

    �܂�A�Е��� import Event �ŁA��������� from Event import * �̂悤�ɁA
    �N���X���Q�Ƃ����ł̃p�X�i�H�j���݂��ɈقȂ�ƁA�ǂݏo�����ɖ���`
    �N���X�ƌ����Ď��s����B
