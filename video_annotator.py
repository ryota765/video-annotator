import os
import json
import tkinter

# Hyper parameters -------------------------------
source_dir = 'video'
output_dir = 'output'
class_list = ['feed', 'no_feed', 'unknown']
display_num = 1 # 4
# ------------------------------------------------

# def generate_tk(title="Video Annotator",geometry_str="400x300"):
#     root = tkinter.Tk()
#     root.title(title)
#     root.geometry(geometry_str)
#     return root


class MainWindow():

    def __init__(self, root, args):
        self.current_video_num = 0
        self.root= root
        self.source_dir = args["source_dir"]
        self.output_dir = args["output_dir"]
        self.class_list = args["class_list"]
        self.class_num = len(class_list)
        # self.image_width = args["width"]
        # self.image_height = args["height"]
        self.source_list = os.listdir(self.source_dir)
        self.source_num = len(self.source_list)
        # self.img = []
        self.init_window()
        # self.init_shortcuts()

    def init_window(self):
        # font_label_class = font.Font(size=20, weight='bold')
        # font_label_index = font.Font(size=15)

        self.root.title(u"Video Annotator")
        # 画像を表示するキャンバスを作る
        # self.canvas = tkinter.Canvas(self.root,width=100,height=100)
        # self.canvas.grid(row=0, column=0, columnspan=7, rowspan=1)
        # 次の画像を表示するボタン
        # self.button_next = tkinter.Button(
        #     self.root, text="Next (→)", command=self.onNextButton, height=3)
        # self.button_next.grid(row=2, column=5, pady=10, sticky='nsew')
        # self.button_back = tkinter.Button(
        #     self.root, text="Back (←)", command=self.onBackButton, height=3)
        # self.button_back.grid(row=2, column=1, pady=10, sticky='nsew')
        # クラスを決定するボタン
        # self.button_class = []
        # for i, c in enumerate(self.class_list):
        #     self.button_class.append(tkinter.Button(self.root, text="{}".format(c), command=self.labeling(class_num=i), width=10))
        #     self.button_class[i].grid(row=(i//self.class_num)+self.class_num//2, column=i%self.class_num, padx=5, pady=10, sticky='nsew')
        # ラベルの内容の初期化
        # self.message_image_index = tkinter.StringVar()
        # self.message_image_class = tkinter.StringVar()
        # self.set_message()
        # クラスを表示するラベル
        # self.label_image_class = tkinter.Label(self.root, textvariable=self.message_image_class, width=50, font=font_label_class, background='#CCDDDD')
        # self.label_image_class.grid(row=1, columnspan=7)
        # 現在の画像番号を表示するラベル
        # self.label_image_index = tkinter.Label(self.root, textvariable=self.message_image_index, font=font_label_index)
        # self.label_image_index.grid(row=2, column=3, pady=10, sticky='nsew')
        # 最初の画像をセット
        # self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        # self.set_image()

    # def init_shortcuts(self):
    #     self.main.focus_set()
    #     self.main.bind('<Key-Right>', self.onNextButton)
    #     self.main.bind('<Key-Left>', self.onBackButton)
    #     for i in list(range(len(self.button_class))):
    #         if i < 35:
    #             self.main.bind("<Key-{}>".format(self.kyboard_str[i]), self.labeling(i))

    # def set_message(self):
    #     self.message_image_index.set("{}/{}".format(str(self.current_video_num+1),str(self.source_num)))
    #     self.message_image_class.set("{}".format(self.get_class_name(self.source_list[self.current_video_num])))

    # def set_image(self,e=None):
    #     img = Image.open(os.path.join(self.images_dir,self.images_list[self.current_image_num]))
    #     img = img.resize((self.image_width,self.image_height), Image.LANCZOS)
    #     self.img = ImageTk.PhotoImage(img)
    #     self.canvas.itemconfig(self.image_on_canvas, image=self.img)

    # def set_video(self):


    # def get_class_name(self, img_path):
    #     data = self.load_json()
    #     if img_path in data:
    #         return self.classes[data[img_path]]
    #     else:
    #         return "No Label"

    # def onNextButton(self,e=None):
    #     # 一つ進む
    #     self.current_image_num += 1
    #     # 最初の画像に戻る
    #     if self.current_image_num == self.images_num:
    #         self.current_image_num = 0
    #     # 表示画像を更新
    #     self.set_image()
    #     self.set_message()

    # def onBackButton(self,e=None):
    #     # 一つ戻る
    #     self.current_image_num -= 1
    #     # 最後の画像へ
    #     if self.current_image_num == -1:
    #         self.current_image_num = self.images_num - 1
    #     # 表示画像を更新
    #     self.set_image()
    #     self.set_message()

    # def labeling(self, class_num):
    #     def x(e=None):
    #         img_path =self.images_list[self.current_image_num]
    #         self.update_json(img_path, class_num)
    #         self.set_message()
    #     return x

    # def load_json(self):
    #     data = {}
    #     try:
    #         data = json.load(open(self.json_path,'r'))
    #     except json.JSONDecodeError as e:
    #         pass
    #     except FileNotFoundError as e:
    #         with open(self.json_path, 'w'):
    #             pass
    #     return data

    # def update_json(self,img_path, class_num):
    #     data = self.load_json()
    #     data[img_path] = class_num
    #     json.dump(data, open(self.json_path,'w'),indent=4)

root = tkinter.Tk()
args = {"source_dir":source_dir, "output_dir":output_dir, "class_list":class_list}
MainWindow(root,args)
root.mainloop()