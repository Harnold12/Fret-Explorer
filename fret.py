"""
DEV LOG - ORDEM DE IMPLEMENTAÇÃO

1.  Definição do braço e da lógica cromática de 12 notas.
2.  Mapeamento de intervalos e cálculo automático de posições relativo à tônica.
3.  Criação do menu de configurações (afinação, trastes e escolha da root).
4.  Implementação de salvamento de dados e presets via JSON. 
5.  Inclusão de sistema de exclusão de presets e ordenação alfabética automática.
6.  Correção na sincronização dos labels dos botões ao alterar a tônica (Root).
7.  Implementação de labels dinâmicos que alternam entre C-D-E e 1-2-3.
8.  Inclusão de paleta de cores para agrupar ou marcar notas, tríades...
9.  Correção de alinhamentos na interface.
10. Desenvolvimento de exibição bicolor das notas via arcos.
11. Implementação de interação via botão direito para limpeza de cores secundárias.
12. Re-organização da ordem das funções e correções de bugs.
13. Inclusão de biblioteca de escalas comuns e seletor rápido no menu.
14. Internacionalização (i18n): Suporte a Inglês e Português.
15. Tradução completa da biblioteca de escalas padrões.
16. Implementação de seletor dinâmico de número de cordas (4 a 12).
17. Inclusão de Inlays (marcações) com ajuste dinâmico de posição e opacidade.
18. Correção de bugs quanto a seleção de quantas cordas.
19. Automatização de afinações padrão (4 a 9 cordas).
20. Validação de afinações com bloqueio de notas inválidas e tratamento de caracteres 'X' para 10 cordas ou mais.
21. Implementação de lógica para caso diminua e aumente quantidade de cordas.
22. Implementação do Modo Canhoto (Lefty Mode) com inversão horizontal do braço.
23. Implementação de lógica para que exista uma única janela de configurações.
24. Ajustes ao tamanho da interface e adição da assinatura (Fret Explorer by Henrique Arnold).
25. Re-organização e compactação do código.
26. Correção de bugs e ajustes finais. 
"""

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import json
import os
import sys

def resource_path(relative_path):
    """ Retorna o caminho absoluto para o recurso, funcionando no dev e no PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class FretboardApp:
    def __init__(self, root):
        # Inicialização da janela principal e variáveis de estilo
        self.root = root
        self.root.title("Python Fretboard Explorer")
        self.root.geometry("1240x680")
        self.root.configure(bg="#2c3e50")

        # Tenta carregar o ícone na janela (barra de título e barra de tarefas)
        try:
            icon_p = resource_path("icone.ico")
            self.root.iconbitmap(icon_p)
        except:
            pass

        # Dados estruturais e arquivos de persistência
        self.preset_file = "guitar_presets.json"
        self.notes_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.interval_map = {0:'1', 1:'b2', 2:'2', 3:'b3', 4:'3', 5:'4', 6:'b5', 7:'5', 8:'b6', 9:'6', 10:'b7', 11:'7'}
        self.bg_color = "#2c3e50"
        self.inlay_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
        self.settings_window = None 

        # Mapas de afinação padrão para instrumentos comerciais
        self.std_tunings = {
            4: ["E", "A", "D", "G"], 5: ["B", "E", "A", "D", "G"],
            6: ["E", "A", "D", "G", "B", "E"], 7: ["B", "E", "A", "D", "G", "B", "E"],
            8: ["F#", "B", "E", "A", "D", "G", "B", "E"],
            9: ["C#", "F#", "B", "E", "A", "D", "G", "B", "E"]
        }

        # Configurações de tradução e estado da interface
        self.languages = ["English", "Português"]
        self.current_lang = tk.StringVar(value="English")
        self.lefty_mode = tk.BooleanVar(value=False)
        self.trans = {
            "English": {
                "settings_btn": "⚙ Settings", "display_mode": "View:", "notes_colors": "Notes:",
                "reset_colors": "Reset", "instrument": "INSTRUMENT", "strings": "Strings:",
                "tuning": "Tuning:", "frets": "Frets:", "root": "Root:", "lefty": "Lefty Mode",
                "scale_lib": "Scales:", "apply": "Apply", "manage_pre": "PRESETS",
                "load": "Load", "delete": "Delete", "save_as": "Name:", "save_btn": "Save Preset",
                "lang_sel": "Language:", "msg_success": "Success", "msg_saved": "Saved!",
                "msg_del_conf": "Delete '{}'?", "modes": ["Notes", "Intervals"],
                "err_invalid": "Invalid Tuning! Check notes and 'X'.",
                "scales": {
                    "Custom": "Manual", "Major": "Major", "Minor": "Minor", "MajPent": "Maj Pentatonic",
                    "MinPent": "Min Pentatonic", "Blues": "Blues", "Dorian": "Dorian", 
                    "Mixolydian": "Mixolydian", "Lydian": "Lydian", "HarmonicMin": "Harmonic Minor"
                }
            },
            "Português": {
                "settings_btn": "⚙ Ajustes", "display_mode": "Ver:", "notes_colors": "Notas:",
                "reset_colors": "Resetar", "instrument": "INSTRUMENTO", "strings": "Cordas:",
                "tuning": "Afinação:", "frets": "Trastes:", "root": "Tônica:", "lefty": "Canhoto",
                "scale_lib": "Escalas:", "apply": "Aplicar", "manage_pre": "PRESETS",
                "load": "Abrir", "delete": "Excluir", "save_as": "Nome:", "save_btn": "Salvar Preset",
                "lang_sel": "Idioma:", "msg_success": "Sucesso", "msg_saved": "Salvo!",
                "msg_del_conf": "Excluir '{}'?", "modes": ["Notas", "Intervalos"],
                "err_invalid": "Afinação Inválida! Cheque as notas e os 'X'.",
                "scales": {
                    "Custom": "Manual", "Major": "Maior", "Minor": "Menor", "MajPent": "Pentatônica Maior",
                    "MinPent": "Pentatônica Menor", "Blues": "Blues", "Dorian": "Dórico", 
                    "Mixolydian": "Mixolídio", "Lydian": "Lídio", "HarmonicMin": "Menor Harmônica"
                }
            }
        }

        # Definição dos intervalos das escalas da biblioteca
        self.scales_data = {
            "Custom": [], "Major": [0, 2, 4, 5, 7, 9, 11], "Minor": [0, 2, 3, 5, 7, 8, 10], "MajPent": [0, 2, 4, 7, 9],
            "MinPent": [0, 3, 5, 7, 10], "Blues": [0, 3, 5, 6, 7, 10], "Dorian": [0, 2, 3, 5, 7, 9, 10],
            "Mixolydian": [0, 2, 4, 5, 7, 9, 10], "Lydian": [0, 2, 4, 6, 7, 9, 11], "HarmonicMin": [0, 2, 3, 5, 7, 8, 11]
        }

        # Estado inicial do instrumento e cores
        self.note_colors = {i: ("#e74c3c" if i == 0 else "#3498db") for i in range(12)}
        self.note_colors_sec = {i: None for i in range(12)}
        self.tuning = self.std_tunings[6]
        self.num_frets = 15
        self.selected_root = tk.StringVar(value="C")
        self.display_mode = tk.StringVar(value="Notes")
        self.active_intervals = {i: tk.BooleanVar(value=(i==0)) for i in range(12)}
        
        # Referências para widgets dinâmicos
        self.interval_checkboxes, self.color_boxes_prim, self.color_boxes_sec = [], [], []
        self.setup_ui()
        
        # Sincronização do Trace: Observa a variável display_mode para atualizar os labels dinamicamente
        self.display_mode.trace_add("write", lambda *a: self.update_ui_and_labels())
        for v in [self.selected_root, self.lefty_mode]: v.trace_add("write", lambda *a: self.draw_fretboard())

    def get_t(self, key): return self.trans[self.current_lang.get()][key]

    def setup_ui(self):
        # Construção da barra de ferramentas superior
        self.top_bar = tk.Frame(self.root, bg="#34495e", height=50); self.top_bar.pack(fill="x", side="top")
        self.btn_settings = tk.Button(self.top_bar, text=self.get_t("settings_btn"), command=self.open_settings, bg="#95a5a6", fg="white", font=("Arial", 9, "bold")); self.btn_settings.pack(side="left", padx=10, pady=5)
        self.chk_lefty = tk.Checkbutton(self.top_bar, text=self.get_t("lefty"), variable=self.lefty_mode, bg="#34495e", fg="white", selectcolor="#2c3e50", activebackground="#34495e", font=("Arial", 9)); self.chk_lefty.pack(side="left", padx=10)
        self.lbl_mode = tk.Label(self.top_bar, text=self.get_t("display_mode"), bg="#34495e", fg="white", font=("Arial", 9)); self.lbl_mode.pack(side="left", padx=5)
        # Combobox Read-only: Evita entradas aleatórias do usuário
        self.combo_mode = ttk.Combobox(self.top_bar, textvariable=self.display_mode, values=self.get_t("modes"), width=10, state="readonly"); self.combo_mode.pack(side="left", padx=5)

        # Canvas principal para renderização do braço
        self.canvas = tk.Canvas(self.root, bg=self.bg_color, highlightthickness=0); self.canvas.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Créditos autorais no rodapé
        tk.Label(self.root, text="Fret Explorer by Henrique Arnold", bg=self.bg_color, fg="#7f8c8d", font=("Arial", 8, "italic")).pack(side="bottom", anchor="se", padx=10, pady=5)

        # Container inferior para seleção de notas e cores
        self.selection_container = tk.Frame(self.root, bg=self.bg_color); self.selection_container.pack(fill="x", pady=(0, 10))
        self.lbl_notes_colors = tk.Label(self.selection_container, text=self.get_t("notes_colors"), bg=self.bg_color, fg="white", font=("Arial", 10, "bold")); self.lbl_notes_colors.pack(side="left", padx=(15, 5))

        self.blocks_frame = tk.Frame(self.selection_container, bg=self.bg_color); self.blocks_frame.pack(side="left")
        for i in range(12):
            block = tk.Frame(self.blocks_frame, bg=self.bg_color); block.pack(side="left", padx=(2, 5))
            cb = tk.Checkbutton(block, text="", variable=self.active_intervals[i], command=self.draw_fretboard, bg=self.bg_color, fg="#ecf0f1", selectcolor="#34495e", activebackground=self.bg_color); cb.pack(anchor="w"); self.interval_checkboxes.append(cb)
            cp = tk.Canvas(block, width=12, height=12, bg=self.note_colors[i], highlightbackground="#ecf0f1", cursor="hand2"); cp.pack(pady=(2, 1), anchor="w", padx=(3, 0)); cp.bind("<Button-1>", lambda e, idx=i: self.pick_color(idx, True)); self.color_boxes_prim.append(cp)
            cs = tk.Canvas(block, width=12, height=12, bg=self.bg_color, highlightbackground="#7f8c8d", cursor="hand2"); cs.pack(pady=(1, 5), anchor="w", padx=(3, 0)); cs.bind("<Button-1>", lambda e, idx=i: self.pick_color(idx, False)); cs.bind("<Button-3>", lambda e, idx=i: self.clear_sec_color(idx)); self.color_boxes_sec.append(cs)

        self.btn_reset = tk.Button(self.selection_container, text=self.get_t("reset_colors"), command=self.reset_colors, bg="#7f8c8d", fg="white", font=("Arial", 7), width=10); self.btn_reset.pack(side="left", padx=20, anchor="s", pady=(0, 5))
        self.update_ui_and_labels(); self.root.bind("<Configure>", lambda e: self.draw_fretboard())

    def open_settings(self):
        # Lógica de instância única para a janela de configurações
        if self.settings_window and self.settings_window.winfo_exists():
            self.settings_window.lift(); return
        
        self.settings_window = tk.Toplevel(self.root); win = self.settings_window; win.title("Settings"); win.geometry("400x780")
        tk.Label(win, text=self.get_t("lang_sel"), font=("Arial", 9, "bold")).pack(pady=(10,0))
        lang_combo = ttk.Combobox(win, textvariable=self.current_lang, values=self.languages, state="readonly"); lang_combo.pack(pady=5); lang_combo.bind("<<ComboboxSelected>>", lambda e: [self.refresh_main_ui_text(), win.destroy(), self.open_settings()])
        tk.Frame(win, height=1, bg="lightgray").pack(fill="x", pady=10)
        
        tk.Label(win, text=self.get_t("instrument"), font=("Arial", 10, "bold")).pack(pady=5)
        tk.Label(win, text=self.get_t("strings")).pack(); s_spn = tk.Spinbox(win, from_=1, to=12); s_spn.delete(0, "end"); s_spn.insert(0, len(self.tuning)); s_spn.pack()
        tk.Label(win, text=self.get_t("tuning")).pack(); t_ent = tk.Entry(win, width=30); t_ent.insert(0, ",".join(self.tuning)); t_ent.pack()

        # Atualização inteligente da afinação conforme o número de cordas
        def update_tuning_entry():
            try:
                n = int(s_spn.get())
                if n in self.std_tunings: t_ent.delete(0, "end"); t_ent.insert(0, ",".join(self.std_tunings[n]))
                elif n < 4: t_ent.delete(0, "end"); t_ent.insert(0, ",".join(self.std_tunings[4][:n]))
                elif n >= 10: 
                    cur = self.std_tunings[9][:]; [cur.append("X") for _ in range(n-9)]
                    t_ent.delete(0, "end"); t_ent.insert(0, ",".join(cur))
            except: pass
        s_spn.config(command=update_tuning_entry)

        tk.Label(win, text=self.get_t("frets")).pack(); f_spn = tk.Spinbox(win, from_=1, to=24); f_spn.delete(0, "end"); f_spn.insert(0, self.num_frets); f_spn.pack()
        tk.Label(win, text=self.get_t("root")).pack(); ttk.Combobox(win, textvariable=self.selected_root, values=self.notes_sharp).pack()
        tk.Label(win, text=self.get_t("scale_lib"), font=("Arial", 9, "bold")).pack(pady=(10,0))
        trans_scales = self.get_t("scales"); scale_var = tk.StringVar(value=list(trans_scales.values())[0]); ttk.Combobox(win, textvariable=scale_var, values=list(trans_scales.values()), state="readonly").pack(pady=5)
        
        # Aplicação das configurações com validação de notas e placeholders 'X'
        def apply():
            raw_tuning = t_ent.get().replace(" ", "").upper().split(",")
            if not all(n in self.notes_sharp for n in raw_tuning) or "X" in raw_tuning:
                messagebox.showerror("Error", self.get_t("err_invalid")); return
            self.tuning = raw_tuning; self.num_frets = int(f_spn.get())
            sid = next((k for k, v in trans_scales.items() if v == scale_var.get()), None)
            if sid: self.apply_scale_pattern(sid)
            self.update_ui_and_labels(); win.destroy()

        tk.Button(win, text=self.get_t("apply"), bg="#3498db", fg="white", font=("Arial", 9, "bold"), command=apply).pack(pady=15)
        tk.Frame(win, height=2, bg="gray").pack(fill="x", padx=20, pady=10)
        cb_pre = ttk.Combobox(win, values=sorted(self.load_presets().keys())); cb_pre.pack(pady=5)
        tk.Button(win, text=self.get_t("load"), command=lambda: [self.apply_preset(cb_pre.get()), win.destroy()]).pack()
        tk.Button(win, text=self.get_t("delete"), bg="#c0392b", fg="white", command=lambda: self.delete_preset(cb_pre.get(), win)).pack(pady=5)
        name_ent = tk.Entry(win); name_ent.pack(); tk.Button(win, text=self.get_t("save_btn"), bg="#27ae60", fg="white", command=lambda: [self.save_current_preset(name_ent.get()), win.destroy(), self.open_settings()]).pack(pady=5)

    def refresh_main_ui_text(self):
        # Atualização instantânea dos textos ao trocar idioma
        self.btn_settings.config(text=self.get_t("settings_btn")); self.lbl_mode.config(text=self.get_t("display_mode")); self.combo_mode.config(values=self.get_t("modes")); self.lbl_notes_colors.config(text=self.get_t("notes_colors")); self.btn_reset.config(text=self.get_t("reset_colors")); self.chk_lefty.config(text=self.get_t("lefty")); self.update_ui_and_labels()

    def pick_color(self, idx, prim):
        # Seletor de cor para notas e intervalos
        color = colorchooser.askcolor(title="Color")[1]
        if color:
            if prim: self.note_colors[idx] = color; self.color_boxes_prim[idx].config(bg=color)
            else: self.note_colors_sec[idx] = color; self.color_boxes_sec[idx].config(bg=color)
            self.draw_fretboard()

    def clear_sec_color(self, idx): self.note_colors_sec[idx] = None; self.color_boxes_sec[idx].config(bg=self.bg_color); self.draw_fretboard()

    def reset_colors(self):
        # Retorno às cores originais do software
        for i in range(12): self.note_colors[i] = ("#e74c3c" if i == 0 else "#3498db"); self.note_colors_sec[i] = None; self.color_boxes_prim[i].config(bg=self.note_colors[i]); self.color_boxes_sec[i].config(bg=self.bg_color)
        self.draw_fretboard()

    def apply_scale_pattern(self, sid):
        # Ativação em lote das notas de uma escala selecionada
        if sid != "Custom":
            for i in range(12): self.active_intervals[i].set(i in self.scales_data[sid])
        self.draw_fretboard()

    def update_ui_and_labels(self):
        # Lógica Bilingue: Sincronização dos labels inferiores entendendo Notes/Notas e Intervals/Intervalos
        txt = self.selected_root.get()
        if txt in self.notes_sharp:
            idx = self.notes_sharp.index(txt)
            for i, cb in enumerate(self.interval_checkboxes): 
                label_text = self.notes_sharp[(idx+i)%12] if self.display_mode.get() in ["Notes","Notas"] else self.interval_map[i]
                cb.config(text=label_text)
        self.draw_fretboard()

    def load_presets(self):
        if not os.path.exists(self.preset_file): return {}
        try:
            with open(self.preset_file, "r") as f: return json.load(f)
        except: return {}

    def save_current_preset(self, name):
        # Armazenamento do estado atual no arquivo JSON
        if not name: return
        p = self.load_presets(); p[name] = {"root": self.selected_root.get(), "intervals": [i for i, v in self.active_intervals.items() if v.get()], "tuning": self.tuning, "frets": self.num_frets, "colors_prim": self.note_colors, "colors_sec": self.note_colors_sec}
        with open(self.preset_file, "w") as f: json.dump(p, f)
        messagebox.showinfo(self.get_t("msg_success"), self.get_t("msg_saved"))

    def apply_preset(self, name):
        # Carregamento de dados salvos para a interface ativa
        d = self.load_presets().get(name)
        if d:
            self.selected_root.set(d["root"]); self.tuning = d["tuning"]; self.num_frets = d.get("frets", 15); self.note_colors = {int(k): v for k, v in d["colors_prim"].items()}; self.note_colors_sec = {int(k): v for k, v in d["colors_sec"].items()}
            for i in range(12): self.color_boxes_prim[i].config(bg=self.note_colors[i]); self.color_boxes_sec[i].config(bg=self.note_colors_sec[i] or self.bg_color); self.active_intervals[i].set(i in d["intervals"])
            self.update_ui_and_labels()

    def delete_preset(self, name, win):
        # Exclusão definitiva de um preset do banco de dados
        p = self.load_presets()
        if name in p and messagebox.askyesno(self.get_t("delete"), self.get_t("msg_del_conf").format(name)):
            del p[name]
            with open(self.preset_file, "w") as f: json.dump(p, f)
            win.destroy(); self.open_settings()

    def draw_fretboard(self):
        # Lógica central de renderização gráfica do instrumento
        self.canvas.delete("all"); w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w < 10: return
        px, py, fw = 50, 50, (w-100)/self.num_frets; n_str = len(self.tuning); sh = (h-100)/max(1, n_str-1); inst_h = (n_str-1)*sh; icy = py + inst_h/2; is_lefty = self.lefty_mode.get(); fb_end = px + self.num_frets * fw
        
        # Desenho dos trastes (vertical) e numeração horizontal
        for i in range(self.num_frets + 1):
            x = (px + i*fw) if not is_lefty else (fb_end - i*fw); self.canvas.create_line(x, py, x, py+inst_h, fill="#bdc3c7"); nx = x - fw/2 if not is_lefty else x + fw/2
            if i > 0: self.canvas.create_text(nx, py+inst_h+20, text=str(i), fill="white")

        # Marcações (bolinhas) com transparência stipple
        for f in self.inlay_frets:
            if f <= self.num_frets:
                xp = (px + (f-0.5)*fw) if not is_lefty else (fb_end - (f-0.5)*fw); clr = "#95a5a6"
                if f%12==0:
                    off = inst_h/4; self.canvas.create_oval(xp-8, icy-off-8, xp+8, icy-off+8, fill=clr, outline="", stipple="gray50"); self.canvas.create_oval(xp-8, icy+off-8, xp+8, icy+off+8, fill=clr, outline="", stipple="gray50")
                else: self.canvas.create_oval(xp-8, icy-8, xp+8, icy+8, fill=clr, outline="", stipple="gray50")

        # Desenho das cordas (horizontal) e notas mapeadas
        for s_idx, note in enumerate(reversed(self.tuning)):
            y = py + s_idx*sh; self.canvas.create_line(px, y, fb_end, y, fill="#7f8c8d", width=1+s_idx); lx = px - 20 if not is_lefty else fb_end + 20; self.canvas.create_text(lx, y, text=note, fill="white", font=("Arial", 10, "bold"))
            for fret in range(self.num_frets + 1):
                try:
                    n_idx = (self.notes_sharp.index(note.upper()) + fret) % 12; inv = (n_idx - self.notes_sharp.index(self.selected_root.get())) % 12
                    if self.active_intervals[inv].get():
                        x = (px if not is_lefty else fb_end) if fret==0 else ((px+fret*fw-fw/2) if not is_lefty else (fb_end-fret*fw+fw/2))
                        c1, c2 = self.note_colors[inv], self.note_colors_sec[inv]; lbl = self.notes_sharp[n_idx] if self.display_mode.get() in ["Notes","Notas"] else self.interval_map[inv]
                        if c2: self.canvas.create_arc(x-15, y-15, x+15, y+15, start=90, extent=180, fill=c1, outline="white"); self.canvas.create_arc(x-15, y-15, x+15, y+15, start=270, extent=180, fill=c2, outline="white")
                        else: self.canvas.create_oval(x-15, y-15, x+15, y+15, fill=c1, outline="white")
                        self.canvas.create_text(x, y, text=lbl, fill="white", font=("Arial", 9, "bold"))
                except: continue

if __name__ == "__main__":
    root = tk.Tk(); app = FretboardApp(root); root.mainloop()