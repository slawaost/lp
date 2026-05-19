import tkinter as tk
from service import BenutzerService
from tkinter import messagebox
from tkinter.simpledialog import askstring
from warehouse_gui import open_warehouse as WarehouseGUI
class GUI:
    def __init__(self, service: BenutzerService):
        self.service = service
        self.root = tk.Tk()
        self.root.title("Benutzerverwaltung")
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=80, pady=80)
        self.build_login()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def build_login(self):
        self.clear_frame()
        tk.Label(self.frame, text="Name").pack()
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()
        tk.Label(self.frame, text="Passwort").pack()
        self.pass_entry = tk.Entry(self.frame, show="*")
        self.pass_entry.pack()
        tk.Button(self.frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.frame, text="Register", command=self.register).pack(pady=5)

    def login(self):
        name = self.name_entry.get()
        pas = self.pass_entry.get()
        result = self.service.anmelden(name, pas)
        messagebox.showinfo("Info", result)
        if result == "Login erfolgreich":
            self.build_main()

    def open_warehouse(self):
        WarehouseGUI(self.root, self.service.aktueller.name)

    def register(self):
        name = self.name_entry.get()
        pas = self.pass_entry.get()
        result = self.service.registrieren(name, pas)
        messagebox.showinfo("Info", result)

    def build_main(self):
        self.clear_frame()
        tk.Label(self.frame, text="Hauptmenü", font=("Arial", 14, "bold")).pack(pady=10)
        # ganz wichtig, damit user nicht hauptmenü sehen kann
        if self.service.ist_admin():
            tk.Button(self.frame, text="Benutzer anzeigen", command=self.anzeigen).pack(pady=5)
            tk.Button(self.frame, text="Lagerverwaltung öffnen", command=self.open_warehouse).pack(pady=5)
            tk.Button(self.frame, text="User sofort löschen", command=self.loeschen).pack(pady=5)
            tk.Button(self.frame, text="User später löschen", command=self.loeschen_spaeter).pack(pady=5)
            tk.Button(self.frame, text="Geplante Löschungen anzeigen", command=self.geplante_loeschungen_anzeigen).pack(pady=5)
            tk.Button(self.frame, text="Benutzer bearbeiten", command=self.bearbeiten).pack(pady=5)
            tk.Button(self.frame, text="Benutzer aktivieren", command=self.aktiv).pack(pady=5)
            tk.Button(self.frame, text="Benutzer deaktivieren", command=self.deaktiv).pack(pady=5)
        tk.Button(self.frame, text="Logout", command=self.logout).pack(pady=5)

    def loeschen_spaeter(self):
        name = askstring("Löschen", "Name:")
        if name:
            result = self.service.löschen_in_woche(name)
            messagebox.showinfo("Info", result)

    def bearbeiten(self):
        name = askstring("Bearbeiten", "Name:")
        neuer_name = askstring("Bearbeiten", "Neuer Name (optional):")
        neues_pass = askstring("Bearbeiten", "Neues Passwort (optional):")
        if name:
            result = self.service.bearbeiten(name, neuer_name, neues_pass)
            messagebox.showinfo("Info", result)

    def deaktiv(self):
        name = askstring("Deaktivieren", "Name:")
        if name:
            result = self.service.deaktiv(name)
            messagebox.showinfo("Info", result)

    def aktiv(self):
        name = askstring("Aktivieren", "Name:")
        if name:
            result = self.service.deaktiv(name)
            messagebox.showinfo("Info", result) 
         
    def logout(self):
        self.service.logout()
        self.build_login()

    def anzeigen(self):
        users = self.service.anzeigen()
        text = "\n".join([f"{b.name} ({b.rolle})" for b in users])
        messagebox.showinfo("Benutzer", text)

    def loeschen(self):
        name = askstring("Löschen", "Name:")
        if name:
            result = self.service.löschen(name)
            messagebox.showinfo("Info", result)

    def geplante_loeschungen_anzeigen(self):
        users = self.service.geplante_loeschungen_anzeigen()
        text = "\n".join([f"{b.name} (Löscht am {b.expiry_date})" for b in users])
        if not text:
            text = "Keine geplanten Löschungen."
        messagebox.showinfo("Geplante Löschungen", text)

    def run(self):
        self.root.mainloop()