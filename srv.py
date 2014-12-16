'OpenStatus-web - The OpenStatus front-end HTML page generator for OpenStatus.'
'GNU General Public License version three or above - <http://gnu.org/licenses/gpl.txt>'

import OpenStatus as 0ostatus

class AppInfo():
    version = "1.0.0.0"

app = AppInfo()

def about():
    'Display about information'
    print("OpenStatus-web (v" + app.version + ")\n")
    print("Below is a list of available commands:\n\n")
    exit()

def render():
    'Render the HTML file for the frontend.'
    


def start_server():
    render()
    start_server()

def init():
    count = 0
    for args in sys.argv:
        count = count + 1
        if count == 1:
            'Do nothing'
        elif count == 2:
            if args == "--help" or args == "-help": about()
            elif args == "--start" or args == "-start": start_server()
            else: print("'" + args + "' is not a valid command. Use `--help` for a list of available commands.")
