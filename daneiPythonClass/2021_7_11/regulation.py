import re
"""
1-> ^,$ start end
2-> | or
3-> * ->  woooo
4-> + ->  could find capital word like L in "L am good"
5-> ? ->  the word before ? shows up 0 or 1 time   =>"-?[0-9]+"
6-> {}:    ab{3} the word before {}show up 3 times  
7-> {1,5}: show times between 1 to 5
8-> \d+ means number  \D+ means not number
9-> w+   include number character \ and utf-8 charset
10-> W+ is opposite to w+  
11-> \s  match empty character(\n \r \t \f )  \S match character which is not empty
"""
if __name__ == '__main__':
#     s="zyk:增益开，曾驿凯\n\\nee\\\\n：qtx@tedu.cn882312"
#     print(re.findall("\w\w凯\n",s))
#     print(re.findall("凯\n", s))
#     print(re.findall("[\n]", s))
#     print(re.findall("[^aeiou]","hellow world\n "))   #^in[] means !
#     print(re.findall("^Jame","HI,Jame"))              #must start with Jame
#     print(re.findall("^Jame", "Jame,wow"))
#     print(re.findall("Jame$", "Jame,wow"))
#     print(re.findall("Jame$", "hello,Jame"))          # $ means end with Jame
#     print(re.findall("wo*", "wooooooooooo__~~~``w!")) #* ->the character in the front of *
# #                                                        show up 0 time or several times
#     print(re.findall("\wd*", "wooooooooooo__~~~``w!"))
#     print(re.findall("\w+",'how are you'))
#     print(re.findall("[a-zA-Z]*",'how are you'))
#     print(re.findall("[A-Z][a-z]*", 'How are you!Find Jame,No'))# findAll capital word
#     print(re.findall("[A-Z][a-z]+", 'L am good!A boy'))    #the character in the front of + shows up 1 or more than 1 times
#     print(re.findall("\d+","167 -99 32 -5 adss1221 sda-12"))
    print(re.findall("[^ ]+","Port-9 Error #404# %@STD"))
    print(re.findall("ab{3}","abcdabbbbbbbbbbbbbbbbabbbabbbbbb"))
    print(re.findall("1[0-9]{10}","zyk:19923479049"))
    print(re.findall("[1-9][0-9]{5,10}","qq:787950451,qq:239975642"))
    print(re.findall("\W+","hello   world1212"))


