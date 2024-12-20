import tkinter, ttkthemes, tkinter.filedialog

import globalvars, importdatabase, BrMdata

class Injection(ttkthemes.ThemedTk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Inject')
        self.geometry('500x400')
        self.set_theme('radiance')
        # define a frame
        self.main_frame = tkinter.ttk.Frame(self)
        self.main_frame.pack()
        ## label for username
        self.username_label = tkinter.ttk.Label(self.main_frame, text = 'Username')
        self.username_label.grid(row = 1, column = 1)
        ## entry for username
        self.username_entry = tkinter.ttk.Entry(self.main_frame, width = 30, state = tkinter.NORMAL)
        self.username_entry.grid(row = 2, column = 1)
        ## label for password
        self.password_label = tkinter.ttk.Label(self.main_frame, text = 'Password')
        self.password_label.grid(row = 3, column = 1)
        ## entry for password
        self.password_entry = tkinter.ttk.Entry(self.main_frame, width = 30, state = tkinter.NORMAL, show = '*')
        self.password_entry.grid(row = 4, column = 1)
        ## label for importing data
        self.import_label = tkinter.ttk.Label(self.main_frame, text = 'Select Folder that Contains the Field Notes')
        self.import_label.grid(row = 5, column = 1)
        ## entry for importing data
        self.import_entry = tkinter.ttk.Entry(self.main_frame, width = 40, state = tkinter.NORMAL)
        self.import_entry.grid(row = 6, column = 1)
        ## button for importing data
        self.import_button = tkinter.ttk.Button(self.main_frame, text = '...', state = tkinter.NORMAL, command = self.import_ids, width = 2)
        self.import_button.grid(row = 6, column = 2)
        ## button for starting the process
        self.start_button = tkinter.ttk.Button(self.main_frame, text = 'Start', command = self.update_BrM, state = tkinter.NORMAL, width = 4)
        self.start_button.grid(row = 7, column = 1) 


    # define function that imports the Excel file
    def import_ids(self):
        # variable that handles the Excel path
        path = tkinter.filedialog.askdirectory()
        # fill entry bar with the path
        self.import_entry.insert(tkinter.END, path)
        # import bridge IDs
        importdatabase.bridgeID(path)
        # update user_var
        count = 0
        i = 0
        j = 0
        for k in range(len(path)):
            if path[k] == "/":
                count += 1
            elif count == 2 and i == 0:
                i = k
            elif count == 3:
                j = k - 1
                break
        # update the globalvars
        globalvars.user_path = path[i:j]
        globalvars.main_path = path

    # define function that imports the Excel file
    def get_fielnotes_path(self):
        # variable that handles the Excel path
        folder_path = tkinter.filedialog.askdirectory()
        # fill entry bar with the path
        self.fieldnotes_entry.insert(tkinter.END, folder_path)
        # update the globalvars
        globalvars.main_path = folder_path


    # use the field notes to update BrM data
    def update_BrM(self):
        # update username and password
        globalvars.username = self.username_entry.get()
        globalvars.password = self.password_entry.get()
        # get the date inputed by user
        #globalvars.inspection_date = self.date_entry.get()
        # update BrM with new data
        BrMdata.post_data()


if __name__ == "__main__":
    app = Injection()
    app.mainloop()