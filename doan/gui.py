import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
# load the trained model to classify sign
from keras.models import load_model

model = load_model('traffic_classifier.h5')

# dictionary to label all traffic signs class.
classes = {1: 'Tốc độ tối đa (20km/h)',
           2: 'Tốc độ tối đa (30km/h)',
           3: 'Tốc độ tối đa (50km/h)',
           4: 'Tốc độ tối đa (60km/h)',
           5: 'Tốc độ tối đa (70km/h)',
           6: 'Tốc độ tối đa (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Tốc độ tối đa (100km/h)',
           9: 'Tốc độ tối đa (120km/h)',
           10: 'Không được vượt',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Đường ưu tiên',
           14: 'Nhường đường',
           15: 'Dừng lại',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'Không vào   ',
           19: 'Cẩn thận',
           20: 'Chỗ ngoặt nguy hiểm vòng bên trái',
           21: 'Chỗ ngoặt nguy hiểm vòng bên phải',
           22: 'Double curve',
           23: 'Đường gập ghềnh',
           24: 'Đường trơn trượt',
           25: 'Road narrows on the right',
           26: 'Đường đang thi công',
           27: 'Biển báo giao thông',
           28: 'Pedestrians',
           29: 'Trẻ em qua đường',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Rẽ phải phía trước',
           35: 'Rẽ trái phía trước',
           36: 'Đi thẳng',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

# initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = numpy.argmax(model.predict(image), axis=-1)[0]
    sign = classes[pred + 1]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
