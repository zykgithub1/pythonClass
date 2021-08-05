from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba


# dictionary feature extraction
def cut_words(text):
    """
    cut chinese words
    :param text:
    :return:
    """
    ret = " ".join(list(jieba.cut(text)))
    return ret


def dic_demo():
    """
    dictionary feature extraction
    :return: None
    """
    data = [{'city': '北京', "temperature": 100},
            {'city': '上海', "temperature": 60},
            {'city': '深圳', "temperature": 30}, {'city': '天津', "temperature": 40}]
    # instantiation
    transfer = DictVectorizer()
    # fransform
    new_data = transfer.fit_transform(data)
    print(new_data)
    # get teature name
    names = transfer.get_feature_names()
    print(names)


def english_text_demo():
    """
    extraction of text ->count rate of each words
    :return:
    """
    data = ["life is short,i like python",
            "life is too long,i dislike python"]
    transfer = CountVectorizer(stop_words=["dislike"])
    new_data = transfer.fit_transform(data)
    print(new_data)
    names = transfer.get_feature_names()
    print(names)


def chinese_text_demo():
    data = ["人生苦短,我喜欢python", "生活太长久，我不喜欢python"]
    transfer = CountVectorizer()
    new_data = transfer.fit_transform(data)
    print(new_data)
    print(new_data.toarray())
    names = transfer.get_feature_names()
    print(names)


def chinese_text_demo2():
    data = ["中方坚决反对打着所谓“自由”“人权”“民主”等旗号滥施单边制裁、干涉他国内政。近期美国陆续宣布对古巴机构、官员实施制裁，严重违反国际关系基本准则，再一次向世人展示了什么是美式双标和霸凌。",
            "众所周知，美国的经济、商业、金融封锁才是妨碍古巴改善经济民生、侵犯古人民生存权发展权的根源.",
            "我们要求美方认真倾听国际社会的普遍呼声，立即全面取消对古制裁封锁，立即停止借题发挥，粗暴干涉，破坏稳定。"]
    words_list = []
    for i in data:
        words_list.append(cut_words(i))
    print(words_list)
    transfer = CountVectorizer()
    new_data = transfer.fit_transform(data)
    print(new_data)
    print(new_data.toarray())
    names = transfer.get_feature_names()
    print(names)


def tfidf_demo():
    data = ["中方坚决反对打着所谓自由人权民主等旗号滥施单边制裁、干涉他国内政。近期美国陆续宣布对古巴机构、官员实施制裁，严重违反国际关系基本准则，再一次向世人展示了什么是美式双标和霸凌。",
            "众所周知，美国的经济、商业、金融封锁才是妨碍古巴改善经济民生、侵犯古人民生存权发展权的根源.",
            "我们要求美方认真倾听国际社会的普遍呼声，立即全面取消对古制裁封锁，立即停止借题发挥，粗暴干涉，破坏稳定。"]
    words_list = []
    for i in data:
        words_list.append(cut_words(i))
    print(words_list)
    transfer = TfidfVectorizer()
    new_data = transfer.fit_transform(data)
    print(new_data)
    print(new_data.toarray())
    names = transfer.get_feature_names()
    print(names)

if __name__ == '__main__':
    tfidf_demo()
