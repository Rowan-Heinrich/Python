# rules.py
# used for processing the text - finds a condition and performs an action.

class Rule():
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    # a heading is a single line with at most 70 char's and doesnt end with ;.
    type = 'heading'
    def condition(self,block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'
    
class TitleRule(HeadingRule):
    # a title is the first block of a document, provided it is a heading.
    type = 'title'
    first = True
    def condition(self, block):
        # if the block fits the definition of a title return true;
        # otherwise return false.
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)

class ListItemRule(Rule):
    # A list is a block that begins with a '-'. as part of formatting '-' is removed.
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
    # a list begins with a block that is not a list item and a
    # subsequent list item. It ends after the last consecutive list item.
    type = 'list'
    inside = False
    def condition(self, block):
        return True
    def action(self, block, handler):
        # first case; entering the list
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        # if inside the list, and listItemRule is false (doesnt start with '-')
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    #paragraph rule is the fallback / used when no other rules are applicable.
    type = 'paragraph'
    def condition(self, block):
        return True
