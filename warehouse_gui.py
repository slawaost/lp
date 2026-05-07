import tkinter as tk
from tkinter import messagebox
from warehouse import Warehouse


def handle_inbound():
    sku = sku_entry.get()
    location = location_entry.get()
    try:
        warehouse.store(sku, location)
        messagebox.showinfo("OK", "Artikel erfolgreich eingebucht!")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))
    update_overview()


def handle_search():
    sku = sku_entry2.get()
    try:
        location = warehouse.find(sku)
        if location == "0":
            messagebox.showwarning("Nicht gefunden", "Artikel wurde nicht gefunden.")
        else:
            messagebox.showinfo("Gefunden", f"Artikel {sku} ist in {location}.")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))


def handle_outbound():
    sku = sku_entry3.get()
    try:
        warehouse.retrieve(sku)
        messagebox.showinfo("OK", "Artikel erfolgreich ausgebucht!")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))
    update_overview()


def update_overview():
    warehouse_overview_text.delete("1.0", tk.END)
    warehouse_overview_text.insert(tk.END, warehouse.getOverview())


def open_warehouse(master, username):
    global warehouse
    global sku_entry, location_entry, sku_entry2, sku_entry3, warehouse_overview_text

    warehouse = Warehouse()

    window = tk.Toplevel(master)
    window.title("Lagerverwaltung")
    admin_label = tk.Label(window, text=f"Angemeldet als: {username}", fg="green", font=("Arial", 10, "bold"))
    admin_label.pack(pady=5)

    title_label = tk.Label(window, text="Lagerverwaltung", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # --- Inbound ---
    inbound_frame = tk.LabelFrame(window, text="Einbuchen")
    inbound_frame.pack(padx=10, pady=5, fill="both")

    sku_label = tk.Label(inbound_frame, text="SKU:")
    sku_label.grid(row=0, column=0)
    sku_entry = tk.Entry(inbound_frame)
    sku_entry.grid(row=0, column=1)

    location_label = tk.Label(inbound_frame, text="Lagerplatz:")
    location_label.grid(row=1, column=0)
    location_entry = tk.Entry(inbound_frame)
    location_entry.grid(row=1, column=1)

    tk.Button(inbound_frame, text="Einbuchen", command=handle_inbound).grid(row=2, columnspan=2)

    # --- Search ---
    search_frame = tk.LabelFrame(window, text="Suchen")
    search_frame.pack(padx=10, pady=5, fill="both")

    sku_label2 = tk.Label(search_frame, text="SKU:")
    sku_label2.grid(row=0, column=0)
    sku_entry2 = tk.Entry(search_frame)
    sku_entry2.grid(row=0, column=1)

    tk.Button(search_frame, text="Suchen", command=handle_search).grid(row=1, columnspan=2)

    # --- Outbound ---
    outbound_frame = tk.LabelFrame(window, text="Ausbuchen")
    outbound_frame.pack(padx=10, pady=5, fill="both")

    sku_label3 = tk.Label(outbound_frame, text="SKU:")
    sku_label3.grid(row=0, column=0)
    sku_entry3 = tk.Entry(outbound_frame)
    sku_entry3.grid(row=0, column=1)

    tk.Button(outbound_frame, text="Ausbuchen", command=handle_outbound).grid(row=1, columnspan=2)

    # --- Overview ---
    tk.Label(window, text="Übersicht", font=("Arial", 14, "bold")).pack()

    warehouse_overview_text = tk.Text(window, height=10)
    warehouse_overview_text.pack()

    tk.Button(window, text="Aktualisieren", command=update_overview).pack()

    update_overview()