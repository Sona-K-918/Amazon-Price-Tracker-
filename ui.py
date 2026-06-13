import customtkinter as ctk
from PIL import Image
from tracker import get_product_info
import threading  

def track():
    result_box.delete("1.0", "end")
    result_box.insert("end", "\n\n Fetching Product Details... Please wait...")
    
    # The worker function that handles the heavy lifting
    def async_track_worker():
        url = url_entry.get()
        try:
            title, price, status = get_product_info(url)
            result_box.delete("1.0", "end")

            formatted_result = f"""
            📦  PRODUCT
            {title[:120]}...

            💰  PRICE
            ₹{price}

            📊  STATUS
            {status}"""
            
            result_box.insert("end", formatted_result)

        except Exception as e:
            result_box.delete("1.0", "end")
            result_box.insert("end", f"\n Error: Could not fetch data.\n Reason: {e}")

    # 3. Start the worker function inside a background thread
    threading.Thread(target=async_track_worker, daemon=True).start()

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("1200x700")
app.title("Amazon Price Tracker")
app.resizable(False, False) # Keeps background from distorting

# ---------------- BACKGROUND ---------------- #
bg_image = ctk.CTkImage(
    light_image=Image.open("assets/bg.png"),
    dark_image=Image.open("assets/bg.png"),
    size=(1200, 700)
)

bg_label = ctk.CTkLabel(
    app,
    text="",
    image=bg_image
)
bg_label.place(x=0, y=0)

# ---------------- LOGO & TITLE HEADER ---------------- #

title_label = ctk.CTkLabel(app, text="Amazon Price Tracker", font=("Georgia", 36, "bold"), fg_color="transparent")
title_label.place(relx=0.5, y=60, anchor="center")

# ---------------- URL BOX ---------------- #
url_entry = ctk.CTkEntry(
    app,
    width=800, # Widened slightly to match your mock's broad width
    height=45,
    placeholder_text="Enter your URL",
    font=("Helvetica", 14),
    corner_radius=10,
    fg_color="#a18cb5", # Semi-transparent tint to blend into the purple mockup style
    text_color="white",
    placeholder_text_color="#dedede",
    border_width=0
)
url_entry.place(relx=0.5, y=160, anchor="center")

# ---------------- BUTTON ---------------- #
def track():
    result_box.delete("1.0", "end")
    # Provide visual feedback while Selenium loads
    result_box.insert("end", "\n\n Fetching Product Details... Please wait...")
    app.update()

    url = url_entry.get()

    try:
        title, price, status = get_product_info(url)
        result_box.delete("1.0", "end")

        # Custom-tailored layout matching your clean mockup card style
        formatted_result = f"""
    📦  PRODUCT
    {title[:120]}...

    💰  PRICE
    ₹{price}

    📊  STATUS
    {status}
        """
        result_box.insert("end", formatted_result)

    except Exception as e:
        result_box.delete("1.0", "end")
        result_box.insert("end", f"\n Error: Could not fetch data.\n Reason: {e}")

track_btn = ctk.CTkButton(
    app,
    text="Track Price",
    command=track,
    font=("Helvetica", 14, "bold"),
    width=150,
    height=40,
    corner_radius=8,
    fg_color="#1f538d",
    hover_color="#14375e"
)
# Placed compactly under the entry bar
track_btn.place(relx=0.5, y=225, anchor="center")

# ---------------- RESULT BOX ---------------- #
result_box = ctk.CTkTextbox(
    app,
    width=960,
    height=360,
    corner_radius=15,
    font=("Helvetica", 16),
    fg_color="#9e8ca3", # Soft purple-grey tint to mimic the glass/translucent card look
    text_color="#1a1a1a", # Dark text color so it stands out cleanly on light tint
    border_width=0
)
result_box.place(relx=0.5, y=460, anchor="center")

app.mainloop()