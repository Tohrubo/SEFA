"""
search_engine.py
================
Mesin Pencari TF-IDF - Bahasa Indonesia
(TF-IDF Search Engine for Indonesian documents)

HOW TO RUN:
    python search_engine.py                  # uses ./documents/ folder
    python search_engine.py path/to/folder   # custom folder

INSTALL DEPENDENCIES:
    pip install scikit-learn pandas numpy nltk PySastrawi

INDEX STRUCTURE (returned by build_index)
-----------------------------------------
{
  "documents"        : list[str]
      Daftar nama file dokumen (.txt) yang ditemukan di folder.
      e.g. ["teknologi_01.txt", "ekonomi_01.txt", ...]

  "vocabulary"       : list[str]
      Daftar terurut semua term unik yang lolos pre-processing
      dari seluruh dokumen.

  "tf"               : dict[str, dict[str, float]]
      tf[nama_doc][term] = frekuensi term mentah untuk dokumen tsb.
      Raw TF = jumlah(term di doc) / total_token(doc)

  "df"               : dict[str, int]
      df[term] = jumlah dokumen yang mengandung term tersebut.

  "idf"              : dict[str, float]
      idf[term] = log((1+N)/(1+df[term])) + 1   (rumus smooth sklearn)
      N = total jumlah dokumen.

  "tfidf_matrix"     : scipy.sparse matrix  shape (n_docs x n_terms)
      Matriks TF-IDF sparse dari TfidfVectorizer.

  "feature_names"    : np.ndarray  shape (n_terms,)
      Label term yang berkorespondensi dengan kolom tfidf_matrix.

  "vectorizer"       : TfidfVectorizer (sudah di-fit)
      Digunakan ulang untuk mentransformasi query ke ruang TF-IDF.

  "tfidf_df"         : pd.DataFrame  shape (n_docs x n_terms)
      DataFrame padat - baris = dokumen, kolom = term.

  "tfidf_transposed" : pd.DataFrame  shape (n_terms x n_docs)
      TRANSPOSE dari tfidf_df.
      baris = term/token, kolom = nama dokumen.
      Inilah tabel yang ditampilkan pada tugas.
}
"""

import os
import re
import math
import sys
import pandas as pd
import numpy as np

from nltk.util import ngrams
from collections import Counter


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =============================================================================
# STOPWORDS BAHASA INDONESIA
# =============================================================================

_STOPWORDS_ID_BUILTIN = {
    "ada","adalah","adanya","adapun","agak","agaknya","agar","akan","akankah",
    "akhir","akhiri","akhirnya","aku","akulah","amat","amatlah","anda","andalah",
    "antar","antara","antaranya","apa","apaan","apabila","apakah","apalagi",
    "apatah","artinya","asal","asalkan","atas","atau","ataukah","ataupun",
    "awal","awalnya","bagai","bagaikan","bagaimana","bagaimanapun","bagaimankah",
    "bagaimanakah","bagi","bagian","bahkan","bahwa","bahwasanya","baik","bakal",
    "bakalan","balik","banyak","bapak","baru","bawah","beberapa","begini",
    "begininya","begitu","begitukah","begitupun","belakang","belum","belumlah",
    "benar","benarkah","benarnya","beri","berikan","berikut","berikutnya",
    "bersama","bisa","bisakah","biasanya","bila","bilakah","bukan","bukankah",
    "bukanlah","bukannya","cara","caranya","cukup","cukupkah","cukuplah",
    "dah","dalam","dan","dapat","dari","daripada","datang","dekat","demi",
    "demikian","demikianlah","dengan","depan","di","dia","diantara","diantaranya",
    "diri","dirinya","disini","disinilah","dong","dulu","enggak","enggaknya",
    "entah","entahlah","guna","gunakan","hal","hampir","hanya","hanyalah",
    "hari","harus","haruslah","harusnya","hendak","hendaklah","hendaknya",
    "hingga","ia","ibaratkan","ibaratnya","ibu","ikut","ingat","ini","inikah",
    "inilah","itu","itukah","itulah","jadi","jadilah","jadinya","jangan",
    "jangankan","janganlah","jauh","jelas","jelaskan","jelaslah","jelasnya",
    "jika","jikalau","juga","jumlah","jumlahnya","justru","kala","kalau",
    "kalaulah","kalaupun","kalian","kami","kamilah","kamu","kamulah","kan",
    "kapan","kapankah","kapanpun","karena","karenanya","kata","ke","keadaan",
    "kebetulan","kemudian","kenapa","kepada","kepadanya","ketika","khususnya",
    "kini","kinilah","kiranya","kita","kitalah","kok","kurang","lagi","lagian",
    "lah","lain","lainnya","lalu","lama","lamanya","langsung","lebih","lewat",
    "luar","maka","makanya","makin","malah","malahan","manapun","masa","masih",
    "masihkah","masing","masingnya","mau","maupun","melainkan","melalui",
    "memang","meski","meskipun","misalkan","misalnya","mu","mula","mulai",
    "mulailah","mulanya","mungkin","mungkinkah","nah","namun","nanti",
    "nantinya","nyaris","nyatanya","oleh","olehnya","pada","padahal","paling",
    "pasti","pastilah","pastinya","pernah","perlu","perlukah","perlunya",
    "pertama","pertamanya","pihak","pula","pun","punya","rasa","rasanya",
    "rupanya","saat","saatnya","saja","sajalah","saling","sama","sambil",
    "sampai","sampainya","sana","sangat","sangatlah","satu","saya","sayalah",
    "se","sebab","sebabnya","sebelum","sebelumnya","sebenarnya","sebesar",
    "sebuah","secara","sedang","sedangkan","sedikit","segala","segalanya",
    "segera","sejak","sejauh","sejenak","sekali","sekarang","sekiranya",
    "selain","selalu","selama","seluruh","seluruhnya","semua","semuanya",
    "sendiri","seperti","seringkali","serta","siapa","siapakah","siapapun",
    "sini","sinilah","soal","soalnya","sudah","sudahkah","sudahlah","supaya",
    "tadi","tadinya","tahu","tahukah","tahun","tapi","terus","terutama",
    "tetapi","tidak","tidakkah","tidaklah","tiap","tiba","tibanya","tinggal",
    "tentang","tentu","tentulah","tentunya","tersebut","tersebutlah","tiada",
    "toh","untuk","usah","usahlah","waktu","waktunya","walaupun","ya","yaitu",
    "yakin","yakni","yang",
}


# =============================================================================
# STEMMER BAHASA INDONESIA
# =============================================================================

try:
    from Sastrawi.Stemmer.StemmerFactory import StemmerFactory as _SastrawiFactory
    _sastrawi_stemmer = _SastrawiFactory().create_stemmer()

    class _IndonesianStemmer:
        """Wrapper PySastrawi (pilihan utama)."""
        def stem(self, word):
            return _sastrawi_stemmer.stem(word)

    _USE_SASTRAWI = True

except ImportError:
    _USE_SASTRAWI = False

    class _IndonesianStemmer:
        """
        Stemmer fallback berbasis aturan untuk Bahasa Indonesia.
        Menangani imbuhan umum:
          Prefiks : me(N)-, ber-, di-, ter-, ke-, pe(N)-, se-
          Sufiks  : -kan, -an, -i, -lah, -kah, -pun, -nya
        Tidak seakurat PySastrawi, cukup untuk tugas IR dasar.
        Install PySastrawi untuk akurasi lebih baik: pip install PySastrawi
        """
        _prefixes = [
            "memperlakukan","mempermasalah","memperbesar","memperindah",
            "memperkenalkan","memper","memberikan","memberi","membantu",
            "membuat","memiliki","menyampaikan","menyebabkan","menggunakan",
            "mengemukakan","mengembangkan","mengakhiri","mengajukan",
            "menge","meng","men","mem","me",
            "pengembangan","penggunaan","pengajaran","pengaruh",
            "penge","peng","pen","pem","pe",
            "berdasarkan","berdampak","berkembang","berlangsung",
            "ber","ter","ke","di","se",
        ]
        _suffixes = ["kan","lah","kah","pun","nya","an","i"]

        def stem(self, word):
            w = word
            for s in self._suffixes:
                if w.endswith(s) and len(w) - len(s) >= 3:
                    w = w[: -len(s)]
                    break
            for p in self._prefixes:
                if w.startswith(p) and len(w) - len(p) >= 3:
                    w = w[len(p):]
                    break
            return w if len(w) >= 3 else word


_stemmer = _IndonesianStemmer()


# =============================================================================
# NLTK stopwords (tambahan jika tersedia)
# =============================================================================

_USE_NLTK = False
try:
    import nltk
    for _pkg, _kind in [("stopwords","corpora"),("punkt","tokenizers"),("punkt_tab","tokenizers")]:
        try:
            nltk.data.find(f"{_kind}/{_pkg}")
        except LookupError:
            nltk.download(_pkg, quiet=True)
    from nltk.corpus import stopwords as _nltk_sw
    try:
        _STOPWORDS = set(_nltk_sw.words("indonesian")) | _STOPWORDS_ID_BUILTIN
        _USE_NLTK  = True
    except OSError:
        _STOPWORDS = _STOPWORDS_ID_BUILTIN
except ImportError:
    _STOPWORDS = _STOPWORDS_ID_BUILTIN

# Print status at startup
if not _USE_SASTRAWI:
    print("[INFO] PySastrawi tidak ditemukan - menggunakan stemmer fallback.")
    print("[INFO] Untuk hasil optimal: pip install PySastrawi\n")
if not _USE_NLTK:
    print("[INFO] NLTK tidak ditemukan - menggunakan daftar stopword bawaan.")
    print("[INFO] Untuk hasil optimal: pip install nltk\n")


# =============================================================================
# 1.  PRE-PROCESSING
# =============================================================================

def preprocess(text):
    """
    Simple preprocessing for:
    - TF-IDF Search
    - N-Gram Query Prediction
    """

    text = text.lower()

    # keep letters, numbers, spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    tokens = text.split()

    return tokens




def preprocess_to_string(text):
    """Pre-process teks dan kembalikan sebagai string dipisah spasi."""
    return " ".join(preprocess(text))


# =============================================================================
# 2.  TERM FREQUENCY
# =============================================================================

def compute_tf(token_list):
    """
    Raw TF untuk satu dokumen.
    tf(t, d) = jumlah(t di d) / total_token(d)
    """
    total = len(token_list)
    freq  = {}
    for t in token_list:
        freq[t] = freq.get(t, 0) + 1
    return {t: c / total for t, c in freq.items()} if total else {}


# =============================================================================
# 3.  DOCUMENT FREQUENCY
# =============================================================================

def compute_df(tf_all):
    """
    df[term] = jumlah dokumen yang mengandung term tersebut.
    tf_all : { nama_doc: { term: nilai_tf, ... }, ... }
    """
    df = {}
    for doc_tf in tf_all.values():
        for term in doc_tf:
            df[term] = df.get(term, 0) + 1
    return df


# =============================================================================
# 4.  BUILD INDEX
# =============================================================================

def build_index(folder_path):
    """
    Baca setiap file .txt di folder_path, jalankan pre-processing,
    dan bangun indeks TF-IDF lengkap.
    Lihat docstring modul untuk deskripsi lengkap struktur indeks.
    """
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder tidak ditemukan: '{folder_path}'")

    txt_files = sorted(f for f in os.listdir(folder_path) if f.endswith(".txt"))
    if not txt_files:
        raise ValueError(f"Tidak ada file .txt di: '{folder_path}'")

    processed_tokens  = {}
    processed_strings = {}

    print(f"  Membaca {len(txt_files)} dokumen...")
    for fname in txt_files:
        path = os.path.join(folder_path, fname)
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            raw = fh.read()
        tokens = preprocess(raw)
        processed_tokens[fname]  = tokens
        processed_strings[fname] = " ".join(tokens)

    # ==========================================================
    # BUILD GLOBAL TOKEN LIST FOR LANGUAGE MODEL
    # ==========================================================

    # ==========================================================
    # CHARACTER N-GRAM INDEX FOR QUERY PREDICTION
    # ==========================================================

    word_ngram_index = {}

    # vocabulary later comes from feature_names

    # TF
    tf = {doc: compute_tf(tokens) for doc, tokens in processed_tokens.items()}

    # DF
    df = compute_df(tf)

    # IDF (smooth sklearn: log((1+N)/(1+df)) + 1)
    N   = len(txt_files)
    idf = {term: math.log((1 + N) / (1 + cnt)) + 1 for term, cnt in df.items()}

    # TF-IDF via sklearn TfidfVectorizer
    vectorizer = TfidfVectorizer(
        preprocessor = lambda x: x,
        tokenizer    = lambda x: x.split(),
        smooth_idf   = True,
        sublinear_tf = False,
    )
    corpus        = [processed_strings[f] for f in txt_files]
    tfidf_matrix  = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()

    # ==========================================================
    # BUILD CHARACTER UNIGRAM / BIGRAM / TRIGRAM INDEX
    # ==========================================================

    word_ngram_index = {}

    for word in feature_names:

        grams = set()

        # unigram
        grams.update(
            "".join(g)
            for g in ngrams(word, 1)
        )

        # bigram
        grams.update(
            "".join(g)
            for g in ngrams(word, 2)
        )

        # trigram
        grams.update(
            "".join(g)
            for g in ngrams(word, 3)
        )

        word_ngram_index[word] = grams

    tfidf_dense      = tfidf_matrix.toarray()
    tfidf_df         = pd.DataFrame(tfidf_dense, index=txt_files, columns=feature_names)
    tfidf_transposed = tfidf_df.T

    return {
        "documents"        : txt_files,
        "vocabulary"       : sorted(feature_names.tolist()),
        "tf"               : tf,
        "df"               : df,
        "idf"              : idf,
        "tfidf_matrix"     : tfidf_matrix,
        "feature_names"    : feature_names,
        "vectorizer"       : vectorizer,
        "tfidf_df"         : tfidf_df,
        "tfidf_transposed" : tfidf_transposed,
        "word_ngram_index": word_ngram_index,
    }


# =============================================================================
# 5.  DISPLAY TABEL TF-IDF (TRANSPOSED)
# =============================================================================

def display_tfidf_table(index, max_terms=40, decimals=4):
    """
    Tampilkan tabel TF-IDF transposed (term sebagai baris, dokumen sebagai kolom).
    Dibatasi max_terms baris agar mudah dibaca di konsol.
    """
    df          = index["tfidf_transposed"].round(decimals)
    total_terms = len(df)

    print("\n" + "=" * 72)
    print("  TABEL TF-IDF  (baris = term | kolom = dokumen)")
    print("=" * 72)

    if total_terms > max_terms:
        print(f"  [Menampilkan {max_terms} dari {total_terms} term]\n")
        df = df.head(max_terms)

    short_cols = {c: c[:10] for c in df.columns}
    print(df.rename(columns=short_cols).to_string())
    print("=" * 72 + "\n")


# =============================================================================
# 6.  SEARCH  (query -> TF-IDF -> Cosine Similarity)
# =============================================================================

def search(query, index, top_n=None):
    """
    Pre-proses query, proyeksikan ke ruang TF-IDF, lalu urutkan dokumen
    berdasarkan Cosine Similarity.

    Parameter
    ---------
    query  : string query mentah yang diketik pengguna
    index  : dict yang dikembalikan oleh build_index()
    top_n  : jika diberikan, kembalikan tepat top_n hasil;
             jika None, kembalikan hanya dokumen dengan similarity > 0

    Mengembalikan
    -------------
    list of (nama_doc, similarity) diurutkan dari similarity tertinggi
    """
    vectorizer   = index["vectorizer"]
    tfidf_matrix = index["tfidf_matrix"]
    documents    = index["documents"]

    processed = preprocess_to_string(query)
    if not processed.strip():
        return []

    query_vec    = vectorizer.transform([processed])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    results = [(documents[i], float(similarities[i])) for i in range(len(documents))]
    results.sort(key=lambda x: x[1], reverse=True)

    if top_n is None:
        results = [(d, s) for d, s in results if s > 0.0]
    else:
        results = results[:top_n]

    return results


def display_results(results):
    """Tampilkan hasil pencarian sebagai tabel berurutan."""
    print("\n" + "=" * 52)
    print("  HASIL PENCARIAN")
    print("=" * 52)
    if not results:
        print("  Tidak ada dokumen yang cocok.")
    else:
        print(f"  {'Rank':<6}  {'Dokumen':<28}  {'Similarity':>8}")
        print("  " + "-" * 46)
        for rank, (doc, score) in enumerate(results, 1):
            print(f"  {rank:<6}  {doc:<28}  {score:>8.4f}")
    print("=" * 52 + "\n")


def predict_word(query, index, top_n=5):

    query = query.lower().strip()

    if not query:
        return []

    query_grams = set()

    # unigram
    query_grams.update(
        "".join(g)
        for g in ngrams(query, 1)
    )

    # bigram
    query_grams.update(
        "".join(g)
        for g in ngrams(query, 2)
    )

    # trigram
    query_grams.update(
        "".join(g)
        for g in ngrams(query, 3)
    )

    scores = []

    for word, word_grams in index["word_ngram_index"].items():

        if not word.startswith(query):
            continue

        overlap = len(query_grams.intersection(word_grams))

        scores.append((word, overlap))

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return scores[:top_n]


# =============================================================================
# 7.  INTERACTIVE CLI
# =============================================================================

def run_cli(folder_path):
    """Bangun indeks lalu jalankan loop pencarian interaktif."""
    print("\n" + "=" * 52)
    print("  MESIN PENCARI TF-IDF - BAHASA INDONESIA")
    print("=" * 52)
    print(f"  Folder : {os.path.abspath(folder_path)}")

    index = build_index(folder_path)

    print(f"  Dokumen terindeks : {len(index['documents'])}")
    print(f"  Ukuran kosakata   : {len(index['vocabulary'])} term\n")
    print("  Dokumen dalam indeks:")
    for i, doc in enumerate(index["documents"], 1):
        print(f"    {i:>2}. {doc}")

    display_tfidf_table(index)

    print("Ketik query pencarian (atau 'keluar' / 'q' untuk berhenti).\n")
    while True:
        try:
            query = input("Cari > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSampai jumpa!")
            break

        if query.lower() in ("keluar", "quit", "exit", "q", ""):
            print("Sampai jumpa!")
            break

        # ==========================================
        # SEARCH ENGINE RESULTS
        # ==========================================

        results = search(query, index)
        display_results(results)

        # ==========================================
        # NEXT WORD PREDICTION
        # ==========================================

        predictions = predict_word(query, index)

        print("\n" + "=" * 52)
        print("  PREDIKSI KATA BERIKUTNYA")
        print("=" * 52)

        if not predictions:
            print("  Tidak ada prediksi.")
        else:
            for i, (word, score) in enumerate(predictions, 1):
                print(f"  {i}. {word:<20} Score: {score}")

        print("=" * 52 + "\n")



# =============================================================================
# 8.  ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "/documents"
    run_cli(folder)
