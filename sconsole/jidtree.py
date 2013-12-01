'''
Manage the job tree
'''

# Import third party libs
import urwid

# Import sconsole libs
import sconsole.static


class JIDWidget(urwid.TreeWidget):
    '''
    Manage the display of the job return data
    '''
    def get_display_text(self):
        return 'Job ID'


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
        data = self.get_value()
        return range(len(data))

    def load_child_node(self, key):
        value = self.get_value()
        if 'jids' in value:
            data = value['jids'][key]
            childclass = JIDParent
        if 'minions' in value:
            data = value['minions'][key]
            childclass = JIDParent
        else:
            data = value
            childclass = JIDNode
        return childclass(data, parent=self, key=key)


class JIDView(object):
    def __init__(self):
        self.treetop = JIDParent({})
        self.listbox = urwid.TreeListBox(urwid.TreeWalker(self.treetop))
        self.listbox.offset_rows = 1

    def update(self, loop, user_data=None):
        pass
