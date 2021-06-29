from linkedStack import LStack
if __name__ == '__main__':
    str_words = "{{}}}}}"
    ls = LStack()
    oppsite = {")": "(", "}": "{", "]": "["}
    left_parent = "({["
    right_parent = "}])"
    parent="{}[]()"
    def get_location(text):
        text_len=len(text)
        for i in range(text_len):
            if text[i] in parent:
                yield text[i],i
    # for i,j in get_location(str_words):
    #     print(i,j)
    def checkOpe(text):
        for pr,i in get_location(text):
            if pr in left_parent:
                ls.push((pr,i))
            elif ls.isEmpty()or ls.poll()[0]!=oppsite[pr]:
                print("在%d号位置出错%s"%(i,pr))
                break
        else:
            if ls.isEmpty():
                print("mathching  ")
            else:
                print("左括号多了 在%d号位置的%s"%(ls.poll()[0],ls.poll()[1]))
    checkOpe(str_words)



