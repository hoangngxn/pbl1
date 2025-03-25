import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from app import schedule_jobs
import datetime


class ModernJobSchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lập Lịch Công Việc")
        self.root.geometry("600x600")

        self.colors = {
            "primary": "#28a745",
            "text_light": "#ffffff",
            "text_dark": "#333333",
            "bg_light": "#ffffff",
            "bg_grey": "#f4f4f9",
            "border": "#e0e0e0",
        }

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        style = ttk.Style()
        style.configure("TFrame", background=self.colors["bg_light"])
        style.configure(
            "Header.TLabel",
            font=("Helvetica", 24, "bold"),
            background=self.colors["bg_light"],
            foreground=self.colors["primary"],
        )
        style.configure(
            "Primary.TButton",
            font=("Helvetica", 11),
            background=self.colors["primary"],
            foreground=self.colors["text_dark"],
            padding=(15, 10),
            borderwidth=0,
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#1e7e34"), ("pressed", "#1c7430")],
        )
        style.configure(
            "Secondary.TButton",
            font=("Helvetica", 11),
            background="#e0e0e0",
            foreground=self.colors["text_dark"],
            padding=(15, 10),
            borderwidth=0,
        )
        style.map(
            "Secondary.TButton",
            background=[("active", "#d0d0d0"), ("pressed", "#c0c0c0")],
        )
        self.root.configure(bg=self.colors["bg_light"])

    def create_widgets(self):
        content = ttk.Frame(self.root, padding=25)
        content.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        header_frame = ttk.Frame(content)
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        ttk.Label(
            header_frame, text="🚀 Lập Lịch Công Việc", style="Header.TLabel"
        ).grid(row=0, column=0, sticky="w")

        config_frame = ttk.LabelFrame(
            content, text="Cấu Hình Công Việc", padding=(20, 10)
        )
        config_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ttk.Label(config_frame, text="Số lượng công việc:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.n_jobs = ttk.Entry(config_frame, width=15)
        self.n_jobs.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(config_frame, text="Thời gian xử lý:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.processing_times = ttk.Entry(config_frame, width=40)
        self.processing_times.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(config_frame, text="Thời hạn:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.deadlines = ttk.Entry(config_frame, width=40)
        self.deadlines.grid(row=2, column=1, pady=5, padx=5)

        button_frame = ttk.Frame(content)
        button_frame.grid(row=2, column=0, sticky="ew", pady=(0, 20))
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        ttk.Button(
            button_frame,
            text="Tải từ File",
            style="Secondary.TButton",
            command=self.load_from_file,
        ).grid(row=0, column=0, padx=10, sticky="e")

        ttk.Button(
            button_frame,
            text="Lập Lịch",
            style="Primary.TButton",
            command=self.schedule,
        ).grid(row=0, column=1, padx=10, sticky="w")

        results_frame = ttk.LabelFrame(content, text="Kết Quả", padding=15)
        results_frame.grid(row=3, column=0, sticky="nsew", pady=(0, 15))

        self.result_text = tk.Text(
            results_frame,
            height=15,
            wrap=tk.WORD,
            font=("Consolas", 10),
            padx=10,
            pady=10,
        )
        self.result_text.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            results_frame, orient=tk.VERTICAL, command=self.result_text.yview
        )
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.result_text.configure(yscrollcommand=scrollbar.set)

        self.status_var = tk.StringVar()
        ttk.Label(
            content,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            background="#f0f0f0",
            padding=(10, 5),
        ).grid(row=4, column=0, sticky="ew")
        self.status_var.set("Sẵn sàng")

        content.grid_rowconfigure(3, weight=1)

    def load_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Input Files", "*.inp")])
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                if len(lines) != 3:
                    raise ValueError("File không đúng định dạng!")

                n = lines[0].strip()
                p = lines[1].strip()
                d = lines[2].strip()

                self.n_jobs.delete(0, tk.END)
                self.processing_times.delete(0, tk.END)
                self.deadlines.delete(0, tk.END)

                self.n_jobs.insert(0, n)
                self.processing_times.insert(0, p)
                self.deadlines.insert(0, d)

                self.status_var.set(f"Đã tải dữ liệu từ {file_path}")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải dữ liệu từ file:\n{str(e)}")

    def schedule(self):
        try:
            n = int(self.n_jobs.get())
            p = list(map(int, self.processing_times.get().split()))
            d = list(map(int, self.deadlines.get().split()))

            if len(p) != n or len(d) != n:
                raise ValueError("Dữ liệu không hợp lệ!")

            completed_jobs, schedule = schedule_jobs(n, p, d)

            self.result_text.delete(1.0, tk.END)
            result = f"✅ Số công việc hoàn thành: {completed_jobs}\n"
            result += f"📋 Trình tự công việc: {' → '.join(map(str, schedule))}\n"
            self.result_text.insert(1.0, result)

            self.status_var.set(f"Đã lập lịch thành công {completed_jobs} công việc")

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.out"
            with open(filename, "w") as f:
                f.write(f"{completed_jobs}\n")
                f.write(" ".join(map(str, schedule)) + "\n")

        except Exception as e:
            self.status_var.set("Lỗi lập lịch!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernJobSchedulerGUI(root)
    root.mainloop()
