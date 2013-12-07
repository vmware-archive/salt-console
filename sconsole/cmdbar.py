'''
Define the command bar
'''
# Import third party libs
import urwid

# Import salt libs
import salt.client


class CommandBar(object):
    '''
    The object to manage the command bar
    '''
    def __init__(self, opts):
        self.opts = opts
        self.local = salt.client.LocalClient(mopts=opts)
        self.tgt_txt = urwid.Text('Target')
        self.tgt_edit = urwid.Edit()
        self.fun_txt = urwid.Text('Function')
        self.fun_edit = urwid.Edit()
        self.arg_txt = urwid.Text('Arguments')
        self.arg_edit = urwid.Edit()
        self.go_button = urwid.Button('GO!', self.run_command)
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

    def run_command(self, button, user_data):
        '''
        Execute the corresponding salt command
        '''
        tgt = self.tgt_edit.get_edit_text()
        fun = self.fun_edit.get_edit_text()
        args = self.arg_edit.get_edit_text().split()
        self.local.cmd_async(tgt, fun, args)
