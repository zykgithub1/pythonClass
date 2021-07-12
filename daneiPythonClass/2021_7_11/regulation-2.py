import re
"""
/A start with /Z end with
\b word edge \B not a word edge
->
match character :  .  [...] \d \D \w \W \s \S
match     repeat:  * + ? {n} {m,n}
match   position:  ^ $ \Z \A \b \B
other           :  | ()  \   
"""
if __name__ == '__main__':
    print(re.findall("world\Z","hello world"))
    print(re.findall("\Aworld\Z", "world"))
    print(re.findall("is", "this is a test"))
    print(re.findall(r"\Bis\b", "this is a test"))
    print(re.findall(r"-?\d+\.?\d*", "12 -36 28 1.34 -3.8"))
    print(re.findall("\\$\\d+", "日薪：$100"))
    print(re.findall("\\w+", "日薪：$100"))
    print(re.findall(r"\\", r"\\"))
    s=r"hello \n word "
    print(s)
    pass
