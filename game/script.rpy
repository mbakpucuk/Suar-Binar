# Define Characters
define p = Character("Putri", color="#000000", image='putri')
define r = Character("Reza", color="#000000", image='reza')
define i = Character("Ibu", color="#000000", image='ibu')
define s1 = Character("Ibu Pasar1", color="#000000", image='ibupasar1')
define s2 = Character("Ibu Pasar2", color="#000000", image='ibupasar2')
define o = Character("Polisi", color="#000000", image='polisi')
define k = Character("Bapak Kos", color="#000000", image='bapakkos')
define a = Character("???", color="#000000", image='binar')
define b = Character("Binar", color="#000000", image='binar')

# Chara Profile
'''
    TODO: 
    - Replace placeholder images with the real images
    - Fix image position on windows
'''
# Putri
image side putri happy = im.Scale("images/chara/putri/side putri happy.png", 657, 855, xoffset=-180, yoffset=100)
image side putri mikir = im.Scale("images/chara/putri/side putri mikir.png", 657, 855, xoffset=-180, yoffset=100)
image side putri confused = im.Scale("images/chara/putri/side putri confused.png", 657, 855, xoffset=-180, yoffset=100)
image side putri cry = im.Scale("images/chara/putri/side putri cry.png", 657, 855, xoffset=-180, yoffset=100)
image side putri neutral = im.Scale("images/chara/putri/side putri neutral.png", 657, 855, xoffset=-180, yoffset=100)
image side putri smile = im.Scale("images/chara/putri/side putri smile.png", 657, 855, xoffset=-180, yoffset=100)
image side putri conflicted = "images/chara/putri/side putri conflicted.png"
# Ibu
image ibu neutral = "images/chara/ibu/placeholder-ibu.png"
image ibu happy = "images/chara/ibu/placeholder-ibu.png"
image ibu angry = "images/chara/ibu/placeholder-ibu.png"
# Polisi
image polisi neutral = im.Scale("images/chara/polisi/polisi neutral.png", 500, 800)
# Ibu-ibu Pasar
image ibu_pasar 1 = "images/chara/ibu pasar/ibu pasar 1.png"
image ibu_pasar 2 = "images/chara/ibu pasar/ibu pasar 2.png"

# Scene Bg
image bg kamar pagi = "images/bg/bg kamar pagi.png"
image bg kamar malam = "images/bg/bg kamar malam.png"
image bg pasar = im.Scale("images/bg/bar.png", 1920, 1080)
image bg teras = "images/bg/outside.png"
image bg roads = im.Scale("images/bg/roads.jpg", 1920, 1080)

# NVL characters are used for the phone texting
define p_nvl = Character("Putri", kind=nvl, image="putri", callback=Phone_SendSound)
define r_nvl = Character("Reza", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# Chara Points
default moral_points = 0
default courage_point = 0

label start:

    # First Scene
    scene bg kamar pagi with fade
    play sound "pagihari.mp3"

    "{i}Embun pagi yang dingin tidak bisa mengganggu tidur nyenyak Putri yang sedang tergulung di dalam selimutnya, justru hawa dingin itu membuatnya semakin tenggelam dalam pulasnya tidur di hari Minggu.{/i}"
    "{i}Para embun sudah mulai beranjak, digantikan oleh sinar matahari pagi yang berusaha menembus tirai kamar Putri.{/i}"
    
    show ibu neutral
    i "Putri, bangun nak, ini udah siang lho!"
    hide ibu neutral

    "{i}Seketika Putri terbangun. Kepalanya sedikit pusing karena dibangunkan dengan tiba-tiba. Faktanya, jam dinding di hadapan Putri menunjukkan pukul 6 lewat, masih pagi sekali untuk bangun di hari libur seperti ini.{/i}"
    "{i}Dengan malas, Putri melangkah untuk membukakan pintu.{/1}"

    show side putri neutral
    p "Ada apa, Ibu?"
    hide side putri neutral
    
    show ibu neutral
    i "Ibu mau bikin nasi kuning buat sarapan, tapi Ibu lupa telurnya sudah habis. Kamu tolong beliin ke pasar, ya, sekalian bahan-bahan lain buat stok seminggu ke depan."
    "{i}Putri terdiam sejenak.{/i}"

    menu:
        "Patuhi ibu":
            $ moral_points+=1
            jump choice_1a
        "Tidak mengikuti permintaan ibu":
            $ moral_points-=1
            jump choice_2a
        
label choice_1a:
    hide ibu neutral

    "{i}Walaupun Putri masih cukup mengantuk, ia memilih untuk menuruti ibunya.{/i}"

    show side putri neutral
    p mikir "(Kadang, rasanya males banget kalau disuruh pagi-pagi begini.)"
    p "(Tapi... ibu udah capek-capek bangun lebih awal, masak buat keluarga. Masa aku nggak mau bantu sedikit?"
    
    show side putri happy
    p smile "Oke, aku harus beli apa aja nih, Bu?"
    hide side putri happy
    
    show ibu happy
    i "Ini udah ibu tulis biar kamu gak lupa, sana kamu siap-siap dulu."
    hide ibu happy

    show side putri happy
    p "Baik, Bu."
    hide side putri happy

    jump teras_scene

label choice_2a:
    hide ibu neutral

    p "Ih, Bu. Kan masih pagi banget. Kenapa Ibu nggak beli sendiri aja atau minta Ayah? Aku masih ngantuk, tau..."
    
    show ibu angry
    i "Putri! Cara kamu ngomong ke Ibu itu nggak sopan. Kamu pikir Ibu ini siapa, nyuruh-nyuruh kamu tanpa alasan? Ibu bangun pagi-pagi masak buat kalian semua, dan kamu malah membantah?!"
    hide ibu angry

    show side putri conflicted
    p "Tapi, Bu..."
    hide side putri conflicted

    show ibu angry
    i "Nggak ada tapi-tapian! Segera berangkat ke pasar. Ibu nggak mau denger alasan lagi!"
    hide ibu angry

    show side putri conflicted
    p "Iya, iya. Aku berangkat."
    hide side putri conflicted

    "{i}Putri mengambil jaketnya dan berjalan keluar rumah dengan wajah kesal. Selagi melangkah, ia melirik helm yang sedang tergantung. Di benaknya terpikirkan apa ia harus mengenakannya atau tidak.{/i}"

    jump teras_scene

# Second Scene
label teras_scene:
    scene bg teras with fade

    menu:
        "Gunakan helm":
            $ moral_points+=1

            show side putri smile with moveinleft
            "{i}Setelah memakai jaket, Putri mengambil helm dari gantungan dan mengenakannya sebelum ke menyalakan motornya.{/i}"
            p "(Pakai helm itu penting. Nggak cuma soal aturan, tapi buat keselamatan. Kalau terjadi apa-apa di jalan, setidaknya kepala terlindungi.)"
            "{i}Ia mengecek kembali tali helm untuk memastikan terpasang dengan benar.{/i}"
            p "(Kadang orang mikir dekat nggak perlu helm, tapi kecelakaan nggak lihat jarak. Lebih baik aman daripada menyesal.)"
            "{i}Putri menyalakan motor dan melaju ke pasar dengan hati-hati, memastikan dirinya tetap patuh pada aturan lalu lintas.{/i}"
            hide side putri smile
        "Pergi tanpa helm":
            $ moral_points-=2

            show side putri conflicted with moveinleft
            p "(Ah, cuma ke pasar, nggak jauh ini. Lagian nggak ada polisi juga, aman kok)"
            hide side putri conflicted

            scene bg roads with fade
            "{i}Ia menyalakan motor dan melaju. Di tengah perjalanan, tiba-tiba seorang polisi menghentikannya di pos jalan{/i}"
            
            show polisi neutral at right with moveinleft
            o "Selamat pagi. Kenapa Anda tidak memakai helm? Mohon ditunjukkan SIM dan STNK-nya"
            
            show side putri conflicted at left with moveinright
            p "Aduh, Pak. Maaf, tadi saya cuma mau ke pasar, jadi nggak kepikiran pakai helm"

            o "Mau ke mana pun, tetap harus pakai helm. Ini soal keselamatan, bukan soal jarak. Saya akan menilang Anda"

            p "Aduh, Pak. Kalau bisa diselesaikan di sini aja, nggak usah pakai tilang. Saya nggak mau ribet urus tilang ke kantor polisi."

            o "Aturannya jelas. Kalau melanggar, ya ada konsekuensinya"

            "{i}Putri kemudian mengambil uang dari dompetnya dan berbicara dengan pelan{/i}"

            p "Pak, ini aja ya. Biar cepat selesai. Saya nggak mau buang waktu. Mohon pengertiannya"

            "{i}Polisi tersebut tampak ragu, tetapi akhirnya ia menerima uang tersebut.{/i}"

            o "Baiklah, hati-hati dijalan"

            p "Iya, Pak. Terima kasih, ya."

            hide side putri conflicted
            hide polisi neutral

            "{i}Mereka berdua tahu apa yang telah dilakukan salah. Namun bukankah hal tersebut sudah wajar dilakukan di lingkungan sekitarnya? Terjadi perdebatan kecil di kepala Putri. Namun ia memutuskan untuk mengabaikannya dan melanjutkan tugasnya di pasar{/i}"

    jump pasar_scene

# Third Scene
label pasar_scene:
    scene bg pasar with fade

    transform move_right:
        xpos 0.8
        ypos 0.0

    transform move_center:
        xpos 0.5
        ypos 0.5

    "{i}Sesampainya di lokasi, Putri tidak sengaja mendengar percakapan antara ibu-ibu yang juga berbelanja sayur{/i}"

    show ibu_pasar 1 at left with moveinright
    s1 "Kamu inget ga, Bu? Si Ibu yang jualan skincare itu, yang dulunya tinggal di komplek sebelah, kemarin beli barang mahal, katanya aksesoris bermerek atau apalah itu. Padahal katanya lagi susah, kemaren tetangga saya mau minjem 100 katanya lagi ga ada duit. Heran deh, dari mana tuh duitnya"
    
    show ibu_pasar 2 at right with moveinleft
    s2 "Iya, malah saya dengar tuh, anaknya saja sampai kerja sana sini buat cari uang sendiri biar bisa kuliah. Emangnya ibunya ga mau biayain kuliah anak sendiri?"

    "{i}Putri sekilas teringat dengan ibu pacarnya, Reza. Beliau juga berjualan skincare dan sering memamerkan harta yang ia miliki. Mungkin ia perlu berbicara dengan Reza terkait ini.{/i}"

    menu:
        "Diam dan lanjut berbelanja":
            $ courage_point-=1

            hide ibu_pasar 1
            hide ibu_pasar 2

            "{i}Putri memilih diam ketika mendengar gosip tersebut, melanjutkan belanja dan langsung bergegas keluar dari keramaian{/i}"

            show side putri confused
            p "(Kenapa sih mereka ngomongin orang kayak gitu? Rasanya nggak enak banget didengar. Tapi aku juga nggak berani bilang apa-apa. Mereka kan lebih tua dariku)"

            "{i}Putri menyalakan motornya dan mulai perjalanan pulang. Angin pagi membelai lembut wajahnya, tetapi pikirannya tetap gelisah.{/i}"

            p "(Harusnya aku ngomong sesuatu tadi. Tapi gimana caranya ngomong ke orang yang lebih tua tanpa bikin mereka marah atau tersinggung? Aku cuma diem aja, rasanya salah juga...)"

            "{i}Ia melaju pelan, merenungkan kejadian tersebut{/i}"

            p "(Kalau aku terus diem kayak gini, mereka bakal ngerasa nggak salah. Tapi kalau ngomong sembarangan, malah bisa bikin masalah. Aduh, bingung...)"

            "{i}Dengan pikiran yang bercampur aduk, Putri akhirnya sampai di rumah, tapi hatinya masih merasa belum lega dengan kejadian di pasar tadi.{/i}"

            jump house_scene

        "Tegur ibu-ibu itu":
            $ courage_point+=1

            show ibu_pasar 2 at move_right
            show side putri conflicted at left with moveinright

            "{i}Putri berhenti sejenak, merasa tidak nyaman dengan ibu-ibu yang bergosip. Ia menoleh ke arah mereka dan memberanikan diri berbicara{/i}"

            p "Maaf, Bu, bukannya saya sok tahu, tapi sepertinya nggak baik kalau kita membicarakan orang lain seperti ini, apalagi hanya dapat informasi dari sumber yang tidak jelas. Kita kan nggak tahu keadaan sebenarnya."

            "{i}Ibu-ibu itu langsung menghentikan obrolan mereka, menatap Putri dengan ekspresi terkejut dan sedikit tersinggung{/i}"

            s1 "Heh, anak muda. Kamu ini siapa, ya? Baru di sini kok sudah mengatur-ngatur. Anak muda itu harus tahu sopan santun kalau bicara sama orang tua"
            s2 "Iya, jangan sembarangan bicara. Kamu ini ikut campur urusan orang, deh. Anak muda zaman sekarang memang ga ada sopan santun sama orang tua, kurang ajar"

            "{i}Putri ingin menjawab, tetapi bingung bagaimana caranya agar tetap sopan.{/i}"

            p "Saya minta maaf kalau kata-kata saya tadi kurang sopan, Bu. Saya hanya berpikir, kalau kita nggak tahu yang sebenarnya, lebih baik kita tidak membicarakan orang lain. Lagi pula, saya yakin maksud Ibu-Ibu juga bukan untuk hal buruk, kan?"

            "{i}Mereka berdua mengabaikan kata-kata Putri yang akhirnya memutuskan untuk menyelesaikan belanjanya dan pergi. Dalam perjalanan pulang, Putri merenungkan kejadian tadi.{/i}"

            hide ibu_pasar 1
            hide ibu_pasar 2
            hide side putri conflicted

            show side putri cry at move_center
            p "Aku tahu aku benar, tapi kenapa rasanya malah salah? Kadang norma kesopanan bikin susah bilang sesuatu yang penting. Mungkin aku harus belajar cara yang lebih baik untuk bicara ke orang tua..."
            hide side putri cry

            "{i}Putri melanjutkan perjalanan dengan perasaan campur aduk, masih mencoba memahami apa yang baru saja terjadi.{/i}"

    return

label choice_1b:
    #p "" ayam

    scene pasar
    menu:
        "Diam saja":
            jump choice_1c
        "Tegur Ibu-ibu tersebut":
            jump choice_2c

label choice_1c:
    p ""

label choice_2c:


    # This ends the game.


    return
