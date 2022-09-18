import os
from pyltp import Segmentor

# 分词
sentence = '我想听一首周杰伦的歌'
LTP_DIR = "./ltp_data_3.3.1"
segmentor = Segmentor(os.path.join(LTP_DIR, "cws.model"))
#segmentor.load(os.path.join(LTP_DIR, "cws.model"))
words = list(segmentor.segment(sentence))
segmentor.release() #释放模型
print(words)


# 词性标注
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller
postagger = Postagger(os.path.join(LTP_DIR,"pos.model"))
#postagger.load(os.path.join(LTP_DIR,"pos.model"))
postags = list(postagger.postag(words))
postagger.release()
for x,y in zip(words,postags):
    print(x,y)


# 依存句法分析
parser = Parser(os.path.join(LTP_DIR, "parser.model"))
#parser.load(os.path.join(LTP_DIR, "parser.model"))
arcs = parser.parse(words, postags)


i=0
for word,arc in zip(words,arcs):
    i=i+1
    #print(str(i)+'/'+word+'/'+str(arc.head)+'/'+str(arc.relation))
    #print(str(i)+'/'+str(arc[0]))
    print(str(i)+'/'+word+'/'+str(arc[0])+'/'+str(arc[1]))
    #print(str(i)+'/'+word+'/'+str(arc['head'])+'/'+str(arc['relation'])) #这个不行
parser.release()
