import tkinter as tk
import tkinter.ttk as ttk
import subprocess
from openai import openai
from plugin import *
################################################################################################################################
jmeter_executable = "G:\\JMeter\\apache-jmeter-5.5\\bin\\jmeter.bat"  # Update this with your JMeter executable path
jmx_file = "G:\\ChatGPT\\JMeter\\Script\\Demo.jmx"                    # Update this with your JMX file path
log_file = "G:\\ChatGPT\\JMeter\\Script\\Demo.csv"                    # Update this with the desired log file path
csv_output = "G:\\ChatGPT\\JMeter\\Script\\metrics.xml"               # Update this with the desired CSV output path
xml_file_path = "G:\\ChatGPT\\JMeter\\Script\\metrics.xml"
existing_html = "G:\\ChatGPT\\JMeter\\Report\\existing.html"
input_data = 'G:\\ChatGPT\\JMeter\\Script\\input.csv'                 # Define the output folder path of data created
################################################################################################################################

def chatbot_response(input):
    #user_input = input.split(",")
    if "hello" in input.lower():
        return "How can I help you?"
    elif "create script" in input.lower():
        script(jmx_file)
        return "JMeter script created sucessfully."
    elif "analyze script" in input.lower():
        response = analyze_script(jmx_file)
        return response
    elif "start jmeter" in input.lower():
        process = subprocess.Popen(['start', '', jmeter_executable], shell=True)
        return "Script edit completed Yes (or) No"
    elif "create test data" in input.lower():
        data_create(input_data)
        return "Test data created sucessfully"
    elif "start test" in input.lower():
        execute_jmeter_script(jmeter_executable, jmx_file, log_file)
        xml = extract_metrics_from_csv(log_file, csv_output)        
        html_table = convert_xml_to_html(xml_file_path)
        generate_index_html(html_table,xml,existing_html)
        return xml
    elif "analyze code" in input.lower():
        response = security()
        return response
    else:
        response = openai(input)
        return response

def send_message():
    user_input = entry.get()
    if user_input.lower() == "exit":
        chatbox.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n")
        window.after(1000, window.destroy)
    else:
        chatbox.insert(tk.END, f"You: {user_input}\n")
        chatbox.insert(tk.END, "Chatbot: Chatbot is typing...")
        window.update_idletasks()
        window.after(1000)  # Add a 1-second delay for animation effect
        response = chatbot_response(user_input)
        chatbox.delete('end-1c linestart', tk.END)
        chatbox.insert(tk.END, f"\nChatbot: {response}\n", "blue")

def main():
    global window, entry, chatbox

    window = tk.Tk()
    window.title("Chatbot Application")
    window.configure(background="#eff7e6")

    # Set the initial size of the window
    window.geometry("800x700")

    chatbox = tk.Text(window, height=28, width=140)
    chatbox.pack(padx=10, pady=10)
    chatbox.insert(tk.END, "Chatbot: Hello! I am your friendly Performance Tester chatbot.\n")
    chatbox.insert(tk.END, "Chatbot: You can start a conversation by saying 'hello'.\n")
    chatbox.insert(tk.END, "Chatbot: Enter 'exit' to end the conversation.\n")
    chatbox.config(font=("Cascadia Code", 12), fg="#000000", bg="#ffffff")
    chatbox.config(borderwidth=0, relief="solid")
    chatbox.config(highlightthickness=2, highlightbackground="#787beb")

    chatbox.pack_propagate(False)

    chatbox_style = ttk.Style()
    chatbox_style.configure("chatbox.TEntry", relief="flat", borderwidth=5, 
                            background="#ffffff", 
                            foreground="#000000", 
                            highlightthickness=0, 
                            highlightbackground="#080807")

    chatbox.style = "chatbox.TEntry"

    entry = tk.Entry(window, width=50)
    entry.pack(padx=10, pady=5)
    entry.config(font=("Segoe UI", 12), fg="#000000", bg="#ffffff")
    entry.config(borderwidth=1, relief="sunken", highlightthickness=1, highlightbackground="#000000")
    entry.config(justify="left")
    entry.place(x=450, y=610)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(pady=5)
    send_button.config(font=("Arial Black", 12), fg="#000000", bg="#a3b051")
    send_button.config(borderwidth=5, relief="flat")
    send_button.config(highlightthickness=0, highlightbackground="#ffffff")
    send_button.place(x=650, y=650)

    window.mainloop()
if __name__ == "__main__":
    main()