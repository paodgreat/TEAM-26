import requests
import tkinter as tk
from tkinter import ttk


def fetch_ip_info(url):
    """Fetch IP information from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}


def update_ui(url, label):
    """Update the UI with fetched IP information."""
    data = fetch_ip_info(url)
    
    if 'error' in data:
        label.config(text=f"Error: {data['error']}")
    else:
        label.config(text=(
            f"IP Address: {data.get('ip', 'N/A')}\n"
            f"City: {data.get('city', 'N/A')}\n"
            f"Region: {data.get('region', 'N/A')}\n"
            f"Country: {data.get('country_name', 'N/A')}\n"
            f"ISP: {data.get('org', 'N/A')}"
        ))


def show_info_page():
    """Display the IP information page."""
    clear_frame()
    
    title_label = ttk.Label(frame, text="Team's 26 PC Information", font=('Impact', 18, 'bold'))
    title_label.grid(row=0, column=0, pady=(20, 10), sticky="nsew")

    global ip_info_label
    ip_info_label = ttk.Label(frame, text="Loading...", justify="center", font=('Impact', 14))
    ip_info_label.grid(row=1, column=0, sticky="nsew")

    update_ui('https://ipapi.co/json/', ip_info_label)

    back_button.grid(row=5, column=0, pady=(10, 20), sticky="nsew")


def show_start_page():
    """Display the start page."""
    clear_frame()
    
    header_label = ttk.Label(frame, text="Team 26's App", font=('Impact', 24, 'bold'))
    header_label.grid(row=0, column=0, pady=(40, 20), sticky="nsew")

    subheader_label = ttk.Label(frame, text="IPv4/IPv6 App", font=('Impact', 18))
    subheader_label.grid(row=1, column=0, pady=(10, 20), sticky="nsew")

    start_button = ttk.Button(frame, text="Start", command=show_info_page)
    start_button.grid(row=2, column=0, pady=(10, 20), sticky="nsew")
    start_button.config(width=15)

    back_button.grid_remove()


def clear_frame():
    """Clear all widgets in the frame except the back button."""
    for widget in frame.winfo_children():
        if widget != back_button:
            widget.destroy()


# Main application setup
root = tk.Tk()
root.title("IP Address Info")
root.geometry("800x600")
root.resizable(True, True)
root.configure(bg="#f4f4f4")

frame = ttk.Frame(root, padding="20", relief="raised", borderwidth=2)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.configure(style='TFrame')

# Configure grid weights for responsive layout
frame.grid_rowconfigure((0, 1, 2), weight=1)
frame.grid_columnconfigure(0, weight=1)

# Style configuration
style = ttk.Style()
style.configure('TButton', font=('Impact', 12), padding=10)

# Back button to navigate to the start page
back_button = ttk.Button(frame, text="Back", command=show_start_page)

# Start with the start page
show_start_page()
root.mainloop()