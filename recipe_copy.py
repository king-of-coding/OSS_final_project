#2024-06-14(금)
#오픈소스소프트웨어 기말 프로젝트
#Silver Chef

import tkinter as tk
import requests
from PIL import Image, ImageTk
from googletrans import Translator
import webbrowser

translator = Translator()

def translate_and_search():
    recipe_name_ko = entry_recipe_name.get()
    if recipe_name_ko:
        recipe_name_en = translator.translate(recipe_name_ko, scr='ko', dest='en').text
        get_top_5_recipes(recipe_name_en)

def get_top_5_recipes(recipe_name):
    api_url = "https://api.edamam.com/search"
    app_id = "3fb51f64"
    app_key = "95d50643632f0c49d6d2ab3d5a2068d2"

    params = {
        "q": recipe_name,
        "app_id": app_id,
        "app_key": app_key,
        "from": 0,
        "to": 5,
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    clear_recipe_list()

    if "hits" in data and data["hits"]:
        for i, hit in enumerate(data["hits"]):
            recipe = hit["recipe"]
            recipe_list.append(recipe)
            recipe_name = recipe["label"]
            recipe_link = recipe["url"]
            image_url = recipe["image"]

            image_response = requests.get(image_url, stream=True)
            image = Image.open(image_response.raw)
            image = image.resize((200, 200), Image.LANCZOS)
            photo_image = ImageTk.PhotoImage(image)

            recipe_title_label = tk.Label(
                canvas_frame,
                text=f"{i+1}. {recipe_name}",
                font=("Helvetica", 12, "bold"),
            )
            recipe_title_label.pack(pady=(5, 0), anchor=tk.CENTER)

            image_label = tk.Label(canvas_frame, image=photo_image)
            image_label.image = photo_image
            image_label.pack(pady=(0, 5), anchor=tk.CENTER)

            link_label = tk.Label(
                canvas_frame, text=recipe_link, fg="blue", cursor="hand2"
            )
            link_label.pack(pady=(0, 10), anchor=tk.CENTER)
            link_label.bind(
                "<Button-1>", lambda event, link=recipe_link: open_link(link)
            )

            recipe_labels.append(recipe_title_label)
            image_labels.append(image_label)
            recipe_links.append(link_label)

def clear_recipe_list():
    recipe_list.clear()
    for label in recipe_labels:
        label.pack_forget()
    recipe_labels.clear()
    for image_label in image_labels:
        image_label.pack_forget()
    image_labels.clear()
    for link_label in recipe_links:
        link_label.pack_forget()
    recipe_links.clear()

def open_link(link):
    webbrowser.open(link)

root = tk.Tk()
root.title("Recipe Finder")
root.geometry("800x700")
root.configure(bg="#dbd9da") # 테두리 색상

frame = tk.Frame(root, bg="#fae823") # 바탕색
frame.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=20)

label_recipe_name = tk.Label(
   frame, text="Enter Recipe Name (Korean):", font=("Arial", 18), bg="#fa1b5b"
)
label_recipe_name.pack()

entry_recipe_name = tk.Entry(frame, font=("Helvetica", 12))
entry_recipe_name.pack(pady=5)

translate_button = tk.Button(
   frame,
   text="Translate and Search Recipes",
   font=("Helvetica", 12, "bold"),
   command=translate_and_search,
)
translate_button.pack(pady=10)

canvas = tk.Canvas(frame, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

canvas_frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_frame, anchor=tk.NW)
canvas_frame.bind(
   "<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
)

recipe_list = []
recipe_labels = []
image_labels = []
recipe_links = []

root.mainloop()