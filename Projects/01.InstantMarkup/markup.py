# markup.py
# this is the parser to run that takes plain text and converts to HTML
import sys, re
from handlers import *
from rules import *
from util import *


class Parser:
    # A parser reads a text file, applying rules and controlling
    # a handler.
    def __init__(self, handler):
        # initialised the handler, rules list and filters list
        self.handler = handler
        self.rules = []
        self.filters = []
        
    def addRule(self, rule):
        # adds rules to the self.rule list.
        self.rules.append(rule)
    
    def addFilter(self,pattern,name):
        # adds a filter to the self.filter list.
        def filter(block, handler):
            # applies the regular expression format to the filter.
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
        
    def parse(self, file):
        # starts the document
        self.handler.start('document')
        # iterates over the blocks in the text file. For each block
        # it applies the filters and rules.
        for block in blocks(file):
            for filtera in self.filters:
                # filter replaces *emphasis* with <em>emphasis<\em>
                block=filtera(block,self.handler)
            for rule in self.rules:
                # rules check if the rule applies.
                # allows headings to be finished before para is started. 
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        # ends document
        self.handler.end('document')
    
class BasicTextParser(Parser):
    # a specific parser that adds rules and filters in its constructor.
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
    
handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
