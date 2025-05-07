import tkinter as tk
from tkinter import PhotoImage

#Creates my main application
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Genshin Character Optimizer")
        self.geometry("800x700") 
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        main_frame = MainWindow(self.container, self)
        self.frames["MainWindow"] = main_frame
        main_frame.grid(row=0, column=0, sticky="nsew")

        hutao_frame = InfoScreen1(self.container, self)
        self.frames["InfoScreen1"] = hutao_frame
        hutao_frame.grid(row=0, column=0, sticky="nsew")

        kazuha_frame = InfoScreen2(self.container, self)
        self.frames["InfoScreen2"] = kazuha_frame
        kazuha_frame.grid(row=0, column=0, sticky="nsew")
        
        ganyu_frame = InfoScreen3(self.container, self)
        self.frames["InfoScreen3"] = ganyu_frame
        ganyu_frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("MainWindow")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        
#Creates my main window 
class MainWindow(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.master = master
        self.controller = controller 
        self.configure(bg="#f8d4fd")
        self.pack(fill="both", expand=True)
        
        #Title of main program
        label = tk.Label(self, text="Genshin Character Optimizer", font=("Comfortaa", 26), bg="#f8d4fd")
        label.pack(pady=(20, 10))

        #Pulls character images
        self.hutao_img = PhotoImage(file="C:/Users/baker/OneDrive/Desktop/Genshin Optimizer/HuTao.gif")
        self.kazuha_img = PhotoImage(file="C:/Users/baker/OneDrive/Desktop/Genshin Optimizer/Kazuha.gif")
        self.ganyu_img = PhotoImage(file="C:/Users/baker/OneDrive/Desktop/Genshin Optimizer/Ganyu.gif")

        #Creates frame for buttons, see buttons below
        button_frame = tk.Frame(self, bg="#f8d4fd")
        button_frame.pack(pady=10)

        hutao_button = tk.Button(button_frame, image=self.hutao_img, width=213, height=133, 
                              command=self.show_hutao_info)
        hutao_button.grid(row=0, column=0, padx=20, pady=20)

        kazuha_button = tk.Button(button_frame, image=self.kazuha_img, width=213, height=133,
                               command=self.show_kazuha_info)
        kazuha_button.grid(row=0, column=1, padx=20, pady=20)

        ganyu_button = tk.Button(button_frame, image=self.ganyu_img, width=213, height=133,
                              command=self.show_ganyu_info)
        ganyu_button.grid(row=0, column=2, padx=20, pady=20)
            
        #Close program button
        close_button = tk.Button(self, text="Close", bg="lightgrey", fg="black", width=15, font=("Comfortaa", 12), command=self.close_window)
        close_button.pack(pady=20)

    def show_hutao_info(self):
        self.controller.show_frame("InfoScreen1")

    def show_kazuha_info(self):
        self.controller.show_frame("InfoScreen2")
        
    def show_ganyu_info(self):
        self.controller.show_frame("InfoScreen3")
        
    def close_window(self):
        self.controller.destroy()
        
#Class for my second window that opens when buttons are clicked
class InfoScreenMain(tk.Frame):
    def __init__(self, master, controller, character_name, image_path):
        super().__init__(master)
        self.master = master
        self.controller = controller  
        self.character_name = character_name
        self.configure(bg="#BFEFDF")
        
        content_frame = tk.Frame(self, bg="#BFEFDF")
        content_frame.pack(fill="both", expand=True)
        
        #Title of each info window
        label = tk.Label(content_frame, text=f"{self.character_name} Infographic", 
                      font=("Comfortaa", 24), bg="#BFEFDF")
        label.pack(pady=(20, 10))
        
        #Loads image for info screens
        self.char_image = PhotoImage(file=image_path)
        image_label = tk.Label(content_frame, image=self.char_image, bg="#BFEFDF")
        image_label.pack(pady=5)
        
        #Button to return to MainWindow
        back_button = tk.Button(content_frame, text="Back", font=("Comfortaa", 12),
                             bg="lightgrey", width=15, command=self.back_to_main)
        back_button.pack(pady=15)
        
    def back_to_main(self):
        self.controller.show_frame("MainWindow")

#Creates each of my infoscreens            
class InfoScreen1(InfoScreenMain):
    def __init__(self, master, controller):
        super().__init__(
            master=master, 
            controller=controller,
            character_name="Hu Tao", 
            image_path="C:/Users/baker/OneDrive/Desktop/Genshin Optimizer/HGraphic.gif")
        
class InfoScreen2(InfoScreenMain):
    def __init__(self, master, controller):
        super().__init__(
            master=master, 
            controller=controller,
            character_name="Kazuha", 
            image_path="C:/Users/baker/OneDrive/Desktop/Genshin Optimizer/KGraphic.gif")
        
class InfoScreen3(InfoScreenMain):
    def __init__(self, master, controller):
        super().__init__(
            master=master, 
            controller=controller,
            character_name="Ganyu", 
            image_path="C:/Users/baker/OneDrive/Desktop/Genshin Optimizer/GGraphic.gif")

#Runs program
if __name__ == "__main__":
    app = Application()
    app.mainloop()