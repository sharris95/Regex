#Email Extraction Enhancement

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
exclude_domain = 'exclude.com'
pattern = fr"\b[A-Za-z0-9._%+-]+@(?!{exclude_domain})[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)