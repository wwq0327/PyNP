#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    domparsesample.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-22
    :from: Python Network Programming
"""

from xml.dom import minidom, Node
import re, textwrap

class SampleScanner:
    def __init__(self, doc):
        for child in doc.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and child.tagName == 'book':
                self.handleBook(child)

    def gettext(self, nodelist):
        '''扫描节点，查询文本并建立一个含有这些文本的字符串列表。接着它把这个列表合成一个
        单独的字符串，并把一个或多个空格字符转成一个单独的空格。
        '''
        
        retlist = []
        for node in nodelist:
            if node.nodeType == Node.TEXT_NODE: # 空格
                retlist.append(node.wholeText)
            elif node.hasChildNodes:  # 存在了节点
                retlist.append(self.gettext(node.childNodes)) # 递归调用本身

        return re.sub('\s+', ' ', ''.join(retlist))

    def handleBook(self, node):
        """这段处理<book>的直接子节点。如果发现一个标题，它就打印出来。对于作者和章节，
        它会调用这些标签相应的处理函数，其它的则它忽略。
        """
        
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'title':
                print "Book title is:", self.gettext(child.childNodes)
            if child.tagName == 'author':
                self.handleAuthor(child) # 调用作者标签处理函数
            if child.tagName == 'chapter':
                self.handleChapter(child) # 调用章节签标处理函数

    def handleAuthor(self, node):
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'name':
                self.handleAuthorName(child)
            elif child.tagName == 'affiliation':
                print "author affiliation:", self.gettext([child])

    def handleAuthorName(self, node):
        surname = self.gettext(node.getElementsByTagName("last"))
        givenname = self.gettext(node.getElementsByTagName("first"))
        print "Author Name: %s, %s" % (surname, givenname)

    def handleChapter(self, node):
        print " *** Start of Chapter %s: %s" % (node.getAttribute('number'),
                                                self.gettext(node.getElementsByTagName('title')))
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
            if child.tagName == 'para':
                self.handlePara(child)

    def handlePara(self, node):
        partext = self.gettext([node])
        partext = textwrap.fill(partext)
        print  partext
        print

if __name__ == '__main__':
    doc = minidom.parse('sample.xml')
    SampleScanner(doc)

        
