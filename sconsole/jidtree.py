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
        value = self.get_node().get_value()
        if 'jids' in value:
            return 'Job IDS'
        elif value.keys()[0].startswith('_|-'):
            return value.keys()[0]
        elif not value.keys()[0].startswith('_|-') and 'return' not in value:
            return value.keys()[0]
        else:
            return str(value['return'])


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
        value = self.get_value()
        if 'jids' in value:
            keys = range(len(value['jids']))
            return keys
        elif value.keys()[0].startswith('_|-'):
            keys = range(len(value[value.keys()[0]]))
            return keys
        elif not value.keys()[0].startswith('_|-') and 'return' not in value:
            return range(len(value))
        return range(len(value))

    def load_child_node(self, key):
        value = self.get_value()
        if 'jids' in value:
            data = value['jids'][key]
            childclass = JIDParent
        elif value.keys()[0].startswith('_|-'):
            data = value[value.keys()[0]][key]
            childclass = JIDParent
        elif not value.keys()[0].startswith('_|-') and 'return' not in value:
            data = value[value.keys()[0]]
            childclass = JIDNode
        else:
            data = value
            childclass = JIDNode
        return childclass(data, parent=self, key=key)


class JIDView(object):
    def __init__(self):
        self.treetop = JIDParent(sconsole.static.tree_seed())
        self.listbox = urwid.TreeListBox(urwid.TreeWalker(self.treetop))
        self.listbox.offset_rows = 1

    def update(self, loop, user_data=None):
        pass
        #self.treetop.set_child_node(JIDNode)
        #sconsole.static.msg(dir(self.treetop))
