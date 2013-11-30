# Import third party libs
import urwid

# Import sconsole libs
import sconsole.cmdbar
import sconsole.static
import sconsole.jidtree

FOOTER = [
        ('title', 'Salt Console'), '  ',
        ('key', 'UP'), '  ',
        ('key', 'DOWN'), '  ']


class Manager(object):
    def __init__(self, opts):
        self.opts = opts
        self.cmdbar = sconsole.cmdbar.CommandBar(self.opts)
        self.header = urwid.LineBox(urwid.Text(('banner', 'Salt Console'), align='center'))
        self.jidtree = sconsole.jidtree.JIDView()
        self.body_frame = self.body()
        self.footer = urwid.AttrMap(urwid.Text(FOOTER), 'banner')
        self.view = urwid.Frame(
                body=self.body_frame,
                header=self.header,
                footer=self.footer)

    def body(self):
        return urwid.Frame(self.jidtree.listbox, header=self.cmdbar.grid)

    def unhandled_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def start(self):
        palette = sconsole.static.get_palette(
                self.opts.get('theme', 'std')
                )
        loop = urwid.MainLoop(
                self.view,
                palette=palette,
                unhandled_input=self.unhandled_input)
        loop.run()
