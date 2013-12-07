'''
A job tree!
'''
# Import salt libs
import salt.utils.event
import salt.version
import salt.output

# Import sconsole libs
import sconsole.static
import sconsole.widgets
import sconsole.widgets.decoration


class JobTree(object):
    '''
    Manage a job tree
    '''
    def __init__(self, opts):
        self.opts = opts
        self.event = salt.utils.event.MasterEvent(self.opts['sock_dir'])
        self.tree = self.__job_tree()

    def __job_tree(self):
        '''
        Return a job tree for the body of the console
        '''
        simple_tree = sconsole.static.job_seed()
        if_grandchild = lambda pos: simple_tree.depth(pos) > 1
        tree = sconsole.widgets.decoration.CollapsibleIndentedTree(
                simple_tree,
                is_collapsed=if_grandchild,
                icon_focused_att='focus')
        return sconsole.widgets.TreeBox(tree)

    def get_struct(self):
        '''
        Return the underlying tree data structure for manipulation
        '''
        return self.tree._tree._tree._treelist[0][1]

    def new_jid(self, jid):
        '''
        Set up a new jid in the lower tree structure
        '''
        struct = self.get_struct()
        for subtree in struct:
            if len(subtree) > 0:
                if jid == subtree[0].text:
                    return subtree
        subtree = (sconsole.widgets.FocusText(jid), [])
        struct.insert(0, subtree)
        return subtree

    def new_ret(self, jid, minion, ret):
        subtree = self.new_jid(jid)
        found = False
        for minion_wid in subtree[1]:
            if minion_wid.text == minion:
                # update the return value
                found = True
        if not found:
            subtree[1].append(
                    (sconsole.widgets.FocusText(minion),
                        [(sconsole.widgets.FocusText(str(ret)), None)]
                        )
                    )

    def update(self, loop, user_data):
        '''
        Read in from the Salt event bus and update the job tree
        '''
        while True:
            #TODO: make work with older jid tags
            event = self.event.get_event(0.001, 'salt/job', True)
            if event is None:
                break
            if any(key not in event for key in ('tag', 'data')):
                continue
            if event['tag'].endswith('new'):
                # Throw away new job events for now, we want to use these
                # later....
                continue
            if any(key not in event['data'] for key in ('jid', 'id', 'return', 'fun')):
                continue
            disp_ret = salt.output.out_format(event['data']['return'], 'nested', self.opts)
            disp_jid = '{0}: {1}'.format(event['data']['fun'], event['data']['jid'])
            self.new_ret(
                    disp_jid,
                    event['data']['id'],
                    disp_ret)
            self.tree.refresh()
        loop.set_alarm_in(0.1, self.update)
