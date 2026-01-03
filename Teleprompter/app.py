import tkinter as tk
from tkinter import ttk
import os
import glob

class ScriptReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("研修用テレプロンプター")
        self.root.geometry("600x400")
        
        # 常に最前面に表示
        self.root.attributes('-topmost', True)
        # 初期透明度 (0.1〜1.0)
        self.root.attributes('-alpha', 0.8)
        
        # 背景色設定（目に優しいダークテーマ）
        self.bg_color = "#1e1e1e"
        self.fg_color = "#d4d4d4"
        self.root.configure(bg=self.bg_color)

        # --- レイアウト構成 ---
        # 左側：ファイル一覧リスト
        # 右側：テキスト表示エリア
        
        # 全体のコンテナ
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 左サイドバー（ファイルリスト）
        left_frame = tk.Frame(main_frame, width=150, bg=self.bg_color)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))

        tk.Label(left_frame, text="台本リスト", bg=self.bg_color, fg="#aaaaaa", font=("Meiryo", 9)).pack(pady=2)
        
        self.file_listbox = tk.Listbox(left_frame, bg="#252526", fg="white", selectbackground="#007acc", font=("Meiryo", 10), bd=0)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_listbox.bind('<<ListboxSelect>>', self.load_content)
        
        # スクロールバー（リスト用）
        list_scroll = tk.Scrollbar(left_frame, command=self.file_listbox.yview, bg=self.bg_color)
        list_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=list_scroll.set)

        # 右メインエリア（テキスト表示）
        right_frame = tk.Frame(main_frame, bg=self.bg_color)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # コントロールバー（透明度・フォントサイズ）
        control_frame = tk.Frame(right_frame, bg=self.bg_color)
        control_frame.pack(fill=tk.X, pady=(0, 5))

        # 透明度スライダー
        tk.Label(control_frame, text="透明度:", bg=self.bg_color, fg="#aaaaaa", font=("Meiryo", 8)).pack(side=tk.LEFT)
        self.alpha_scale = tk.Scale(control_frame, from_=0.2, to=1.0, resolution=0.05, orient=tk.HORIZONTAL, 
                                    bg=self.bg_color, fg="white", highlightthickness=0, length=100, command=self.change_alpha)
        self.alpha_scale.set(0.8) # 初期値
        self.alpha_scale.pack(side=tk.LEFT, padx=5)

        # 文字サイズスライダー
        tk.Label(control_frame, text="文字サイズ:", bg=self.bg_color, fg="#aaaaaa", font=("Meiryo", 8)).pack(side=tk.LEFT, padx=(10,0))
        self.font_scale = tk.Scale(control_frame, from_=10, to=40, orient=tk.HORIZONTAL, 
                                   bg=self.bg_color, fg="white", highlightthickness=0, length=100, command=self.change_font_size)
        self.font_scale.set(16) # 初期値
        self.font_scale.pack(side=tk.LEFT, padx=5)

        # リロードボタン
        tk.Button(control_frame, text="更新", command=self.load_file_list, bg="#333333", fg="white", bd=1, relief="flat", font=("Meiryo", 8)).pack(side=tk.RIGHT)

        # テキストウィジェット（本文）
        self.text_area = tk.Text(right_frame, bg="#1e1e1e", fg=self.fg_color, font=("Meiryo", 16), bd=0, padx=10, pady=10)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # スクロールバー（本文用）
        text_scroll = tk.Scrollbar(right_frame, command=self.text_area.yview)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=text_scroll.set)

        # 初期ロード
        self.load_file_list()

    def load_file_list(self):
        """scriptsフォルダ内のtxtファイルを読み込む"""
        self.file_listbox.delete(0, tk.END)
        self.files = []
        
        # scriptsフォルダのパス（実行ファイルと同じ場所にある前提）
        script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "talk scripts")
        
        if not os.path.exists(script_dir):
            os.makedirs(script_dir)
            with open(os.path.join(script_dir, "00_sample.txt"), "w", encoding="utf-8") as f:
                f.write("ここに台本が表示されます。\nscriptsフォルダにテキストファイルを置いてください。")

        # ファイル検索とソート
        file_paths = glob.glob(os.path.join(script_dir, "*.txt"))
        file_paths.sort() # 名前順にソート

        for path in file_paths:
            filename = os.path.basename(path)
            self.files.append(path)
            self.file_listbox.insert(tk.END, filename)

    def load_content(self, event):
        """リストで選択されたファイルの中身を表示"""
        selection = self.file_listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        file_path = self.files[index]
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
        except Exception as e:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", f"読み込みエラー: {e}")

    def change_alpha(self, value):
        """透明度の変更"""
        self.root.attributes('-alpha', float(value))

    def change_font_size(self, value):
        """フォントサイズの変更"""
        self.text_area.config(font=("Meiryo", int(value)))

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptReaderApp(root)
    root.mainloop()