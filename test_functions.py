#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test_output():
    """
    :return:
    """
    # output
    print('100 + 200 = %d' % (100 + 200))
    print("I'm OK!")  # 单引号中可包含双引号，双引号中可包含单引号
    print('I\'m "OK"!')
    print('I\'m \"OK\"!')
    print('\\\n\\')
    print(r'\\\t\\')
    print("A -> %s, a -> %s" % (ord('A'), ord('a')))
    print("65 -> %s, 97 -> %s" % (chr(65), chr(97)))

    # calculate
    print(1 / 3, 2 / 3, 3 / 3, 4 / 3)
    print(1.0 / 3, 2.0 / 3, 3.0 / 3, 4.0 / 3)
    print(1.0 // 3, 2.0 // 3, 3.0 // 3, 4.0 // 3)
    print(1 % 2, 2 % 2, 3 % 2, 4 % 2)


def my_abs(x):
    """
    :param x:
    :return:
    """

    if x >= 0:
        return x
    else:
        return -x


def nanoi(n, pillar_src="A", pillar_bridge="B", pillar_tar="C"):
    """
    :param n:
    :param pillar_src:
    :param pillar_bridge:
    :param pillar_tar:
    :return:
    """

    if n == 1:
        print("%s -> %s" % (pillar_src, pillar_tar))
        return

    nanoi(n - 1, pillar_src, pillar_tar, pillar_bridge)
    print("%s -> %s" % (pillar_src, pillar_tar))
    nanoi(n - 1, pillar_bridge, pillar_src, pillar_tar)
    return


if __name__ == "__main__":
    my_abs(-3)
