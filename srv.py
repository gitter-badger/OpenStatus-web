'OpenStatus-web - The OpenStatus front-end HTML page generator for OpenStatus.'
'GNU General Public License version three or above - <http://gnu.org/licenses/gpl.txt>'

class AppInfo():
    version = "1.0.0.0"

app = AppInfo()

def about():
    'Display about information'
    print("OpenStatus-web (v" + app.version + ")\n")
    exit()

def render():
    'Render the HTML file for the frontend.'
    content = "<html>\n<head>\n<title<OpenStatus</title>\n</head>"

def init():
    count = 0
    for args in sys.argv:
        count = count + 1
        if count == 1:
            'Do nothing'
        elif count == 2:
            if args == "--help" or args == "-help": about()
