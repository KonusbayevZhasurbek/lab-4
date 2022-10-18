"""
#1 
text = 'Мен, бүгін сабаққа бардым'
print(text.find('б',0,9))
"""

"""
#2 әріптер алмастыру
print('Hello'.replace('e', 'E'))
"""
"""
#3 
text = 'Zhasurbek is a  student of Kazakh National Technical University'
print(text.replace("Kazakh National Technical", "Satbayev")) 
"""
"""
#4 іздеп табады
S = 'Hello'
print(S.find('l'))
"""
"""
#5 үлкен әріпке алмастырады
a = "Hello, World!"
print(a.upper())
"""
"""
#6 кіші әріпке алмастыру
a = "Hello, World!"
print(a.lower())
"""
"""
#7 бос орынды толтыру
txt = "Zhasurbek"
x = txt.center(15, '*')
print(x)
"""
"""
#8 есеп каждый элементті жеке жеке қарастыру
txt = "kazakhstan ote keremet memleket"
x = txt.split()
print(x)
"""
"""
#9 әріптерді ауыстыру үлкенді кішіге кішіні үлкенге
txt = "My name is Zhasurbek"
x = txt.swapcase()
print(x)
"""
"""
#10 сөзімізді қосу
txt = "     mawina     "
n = txt.strip()
print("kalada", n, "aidap", "juru")
"""