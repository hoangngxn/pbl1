import tkinter as tk
from tkinter import ttk, messagebox
from app import schedule_jobs

class ModernJobSchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lập Lịch Công Việc")
        self.root.geometry("800x850")
        
        # Modern color scheme
        self.colors = {
            "primary": "#28a745",       # Green for primary elements
            "text_light": "#ffffff",     # White text
            "text_dark": "#333333",      # Dark text
            "bg_light": "#ffffff",       # White background
            "bg_grey": "#f4f4f9",        # Light grey
            "border": "#e0e0e0"          # Light border
        }
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        style = ttk.Style()
        
        # Configure base styles
        style.configure("TFrame", background=self.colors["bg_light"])
        
        # Label styles
        style.configure("Header.TLabel",
                       font=("Helvetica", 24, "bold"),
                       background=self.colors["bg_light"],
                       foreground=self.colors["primary"])
        
        style.configure("SubHeader.TLabel",
                       font=("Helvetica", 12),
                       background=self.colors["bg_light"],
                       foreground=self.colors["text_dark"])
        
        # Button styles - green rounded buttons
        style.configure("Primary.TButton",
                       font=("Helvetica", 11),
                       background=self.colors["primary"],
                       foreground=self.colors["text_dark"],
                       padding=(15, 10),
                       borderwidth=0)
                       
        style.map("Primary.TButton",
                 background=[('active', '#1e7e34'), ('pressed', '#1c7430')])
                 
        # Secondary button
        style.configure("Secondary.TButton",
                       font=("Helvetica", 11),
                       background="#e0e0e0",
                       foreground=self.colors["text_dark"],
                       padding=(15, 10),
                       borderwidth=0)
                       
        style.map("Secondary.TButton",
                 background=[('active', '#d0d0d0'), ('pressed', '#c0c0c0')])
        
        # Entry style
        style.configure("TEntry", 
                       padding=(10, 5),
                       fieldbackground="#f8f9fa")
                       
        # Labelframe style
        style.configure("TLabelframe", 
                       background=self.colors["bg_light"],
                       bordercolor=self.colors["border"])
        
        style.configure("TLabelframe.Label", 
                       font=("Helvetica", 12, "bold"),
                       background=self.colors["bg_light"],
                       foreground=self.colors["text_dark"])
        
        # Configure the root background
        self.root.configure(bg=self.colors["bg_light"])
        
    def create_widgets(self):
        # Main container
        content = ttk.Frame(self.root, style="TFrame", padding=25)
        content.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)
        
        # Header with app logo and title
        header_frame = ttk.Frame(content, style="TFrame")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        app_icon = "🚀"  # Using an emoji as a placeholder for the icon
        header_title_frame = ttk.Frame(header_frame, style="TFrame")
        header_title_frame.grid(row=0, column=0, sticky="w")
        
        ttk.Label(header_title_frame, 
                 text=f"{app_icon} Lập Lịch Công Việc Pro", 
                 style="Header.TLabel").grid(row=0, column=0, sticky="w")
        
        ttk.Label(header_title_frame,
                 text="Tối ưu hóa lập lịch công việc của bạn một cách hiệu quả",
                 style="SubHeader.TLabel").grid(row=1, column=0, sticky="w", pady=(5, 0))
        
        # Job Configuration Section
        config_frame = ttk.LabelFrame(content, text="Cấu Hình Công Việc", padding=(20, 10))
        config_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))
        config_frame.grid_columnconfigure(1, weight=1)
        
        # Number of jobs
        ttk.Label(config_frame, 
                 text="Số lượng công việc:",
                 font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
                 
        self.n_jobs = ttk.Entry(config_frame, width=15, font=("Helvetica", 10))
        self.n_jobs.grid(row=0, column=1, sticky="w", pady=10, padx=5)
        self.n_jobs.insert(0, "vd: 3")
        self.n_jobs.bind("<FocusIn>", lambda e: self.on_entry_click(self.n_jobs, "vd: 3"))
        self.n_jobs.bind("<FocusOut>", lambda e: self.on_focus_out(self.n_jobs, "vd: 3"))
        
        # Processing times
        ttk.Label(config_frame, 
                 text="Thời gian xử lý:",
                 font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
                 
        self.processing_times = ttk.Entry(config_frame, width=40, font=("Helvetica", 10))
        self.processing_times.grid(row=1, column=1, sticky="ew", pady=10, padx=5)
        self.processing_times.insert(0, "vd: 2 3 4 (các số cách nhau bởi dấu cách)")
        self.processing_times.bind("<FocusIn>", lambda e: self.on_entry_click(self.processing_times, "vd: 2 3 4 (các số cách nhau bởi dấu cách)"))
        self.processing_times.bind("<FocusOut>", lambda e: self.on_focus_out(self.processing_times, "vd: 2 3 4 (các số cách nhau bởi dấu cách)"))
        
        # Deadlines
        ttk.Label(config_frame, 
                 text="Thời hạn:",
                 font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w", pady=10)
                 
        self.deadlines = ttk.Entry(config_frame, width=40, font=("Helvetica", 10))
        self.deadlines.grid(row=2, column=1, sticky="ew", pady=10, padx=5)
        self.deadlines.insert(0, "vd: 3 4 5 (các số cách nhau bởi dấu cách)")
        self.deadlines.bind("<FocusIn>", lambda e: self.on_entry_click(self.deadlines, "vd: 3 4 5 (các số cách nhau bởi dấu cách)"))
        self.deadlines.bind("<FocusOut>", lambda e: self.on_focus_out(self.deadlines, "vd: 3 4 5 (các số cách nhau bởi dấu cách)"))
        
        # Buttons container
        button_frame = ttk.Frame(content, style="TFrame")
        button_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        # Clear button (secondary)
        ttk.Button(button_frame,
                  text="Xóa",
                  style="Secondary.TButton",
                  command=self.clear_inputs).grid(row=0, column=0, padx=(0, 10), sticky="e")
        
        # Schedule button (primary)
        ttk.Button(button_frame,
                  text="Lập Lịch",
                  style="Primary.TButton",
                  command=self.schedule).grid(row=0, column=1, padx=(10, 0), sticky="w")
        
        # Results Section
        results_frame = ttk.LabelFrame(content, text="Kết Quả", padding=15)
        results_frame.grid(row=3, column=0, sticky="nsew", pady=(0, 15))
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(0, weight=1)
        
        self.result_text = tk.Text(results_frame, 
                                 height=15, 
                                 wrap=tk.WORD,
                                 font=("Consolas", 10),
                                 background="#f8f9fa",
                                 borderwidth=1,
                                 relief="solid",
                                 padx=10,
                                 pady=10)
        self.result_text.grid(row=0, column=0, sticky="nsew")
        
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(content, 
                                  textvariable=self.status_var,
                                  relief=tk.SUNKEN, 
                                  background="#f0f0f0",
                                  padding=(10, 5))
        self.status_bar.grid(row=4, column=0, sticky="ew")
        self.status_var.set("Sẵn sàng")
        
        # Make the content frame expandable
        content.grid_rowconfigure(3, weight=1)
        
    def on_entry_click(self, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            entry.config(foreground='black')
            
    def on_focus_out(self, entry, default_text):
        if entry.get() == '':
            entry.insert(0, default_text)
            entry.config(foreground='gray')
            
    def clear_inputs(self):
        self.n_jobs.delete(0, tk.END)
        self.processing_times.delete(0, tk.END)
        self.deadlines.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.status_var.set("Đã xóa dữ liệu nhập")
        
        # Reset default texts
        self.n_jobs.insert(0, "vd: 3")
        self.processing_times.insert(0, "vd: 2 3 4 (các số cách nhau bởi dấu cách)")
        self.deadlines.insert(0, "vd: 3 4 5 (các số cách nhau bởi dấu cách)")
        
    def validate_input(self):
        try:
            # Check if inputs are default placeholder text
            if self.n_jobs.get() == "vd: 3" or \
               self.processing_times.get() == "vd: 2 3 4 (các số cách nhau bởi dấu cách)" or \
               self.deadlines.get() == "vd: 3 4 5 (các số cách nhau bởi dấu cách)":
                raise ValueError("Vui lòng điền đầy đủ thông tin vào tất cả các trường")
            
            n = int(self.n_jobs.get())
            p = list(map(int, self.processing_times.get().split()))
            d = list(map(int, self.deadlines.get().split()))
            
            if len(p) != n or len(d) != n:
                raise ValueError("Số lượng thời gian xử lý và thời hạn phải khớp với số lượng công việc")
            
            if any(x <= 0 for x in p) or any(x <= 0 for x in d):
                raise ValueError("Tất cả thời gian và thời hạn phải là số dương")
            
            return n, p, d
        except ValueError as e:
            messagebox.showerror("Lỗi Nhập Liệu", str(e))
            self.status_var.set("Lỗi: Dữ liệu không hợp lệ")
            return None
        
    def schedule(self):
        input_data = self.validate_input()
        if input_data is None:
            return
            
        n, p, d = input_data
        completed_jobs, schedule = schedule_jobs(n, p, d)
        
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        
        # Format and display results
        result = f"📊 Kết Quả Lập Lịch\n{'='*50}\n\n"
        result += f"✅ Số công việc hoàn thành: {completed_jobs}\n\n"
        result += f"📋 Trình tự công việc: {' → '.join(map(str, schedule))}\n\n"
        
        # Add detailed schedule
        result += "📑 Lịch Chi Tiết:\n" + "─"*50 + "\n"
        current_time = 0
        for job_id in schedule:
            job_idx = job_id - 1
            result += f"🔷 Công việc {job_id}:\n"
            result += f"   ├─ Thời gian bắt đầu: {current_time}\n"
            result += f"   ├─ Thời gian xử lý: {p[job_idx]}\n"
            result += f"   ├─ Thời hạn: {d[job_idx]}\n"
            result += f"   └─ Thời gian hoàn thành: {current_time + p[job_idx]}\n\n"
            current_time += p[job_idx]
            
        self.result_text.insert(1.0, result)
        self.status_var.set(f"Đã lập lịch thành công {completed_jobs} công việc")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernJobSchedulerGUI(root)
    root.mainloop() 