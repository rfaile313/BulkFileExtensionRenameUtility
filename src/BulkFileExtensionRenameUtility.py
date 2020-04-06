__author__ = 'Rudy Faile (@rfaile313)'
__license__ = 'MIT'
__version__ = '1.0.0'
__email__ = 'rudyfaile.com/contact'

from subprocess import call
import PySimpleGUI as sg
import os,sys

TRY_AGAIN = 'Try Again'
EXIT = 'Exit'

def main():
       try:
              sg.theme('TealMono') 

              layout = [[sg.Text('Choose a folder or directory:')], 
                     [sg.InputText(default_text=os.getcwd(), size=(40,1)), sg.FolderBrowse()],
                     [sg.Text('File extensions to change:')],
                     [sg.InputText(focus=True, size=(10,1))],
                     [sg.Text('Change all file extensions in this folder to:')],
                     [sg.InputText(size=(10,1))],
                     [sg.Text('')],
                     [sg.Button('Change all file extensions', key='search'), sg.Cancel()]]

              
              window = sg.Window('Bulk file extension change tool', layout, icon='../Assets/icon.png')

              event, values = window.read()
              
              window.close()

              if event == 'Cancel' or event == None:
                     sys.exit()

              if not values[1] or not values[2]:
                     sg.Popup('Please enter an extension in both boxes', custom_text=TRY_AGAIN)
                     main()

              if '.' not in values[1] or '.' not in values[2]:
                     sg.Popup('You need a "." to have an extension...', custom_text=TRY_AGAIN)
                     main()


              if event == 'search' and values[1] and values[2]:
                     for filename in os.listdir(values[0]):
                            infilename = os.path.join(values[0],filename)
                            if not os.path.isfile(infilename): continue
                            oldbase = os.path.splitext(filename)
                            newname = infilename.replace(values[1], values[2])
                            output = os.rename(infilename, newname)
                     sg.Popup('Done! Changed all {} to {}'.format(values[1], values[2]))

                     #Open target directory in Mac
                     if sys.platform == "darwin":
                            targetDirectory = values[0]
                            call(["open", targetDirectory])
                     #Windows
                     elif sys.platform == "win32":
                            os.startfile(values[0])
                     #TODO add or catch linux
                     else:
                            pass
       except:
              sys.exit()

main()
sys.exit()
