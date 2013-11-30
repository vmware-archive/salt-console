'''
Manage the job tree
'''

# Import third party libs
import urwid


class JIDWidget(urwid.TreeWidget):
    '''
    Manage the display of the job return data
    '''
    def get_display_text(self):
        return 'Widget'


class JIDNode(urwid.TreeNode):
    '''
    Manage the Minion layer
    '''
    def load_widget(self):
        return JIDWidget(self)


class JIDParent(urwid.ParentNode):
    '''
    '''
    def load_widget(self):
        return JIDWidget(self)

    def load_child_keys(self):
        return [1, 2, 3]

    def load_child_node(self, key):
        return JIDNode('node', parent=self, key=key)


class JIDView(object):
    def __init__(self):
        self.treetop = JIDParent({})
        self.listbox = urwid.TreeListBox(urwid.TreeWalker(self.treetop))
        self.listbox.offset_rows = 1
