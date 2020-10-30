#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 加密 MD5 sha1 sha256 sha512
import hashlib

msg = "hello world"

md5 = hashlib.md5(msg.encode('utf-8')).hexdigest()
print(md5)
print(len(md5))
print('-----------------------------')

sha1 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
print(sha1)
print(len(sha1))
print('-----------------------------')

sha256 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
print(sha256)
print(len(sha256))
print('-----------------------------')

sha512 = hashlib.sha512(msg.encode('utf-8')).hexdigest()
print(sha512)
print(len(sha512))
print('-----------------------------')
