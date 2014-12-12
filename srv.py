'OpenStatus-web - The OpenStatus front-end HTML page generator for OpenStatus.'
'GNU General Public License version three or above - <http://gnu.org/licenses/gpl.txt>'

def about():
    'Display about information'
    
def render():
    'Render the HTML file for the frontend.'

def init():
    count = 0
    for args in sys.argv:
        count = count + 1
        if count == 1:
            'Do nothing'
        elif count == 2:
            if args == "--help" or args == "-help": about()
