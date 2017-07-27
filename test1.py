'''
1. F1 score take both precision and recall into consideration and is high when the two criteria are
balanced rather than prefering one of them. Accuracy, instead, are often useless when positive
 and negative cases are very different in numbers.
 
2. I think there are two reasons at least. One is that the early neural computation model prefer
differentiable activation functions so a sigmoidal function is used. Another reason is for deep
neural networks, a binary activation function may have more severe vanishing gradient problem,
hence a ReLU is prefered.

3. Bias is how good a model can fit the target value in average; variance is how stable is the
resuts. In many cases, we have make tradeoff between bias and variance because a bias too low make
cause overfitting.

4. The purpose of pruning a tree is to avoid overfitting (when it goes too deep). For random forest,
the overfitting problem is less severe because each tree are trained with a small part of
randomly-distributed samples.

5. One-hot is when a target value is presented by only an '1' and other values '0' in the value space.
Many classfication problems such as MNIST and image classification naturally use this.

6. Dropout (drop nodes randomly while traning); Augmenting sample (random twist of images for example);
Early stopping; L1/L2 regularization
'''


# -*- coding: utf-8 -*-
"""
I only time for doing part of the quiz 1...XD

"""
bigram_dict = dict()
trigram_dict = dict()

import re

def returnbigram(l):
    return [l[i:i+2] for i in range(0,len(l)-1)]

def returntrigram(l):
    return [l[i:i+3] for i in range(0,len(l)-2)]

def add2dict(gram_list):
    for gram in gram_list:
        gram=' '.join(gram)
        if gram in bigram_dict:
            bigram_dict.update({gram: bigram_dict[gram]+1})
        else:
            bigram_dict.update({gram: 1})

def add3dict(gram_list):
    for gram in gram_list:
        gram=' '.join(gram)
        if gram in trigram_dict:
            trigram_dict.update({gram: trigram_dict[gram]+1})
        else:
            trigram_dict.update({gram: 1})

with open('raw_sentences.txt','r') as fp:
    for line in fp:
        sentence = re.sub('[!,.?;:]', '', line).lower().strip()
        word_list = sentence.split(' ')
        add2dict(returnbigram(word_list))
        add3dict(returntrigram(word_list))
        
print (bigram_dict)  
print (trigram_dict)          
        
        
        
