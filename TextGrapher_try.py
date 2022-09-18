# Author: heyihui
# Date: 22-09-18

from text_grapher import *

with open("news_finance_01.txt",'r',encoding='utf8') as f:
    content = f.read()

# "news_finance_01.txt"
print(content)
handler = CrimeMining()
handler.main(content)
print("Finished!")
