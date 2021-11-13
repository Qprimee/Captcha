#!/usr/bin/env python
# -*- coding: utf-8 -*-

from captcha.image import ImageCaptcha

captcha = ImageCaptcha(width=320, height=100)

name = input("type name : ")

captcha.write(name, "cap.png")