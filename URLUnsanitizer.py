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

unsanitizedColon = re.sub('[:]', ':', URLs)
unsanitizedHTTP = re.sub('hxxp', 'http', unsanitizedColon)
unsanitizedURLs = re.sub('[.]', '\.', unsanitizedHTTP)


print('\nRe-written unsanitized URLs:')
print(unsanitizedURLs)