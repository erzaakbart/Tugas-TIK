import sys
import time
import random
from typing import List, Dict

class VisualNovelGame:
    def __init__(self):
        self.player_name = ""
        self.choices = []
        self.ending = None
        self.inventory = []
        self.health = 100
        self.sanity = 100
        self.knowledge = []
        
    def print_slow(self, text: str, speed: float = 0.02):
        """Menampilkan teks dengan efek slow print"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
    
    def print_scene(self, title: str, description: str):
        """Menampilkan scene dengan judul"""
        print("\n" + "="*60)
        print(f"[ {title} ]")
        print("="*60)
        self.print_slow(description)
    
    def get_choice(self, options: List[str]) -> int:
        """Menampilkan pilihan dan mendapatkan input pemain"""
        print("\n" + "-"*60)
        print("PILIHAN:")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print("-"*60)
        
        while True:
            try:
                choice = int(input("Masukkan pilihan (angka): "))
                if 1 <= choice <= len(options):
                    return choice - 1
                else:
                    print("❌ Pilihan tidak valid! Coba lagi.")
            except ValueError:
                print("❌ Masukkan angka yang valid!")
    
    def show_status(self):
        """Menampilkan status pemain"""
        print("\n" + "━"*60)
        print(f"👤 {self.player_name} | ❤️ Kesehatan: {self.health}/100 | 🧠 Kewarasan: {self.sanity}/100")
        items = ", ".join(self.inventory) if self.inventory else "Kosong"
        print(f"🎒 Inventori: {items}")
        print("━"*60)
    
    def add_item(self, item: str):
        """Menambah item ke inventory"""
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"✨ Anda mengambil: {item}")
    
    def has_item(self, item: str) -> bool:
        """Cek apakah pemain memiliki item"""
        return item in self.inventory
    
    def remove_item(self, item: str):
        """Menghapus item dari inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
    
    def add_knowledge(self, knowledge: str):
        """Menambah pengetahuan"""
        if knowledge not in self.knowledge:
            self.knowledge.append(knowledge)
            print(f"💡 Anda belajar: {knowledge}")
    
    def change_health(self, amount: int):
        """Ubah health"""
        self.health = max(0, min(100, self.health + amount))
        if amount < 0:
            print(f"🔴 Anda terluka! Kesehatan: {self.health}/100")
        else:
            print(f"🟢 Kesehatan pulih! Kesehatan: {self.health}/100")
    
    def change_sanity(self, amount: int):
        """Ubah sanity"""
        self.sanity = max(0, min(100, self.sanity + amount))
        if amount < 0:
            print(f"👻 Kewarasan menurun: {self.sanity}/100")
        else:
            print(f"😌 Kewarasan meningkat: {self.sanity}/100")
    
    def check_game_over(self) -> bool:
        """Cek kondisi game over"""
        if self.health <= 0:
            self.print_scene(
                "GAME OVER - ANDA TEWAS",
                f"\n{self.player_name} tidak mampu bertahan lagi...\n"
                "Kesadaran memudar ke gelap yang abadi..."
            )
            self.ending = "DEATH"
            return True
        
        if self.sanity <= 0:
            self.print_scene(
                "GAME OVER - KEWARASAN HILANG",
                f"\n{self.player_name} tidak lagi membedakan realitas dan fantasi...\n"
                "Pikiran chaos total... tak ada harapan lagi..."
            )
            self.ending = "INSANE"
            return True
        
        return False
    
    def intro(self):
        """Intro game"""
        print("\n")
        print("█" * 60)
        print("█" + " " * 58 + "█")
        print("█" + "   MISTERI DI MANSION TUA   ".center(58) + "█")
        print("█" + "  A Horror Adventure Visual Novel  ".center(58) + "█")
        print("█" + " " * 58 + "█")
        print("█" * 60)
        
        self.print_slow("\n\n🌙 Malam yang kelam, angin berhembus dingin...\n")
        time.sleep(1)
        
        self.player_name = input("👤 Siapa nama Anda? ").strip()
        if not self.player_name:
            self.player_name = "Pemberani"
        
        self.print_scene(
            "SURAT MISTERIUS",
            f"\n{self.player_name}, Anda baru menerima surat dari bibi jauh.\n\n"
            "Bibi yang seharusnya sudah meninggal 10 tahun lalu!\n\n"
            "Surat itu menulis:\n"
            "'Datanglah malam ini. Ada sesuatu penting yang ingin kuberikan.'\n\n"
            "Kini Anda berdiri di depan gerbang besar mansion tua.\n"
            "Cahaya remang terlihat dari jendela lantai atas.\n"
            "Angin membawa bau membusuk dari dalam mansion...\n\n"
            "'Apakah ini benar-benar ide bagus?' pikir Anda."
        )
        time.sleep(2)
    
    def play_game(self):
        """Flow game utama"""
        self.intro()
        self.scene_gate()
    
    def scene_gate(self):
        """Scene di gerbang mansion"""
        self.show_status()
        self.print_scene(
            "GERBANG MANSION TUA",
            f"\n{self.player_name} memandangi gerbang besi karat tinggi.\n"
            "Gerbang terbuka setengah, seperti mengundang.\n"
            "Suara mendesis aneh terdengar dari dalam.\n"
            "Anda bisa melihat 3 jalur masuk yang berbeda dari sini."
        )
        self.change_sanity(-5)
        
        choice = self.get_choice([
            "Masuk langsung dari gerbang utama 🚪",
            "Jelajahi area sekitar gerbang dulu 🔍",
            "Cari jalan alternatif di belakang mansion 👀"
        ])
        
        if choice == 0:
            self.scene_front_path()
        elif choice == 1:
            self.scene_gate_exploration()
        else:
            self.scene_back_path()
    
    def scene_gate_exploration(self):
        """Jelajahi area gerbang"""
        self.print_scene(
            "AREA GERBANG - EKSPLORASI",
            f"\n{self.player_name} berjalan mengelilingi gerbang dengan hati-hati.\n"
            "Di dekat tiang gerbang, ada kotak timah lama.\n"
            "Terbuka setengah, dan di dalamnya gleam sesuatu yang berkilau!"
        )
        
        choice = self.get_choice([
            "Ambil benda berkilau ✨",
            "Baca tulisan di kotak 📝",
            "Abaikan dan masuk saja"
        ])
        
        if choice == 0:
            self.add_item("Kunci Emas Aneh")
            self.add_knowledge("Ada kunci emas - mungkin penting")
        elif choice == 1:
            self.print_slow("\n📝 Tulisannya: 'Untuk membuka yang tersembunyi - dari orang yang peduli'")
            self.add_knowledge("Tulisan misterius di kotak")
        
        self.scene_front_path()
    
    def scene_front_path(self):
        """Masuk dari depan"""
        self.show_status()
        self.print_scene(
            "PINTU UTAMA",
            f"\n{self.player_name} berjalan menuju pintu utama."
            f"\nSetiap langkah membuat suara gemerit di tanah lembab.\n"
            "Di depan pintu ada beberapa benda:\n"
            "- Foto tua dengan satu wajah tergores\n"
            "- Lilin putih di kusen pintu\n"
            "- Pintu setengah terbuka, udara hangat keluar"
        )
        self.change_sanity(-8)
        
        choice = self.get_choice([
            "Ambil foto tua 📸",
            "Ambil lilin putih 🕯️",
            "Ambil keduanya",
            "Langsung masuk tanpa ambil apapun"
        ])
        
        if choice == 0:
            self.add_item("Foto Tua Bergaris")
            self.add_knowledge("Foto ini dari keluargaku - ada yang tergores!")
        elif choice == 1:
            self.add_item("Lilin Putih")
            self.add_knowledge("Lilin putih - mungkin bermanfaat?")
        elif choice == 2:
            self.add_item("Foto Tua Bergaris")
            self.add_item("Lilin Putih")
        
        self.scene_mansion_lobby()
    
    def scene_back_path(self):
        """Jalur belakang"""
        self.show_status()
        self.print_scene(
            "BELAKANG MANSION",
            f"\n{self.player_name} berjalan mengelilingi mansion.\n"
            "Pohon-pohon mati seperti kerangka di malam gelap.\n"
            "Anda menemukan:\n"
            "- Jendela basement yang bisa dimasuki\n"
            "- Pintu belakang tertutup dengan rantai\n"
            "- Kuburan kecil dengan nisan-nisan aneh"
        )
        self.change_sanity(-10)
        
        choice = self.get_choice([
            "Masuk jendela basement 🪟",
            "Cek kuburan lebih dekat ⚰️",
            "Coba buka pintu belakang 🔓",
            "Kembali ke gerbang"
        ])
        
        if choice == 0:
            self.scene_basement_back_entrance()
        elif choice == 1:
            self.scene_graveyardcheck()
        elif choice == 2:
            self.scene_back_door()
        else:
            self.scene_gate()
    
    def scene_mansion_lobby(self):
        """Lobi utama mansion"""
        self.show_status()
        self.print_scene(
            "LOBI MANSION - RUANG MASUK",
            f"\n{self.player_name} masuk ke dalam mansion.\n"
            "Udara dingin menusuk. Furnitur berkarat berserakan.\n"
            "Cahaya remang datang dari beberapa tempat.\n\n"
            "Anda dengar:\n"
            "- Suara langkah di lantai atas\n"
            "- Bisikan pelan dari kamar samping\n"
            "- Tik-tak jam yang acak tempat"
        )
        self.change_sanity(-12)
        
        choice = self.get_choice([
            "Naik ke lantai atas ikuti suara langkah 🪜",
            "Masuk kamar samping yang penuh bisikan 👂",
            "Cari basement dari lobi 🚪",
            "Masuk dapur untuk cari senjata/alat 🔪",
            "Periksa ruangan lain di lobi"
        ])
        
        if choice == 0:
            self.scene_upstairs_corridor()
        elif choice == 1:
            self.scene_side_room()
        elif choice == 2:
            self.scene_basement_door()
        elif choice == 3:
            self.scene_kitchen()
        else:
            self.scene_lobby_exploration()
    
    def scene_lobby_exploration(self):
        """Eksplorasi lobi"""
        self.print_scene(
            "EKSPLORASI LOBI",
            f"\n{self.player_name} memeriksa ruangan lebih teliti.\n"
            "Di dinding ada lukisan-lukisan aneh dan mencolok.\n"
            "Di pojok ada lemari dengan pintu setengah terbuka.\n"
            "Anda bisa melihat barang-barang di dalam!"
        )
        
        choice = self.get_choice([
            "Buka lemari untuk cek isinya 🗄️",
            "Lihat lukisan-lukisan aneh 🖼️",
            "Lanjut jalan"
        ])
        
        if choice == 0 or choice == 1:
            self.print_slow("\n🖼️ Lukisan-lukisan menunjukkan ritual aneh dengan simbol gelap!")
            self.add_knowledge("Ritual dilakukan di mansion ini!")
            self.change_sanity(-10)
        
        self.scene_mansion_lobby()
    
    def scene_upstairs_corridor(self):
        """Koridor lantai atas"""
        self.show_status()
        self.print_scene(
            "LANTAI ATAS - KORIDOR GELAP",
            f"\n{self.player_name} mendaki tangga yang berderit mengerikan.\n"
            "Koridor panjang dengan pintu-pintu di kedua sisi.\n"
            "Cahaya lilin terlihat dari ujung koridor.\n"
            "Suara langkah terus terdengar... tapi dari mana?"
        )
        self.change_sanity(-15)
        
        choice = self.get_choice([
            "Masuk pintu dengan cahaya lilin 🕯️",
            "Buka pintu yang perlahan terbuka 🔓",
            "Paksa buka pintu yang tertutup 💪",
            "Ikuti suara langkah ke ujung koridor 👣",
            "Kembali ke bawah"
        ])
        
        if choice == 0:
            self.scene_light_room()
        elif choice == 1:
            self.scene_mysterious_door()
        elif choice == 2:
            self.scene_forced_door()
        elif choice == 3:
            self.scene_follow_footsteps()
        else:
            self.scene_mansion_lobby()
    
    def scene_light_room(self):
        """Ruang dengan cahaya lilin"""
        self.show_status()
        self.print_scene(
            "KAMAR DENGAN CAHAYA LILIN",
            f"\n{self.player_name} membuka pintu.\n"
            "Ruangan penuh dengan lilin putih dan hitam.\n"
            "Di tempat tidur... ada seseorang yang duduk dengan punggung ke pintu.\n"
            "Itu... bibi Anda! Atau yang terlihat seperti bibi."
        )
        self.change_sanity(-20)
        
        choice = self.get_choice([
            "Tanya 'Bibi?!' dengan keras ❓",
            "Dekati perlahan untuk lihat lebih dekat 👣",
            "Ambil lilin untuk usir kegelapan 🕯️",
            "Mundur dan keluar dari kamar ini 🏃"
        ])
        
        if choice == 0 or choice == 1:
            self.scene_bibi_encounter()
        elif choice == 2:
            self.print_slow("\n🕯️ Saat Anda mengambil lilin...\n"
                          "Sosok itu berputar dengan gerakan yang salah!")
            self.scene_bibi_encounter()
        else:
            self.change_sanity(-8)  # Kecil penalty karena lari
            self.scene_upstairs_corridor()
    
    def scene_bibi_encounter(self):
        """Pertemuan dengan bibi"""
        self.print_scene(
            "HADAPAN DENGAN BIBI",
            f"\nSosok itu berputar... wajahnya pucat dan bermata kosong.\n"
            "'Akhirnya datang juga...' bisik sosok itu.\n"
            "'Aku sudah menunggu puluhan tahun untuk ini.'\n\n"
            "Itu benar-benar bibi Anda... tapi tidak benar-benar hidup!"
        )
        self.change_sanity(-25)
        
        choice = self.get_choice([
            "Tanya apa yang dia inginkan ❓",
            "Tunjukkan foto jika punya 📸",
            "Lari dari kamar! 🏃",
            "Coba komunikasi dengan tenang 💬"
        ])
        
        if choice == 0 or choice == 1:
            self.print_slow("\n'Aku melakukan ritual untuk hidup selamanya...'\n"
                          "'Dan saatnya memindahkanya ke tubuhmu...'\n"
                          "Energi gelap mulai bergerak di ruangan!")
            self.change_sanity(-20)
        
        if choice == 1 and self.has_item("Foto Tua Bergaris"):
            self.print_slow("\nSaat Anda menunjukkan foto...\n"
                          "Wajah bibi berubah... ada kilasan memori!")
            self.change_sanity(-5)
        
        if choice == 2:
            self.change_health(-15)
            self.print_slow("\n🏃 Energi gelap menyerang Anda saat lari!")
            self.change_sanity(-10)
            if self.check_game_over():
                return
            self.scene_upstairs_corridor()
        else:
            self.scene_ritual_climax()
    
    def scene_ritual_climax(self):
        """Klimaks ritual"""
        self.show_status()
        self.print_scene(
            "KLIMAKS - RITUAL DIMULAI!",
            f"\n{self.player_name} merasakan energi gelap yang sangat kuat!\n"
            "Bibi mulai berubah bentuk, tubuhnya transparan dengan cahaya gelap.\n"
            "\nAnda harus membuat keputusan SEKARANG:"
        )
        self.change_sanity(-30)
        
        choice = self.get_choice([
            "Gunakan lilin putih jika punya untuk melawan 🕯️",
            "Gunak foto untuk ingatkan kembali kemanusiaan bibi 📸",
            "Lari menuju basement untuk cari cara hentikan ritual 🏃",
            "Serah diri pada kekuatan gelap 👻"
        ])
        
        if choice == 0 and self.has_item("Lilin Putih"):
            self.remove_item("Lilin Putih")
            self.print_slow("\n🕯️ Cahaya putih membanjiri ruangan!\n"
                          "Bibi berteriak kesakitan dan ritual terganggu!")
            self.scene_secret_basement()
        
        elif choice == 1 and self.has_item("Foto Tua Bergaris"):
            self.print_slow("\n📸 Foto itu... mengingatkan bibi siapa dia!\n"
                          "Sebentar saja, matanya kembali normal!\n"
                          "'Aku... aku apa yang aku lakukan?'")
            self.scene_bibi_redemption()
        
        elif choice == 2:
            self.print_slow("\n🏃 Anda berlari keluar dengan bibi mengejar!")
            self.change_health(-20)
            if self.check_game_over():
                return
            self.scene_basement_door()
        
        else:
            self.print_slow("\nEnerg gelap menerima Anda... tubuh Anda menjadi ringan...")
            self.ending_b_dark_union()
    
    def scene_bibi_redemption(self):
        """Bibi kembali normal sebentar"""
        self.print_scene(
            "MOMEN KEMANUSIAAN",
            f"\nBibi untuk pertama kalinya menoleh sebagai manusia.\n"
            "Air mata mengalir dari matanya.\n"
            "'Aku terjebak... di antara hidup dan mati...\n"
            "'Ritualku salah... aku ingin hidup selamanya tapi malah terperangkap!'\n\n"
            "'Tolong... hentikan ini...'"
        )
        
        choice = self.get_choice([
            "Bantu bibi mencari cara hentikan ritual 💪",
            "Cari basement untuk matikan ritual pusatnya 🚪",
            "Tunggu bibi memberitahu cara membatalkan ritual 👂"
        ])
        
        self.scene_secret_basement()
    
    def scene_secret_basement(self):
        """Basement rahasia dengan ritual center"""
        self.show_status()
        self.print_scene(
            "BASEMENT RAHASIA - JANTUNG RITUAL",
            f"\n{self.player_name} akhirnya sampai ke basement utama.\n"
            "Ada lingkaran besar dengan simbol-simbol kuno!\n"
            "Di tengahnya bersinar kristal hitam yang aneh.\n"
            "Energi gelap berkumpul di sini!\n\n"
            "Ini adalah sumber kekuatan ritual bibi!"
        )
        self.change_sanity(-35)
        
        choice = self.get_choice([
            "Sentuh kristal untuk hentikan ritual ⚡",
            "Baca simbol-simbol untuk batalkan ritual 📖",
            "Hancurkan kristal dengan apa yang ada 💥",
            "Pergi dari sini - terlalu berbahaya 🏃"
        ])
        
        if choice == 0:
            self.print_slow("\n⚡ Saat Anda sentuh kristal...\n"
                          "Semua energi gelap bersatu dalam satu pukulan!\n"
                          "Cahaya putih dan hitam saling bertarung!")
            self.change_health(-20)
            if self.check_game_over():
                return
            self.ending_c_break_curse()
        
        elif choice == 1:
            self.print_slow("\n📖 Anda membaca simbol-simbol dengan suara tinggi...\n"
                          "Ritual itu bergetar... apakah ini akan berhasil?")
            if random.random() > 0.4:
                self.ending_c_break_curse()
            else:
                self.print_slow("\n❌ Simbol salah! Ritual malah lebih kuat!")
                self.ending_b_dark_union()
        
        elif choice == 2:
            self.print_slow("\n💥 Kristal pecah dengan luaran energi dahsyat!")
            self.change_health(-30)
            if self.check_game_over():
                return
            self.ending_c_break_curse()
        
        else:
            self.print_slow("\n🏃 Anda lari tapi energi gelap mengejar!")
            self.change_health(-25)
            self.change_sanity(-20)
            if self.check_game_over():
                return
            self.scene_escape_mansion()
    
    def scene_escape_mansion(self):
        """Pelarian dari mansion"""
        self.show_status()
        self.print_scene(
            "LARI DARI MANSION",
            f"\n{self.player_name} berlari keluar mansion dengan sekuat tenaga!\n"
            "Pintu dan jendela bergetar, seperti mencoba menahan Anda.\n"
            "Energi gelap mengikuti dari belakang...\n"
            "Pintu depan masih jauh! Bisa Anda sampai?"
        )
        
        choice = self.get_choice([
            "Sprint penuh ke depan! 💨",
            "Balik dan hadapi energi gelap! ⚔️",
            "Cari cara lain untuk keluar 🔍"
        ])
        
        if choice == 0:
            self.print_slow("\n💨 Anda berlari dengan segala tenaga!\n"
                          "Pintu depan terbuka lebar... ANDA KELUAR!")
            self.ending_a_escape()
        
        elif choice == 1:
            self.change_health(-40)
            if self.check_game_over():
                return
            self.print_slow("\nAnda kalah lawan energi gelap...")
            self.ending_b_dark_union()
        
        else:
            self.print_slow("\n🔍 Anda cari jendela belakang...\n"
                          "Tapi energi gelap terlalu cepat!")
            self.change_health(-35)
            if self.check_game_over():
                return
            self.ending_b_dark_union()
    
    def scene_mysterious_door(self):
        """Pintu yang terbuka perlahan"""
        self.print_scene(
            "RUANG MUSIK LAMA",
            f"\n{self.player_name} membuka pintu perlahan terbuka.\n"
            "Ini ruang musik klasik dengan piano raksasa.\n"
            "Seolah seseorang baru saja bermain... tombol piano bergetar!"
        )
        self.change_sanity(-8)
        
        choice = self.get_choice([
            "Mainkan piano - ada kombinasi secret? 🎹",
            "Cari di sekitar ruang 🔍",
            "Mundur ke koridor"
        ])
        
        if choice == 0:
            self.print_slow("\n🎹 Anda mainkan nada-nada tertentu...\n"
                          "Pintu rahasia di dinding membuka!")
            self.scene_hidden_library()
        else:
            self.scene_upstairs_corridor()
    
    def scene_hidden_library(self):
        """Perpustakaan tersembunyi"""
        self.show_status()
        self.print_scene(
            "PERPUSTAKAAN TERSEMBUNYI",
            f"\n{self.player_name} masuk ke perpustakaan rahasia!\n"
            "Buku-buku tentang ritual hitam, occult, dan keabadian.\n"
            "Dan... jurnal bibi! Berisi semua detail ritual!"
        )
        self.add_knowledge("Jurnal bibi - ritual untuk hidup selamanya!")
        
        choice = self.get_choice([
            "Baca jurnal secara detail 📖",
            "Ambil buku tentang pembatalan ritual 📚",
            "Cari pintu rahasia lain 🚪",
            "Keluar dan lanjut eksplorasi"
        ])
        
        if choice == 0 or choice == 1:
            self.add_item("Jurnal Bibi")
            self.add_knowledge("Cara membatalkan ritual ada di basement!")
            self.change_sanity(-10)
        
        if choice == 2:
            self.print_slow("\n🚪 Di rak terakhir, ada pintu turun ke basement!")
            self.scene_secret_basement()
        else:
            self.scene_upstairs_corridor()
    
    def scene_forced_door(self):
        """Paksa buka pintu"""
        self.print_scene(
            "RUANG GELAP TOTAL",
            f"\n{self.player_name} paksa membuka pintu dengan susah payah.\n"
            "Di dalam adalah kegelapan total!\n"
            "Anda bisa mendengar... bernafas. Ada sesuatu di sini!"
        )
        self.change_sanity(-25)
        
        choice = self.get_choice([
            "Masuk ke kegelapan! ⚫",
            "Tutup pintu dan lari! 🏃"
        ])
        
        if choice == 0:
            self.print_slow("\n⚫ Kegelapan itu sendiri menyerang Anda!")
            self.change_health(-30)
            if self.check_game_over():
                return
        
        self.scene_upstairs_corridor()
    
    def scene_follow_footsteps(self):
        """Ikuti suara langkah"""
        self.print_scene(
            "MENGIKUTI JEJAK",
            f"\n{self.player_name} mengikuti suara langkah di koridor.\n"
            "Suara itu membawa Anda ke ujung koridor...\n"
            "Ke ruang dengan cahaya lilin!"
        )
        self.scene_light_room()
    
    def scene_side_room(self):
        """Ruang samping di lobi"""
        self.show_status()
        self.print_scene(
            "RUANG SAMPING - RUANG BELAJAR",
            f"\n{self.player_name} membuka pintu ke ruang samping.\n"
            "Ini perpustakaan kecil dengan meja kerja.\n"
            "Ada jurnal terbuka di meja!\n"
            "Foto-foto keluarga di dinding dengan satu orang dalam bayangan."
        )
        self.add_knowledge("Ada jurnal terbuka!")
        
        choice = self.get_choice([
            "Baca jurnal 📖",
            "Lihat foto-foto 📸",
            "Ambil buku occult 📚",
            "Cari pintu tersembunyi 🔍",
            "Kembali ke lobi"
        ])
        
        if choice == 0:
            self.print_slow("\n📖 Jurnal berisi tentang ritual... ritual untuk hidup selamanya!\n"
                          "'Aku akan abadi...' - tulisannya")
            self.add_knowledge("Ritual memerlukan orang lain!")
            self.change_sanity(-15)
            self.add_item("Jurnal Bibi")
        
        elif choice == 1:
            self.print_slow("\n📸 Foto-foto menunjukkan keluarga normal...\n"
                          "Tapi di foto terakhir, ada bayangan di belakang!\n"
                          "Bayangan itu semakin terlihat di setiap foto!")
            self.change_sanity(-12)
        
        elif choice == 2:
            self.add_item("Buku Occult Kuno")
            self.add_knowledge("Buku tentang kontrol entitas gelap")
        
        elif choice == 3:
            self.print_slow("\n🔍 Di rak buku, sesuatu mengilap...\n"
                          "Kunci Emas! Ada petunjuk ke basement!")
            if not self.has_item("Kunci Emas Aneh"):
                self.add_item("Kunci Emas Misterius")
        
        if choice != 4:
            choice2 = self.get_choice([
                "Lanjut eksplorasi sini",
                "Kembali ke lobi"
            ])
            if choice2 == 1:
                self.scene_mansion_lobby()
        else:
            self.scene_mansion_lobby()
    
    def scene_kitchen(self):
        """Dapur mansion"""
        self.print_scene(
            "DAPUR TERPENCIL",
            f"\n{self.player_name} masuk ke dapur yang hangat.\n"
            "Kursi kompor masih panas! Piring setengah termakan!\n"
            "Seolah seseorang baru saja ke luar..."
        )
        self.add_knowledge("Ada orang di mansion sekarang!")
        
        choice = self.get_choice([
            "Ambil pisau dapur untuk senjata 🔪",
            "Ambil botol herbal mencurigakan 🧪",
            "Baca catatan di meja 📝",
            "Cari makanan/minuman 🍞",
            "Keluar dapur"
        ])
        
        if choice == 0:
            self.add_item("Pisau Dapur")
            self.print_slow("\n🔪 Setidaknya Anda punya senjata sekarang.")
        elif choice == 1:
            self.add_item("Botol Herbal")
            self.add_knowledge("Botol ini rasa untuk ritual!")
        elif choice == 2:
            self.print_slow("\n📝 Catatan itu resep... bukan untuk makanan, tapi ritual!")
            self.add_knowledge("Resep ritual ada di sini!")
        elif choice == 3:
            self.print_slow("\n🍞 Makanan terlihat normal tapi rasa tidak enak.")
        
        if choice != 4:
            choice2 = self.get_choice([
                "Lanjut eksplorasi",
                "Keluar dapur"
            ])
            if choice2 == 1:
                self.scene_mansion_lobby()
        else:
            self.scene_mansion_lobby()
    
    def scene_basement_door(self):
        """Pintu basement dari lobi"""
        self.print_scene(
            "PINTU BASEMENT",
            f"\n{self.player_name} menemukan pintu berat di bawah tangga.\n"
            "Dari celah pintu, cahaya merah aneh terlihat.\n"
            "Dan... Anda mendengar bisikan BANYAK suara!"
        )
        self.change_sanity(-10)
        
        choice = self.get_choice([
            "Buka pintu dan masuk 🔓",
            "Nggak berani, kembali itu"
        ])
        
        if choice == 0:
            self.scene_secret_basement()
        else:
            self.scene_mansion_lobby()
    
    def scene_basement_back_entrance(self):
        """Basement dari belakang"""
        self.show_status()
        self.print_scene(
            "BASEMENT - AKSES BELAKANG",
            f"\n{self.player_name} melompat masuk dari jendela basement.\n"
            "Basement gelap dan bau busuk membanjiri hidung!\n"
            "Di pojok ada boneka-boneka tua yang mencolok!\n"
            "Dan... lingkaran sihir dengan cahaya merah!"
        )
        self.change_sanity(-20)
        
        choice = self.get_choice([
            "Dekati boneka 🧸",
            "Dekati lingkaran sihir 🔮",
            "Cari jalan keluar basement 🚪",
            "Hancurkan boneka-bonekanya! 💥"
        ])
        
        if choice == 0:
            self.scene_possessed_dolls()
        elif choice == 1:
            self.scene_secret_basement()
        elif choice == 3:
            self.print_slow("\n💥 Saat Anda coba hancurkan boneka...\n"
                          "Energi gelap meledak dan menyerang!")
            self.change_health(-25)
            self.change_sanity(-20)
            if self.check_game_over():
                return
            self.scene_secret_basement()
        else:
            self.scene_back_path()
    
    def scene_possessed_dolls(self):
        """Boneka-boneka kerasukan"""
        self.print_scene(
            "BONEKA-BONEKA MISTERIUS",
            f"\n{self.player_name} mendekati boneka-boneka aneh.\n"
            "Matanya membuka saat Anda dekat!\n"
            "'Selamat datang...' mereka bisik bersama!\n"
            "'Akhirnya datang korban baru untuk ritual...'"
        )
        self.add_knowledge("Boneka-boneka kerasukan energi gelap!")
        self.change_sanity(-25)
        
        choice = self.get_choice([
            "Tanya boneka tentang ritual ❓",
            "Hancurkan boneka! 💥",
            "Dengarkan apa mereka mau 👂",
            "Lari dari sini! 🏃"
        ])
        
        if choice == 1 or choice == 3:
            self.print_slow("\n💥 Boneka-boneka itu meledak!")
            self.change_health(-20)
            if not self.check_game_over():
                self.scene_secret_basement()
        else:
            self.scene_secret_basement()
    
    def scene_graveyardcheck(self):
        """Periksa kuburan"""
        self.print_scene(
            "KUBURAN KELUARGA",
            f"\n{self.player_name} melihat kuburan kecil dengan nisan-nisan tak jelas.\n"
            "Satu nisan jelas tertulis: 'Bibi Mira - Meninggal 2015'\n\n"
            "Tapi... bibi bilang dia meninggal tahun lalu?\n"
            "ATAU... ada bibi yang lain?\n"
            "Tanah di depan nisan terlihat BARU digali!"
        )
        self.add_knowledge("Bibi meninggal 10 tahun lalu - tapi masih di mansion!")
        self.change_sanity(-20)
        
        choice = self.get_choice([
            "Gali kuburan untuk lihat isinya ⛏️",
            "Cek nisan-nisan lain 🪦",
            "Pergi dari sini"
        ])
        
        if choice == 0:
            self.print_slow("\n⛏️ Anda gali... peti mayat... KOSONG!\n"
                          "Bibi tidak benar-benar di dalam!")
            self.add_knowledge("Kuburan kosong - bibi tidak mati dengan wajar!")
            self.change_sanity(-15)
            self.change_health(-10)
        
        elif choice == 1:
            self.print_slow("\n🪦 Nama-nama di nisan... mereka semua keluargamu!\n"
                          "Bahkan... namamu sendiri ada di sini!\n"
                          "Dengan tahun belum datang!")
            self.change_sanity(-20)
        
        self.scene_back_path()
    
    def scene_back_door(self):
        """Pintu belakang dengan rantai"""
        self.print_scene(
            "PINTU BELAKANG - TERKUNCI RANTAI",
            f"\n{self.player_name} coba buka pintu belakang.\n"
            "Terkunci dengan rantai! Tapi Anda bisa lihat ke dalam.\n"
            "Itu ruangan penyimpanan... full dengan boneka tua!"
        )
        self.change_sanity(-15)
        
        if self.has_item("Kunci Emas Aneh") or self.has_item("Kunci Emas Misterius"):
            choice = self.get_choice([
                "Gunakan kunci emas untuk buka rantai 🔑",
                "Coba cara lain",
                "Abaikan saja"
            ])
            
            if choice == 0:
                self.print_slow("\n✨ Kunci emas berhasil! Rantai terputus!")
                self.scene_doll_storage_room()
            else:
                self.scene_back_path()
        else:
            choice = self.get_choice([
                "Cari cara lain",
                "Pergi dari sini"
            ])
            self.scene_back_path()
    
    def scene_doll_storage_room(self):
        """Ruang penyimpanan boneka"""
        self.show_status()
        self.print_scene(
            "RUANG PENYIMPANAN BONEKA",
            f"\n{self.player_name} bisa masuk ruangan penuh boneka!\n"
            "Ratusan boneka dengan mata yang... hidup?\n"
            "Semua memandang ke arah Anda!"
        )
        self.change_sanity(-25)
        
        choice = self.get_choice([
            "Ambil salah satu boneka 🧸",
            "Cari pintu ke basement dari sini 🚪",
            "Keluar dari ruangan ini 🏃"
        ])
        
        if choice == 0:
            self.add_item("Boneka Bercerita")
            self.print_slow("\n🧸 Boneka yang Anda ambil tiba-tiba berbicara!\n"
                          "'Bibi Mira menginginkanmu...'")
            self.change_sanity(-15)
        
        elif choice == 1:
            self.print_slow("\n🚪 Anda menemukan tangga turun ke basement!")
            self.scene_secret_basement()
            return
        
        self.scene_back_path()
    
    def ending_a_escape(self):
        """Ending A: Selamat tapi Dilacak"""
        self.ending = "A"
        self.print_scene(
            "ENDING A ★ SELAMAT TAPI DILACAK",
            f"\n{self.player_name} berlari keluar mansion dengan terengah-engah.\n"
            "Mansion menghilang dalam kabut tebal di belakang.\n\n"
            "Anda SELAMAT!\n\n"
            "Namun... setiap malam sejak saat itu,\n"
            "Anda mendengar bisikan yang tidak jelas.\n"
            "nama Anda diucapkan dari kegelapan...\n\n"
            "Anda tidak pernah sepenuhnya terlepas dari mansion itu.\n"
            "Kutukan masih merayap di tepi kesadaran Anda.\n\n"
            "Status: HIDUP - Tapi DILACAK selamanya oleh bibi..."
        )
    
    def ending_b_dark_union(self):
        """Ending B: Bersatu dengan Kegelapan"""
        self.ending = "B"
        self.print_scene(
            "ENDING B ★ SATU DENGAN KEGELAPAN",
            f"\nTubuh {self.player_name} menjadi transparan dan ringan...\n"
            "Mata mulai melihat dimensi yang tidak manusiawi.\n"
            "Bibi menyambutmu dengan tangan berubah bentuk.\n\n"
            "'Selamat datang di kehidupan yang sesungguhnya...'\n"
            "'Selamanya, bersama kami...'\n\n"
            "Besoknya, keluargamu menerima surat.\n"
            "Tulisan tangan Anda... tapi bukan dari Anda.\n\n"
            "'Jangan cari dia. Dia sekarang milik kami.'\n\n"
            "Mansion masih berdiri. Menunggu korban berikutnya.\n"
            "Di malam yang gelap, akan ada sosok baru\n"
            "yang terlihat melalui jendela lantai atas..."
        )
    
    def ending_c_break_curse(self):
        """Ending C: Memecah Kutukan"""
        self.ending = "C"
        self.print_scene(
            "ENDING C ★ MEMECAH KUTUKAN!",
            f"\n{self.player_name} berhasil melakukan tindakan tepat!\n\n"
            "Cahaya putih terang membanjiri seluruh mansion!\n"
            "Semua simbol ritual terbakar.\n"
            "Bibi berteriak... suara itu bergetar seluruh bangunan!\n\n"
            "'Tidak! Aku akhirnya... bebas...'\n\n"
            "Energi gelap yang terjebak bertahun-tahun akhirnya dibebaskan.\n"
            "Semua korban mendapat ketenangan.\n"
            "Bibi pun akhirnya bisa beristirahat.\n\n"
            "Pagi harinya, tanpa ingatan jelas,\n"
            "{self.player_name} ditemukan di halaman mansion.\n"
            "Mansion itu sudah runtuh total.\n\n"
            "Kehidupan Anda kembali normal...\n"
            "Meski kadang saat malam sunyi,\n"
            "Anda merasa kehangatan lembut...\n"
            "Seperti bibi Anda berterima kasih...\n\n"
            "Status: KEMENANGAN - Kutukan Berakhir"
        )
    
    def show_ending_info(self):
        """Tunjukkan info ending"""
        endings_desc = {
            "A": "🤫 SELAMAT TAPI DILACAK - Anda bebas tapi tidak benar-benar terlepas",
            "B": "👻 SATU DENGAN KEGELAPAN - Anda menjadi bagian dari kegelapan itu",
            "C": "✨ MEMECAH KUTUKAN - Anda menggakhiri ritual dan menyelamatkan jiwa!",
            "DEATH": "💀 ANDA TEWAS - Tubuh Anda tidak mampu bertahan",
            "INSANE": "🧠 KEWARASAN HILANG - Pikiran Anda terlalu fragmented untuk hidup"
        }
        
        print("\n" + "="*60)
        print("PERMAINAN SELESAI!".center(60))
        print("="*60)
        print(f"\n{endings_desc.get(self.ending, 'UNKNOWN ENDING')}")
        print(f"\n🎬 Ending yang Anda dapatkan: {self.ending}")
    
    def show_stats(self):
        """Tunjukkan statistik"""
        print("\n" + "-"*60)
        print("📊 STATISTIK AKHIR:")
        print("-"*60)
        print(f"Kesehatan Akhir: {self.health}/100")
        print(f"Kewarasan Akhir: {self.sanity}/100")
        print(f"Item Terkumpul: {len(self.inventory)}")
        print(f"Pengetahuan: {len(self.knowledge)}")
        print(f"Total Pilihan: {len(self.choices)}")
        
        if self.inventory:
            print(f"\nItem Terkumpul: {', '.join(self.inventory)}")
        
        if self.knowledge:
            print(f"\nPengetahuan Dikumpulkan:")
            for i, k in enumerate(self.knowledge, 1):
                print(f"  {i}. {k}")
    
    def play(self):
        """Jalankan game"""
        self.play_game()
        
        if self.check_game_over():
            pass
        
        self.show_ending_info()
        self.show_stats()
        
        print("\n" + "="*60)
        print("Terima kasih telah bermain! 👻")
        print("Coba lagi untuk dapatkan ending lain!")
        print("="*60 + "\n")
