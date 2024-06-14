import pandas as pd
import streamlit as st
import base64
import random
import numpy as np
import time
import string
from pygame.locals import *

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Function to load CSV data
@st.cache_data  # Cache the dataframe for faster access
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()
    
# Function to generate random voucher code
def generate_random_voucher():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def main():
    # Define file paths
    file_path = "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/member.csv"
    logo_path = "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/logo1.jpg"
    sidebar_bg_path = "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/back10.png"
    main_bg_path = "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/back1.png"


    # Load data
    df = load_data(file_path)

    # Convert 'Kode Member' to string and handle NaN values
    df['Kode Member'] = df['Kode Member'].astype(str).fillna('Unknown')

    # Convert logo and background images to base64
    logo_base64 = get_base64_image(logo_path)
    sidebar_bg_base64 = get_base64_image(sidebar_bg_path)
    main_bg_base64 = get_base64_image(main_bg_path)

    # Sidebar logo
    st.sidebar.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sidebar title with background
    st.sidebar.markdown(
        """
        <h1 style='
            text-align: center; 
            font-size: 30px; 
            background-color: #FFC000; 
            padding: 5px; 
            border-radius: 1px;
        '>MENU</h1>
        """, 
        unsafe_allow_html=True
    )

    # Use base64 image data as sidebar background
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{main_bg_base64}');
        background-size: cover;
    }}

    [data-testid="stHeader"]  {{ 
        background-color: rgba(0, 0, 0, 0)
    }}

    [data-testid="stSidebar"] {{
        background-image: url('data:image/png;base64,{sidebar_bg_base64}');
        background-size: cover;
        color: white; /* Change text color on sidebar */
    }}

    /* Bold text in sidebar */
    .css-1d391kg p {{
        font-weight: bold;
    }}

    /* Enlarge and center sidebar title */
    .css-1d391kg h1 {{
        text-align: center;
        font-size: 30px;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Sidebar menu
    menu = st.sidebar.radio("-", ("Data Pembelian", "Katalog Promo", "Katalog Point", "Leaderboard", "Minigames", ))

    # Load unique kode members
    kode_members = sorted(df['Kode Member'].unique())

    if menu == "Data Pembelian":
        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 50px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Data Pembelian</h1>
            """,
            unsafe_allow_html=True
        )

        # Single select box for kode member
        selected_kode_member = st.selectbox("Pilih Kode Member", kode_members)
        st.write("Tampilan data pembelian untuk Kode Member:", selected_kode_member)

        # Filter dataframe based on selected kode member
        filtered_df = df[df['Kode Member'] == selected_kode_member]

        # Display data pembelian
        st.write(filtered_df)

        # Calculate total jumlah belanja and total poin
        total_belanja = filtered_df['Total Belanja'].sum()
        total_point = filtered_df['Point'].sum()

        # Display total jumlah belanja and total poin
        st.write(f"Total Jumlah Belanja: {total_belanja}")
        st.write(f"Total Point: {total_point}")

        # Redeem Points
        st.header("Cairkan Point?")
        st.write("Hubungi CS 08XX XXXX XXXX atau Langsung Datangi Toko")

    if menu == "Katalog Point":
        # Load unique kode members
        kode_members = sorted(df['Kode Member'].unique())

        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 20px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Katalog Point</h1>
            """, 
            unsafe_allow_html=True
        )

       # Select a member
        selected_kode_member = st.selectbox("Pilih Kode Member", kode_members)
        filtered_df = df[df['Kode Member'] == selected_kode_member].iloc[0]
        member_name = filtered_df['Nama'] if 'Nama' in filtered_df else 'Unknown'
        total_point = filtered_df['Point'].sum()

        # Display total points
        st.caption(f"total point: {total_point}")

        # Define the points catalog
        katalog = {
            "Topi": {"points": 200, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/image1.jpg"},
            "Totebag": {"points": 400, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/image2.jpg"},
            "Kipas": {"points": 1000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/image3.jpg"},
            "Kompor": {"points": 2000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/image4.jpg"},
            "Macbook M1": {"points": 100000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/image5.jpg"}
        }

        # Select an item from the catalog
        selected_item = st.selectbox("Pilih Barang", list(katalog.keys()))
        required_points = katalog[selected_item]['points']

        # Generate and display the voucher code upon clicking the button
        if st.button("Enter"):
            if total_point >= required_points:
                voucher_code = generate_random_voucher()
                st.markdown(
                    f"""
                    <h2>Kode Voucher</h2>
                    <h1 style='
                        text-align: Left;
                        font-size: 15px; 
                        background-color: #FFC000;
                        padding: 5px; 
                        border-radius: 1px;
                        display: inline-block;
                    '>{voucher_code}</h1>
                    <h2>Barang yang Dipilih</h2>
                    <p><strong>{selected_item}</strong></p>
                    <h2>Kode Member</h2>
                    <p><strong>{selected_kode_member}</strong></p>
                    <h2>Nama Pemilik Kode Member</h2>
                    <p><strong>{member_name}</strong></p>
                    <h1 style='
                        text-align: Left;
                        font-size: 15px; 
                        background-color: #FFC000;
                        padding: 5px; 
                        border-radius: 1px;
                        display: inline-block;
                        margin-bottom: 50px;
                    '>Tunjukan voucher pada CS BR Market di store terdekat (Membawa KTP)</h1>
                    """,

                    unsafe_allow_html=True
                   
            
                )
            else:
                st.warning("Poin Anda tidak cukup untuk menukarkan barang ini.")


        for item, details in katalog.items():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(details["image"], width=150)  # Adjust width as needed
            with col2:
                st.markdown(
                    f"""
                    <div style='display: flex; align-items: center; height: 100%; font-size: 20px;'>
                        {item} - {details['points']} Poin
                    </div>
                    """, 
                    unsafe_allow_html=True
                )


        
    elif menu == "Katalog Promo":
        sembako_katalog = {
            "Beras Jasmine 5 Kg": {"original_price": 84000, "discounted_price": 74000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo1.jpg"},
            "Bimoli 2 L": {"original_price": 58000, "discounted_price": 42000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo2.jpg"},
            "Gulaku 500 Gr": {"original_price": 13000, "discounted_price": 8700, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo3.jpg"},
            "Terigu Segitiga Biru 1 Kg": {"original_price": 18000, "discounted_price": 13000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo4.jpg"},
            "Khong Ghuan": {"original_price": 140000, "discounted_price": 127000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo5.jpg"}
        }

        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 20px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Katalog Promo</h1>
            """, 
            unsafe_allow_html=True
        )
        st.markdown("Berikut adalah daftar barang-barang promo terbatas!!!!:")

        for item, details in sembako_katalog.items():
            st.markdown(
                f"""
                <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                    <div style='flex: 1;'>
                        <img src="data:image/png;base64,{get_base64_image(details['image'])}" width="150">
                    </div>
                    <div style='flex: 2;'>
                        <h3>{item}</h3>
                        <p>Harga Asli: Rp {details['original_price']}</p>
                        <p>Harga Diskon: Rp {details['discounted_price']}</p>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
         # Example "Beli 2 Gratis 1" catalog items with images
        beli_2_gratis_1_katalog = {
            "Pantene PRO-V 70 Ml": {"harga": 21000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/Promo6.jpg"},
            "Kecap Manis Bango 135 Ml": {"harga": 12000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo7.jpg"},
            "Kapal Api Special Mix 360 Gr": {"harga": 35000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo8.jpg"}
        }

        for item, details in beli_2_gratis_1_katalog.items():
            st.markdown(
                f"""
                <div style='display: flex; align-items: center; margin-bottom: 20px;'>
                    <div style='flex: 1;'>
                        <img src="data:image/png;base64,{get_base64_image(details['image'])}" width="150">
                    </div>
                    <div style='flex: 2;'>
                        <h3>{item}</h3>
                        <p>Harga: Rp {details['harga']}</p>
                        <p>Promo: Beli 2 Gratis 1</p>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
    
    elif menu == "Leaderboard":
        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 20px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Leaderboard</h1>
            """, 
            unsafe_allow_html=True
        )
        
        # Calculate the top 5 customers by total points
        top_points = df.groupby('Kode Member').agg({'Point': 'sum', 'Total Belanja': 'sum'}).reset_index()
        top_points = top_points.sort_values(by='Point', ascending=False).head(10)
        st.write("Top 10 Pembeli by Total Points")
        st.write(top_points)

    elif menu == "Minigames":
        st.markdown(
            """
            <h1 style='
                text-align: Left; margin-bottom: 20px;
                font-size: 30px; 
                background-color: #FFC000; 
                padding: 5px; 
                border-radius: 1px;
            '>Minigames</h1>
            """, 
            unsafe_allow_html=True
        )

        def init(post_init=False):
            if not post_init:
                st.session_state.opponent = 'Human'
                st.session_state.win = {'X': 0, 'O': 0}
            st.session_state.board = np.full((3, 3), '.', dtype=str)
            st.session_state.player = 'X'
            st.session_state.warning = False
            st.session_state.winner = None
            st.session_state.over = False

        def computer_player():
            moves = check_available_moves(extra=True)
            if moves:
                i, j = random.choice(moves)
                handle_click(i, j)

        def handle_click(i, j):
            if (i, j) not in check_available_moves(extra=True):
                st.session_state.warning = True
            elif not st.session_state.winner:
                st.session_state.warning = False
                st.session_state.board[i, j] = st.session_state.player
                st.session_state.player = "O" if st.session_state.player == "X" else "X"
                winner = check_win(st.session_state.board)
                if winner:
                    st.session_state.winner = winner

                if st.session_state.opponent == 'Computer' and st.session_state.player == 'X':
                    computer_player()

        def check_available_moves(extra=False) -> list:
            raw_moves = [row for col in st.session_state.board.tolist() for row in col]
            num_moves = [i for i, spot in enumerate(raw_moves) if spot == '.']
            if extra:
                return [(i // 3, i % 3) for i in num_moves]
            return num_moves

        def check_rows(board):
            for row in board:
                if len(set(row)) == 1 and row[0] != '.':
                    return row[0]
            return None

        def check_diagonals(board):
            if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != '.':
                return board[0][0]
            if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1 and board[0][len(board) - 1] != '.':
                return board[0][len(board) - 1]
            return None

        def check_state():
            if st.session_state.winner:
                st.success(f"Congrats! {st.session_state.winner} won the game! 🎈")
            if st.session_state.warning and not st.session_state.over:
                st.warning('⚠️ This move already exists')
            if st.session_state.winner and not st.session_state.over:
                st.session_state.over = True
                st.session_state.win[st.session_state.winner] += 1
            elif not check_available_moves() and not st.session_state.winner:
                st.info(f'It\'s a tie 📍')
                st.session_state.over = True

        def check_win(board):
            for new_board in [board, np.transpose(board)]:
                result = check_rows(new_board)
                if result:
                    return result
            return check_diagonals(board)

        def tic_tac_toe():
            st.write(
                """
                <h1 style='
                    text-align: Left; margin-bottom: 20px;
                    font-size: 20px; 
                    background-color: #FFC111; 
                    padding: 5px; 
                    border-radius: 1px;
                '>Tic Tac Toe</h1>
                """, 
                unsafe_allow_html=True
            )

            if "board" not in st.session_state:
                init()

            reset, score, player, settings = st.columns([0.5, 0.6, 1, 1])
            reset.button('New game', on_click=init, args=(True,))

            with settings.expander('Settings'):
                st.selectbox(
                    'Set opponent',
                    ['Human', 'Computer'],
                    key='opponent',
                    on_change=init,
                    args=(True,),
                )

            for i, row in enumerate(st.session_state.board):
                cols = st.columns([5, 1, 1, 1, 5])
                for j, field in enumerate(row):
                    cols[j + 1].button(
                        field,
                        key=f"{i}-{j}",
                        on_click=handle_click,
                        args=(i, j),
                    )

            check_state()

            score.button(f'❌{st.session_state.win["X"]} 🆚 {st.session_state.win["O"]}⭕')
            player.button(
                f'{"❌" if st.session_state.player == "X" else "⭕"}\'s turn'
                if not st.session_state.winner
                else f'🏁 Game finished'
            )
        

        def main():
    # Define your promotional catalogs
            promo_catalogs = {
                "Beras Jasmine 5 Kg": {"original_price": 84000, "discounted_price": 74000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo1.jpg"},
                "Bimoli 2 L": {"original_price": 58000, "discounted_price": 42000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo2.jpg"},
                "Gulaku 500 Gr": {"original_price": 13000, "discounted_price": 8700, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo3.jpg"},
                "Terigu Segitiga Biru 1 Kg": {"original_price": 18000, "discounted_price": 13000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo4.jpg"},
                "Khong Ghuan": {"original_price": 140000, "discounted_price": 127000, "image": "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/Lampiran/promo5.jpg"}
            }

            # Create an empty container for the slideshow
            image_container = st.empty()

            # Run the slideshow in a loop
            while True:

                # Iterate over each catalog item
                for item, details in promo_catalogs.items():
                    # Display the image with its caption
                    with image_container.container():
                        st.image(details["image"], width=150)
                        st.write(f"**{item}**")
                        st.write(f"Harga Asli: Rp {details['original_price']}")
                        st.write(f"Harga Diskon: Rp {details['discounted_price']}")

                    # Pause for 2 seconds before showing the next catalog item
                    time.sleep(2)

        
        if __name__ == "__main__":
            tic_tac_toe()
        
        if __name__ == "__main__":
            main()

if __name__ == "__main__":
    main()
