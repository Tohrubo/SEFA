"""
search_gui.py
=============
Antarmuka grafis (Tkinter) untuk Mesin Pencari TF-IDF Bahasa Indonesia.
Mengimpor semua fungsi dari search_engine.py

HOW TO RUN:
    python search_gui.py
    python search_gui.py path/to/documents/folder

REQUIRES:
    - search_engine.py  (harus ada di folder yang sama)
    - pip install scikit-learn pandas numpy PySastrawi
    - tkinter (sudah termasuk dalam Python standar)
"""

import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Import semua fungsi dari search_engine.py

from search_engine import (
    build_index,
    search,
    predict_next,
    display_tfidf_table
)


# ─── Colour palette ──────────────────────────────────────────────────────────
BG_DARK    = "#0d1117"   # background utama
BG_PANEL   = "#161b22"   # panel / card
BG_INPUT   = "#1c2128"   # input field
BORDER     = "#30363d"   # garis tepi
ACCENT     = "#e6a817"   # kuning-amber (aksen utama)
ACCENT2    = "#58a6ff"   # biru terang (aksen sekunder)
TEXT_PRI   = "#e6edf3"   # teks utama
TEXT_SEC   = "#8b949e"   # teks sekunder
TEXT_MUTED = "#484f58"   # teks redup
SUCCESS    = "#3fb950"   # hijau (similarity tinggi)
WARNING    = "#d29922"   # kuning (similarity sedang)
DANGER     = "#f85149"   # merah (similarity rendah)

FONT_UI    = ("Segoe UI", 10)
FONT_MONO  = ("Consolas", 9)
FONT_TITLE = ("Segoe UI Semibold", 13)
FONT_HEAD  = ("Segoe UI Semibold", 10)
FONT_SMALL = ("Segoe UI", 8)


# =============================================================================
# HELPER — warna similarity
# =============================================================================

def similarity_color(score: float) -> str:
    if score >= 0.5:
        return SUCCESS
    elif score >= 0.2:
        return WARNING
    else:
        return DANGER


def similarity_bar(score: float, width: int = 20) -> str:
    filled = round(score * width)
    return "█" * filled + "░" * (width - filled)


# =============================================================================
# MAIN APPLICATION
# =============================================================================

class SearchEngineApp(tk.Tk):

    def __init__(self, folder: str = "documents"):
        super().__init__()
        self.folder  = folder
        self.index   = None
        self._build_window()
        self._build_layout()
        self._load_index_async()

    # ── Window setup ──────────────────────────────────────────────────────────

    def _build_window(self):
        self.title("Mesin Pencari TF-IDF — Bahasa Indonesia")
        self.geometry("1100x720")
        self.minsize(900, 600)
        self.configure(bg=BG_DARK)
        self.option_add("*Font", FONT_UI)

        # Style ttk widgets
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame",       background=BG_DARK)
        style.configure("Panel.TFrame", background=BG_PANEL)
        style.configure("TLabel",       background=BG_DARK,  foreground=TEXT_PRI)
        style.configure("Panel.TLabel", background=BG_PANEL, foreground=TEXT_PRI)
        style.configure("Muted.TLabel", background=BG_PANEL, foreground=TEXT_SEC,
                        font=FONT_SMALL)
        style.configure("TScrollbar",   background=BG_PANEL, troughcolor=BG_DARK,
                        arrowcolor=TEXT_SEC, bordercolor=BORDER, lightcolor=BG_PANEL,
                        darkcolor=BG_PANEL)
        style.configure("Treeview",
                        background=BG_PANEL, foreground=TEXT_PRI,
                        fieldbackground=BG_PANEL, rowheight=26,
                        bordercolor=BORDER, font=FONT_MONO)
        style.configure("Treeview.Heading",
                        background=BG_DARK, foreground=ACCENT,
                        relief="flat", font=FONT_HEAD)
        style.map("Treeview",
                  background=[("selected", "#1f3a5f")],
                  foreground=[("selected", TEXT_PRI)])
        style.map("Treeview.Heading", background=[("active", BG_INPUT)])

    # ── Layout ────────────────────────────────────────────────────────────────

    def _build_layout(self):
        # ── Header ────────────────────────────────────────────────────────────
        header = tk.Frame(self, bg=BG_DARK, pady=0)
        header.pack(fill="x", padx=20, pady=(16, 0))

        tk.Label(header, text="⬡  MESIN PENCARI TF-IDF",
                 bg=BG_DARK, fg=ACCENT,
                 font=("Segoe UI Semibold", 16)).pack(side="left")

        self._lbl_status = tk.Label(header, text="Memuat indeks...",
                                    bg=BG_DARK, fg=TEXT_SEC,
                                    font=FONT_SMALL)
        self._lbl_status.pack(side="right", padx=4)

        # Folder selector
        fold_row = tk.Frame(self, bg=BG_DARK)
        fold_row.pack(fill="x", padx=20, pady=(6, 0))

        tk.Label(fold_row, text="Folder dokumen:", bg=BG_DARK,
                 fg=TEXT_SEC, font=FONT_SMALL).pack(side="left")

        self._var_folder = tk.StringVar(value=os.path.abspath(self.folder))
        tk.Label(fold_row, textvariable=self._var_folder,
                 bg=BG_DARK, fg=ACCENT2, font=FONT_SMALL).pack(side="left", padx=6)

        tk.Button(fold_row, text="Ganti Folder",
                  bg=BG_INPUT, fg=TEXT_SEC, relief="flat",
                  font=FONT_SMALL, cursor="hand2",
                  activebackground=BORDER, activeforeground=TEXT_PRI,
                  command=self._change_folder).pack(side="left", padx=4)

        # Divider
        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", padx=20, pady=10)

        # ── Main paned area ───────────────────────────────────────────────────
        paned = tk.PanedWindow(self, orient="horizontal",
                               bg=BG_DARK, sashwidth=6,
                               sashrelief="flat", sashpad=2)
        paned.pack(fill="both", expand=True, padx=20, pady=(0, 16))

        # LEFT: search + results
        left = tk.Frame(paned, bg=BG_DARK)
        paned.add(left, minsize=380)

        # RIGHT: TF-IDF table
        right = tk.Frame(paned, bg=BG_DARK)
        paned.add(right, minsize=320)

        self._build_left(left)
        self._build_right(right)

    def _build_left(self, parent):
        # Search bar
        search_frame = tk.Frame(parent, bg=BG_PANEL,
                                highlightbackground=BORDER,
                                highlightthickness=1)
        search_frame.pack(fill="x", pady=(0, 12))

        inner = tk.Frame(search_frame, bg=BG_PANEL, padx=12, pady=10)
        inner.pack(fill="x")

        tk.Label(inner, text="QUERY PENCARIAN", bg=BG_PANEL,
                 fg=ACCENT, font=("Segoe UI Semibold", 8)).pack(anchor="w")

        entry_row = tk.Frame(inner, bg=BG_PANEL)
        entry_row.pack(fill="x", pady=(6, 0))

        self._var_query = tk.StringVar()
        self._entry = tk.Entry(entry_row,
                               textvariable=self._var_query,
                               bg=BG_INPUT, fg=TEXT_PRI,
                               insertbackground=ACCENT,
                               relief="flat", font=("Segoe UI", 11),
                               highlightbackground=BORDER,
                               highlightthickness=1)
        self._entry.pack(side="left", fill="x", expand=True, ipady=7, padx=(0, 8))
        self._entry.bind("<Return>", lambda e: self._do_search())

        self._btn_search = tk.Button(entry_row, text="Cari  ▶",
                                     bg=ACCENT, fg=BG_DARK,
                                     relief="flat", font=FONT_HEAD,
                                     cursor="hand2", padx=14, pady=6,
                                     activebackground="#f0b830",
                                     activeforeground=BG_DARK,
                                     command=self._do_search)
        self._btn_search.pack(side="left")

        # Pre-process preview
        prev_row = tk.Frame(inner, bg=BG_PANEL)
        prev_row.pack(fill="x", pady=(6, 0))
        tk.Label(prev_row, text="Token:", bg=BG_PANEL,
                 fg=TEXT_MUTED, font=FONT_SMALL).pack(side="left")
        self._lbl_tokens = tk.Label(prev_row, text="—",
                                    bg=BG_PANEL, fg=TEXT_SEC,
                                    font=("Consolas", 8), wraplength=380,
                                    justify="left")
        self._lbl_tokens.pack(side="left", padx=4)
        self._var_query.trace_add("write", self._update_token_preview)

        # Results area
        tk.Label(parent, text="HASIL PENCARIAN", bg=BG_DARK,
                 fg=TEXT_SEC, font=("Segoe UI Semibold", 8)).pack(anchor="w", pady=(0, 4))

        self._results_canvas = tk.Canvas(parent, bg=BG_DARK,
                                         highlightthickness=0)
        results_scroll = ttk.Scrollbar(parent, orient="vertical",
                                       command=self._results_canvas.yview)
        self._results_canvas.configure(yscrollcommand=results_scroll.set)

        results_scroll.pack(side="right", fill="y")
        self._results_canvas.pack(fill="both", expand=True)

        self._results_inner = tk.Frame(self._results_canvas, bg=BG_DARK)
        self._canvas_window = self._results_canvas.create_window(
            (0, 0), window=self._results_inner, anchor="nw")

        self._results_inner.bind("<Configure>", self._on_results_configure)
        self._results_canvas.bind("<Configure>", self._on_canvas_configure)
        self._results_canvas.bind("<MouseWheel>",
                                  lambda e: self._results_canvas.yview_scroll(
                                      int(-1 * (e.delta / 120)), "units"))

        self._show_placeholder()

    def _build_right(self, parent):
        tk.Label(parent, text="TABEL TF-IDF  (term × dokumen)",
                 bg=BG_DARK, fg=TEXT_SEC,
                 font=("Segoe UI Semibold", 8)).pack(anchor="w", pady=(0, 4))

        tk.Label(parent, text="baris = term  |  kolom = dokumen  |  nilai = bobot TF-IDF",
                 bg=BG_DARK, fg=TEXT_MUTED,
                 font=FONT_SMALL).pack(anchor="w", pady=(0, 6))

        # Treeview + scrollbars
        tree_frame = tk.Frame(parent, bg=BG_PANEL,
                              highlightbackground=BORDER,
                              highlightthickness=1)
        tree_frame.pack(fill="both", expand=True)

        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        vsb.pack(side="right",  fill="y")
        hsb.pack(side="bottom", fill="x")

        self._tree = ttk.Treeview(tree_frame,
                                   yscrollcommand=vsb.set,
                                   xscrollcommand=hsb.set,
                                   show="headings",
                                   selectmode="browse")
        self._tree.pack(fill="both", expand=True)
        vsb.configure(command=self._tree.yview)
        hsb.configure(command=self._tree.xview)

        # Row striping
        self._tree.tag_configure("odd",  background=BG_PANEL)
        self._tree.tag_configure("even", background=BG_INPUT)
        self._tree.tag_configure("nonzero", foreground=ACCENT2)

        # Stats row below table
        self._lbl_vocab = tk.Label(parent, text="",
                                   bg=BG_DARK, fg=TEXT_MUTED,
                                   font=FONT_SMALL)
        self._lbl_vocab.pack(anchor="w", pady=(6, 0))

    # ── Index loading ─────────────────────────────────────────────────────────

    def _load_index_async(self):
        self._lbl_status.configure(text="⏳  Memuat indeks...", fg=WARNING)
        self._btn_search.configure(state="disabled")
        t = threading.Thread(target=self._load_index_worker, daemon=True)
        t.start()

    def _load_index_worker(self):
        try:
            idx = build_index(self.folder)
            self.after(0, self._on_index_ready, idx)
        except Exception as exc:
            self.after(0, self._on_index_error, str(exc))

    def _on_index_ready(self, idx):
        self.index = idx
        n_docs  = len(idx["documents"])
        n_terms = len(idx["vocabulary"])
        self._lbl_status.configure(
            text=f"✓  {n_docs} dokumen  ·  {n_terms} term", fg=SUCCESS)
        self._btn_search.configure(state="normal")
        self._populate_tfidf_table()
        self._entry.focus_set()

    def _on_index_error(self, msg):
        self._lbl_status.configure(text=f"✗  {msg}", fg=DANGER)
        messagebox.showerror("Gagal Memuat Indeks", msg)

    def _change_folder(self):
        path = filedialog.askdirectory(title="Pilih folder dokumen .txt")
        if path:
            self.folder = path
            self._var_folder.set(os.path.abspath(path))
            self.index = None
            self._clear_results()
            self._clear_tfidf_table()
            self._load_index_async()

    # ── TF-IDF table ──────────────────────────────────────────────────────────

    def _populate_tfidf_table(self):
        if self.index is None:
            return
        df   = self.index["tfidf_transposed"].round(4)
        docs = list(df.columns)

        # Define columns: term + one per doc
        cols = ["term"] + docs
        self._tree.configure(columns=cols)

        self._tree.heading("term", text="Term")
        self._tree.column("term", width=130, anchor="w", stretch=False)

        for doc in docs:
            short = doc.replace(".txt", "")[:12]
            self._tree.heading(doc, text=short)
            self._tree.column(doc, width=90, anchor="center", stretch=False)

        # Insert rows
        for i, (term, row) in enumerate(df.iterrows()):
            tag   = "even" if i % 2 == 0 else "odd"
            vals  = [f"{v:.4f}" if v > 0 else "·" for v in row]
            self._tree.insert("", "end", values=[term] + vals, tags=(tag,))

        n = len(df)
        self._lbl_vocab.configure(
            text=f"{n} term  ·  {len(docs)} dokumen  ·  scroll horizontal untuk semua kolom")

    def _clear_tfidf_table(self):
        for row in self._tree.get_children():
            self._tree.delete(row)
        self._lbl_vocab.configure(text="")

    # ── Search ────────────────────────────────────────────────────────────────
    def _do_search(self):

        if self.index is None:
            messagebox.showwarning(
                "Indeks Belum Siap",
                "Tunggu hingga indeks selesai dimuat."
            )
            return

        query = self._var_query.get().strip()

        if not query:
            return

        # ==========================================
        # SEARCH RESULTS
        # ==========================================

        results = search(query, self.index)

        # ==========================================
        # NEXT WORD PREDICTION
        # ==========================================

        predictions = predict_next(query, self.index)

        # ==========================================
        # RENDER BOTH
        # ==========================================

        self._render_results(query, results, predictions)



    def _update_token_preview(self, *_):
        if self.index is None:
            return
        from search_engine import preprocess
        query  = self._var_query.get().strip()
        tokens = preprocess(query) if query else []
        if tokens:
            self._lbl_tokens.configure(text="  ".join(tokens), fg=ACCENT2)
        else:
            self._lbl_tokens.configure(text="—", fg=TEXT_SEC)

    # ── Results rendering ─────────────────────────────────────────────────────

    def _clear_results(self):
        for w in self._results_inner.winfo_children():
            w.destroy()

    def _show_placeholder(self):
        self._clear_results()
        tk.Label(self._results_inner,
                 text="\n\n\n🔍\n\nKetik query dan tekan  Cari  atau  Enter",
                 bg=BG_DARK, fg=TEXT_MUTED,
                 font=("Segoe UI", 11), justify="center").pack(pady=40)

    def _render_results(self, query: str, results: list, predictions: list):
        self._clear_results()

        if not results:
            tk.Label(self._results_inner,
                     text=f'\n\nTidak ada dokumen yang cocok\nuntuk query: "{query}"',
                     bg=BG_DARK, fg=TEXT_SEC,
                     font=("Segoe UI", 10), justify="center").pack(pady=40)
            return

        # Header summary
        hdr = tk.Frame(self._results_inner, bg=BG_DARK, pady=4)
        hdr.pack(fill="x", pady=(0, 8))

        # ==================================================
        # NEXT WORD PREDICTIONS PANEL
        # ==================================================

        pred_card = tk.Frame(
            self._results_inner,
            bg=BG_PANEL,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        pred_card.pack(fill="x", pady=(0, 10))

        pred_inner = tk.Frame(pred_card, bg=BG_PANEL, padx=14, pady=10)
        pred_inner.pack(fill="x")

        tk.Label(
            pred_inner,
            text="PREDIKSI KATA BERIKUTNYA",
            bg=BG_PANEL,
            fg=ACCENT,
            font=("Segoe UI Semibold", 9)
        ).pack(anchor="w")

        if not predictions:

            tk.Label(
                pred_inner,
                text="Tidak ada prediksi tersedia.",
                bg=BG_PANEL,
                fg=TEXT_SEC,
                font=FONT_UI
            ).pack(anchor="w", pady=(6, 0))

        else:

            # Wadah prediksi yang bisa di-scroll horizontal (kiri-kanan)
            # bila jumlah prediksi melebihi lebar panel.
            pred_wrap = tk.Frame(pred_inner, bg=BG_PANEL)
            pred_wrap.pack(fill="x", pady=(8, 0))

            pred_canvas = tk.Canvas(pred_wrap, bg=BG_PANEL, height=54,
                                    highlightthickness=0)
            pred_hsb = ttk.Scrollbar(pred_wrap, orient="horizontal",
                                     command=pred_canvas.xview)
            pred_canvas.configure(xscrollcommand=pred_hsb.set)

            pred_canvas.pack(side="top", fill="x")
            pred_hsb.pack(side="bottom", fill="x")

            # Frame dalam canvas tempat item-item prediksi disusun
            pred_row = tk.Frame(pred_canvas, bg=BG_PANEL)
            pred_canvas.create_window((0, 0), window=pred_row, anchor="nw")

            for i, (word, prob) in enumerate(predictions, 1):

                item = tk.Frame(
                    pred_row,
                    bg=BG_INPUT,
                    padx=10,
                    pady=6,
                    highlightbackground=BORDER,
                    highlightthickness=1
                )

                item.pack(side="left", padx=(0, 8))

                tk.Label(
                    item,
                    text=word,
                    bg=BG_INPUT,
                    fg=ACCENT2,
                    font=("Segoe UI Semibold", 10)
                ).pack()

                tk.Label(
                    item,
                    text=f"{prob:.3f}",
                    bg=BG_INPUT,
                    fg=TEXT_MUTED,
                    font=FONT_SMALL
                ).pack()

            # Perbarui area scroll setelah semua item terpasang
            pred_row.bind(
                "<Configure>",
                lambda _e, _c=pred_canvas: _c.configure(
                    scrollregion=_c.bbox("all"))
            )

            # Scroll horizontal dengan Shift + roda mouse
            pred_canvas.bind(
                "<Shift-MouseWheel>",
                lambda e, _c=pred_canvas: _c.xview_scroll(
                    int(-1 * (e.delta / 120)), "units")
            )

        tk.Label(hdr, text=f"{len(results)} dokumen ditemukan",
                 bg=BG_DARK, fg=SUCCESS, font=FONT_HEAD).pack(side="left")
        tk.Label(hdr, text=f'  untuk  "{query}"',
                 bg=BG_DARK, fg=TEXT_SEC, font=FONT_UI).pack(side="left")

        max_score = results[0][1] if results else 1.0

        for rank, (doc, score) in enumerate(results, 1):
            self._render_result_card(rank, doc, score, max_score)

    def _render_result_card(self, rank: int, doc: str, score: float, max_score: float):
        color = similarity_color(score)

        card = tk.Frame(self._results_inner, bg=BG_PANEL,
                        highlightbackground=color if rank == 1 else BORDER,
                        highlightthickness=1 if rank == 1 else 1)
        card.pack(fill="x", pady=3)

        inner = tk.Frame(card, bg=BG_PANEL, padx=14, pady=10)
        inner.pack(fill="x")

        # Rank badge + doc name
        top_row = tk.Frame(inner, bg=BG_PANEL)
        top_row.pack(fill="x")

        badge_bg = ACCENT if rank == 1 else BG_INPUT
        badge_fg = BG_DARK if rank == 1 else TEXT_SEC
        tk.Label(top_row, text=f" #{rank} ",
                 bg=badge_bg, fg=badge_fg,
                 font=("Segoe UI Semibold", 9)).pack(side="left", padx=(0, 8))

        tk.Label(top_row, text=doc,
                 bg=BG_PANEL, fg=TEXT_PRI,
                 font=("Consolas", 10)).pack(side="left")

        tk.Label(top_row, text=f"{score:.4f}",
                 bg=BG_PANEL, fg=color,
                 font=("Segoe UI Semibold", 10)).pack(side="right")

        # Progress bar
        bar_row = tk.Frame(inner, bg=BG_PANEL)
        bar_row.pack(fill="x", pady=(6, 0))

        bar_bg = tk.Frame(bar_row, bg=BG_INPUT, height=6)
        bar_bg.pack(fill="x")
        bar_bg.pack_propagate(False)

        pct = score / max_score if max_score > 0 else 0

        def draw_bar(event, _bar_bg=bar_bg, _pct=pct, _color=color):
            w = _bar_bg.winfo_width()
            fill_w = max(4, int(w * _pct))
            fill = tk.Frame(_bar_bg, bg=_color, height=6, width=fill_w)
            fill.place(x=0, y=0)

        bar_bg.bind("<Configure>", draw_bar)

        # Similarity label
        tk.Label(inner, text=f"Cosine Similarity: {score:.4f}  ({score*100:.1f}%)",
                 bg=BG_PANEL, fg=TEXT_MUTED,
                 font=FONT_SMALL).pack(anchor="w", pady=(4, 0))

    # ── Canvas helpers ────────────────────────────────────────────────────────

    def _on_results_configure(self, _event):
        self._results_canvas.configure(
            scrollregion=self._results_canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self._results_canvas.itemconfig(
            self._canvas_window, width=event.width)


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "documents"
    app = SearchEngineApp(folder=folder)
    app.mainloop()
