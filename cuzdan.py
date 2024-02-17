from tkinter import *
from tkinter import messagebox
from colorama import Fore, Style, init

# colorama kütüphanesini başlat
init(autoreset=True)

users = {
    "user1": {"balance": 0},
    "user2": {"balance": 0}
}

current_user = None

def set_current_user(username):
    global current_user
    current_user = username
    update_balance_label()

def para_at(para):
    global current_user, users
    users[current_user]["balance"] += para
    messagebox.showinfo("Para Atma", f"Kumbaraya {para} TL attınız.")
    update_balance_label()

def para_al(para):
    global current_user, users
    if users[current_user]["balance"] == 0:
        messagebox.showwarning("Yetersiz Bakiye", "Cüzdanda para olmadığı için para çekme işlemi gerçekleştirilemez.")
    elif para > users[current_user]["balance"]:
        messagebox.showwarning("Yetersiz Bakiye", "Yetersiz bakiye! Cüzdanınızdaki toplam miktarı aşan bir tutar çekemezsiniz.")
    else:
        users[current_user]["balance"] -= para
        messagebox.showinfo("Para Alma", f"Cüzdandan {para} TL para alınmıştır. Cüzdanın güncel değeri: {users[current_user]['balance']} TL")
        update_balance_label()

def bakiye_transferi(kullanici, miktar):
    global current_user, users
    if miktar <= 0:
        messagebox.showwarning("Hatalı İşlem", "Geçersiz miktar! Lütfen pozitif bir miktar girin.")
    elif miktar > users[current_user]["balance"]:
        messagebox.showwarning("Yetersiz Bakiye", "Yetersiz bakiye! Cüzdanınızdaki toplam miktarı aşan bir tutar transfer edemezsiniz.")
    elif kullanici not in users:
        messagebox.showwarning("Kullanıcı Bulunamadı", "Belirtilen kullanıcı adıyla ilişkilendirilmiş bir cüzdan bulunamadı.")
    else:
        users[current_user]["balance"] -= miktar
        users[kullanici]["balance"] += miktar
        messagebox.showinfo("Bakiye Transferi", f"{kullanici} adlı kullanıcıya {miktar} TL bakiye transfer edildi.")
        update_balance_label()

def update_balance_label():
    global current_user, users
    balance_label.config(text=f"{current_user.capitalize()} - Toplam Bakiye: {users[current_user]['balance']} TL")

def on_login_click():
    global current_user
    username = entry_login.get()
    if username in users:
        set_current_user(username)
        login_frame.grid_remove()
        main_frame.grid()
    else:
        messagebox.showwarning("Geçersiz Kullanıcı", "Belirtilen kullanıcı adı bulunamadı.")

def on_para_at_click():
    para = int(entry.get())
    para_at(para)

def on_para_al_click():
    para = int(entry.get())
    para_al(para)

def on_transfer_click():
    kullanici = entry_user.get()
    miktar = int(entry_transfer.get())
    bakiye_transferi(kullanici, miktar)

def on_logout_click():
    global current_user
    current_user = None
    main_frame.grid_remove()
    login_frame.grid()

def on_exit_click():
    result_label.config(text="Akıllı cüzdanı tercih ettiğiniz için teşekkürler. İyi günler :)")
    root.destroy()

# Tkinter window setup
root = Tk()
root.title("Smart Wallet")

# Styling
root.geometry("500x250")
root.configure(bg="#F2F2F2")

# Login UI elements
login_frame = Frame(root, bg="#F2F2F2")
login_frame.grid(row=0, column=0, columnspan=3, pady=10)

login_label = Label(login_frame, text="Kullanıcı Adı:", bg="#F2F2F2", font=("Helvetica", 12))
login_label.grid(row=0, column=0, padx=10, pady=10)

entry_login = Entry(login_frame, font=("Helvetica", 12))
entry_login.grid(row=0, column=1, padx=10, pady=10)

login_button = Button(login_frame, text="Giriş Yap", command=on_login_click, bg="#4285F4", fg="white", font=("Helvetica", 10, "bold"))
login_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Main UI elements
main_frame = Frame(root, bg="#F2F2F2")
main_frame.grid(row=0, column=0, columnspan=3, pady=10)
main_frame.grid_remove()

entry_label = Label(main_frame, text="Miktar:", bg="#F2F2F2", font=("Helvetica", 12))
entry_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)

entry = Entry(main_frame, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=10, pady=10)

para_at_button = Button(main_frame, text="Para At", command=on_para_at_click, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
para_at_button.grid(row=1, column=0, padx=10, pady=10)

para_al_button = Button(main_frame, text="Para Al", command=on_para_al_click, bg="#FF5733", fg="white", font=("Helvetica", 10, "bold"))
para_al_button.grid(row=1, column=1, padx=10, pady=10)

balance_label = Label(main_frame, text="Toplam Bakiye: 0 TL", font=("Helvetica", 12, "bold"), fg="green", bg="#F2F2F2")
balance_label.grid(row=0, column=2, sticky=E, padx=10, pady=10)

logout_button = Button(main_frame, text="Çıkış", command=on_logout_click, bg="#808080", fg="white", font=("Helvetica", 10, "bold"))
logout_button.grid(row=1, column=2, padx=10, pady=10)

# Transfer UI elements
entry_user_label = Label(main_frame, text="Alıcı Kullanıcı Adı:", bg="#F2F2F2", font=("Helvetica", 12))
entry_user_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)

entry_user = Entry(main_frame, font=("Helvetica", 12))
entry_user.grid(row=2, column=1, padx=10, pady=10)

entry_transfer_label = Label(main_frame, text="Transfer Miktarı:", bg="#F2F2F2", font=("Helvetica", 12))
entry_transfer_label.grid(row=3, column=0, sticky=W, padx=10, pady=10)

entry_transfer = Entry(main_frame, font=("Helvetica", 12))
entry_transfer.grid(row=3, column=1, padx=10, pady=10)

transfer_button = Button(main_frame, text="Bakiye Transferi", command=on_transfer_click, bg="#4285F4", fg="white", font=("Helvetica", 10, "bold"))
transfer_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = Label(main_frame, text="", font=("Helvetica", 12, "italic"), fg="#333333", bg="#F2F2F2")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
