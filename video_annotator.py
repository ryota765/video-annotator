import os
import glob
import json

import tkinter
# from tkinter import font

import cv2
from PIL import Image, ImageTk

# Hyper parameters -------------------------------
source_dir = 'video'
output_dir = 'output'
class_list = ['feed', 'no_feed', 'unknown']
display_num = 1 # 4
frame_display_interval = 10 # ms
video_display_width = 700
video_display_height = 500
json_path = 'output/output.json'
# ------------------------------------------------

class MainWindow():

    def __init__(self, root):
        self.current_video_num = 0
        self.root = root
        self.source_dir = source_dir
        self.output_dir = output_dir
        self.class_list = class_list
        self.class_num = len(class_list)
        self.button_class = []
        self.video_width = video_display_width
        self.video_height = video_display_height
        self.source_list = glob.glob(os.path.join(self.source_dir, '*'))
        self.source_num = len(self.source_list)
        self.json_path = json_path
        self.interval = frame_display_interval # ms
        self.loop_job_id = None
        self.init_window()
        self.set_video()

    # Set components without video
    def init_window(self):

        self.root.title(u"Video Annotator")

        # display video
        self.canvas = tkinter.Canvas(self.root,width=self.video_width,height=self.video_height)
        self.canvas.grid(row=0, column=0,columnspan=6, rowspan=1)

        # Buttons to change video
        self.button_next = tkinter.Button(
            self.root, text="Next (→)", command=self.on_next_button, height=3)
        self.button_next.grid(row=2, column=self.class_num+1, pady=10, sticky='nsew')
        self.button_back = tkinter.Button(
            self.root, text="Back (←)", command=self.on_back_button, height=3)
        self.button_back.grid(row=2, column=0, pady=10, sticky='nsew')

        # Buttons for class labeling
        self.button_class = []
        for i, c in enumerate(self.class_list):
            self.button_class.append(tkinter.Button(self.root, text="{}".format(c), command=lambda:[self.labeling(class_num=i), self.on_next_button()], width=10, height=3))
            self.button_class[i].grid(row=3, column=i%self.class_num+1, padx=5, pady=10, sticky='nsew')


    def set_video(self):
        if self.loop_job_id:
            self.root.after_cancel(self.loop_job_id)
        self.cap = cv2.VideoCapture(self.source_list[self.current_video_num])
        self.update_image()

        # Set label
        self.selected_video_class = tkinter.StringVar()
        self.set_label()
        self.label_image_class = tkinter.Label(self.root, textvariable=self.selected_video_class, width=self.class_num*10, background='#CCDDDD')
        self.label_image_class.grid(row=1, columnspan=7)

    def update_image(self):
        ret, image = self.cap.read()
        if ret:
            self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # to RGB
            self.image = Image.fromarray(self.image).resize((self.video_width, self.video_height)) # to PIL format
            self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
            # Update image
            self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.image)
            # Repeat every 'interval' ms
            self.loop_job_id = self.root.after(self.interval, self.update_image)
        else:
            self.set_video()

    def set_label(self):
        self.selected_video_class.set("{}".format(self.get_class_name(self.source_list[self.current_video_num])))

    def get_class_name(self, video_path):
        data = self.load_json()
        if video_path in data:
            return self.class_list[data[video_path]]
        else:
            return "No Label"

    def on_next_button(self,e=None):
        self.current_video_num += 1
        # If last video, return to first video
        if self.current_video_num == self.source_num:
            self.current_video_num = 0
        self.set_video()

    def on_back_button(self,e=None):
        self.current_video_num -= 1
        # If first video, return to last video
        if self.current_video_num == -1:
            self.current_video_num = self.source_num - 1
        self.set_video()

    def labeling(self, class_num):
        def x(e=None):
            video_path =self.source_list[self.current_video_num]
            self.update_json(video_path, class_num)
        return x

    def load_json(self):
        data = {}
        try:
            data = json.load(open(self.json_path,'r'))
        except json.JSONDecodeError as e:
            pass
        except FileNotFoundError as e:
            with open(self.json_path, 'w'):
                pass
        return data

    def update_json(self,video_path, class_num):
        data = self.load_json()
        data[video_path] = class_num
        json.dump(data, open(self.json_path,'w'),indent=4)

root = tkinter.Tk()
MainWindow(root)
root.mainloop()

# References
# https://github.com/takanosuke/classifier_annotation_tool
