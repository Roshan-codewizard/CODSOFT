import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = {}

        self.setup_ui()

    def setup_ui(self):
        # Define colors
        button_bg = "#4CAF50"
        button_fg = "white"
        listbox_bg = "#E8F5E9"
        listbox_fg = "black"
        listbox_select_bg = "#81C784"
        listbox_select_fg = "black"
        main_bg = "#FFFFFF"

        # Set background color for the window
        self.root.configure(bg=main_bg)

        # Add contact button
        self.add_contact_button = tk.Button(self.root, text="Add Contact", bg=button_bg, fg=button_fg, command=self.add_contact)
        self.add_contact_button.grid(row=0, column=0, pady=10, padx=10)

        # View contact list button
        self.view_contacts_button = tk.Button(self.root, text="View Contact List", bg=button_bg, fg=button_fg, command=self.view_contacts)
        self.view_contacts_button.grid(row=0, column=1, pady=10, padx=10)

        # Search contact button
        self.search_contact_button = tk.Button(self.root, text="Search Contact", bg=button_bg, fg=button_fg, command=self.search_contact)
        self.search_contact_button.grid(row=0, column=2, pady=10, padx=10)

        # Update contact button
        self.update_contact_button = tk.Button(self.root, text="Update Contact", bg=button_bg, fg=button_fg, command=self.update_contact)
        self.update_contact_button.grid(row=0, column=3, pady=10, padx=10)

        # Delete contact button
        self.delete_contact_button = tk.Button(self.root, text="Delete Contact", bg=button_bg, fg=button_fg, command=self.delete_contact)
        self.delete_contact_button.grid(row=0, column=4, pady=10, padx=10)

        # Listbox for displaying contacts
        self.contact_listbox = tk.Listbox(self.root, height=15, width=80, bg=listbox_bg, fg=listbox_fg,
                                          selectbackground=listbox_select_bg, selectforeground=listbox_select_fg)
        self.contact_listbox.grid(row=1, column=0, columnspan=5, pady=10, padx=10)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=1, column=5, sticky="ns")
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_listbox.yview)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        if name and phone:
            self.contacts[phone] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for phone, details in self.contacts.items():
            contact_info = f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}"
            self.contact_listbox.insert(tk.END, contact_info)

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number to search:")
        self.contact_listbox.delete(0, tk.END)
        found = False
        for phone, details in self.contacts.items():
            if query.lower() in details['name'].lower() or query in phone:
                contact_info = f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Address: {details['address']}"
                self.contact_listbox.insert(tk.END, contact_info)
                found = True
        if not found:
            messagebox.showinfo("No Results", "No contacts found.")

    def update_contact(self):
        query = simpledialog.askstring("Update", "Enter phone number of contact to update:")
        if query in self.contacts:
            name = simpledialog.askstring("Input", "Enter new contact name:", initialvalue=self.contacts[query]['name'])
            email = simpledialog.askstring("Input", "Enter new email:", initialvalue=self.contacts[query]['email'])
            address = simpledialog.askstring("Input", "Enter new address:", initialvalue=self.contacts[query]['address'])

            self.contacts[query] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Not Found", "No contact found with that phone number.")

    def delete_contact(self):
        query = simpledialog.askstring("Delete", "Enter phone number of contact to delete:")
        if query in self.contacts:
            del self.contacts[query]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.view_contacts()
        else:
            messagebox.showwarning("Not Found", "No contact found with that phone number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
