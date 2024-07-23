# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 08:32:44 2024

@author: tiwashima
"""

import re

urlList = open('c:\\dir\\to\\file.ext')
URLs = urlList.read()
print('Original URLs:')
print(URLs)

sanitizedColon = re.sub(':', '[:]', URLs)
sanitizedHTTP = re.sub('http', 'hxxp', sanitizedColon)
sanitizedURLs = re.sub('\.', '[.]', sanitizedHTTP)


print('\nRe-written sanitized URLs:')
print(sanitizedURLs)