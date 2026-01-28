import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Konfigurasi halaman
st.set_page_config(page_title="Display Jadwal Kapal", layout="wide")

# Data dummy jadwal kapal
def generate_dummy_data():
    jadwal = [
        {
            "waktu": "08:30 15-01-2026",
            "dermaga": "Dermaga Utara A1",
            "kapal": "KM Nusantara Express",
            "image": "https://via.placeholder.com/300x200/4A90E2/ffffff?text=KM+Nusantara"
        },
        {
            "waktu": "10:15 15-01-2026",
            "dermaga": "Dermaga Selatan B2",
            "kapal": "KM Samudra Jaya",
            "image": "https://via.placeholder.com/300x200/E24A4A/ffffff?text=KM+Samudra"
        },
        {
            "waktu": "12:45 15-01-2026",
            "dermaga": "Dermaga Timur C3",
            "kapal": "KM Pelita Bahari",
            "image": "https://via.placeholder.com/300x200/4AE290/ffffff?text=KM+Pelita"
        },
        {
            "waktu": "14:20 15-01-2026",
            "dermaga": "Dermaga Barat D4",
            "kapal": "KM Bahtera Sejahtera",
            "image": "https://via.placeholder.com/300x200/E2A04A/ffffff?text=KM+Bahtera"
        },
        {
            "waktu": "16:00 15-01-2026",
            "dermaga": "Dermaga Utara A2",
            "kapal": "KM Mega Indah",
            "image": "https://via.placeholder.com/300x200/9B4AE2/ffffff?text=KM+Mega"
        },
        {
            "waktu": "18:30 15-01-2026",
            "dermaga": "Dermaga Selatan B1",
            "kapal": "KM Kartika Samudera",
            "image": "https://via.placeholder.com/300x200/E24A90/ffffff?text=KM+Kartika"
        }
    ]
    return jadwal

# Sidebar - Konfigurasi
st.sidebar.header("⚙️ Konfigurasi Display")

# Input Title Display
default_title = "Jadwal Keberangkatan Kapal"
title_display = st.sidebar.text_input(
    "Judul Display",
    value=default_title,
    help="Masukkan judul yang akan ditampilkan"
)

# Pilihan Tipe View
tipe_view = st.sidebar.radio(
    "Tipe Tampilan",
    options=["Tabel", "Kolase"],
    help="Pilih cara menampilkan jadwal kapal"
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tips:**\n- Pilih 'Tabel' untuk tampilan list\n- Pilih 'Kolase' untuk tampilan grid dengan gambar")

# Main Content
st.title(title_display)
st.markdown("---")

# Load data
data_jadwal = generate_dummy_data()

# Tampilan berdasarkan tipe view
if tipe_view == "Tabel":
    # Tampilan Tabel
    st.subheader("📋 Daftar Jadwal Kapal")
    
    # Convert ke DataFrame
    df = pd.DataFrame(data_jadwal)
    df_display = df[['waktu', 'dermaga', 'kapal']].copy()
    df_display.columns = ['Waktu', 'Dermaga', 'Nama Kapal']
    
    # Tampilkan tabel dengan styling
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Waktu": st.column_config.TextColumn(
                "Waktu",
                width="medium",
            ),
            "Dermaga": st.column_config.TextColumn(
                "Dermaga",
                width="medium",
            ),
            "Nama Kapal": st.column_config.TextColumn(
                "Nama Kapal",
                width="medium",
            )
        }
    )
    
    # Informasi tambahan
    st.info(f"📊 Total jadwal: **{len(data_jadwal)}** keberangkatan")

else:  # Kolase
    # Tampilan Kolase (2 kolom)
    st.subheader("🚢 Galeri Jadwal Kapal")
    
    # Buat 2 kolom
    cols_per_row = 2
    
    for i in range(0, len(data_jadwal), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j in range(cols_per_row):
            idx = i + j
            if idx < len(data_jadwal):
                kapal = data_jadwal[idx]
                
                with cols[j]:
                    # Card container
                    with st.container():
                        st.image(
                            kapal['image'],
                            use_container_width=True
                        )
                        
                        # Info kapal
                        st.markdown(f"### {kapal['kapal']}")
                        st.markdown(f"**⏰ Waktu:** {kapal['waktu']}")
                        st.markdown(f"**⚓ Dermaga:** {kapal['dermaga']}")
                        st.markdown("---")

    # Informasi tambahan
    st.success(f"🎨 Menampilkan **{len(data_jadwal)}** jadwal dalam mode kolase")

# Footer
st.markdown("---")
st.caption("Display Jadwal Kapal - Sistem Informasi Pelabuhan")
