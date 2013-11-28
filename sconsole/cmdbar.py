'''
Define the command bar
'''
# Import third party libs
import urwid


class CommandBar(object):
    '''
    The object to manage the command bar
    '''
    def __init__(self, opts):
        self.opts = opts
        self.tgt_txt = urwid.Text('Target')
        self.tgt_edit = urwid.Edit()
        self.fun_txt = urwid.Text('Function')
        self.fun_edit = urwid.Edit()
        self.arg_txt = urwid.Text('Arguments')
        self.arg_edit = urwid.Edit()
        self.go_button = urwid.Button('GO!')
        self.grid = urwid.GridFlow(
                [self.tgt_txt,
                 self.tgt_edit,
                 self.fun_txt,
                 self.fun_edit,
                 self.arg_txt,
                 self.arg_edit,
                 self.go_button],
                cell_width=10,
                h_sep=1,
                v_sep=1,
                align='left')
