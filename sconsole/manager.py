# Import third party libs
import urwid

# Import sconsole libs
import sconsole.cmdbar
import sconsole.static
import sconsole.jobtree

FOOTER = [
        ('title', 'Salt Console'), '  ',
        ('key', 'UP'), '  ',
        ('key', 'DOWN'), '  ']


class Manager(object):
    def __init__(self, opts):
        self.opts = opts
        self.cmdbar = sconsole.cmdbar.CommandBar(self.opts)
        self.cmdbox = urwid.LineBox(self.cmdbar.grid)
        self.header = urwid.LineBox(urwid.Text(('banner', 'Salt Console'), align='center'))
        self.jobtree = sconsole.jobtree.JobTree(self.opts)
        self.jobbox = urwid.LineBox(self.jobtree.tree)
        self.body_frame = self.body()
        self.footer = urwid.AttrMap(urwid.Text(FOOTER), 'banner')
        self.view = urwid.Frame(
                body=self.body_frame,
                header=self.header,
                footer=self.footer)

    def body(self):
        return urwid.Frame(self.jobbox, header=self.cmdbox)

    def unhandled_input(self, key):
        if key in ('meta q', 'meta Q'):
            raise urwid.ExitMainLoop()
        bindings = {'meta t': ['body', 'header', 1],
                    'meta f': ['body', 'header', 3],
                    'meta a': ['body', 'header', 5],
                    'meta j': ['body', 'body'],
                    'meta g': ['body', 'header', 6]}
        if key in bindings:
            self.view.set_focus_path(bindings[key])

    def start(self):
        palette = sconsole.static.get_palette(
                self.opts.get('theme', 'std')
                )
        loop = urwid.MainLoop(
                self.view,
                palette=palette,
                unhandled_input=self.unhandled_input)
        loop.set_alarm_in(1, self.jobtree.thread_update)
        loop.run()
