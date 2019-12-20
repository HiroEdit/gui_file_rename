import PySimpleGUI as g
import os
import random
import string


def setup():
    g.change_look_and_feel("Reddit")

    gui = [[g.Text("Select main folder directory.")],
           [g.Text("Example: main_folder / sub_folder(s) / *files that will get renamed*")],
           [g.Text()],
           [g.Text("Destination Folder")],
           [g.InputText(), g.FolderBrowse()],
           [g.Button("Submit"), g.Button("Cancel")]
           ]

    window = g.Window("Setup", gui)

    while True:
        event, values = window.read()
        path = values[0]  # will throw none type error if user enters path that does not exists and exits

        if event in (None, "Cancel"):
            break

        if event == "Submit" and os.path.exists(path):
            os.chdir(path)
            files = os.listdir(path)

            for items in files:
                # if ".DS_Store" in items:
                #     continue
                print(items)
                if os.path.isdir(items):
                    os.chdir(path + "/" + items)

                    for i in os.listdir():
                        print(i)
                        name = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(5)])
                        new = name + i[-7:]
                        os.rename(i, new)
                os.chdir(path)

            g.popup_ok("Files renamed! You can rename again by clicking submit.",title="Success", keep_on_top=True)

        else:
            g.popup_ok("The path you entered is empty or does not exist", title="Path Error", keep_on_top=True)

    window.close()


setup()
