#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

