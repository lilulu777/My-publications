# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:17:33 2024

@author: Wenhao, Lu
"""


import segno

url = 'https://github.com/lilulu777/My-publications/blob/main/project-MFT/author-list.md'
qr = segno.make(url, error='h')
qr.save('authors.png', scale=10, border = 1, dark='orange', light='#ffffff')
