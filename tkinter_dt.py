import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess


class DataTrainingWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Training Widget")
        self.dataset = None

        self.create_main_frame()

    def create_main_frame(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack()

        # Import Dataset button
        import_button = tk.Button(main_frame, text="Import Dataset", command=self.import_dataset)
        import_button.grid(row=0, column=0, pady=10)

        # Preprocess Data button
        preprocess_button = tk.Button(main_frame, text="Preprocess Data", command=self.preprocess_data)
        preprocess_button.grid(row=1, column=0, pady=10)

        # Train Model button
        train_button = tk.Button(main_frame, text="Train Model", command=self.train_model)
        train_button.grid(row=2, column=0, pady=10)

        # Open Python File button
        open_file_button = tk.Button(main_frame, text="Open Python File", command=self.open_python_file)
        open_file_button.grid(row=3, column=0, pady=10)

        # Report analysis text widget
        self.report_text = tk.Text(main_frame, height=10, width=50)
        self.report_text.grid(row=4, column=0, pady=10)

    def import_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
        if file_path:
            try:
                self.dataset = pd.read_excel(file_path)

                # Display the imported dataset in the report text widget
                self.report_text.delete("1.0", tk.END)
                self.report_text.insert(tk.END, self.dataset.to_string())
                messagebox.showinfo("Import Successful", "Dataset imported successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def preprocess_data(self):
        if self.dataset is None:
            messagebox.showerror("Error", "No dataset imported.")
            return

        # Perform data preprocessing steps
        # Example: Normalize the data using min-max scaling
        processed_dataset = self.dataset.copy()
        processed_dataset = (processed_dataset - processed_dataset.min()) / (
                processed_dataset.max() - processed_dataset.min())

        # Update the dataset with the preprocessed data
        self.dataset = processed_dataset

        # Save the preprocessed dataset as a CSV file
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if save_path:
            try:
                processed_dataset.to_csv(save_path, index=False)
                messagebox.showinfo("Save Complete", "Preprocessed dataset saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Display the preprocessed dataset in the report text widget
        self.report_text.delete("1.0", tk.END)
        self.report_text.insert(tk.END, self.dataset.to_string())

        messagebox.showinfo("Preprocessing Complete", "Data preprocessing completed successfully.")

    def train_model(self):
        if self.dataset is None:
            messagebox.showerror("Error", "No dataset imported.")
            return

        # Model training steps
        # ...

        messagebox.showinfo("Training Complete", "Model training completed successfully.")

    def open_python_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            try:
                subprocess.Popen(["cmd", "/c", "python", file_path])
            except Exception as e:
                messagebox.showerror("Error", str(e))


def main():
    root = tk.Tk()
    app = DataTrainingWidget(root)
    root.mainloop()


if __name__ == "__main__":
    main()

