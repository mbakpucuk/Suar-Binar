define p = Character("Putri", color="#52445b", image='putri')
define r = Character("Reza", color="#52445b", image='reza')
define i = Character("Ibu", color="#52445b", image='ibu')
define s = Character("Ibu-ibu Pasar 1", color="#52445b", image='ibupasarnpc')
define u = Character("Ibu-ibu Pasar 2", color="#52445b", image='ibupasarnpcdua')
define o = Character("Polisi", color="#52445b", image='polisi')
define k = Character("Bapak Kos", color="#52445b", image='bapakkos')
define t = Character("Tetangga 1", color="#52445b", image='tetangganpc')
define q = Character("Tetangga 2", color="#52445b", image='tetangganpcdua')
define x = Character("Tetangga 3", color="#52445b", image='tetangganpctiga')
define v = Character("Tetangga 4", color="#52445b", image='tetangganpcfour')
define a = Character("???", color="#52445b", image='binar')
define b = Character("Binar", color="#52445b", image='binar')
define c = Character("???", color="#52445b")

image side putri happy = im.Scale("images/side putri happy.png", 657, 855, xoffset=-10, yoffset=100)
image side putri mikir = im.Scale("images/side putri mikir.png", 657, 855, xoffset=-10, yoffset=100)
image side putri confused = im.Scale("images/side putri confused.png", 657, 855, xoffset=-10, yoffset=100)
image side putri cry = im.Scale("images/side putri cry.png", 657, 855, xoffset=-10, yoffset=100)
image side putri neutral = im.Scale("images/side putri neutral.png", 657, 855, xoffset=-10, yoffset=100)
image side putri smile = im.Scale("images/side putri smile.png", 657, 855, xoffset=-10, yoffset=100)
image side putri shocked = im.Scale("images/side putri shocked.png", 657, 855, xoffset=-10, yoffset=100)

# NVL characters are used for the phone texting
define p_nvl = Character("Putri", kind=nvl, image="putri", callback=Phone_SendSound)
define r_nvl = Character("Reza", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#splash
label splashscreen:
    scene black
    with Pause(1)

    show text "Kelompok 3 K-26 PKWN 2024 presents" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    stop music fadeout 1.0
    with Dissolve(.5)

    scene bg kamar pagi with dissolve
    with Pause(.5)
    play music "pagihari.mp3"
    "Embun pagi yang dingin tidak bisa mengganggu tidur nyenyak Putri yang sedang tergulung di dalam selimutnya, justru hawa dingin itu membuatnya semakin tenggelam dalam pulasnya tidur di hari Minggu."
    "Para embun sudah mulai beranjak, digantikan oleh sinar matahari pagi yang berusaha menembus tirai kamar Putri."
    
    play sound "ketukpinturamah.mp3"
    #pending
    show ibu neutral
    with Dissolve(1.0)
    i "Putri, bangun nak, ini udah siang lho!"
    hide ibu neutral
    with Dissolve(1.0)

    play sound "nyibakselimut.mp3"
    "Seketika Putri terbangun. Kepalanya sedikit pusing karena dibangunkan dengan tiba-tiba."
    "Faktanya, jam dinding di hadapan Putri menunjukkan pukul 6 lewat, masih pagi sekali untuk bangun di hari libur seperti ini."
    "Dengan malas, Putri melangkah untuk membukakan pintu."
    $ renpy.pause(0.5)
    play sound "bukapintu.mp3"

    p neutral "Ada apa, Ibu?"
    show ibu neutral
    with Dissolve(1.0)
    i "Ibu mau bikin nasi kuning buat sarapan, tapi Ibu lupa telurnya sudah habis."
    i "Kamu tolong beliin ke pasar, ya, sekalian bahan-bahan lain buat stok seminggu ke depan."
    "Putri terdiam sejenak."
    menu:
        "Patuhi ibu":
            jump choice_1a
        "Tidak mengikuti permintaan ibu":
            jump choice_2a

label choice_1a:
    "Walaupun Putri masih cukup mengantuk, ia memilih untuk menuruti ibunya."
    p mikir "(Kadang, rasanya males banget kalau disuruh pagi-pagi begini.)"
    p "(Tapi... ibu udah capek-capek bangun lebih awal, masak buat keluarga. Masa aku nggak mau bantu sedikit?"
    p smile "Oke, aku harus beli apa aja nih, Bu?"
    i "Ini udah ibu tulis biar kamu gak lupa, sana kamu siap-siap dulu."
    p "Baik, Bu."
    "Putri segera mengambil jaketnya dan mengenakannya." 
    "Setelah menerima daftar belanjaan dari Ibu dan menyalaminya untuk berpamitan, Ia melangkah keluar rumah dan menyalakan motornya."
    i "Putri, Ini helmnya jangan lupa dipakai ya!"
    p "Oh iya, makasih ya Bu."
    play sound "helm1.mp3"
    i "Iya, sama-sama. Hati-hati dijalan ya."
    p happy "Siap!"
    hide ibu neutral
    with Dissolve(.5)
    "Putri berpamitan dengan Ibunya dan ia pun mengendarai motornya menuju pasar."
    play sound "motor.mp3"
    jump pasaran

label choice_2a:
    p confused "Ih, Bu. Kan masih pagi banget. Kenapa Ibu nggak beli sendiri aja atau minta Ayah? Aku masih ngantuk, tau..."
    show ibu marah
    with Dissolve(.5)
    with vpunch
    i "Putri! Cara kamu ngomong ke Ibu itu nggak sopan. Kamu pikir Ibu ini siapa, nyuruh-nyuruh kamu tanpa alasan?"
    i "Ibu bangun pagi-pagi masak buat kalian semua, dan kamu malah membantah?!"
    p shocked "Tapi, Bu..."
    i "Nggak ada tapi-tapian! Segera berangkat ke pasar. Ibu nggak mau denger alasan lagi!"
    p mikir "Iya, iya. Aku berangkat."
    hide ibu marah
    with Dissolve(.5)
    "Putri mengambil jaketnya dan berjalan keluar rumah dengan wajah kesal. Selagi melangkah, ia melirik helm yang sedang tergantung. Di benaknya terpikirkan apa ia harus mengenakannya atau tidak."

    scene bg jalan besar with dissolve
    menu:
        "Gunakan helm":
            jump choice_1b
        "Tidak menggunakan helm":
            jump choice_2b

label choice_1b:
    play music "menujupasar.mp3"
    "Setelah memakai jaket, Putri mengambil helm dari gantungan dan mengenakannya sebelum ke menyalakan motornya."
    play sound "helm1.mp3"
    p smile "(Pakai helm itu penting. Nggak cuma soal aturan, tapi buat keselamatan.)"
    p "(Kalau terjadi apa-apa di jalan, setidaknya kepala terlindungi.)"
    "Ia mengecek kembali tali helm untuk memastikan terpasang dengan benar."
    p neutral "(Kadang orang mikir dekat nggak perlu helm, tapi kecelakaan nggak lihat jarak. Lebih baik aman daripada menyesal.)"
    play sound "nyalainmotor.mp3"
    play sound "motor.mp3"
    "Putri menyalakan motor dan melaju ke pasar dengan hati-hati, memastikan dirinya tetap patuh pada aturan lalu lintas."
    jump pasaran

label choice_2b:
    play music "menujupasar.mp3"
    p mikir "(Ah, cuma ke pasar, nggak jauh ini. Lagian nggak ada polisi juga, aman kok.)"
    play sound "nyaalainmotor.mp3"
    play sound "motor.mp3"
    "Ia menyalakan motor dan melaju."
    show bg jalan besar
    with Dissolve(1.0)
    "Di tengah perjalanan, tiba-tiba seorang polisi menghentikannya di pos jalan."
    show polisi
    with Dissolve(1.0)
    o "Selamat pagi. Kenapa Anda tidak memakai helm? Mohon ditunjukkan SIM dan STNK-nya."
    p confused "Aduh, Pak. Maaf, tadi saya cuma mau ke pasar, jadi nggak kepikiran pakai helm."
    o "Mau ke mana pun, tetap harus pakai helm. Ini soal keselamatan, bukan soal jarak."
    o "Saya akan menilang Anda."
    p neutral "Aduh, Pak. Kalau bisa diselesaikan di sini aja, nggak usah pakai tilang. Saya nggak mau ribet urus tilang ke kantor polisi."
    o "Aturannya jelas. Kalau melanggar, ya ada konsekuensinya."
    "Putri kemudian mengambil uang dari dompetnya dan berbicara dengan pelan."
    p "Pak, ini aja ya. Biar cepat selesai. Saya nggak mau buang waktu. Mohon pengertiannya."
    "Polisi tersebut tampak ragu, tetapi akhirnya ia menerima uang tersebut."
    o "Baiklah, hati-hati dijalan."
    p smile "Iya, Pak. Terima kasih, ya."
    hide polisi
    with Dissolve(.5)
    "Mereka berdua tahu apa yang telah dilakukan salah. Namun bukankah hal tersebut sudah wajar dilakukan di lingkungan sekitarnya?" 
    "Terjadi perdebatan kecil di kepala Putri. Namun ia memutuskan untuk mengabaikannya dan melanjutkan tugasnya di pasar."
    play sound "motor.mp3"
    jump pasaran

label pasaran:

    scene bg pasar with dissolve
    with Pause(.5)
    play music "pasar.mp3"
    play sound "crowd.mp3"
    "Sesampainya di lokasi, Putri tidak sengaja mendengar percakapan antara ibu-ibu yang juga berbelanja sayur."
    show ibupasarnpc at left
    with easeinleft
    show ibupasarnpcdua at right
    with easeinright
    s "Kamu inget ga, Bu? Si Ibu yang jualan skincare itu, yang dulunya tinggal di komplek sebelah, kemarin beli barang mahal, katanya aksesoris bermerek atau apalah itu."
    s "Padahal katanya lagi susah, kemaren tetangga saya mau minjem 100 katanya lagi ga ada duit. Heran deh, dari mana tuh duitnya."
    u "Iya, malah saya dengar tuh, anaknya saja sampai kerja sana sini buat cari uang sendiri biar bisa kuliah."
    u "Emangnya ibunya ga mau biayain kuliah anak sendiri?"
    hide ibupasarnpc
    with Dissolve(1.0)
    hide ibupasarnpcdua
    with Dissolve(1.0)
    "Putri sekilas teringat dengan ibu pacarnya, Reza. Beliau juga berjualan skincare dan sering memamerkan harta yang ia miliki."
    "Mungkin ia perlu berbicara dengan Reza terkait ini."

    menu:
        "Diam saja":
            jump choice_1c
        "Tegur Ibu-ibu tersebut":
            jump choice_2c

label choice_1c:
    "Putri memilih diam ketika mendengar gosip tersebut, melanjutkan belanja dan langsung bergegas keluar dari keramaian."
    p shocked "(Kenapa sih mereka ngomongin orang kayak gitu? Rasanya nggak enak banget didengar.)"
    p neutral "(Tapi aku juga nggak berani bilang apa-apa. Mereka kan lebih tua dariku.)"
    scene bg jalan besar
    with Dissolve(1.0)
    "Putri menyalakan motornya dan mulai perjalanan pulang. Angin pagi membelai lembut wajahnya, tetapi pikirannya tetap gelisah."
    p mikir "(Harusnya aku ngomong sesuatu tadi. Tapi gimana caranya ngomong ke orang yang lebih tua tanpa bikin mereka marah atau tersinggung? Aku cuma diem aja, rasanya salah juga...)"
    "Ia melaju pelan, merenungkan kejadian tersebut."
    p "(Kalau aku terus diem kayak gini, mereka bakal ngerasa nggak salah. Tapi kalau ngomong sembarangan, malah bisa bikin masalah. Aduh, bingung...)"
    "Dengan pikiran yang bercampur aduk, Putri akhirnya sampai di rumah, tapi hatinya masih merasa belum lega dengan kejadian di pasar tadi."
    jump rumahkamar


label choice_2c:
    "Putri berhenti sejenak, merasa tidak nyaman dengan ibu-ibu yang bergosip. Ia menoleh ke arah mereka dan memberanikan diri berbicara."
    p confused "Maaf, Bu, bukannya saya sok tahu, tapi sepertinya nggak baik kalau kita membicarakan orang lain seperti ini, apalagi hanya dapat informasi dari sumber yang tidak jelas. Kita kan nggak tahu keadaan sebenarnya."
    show ibupasarnpc at left
    with easeinleft
    show ibupasarnpcdua at right
    with easeinright
    "Ibu-ibu itu langsung menghentikan obrolan mereka, menatap Putri dengan ekspresi terkejut dan sedikit tersinggung."
    with hpunch
    s "Heh, anak muda. Kamu ini siapa, ya? Baru di sini kok sudah mengatur-ngatur."
    s "Anak muda itu harus tahu sopan santun kalau bicara sama orang tua."
    u "Iya, jangan sembarangan bicara. Kamu ini ikut campur urusan orang, deh."
    u "Anak muda zaman sekarang memang ga ada sopan santun sama orang tua, kurang ajar."
    "Putri ingin menjawab, tetapi bingung bagaimana caranya agar tetap sopan."
    p smile "Saya minta maaf kalau kata-kata saya tadi kurang sopan, Bu. Saya hanya berpikir, kalau kita nggak tahu yang sebenarnya, lebih baik kita tidak membicarakan orang lain."
    p "Lagi pula, saya yakin maksud Ibu-Ibu juga bukan untuk hal buruk, kan?"
    "Mereka berdua mengabaikan kata-kata Putri yang akhirnya memutuskan untuk menyelesaikan belanjanya dan pergi."
    hide ibupasarnpc
    with Dissolve(1.0)
    hide ibupasarnpcdua
    with Dissolve(1.0)

    scene bg jalan besar
    with Dissolve (1.0)
    "Dalam perjalanan pulang, Putri merenungkan kejadian tadi."
    p mikir "(Aku tahu aku benar, tapi kenapa rasanya malah salah?)"
    p "(Kadang norma kesopanan bikin susah bilang sesuatu yang penting. Mungkin aku harus belajar cara yang lebih baik untuk bicara ke orang tua...)"
    "Putri melanjutkan perjalanan dengan perasaan campur aduk, masih mencoba memahami apa yang baru saja terjadi."
    jump rumahkamar


label rumahkamar:
    scene bg kamar pagi
    play music "pagihari.mp3"
    with Dissolve(2.0)
    "Sesampainya di rumah, Putri langsung membuka handphonenya untuk menghubungi Reza."
    p_nvl "Reza, hari ini kamu ada waktu luang nggak?"
    r_nvl "Emangnya kenapa, Put, kamu nanya kayak gitu?"
    p_nvl "Aku pengen kita ketemu, aku kangen deh ngobrol sama kamu, udah lama juga kita nggak ketemu."
    r_nvl "Ayo, aku juga kangen pengen liat wajah cantik kamu, kita mau ketemu dimana?"
    p_nvl "Hmm gombal, gimana kalau kita ketemu di kafe kesukaanku?"
    r_nvl "Boleh, aku siap-siap dulu ya, nanti aku jemput kamu."
    stop music
    
    scene bg cafe
    with Dissolve(2.0)
    with Pause(.5)
    play music "cafe.mp3"
    p happy "Reza, senang banget akhirnya bisa ketemu lagi. Udah lama ya kita nggak ngobrol."
    show reza smile kacamata
    with Dissolve(1.0)
    r "Iya, aku juga senang. Maaf ya, akhir-akhir ini aku sibuk banget karena kuliah dan kerja paruh waktu... rasanya nggak ada waktu buat diri sendiri."
    p smile "Aku ngerti kok, pasti berat ya."
    p "Ngomong-ngomong tadi aku tidak sengaja menyimak percakapan ibu-ibu yang sedang belanja di pasar tadi pagi dan sepertinya mereka membicarakan gosip tentang ibumu."
    show reza datar kacamata
    r "Mereka bilang apa, Put?"
    p neutral "Katanya, ibumu baru saja membeli barang yang mahal."
    r "Ternyata beritanya sudah tersebar ya? Sebenarnya Ibu baru saja membeli jam tangan bermerek."
    r "ah, Ibu memang selalu begitu, manajemen keuangannya sangat buruk dan terlalu mementingkan gaya dan tren mewah terkini, tak jarang ia berhutang dan melakukan pinjol sana sini, Bapak pun sama saja."
    r "Makanya aku berinisiatif mencari uang sendiri untuk biaya kuliahku."
    show reza smile kacamata
    r "Kau tau kan biaya kuliah saat ini semakin tidak masuk akal, bahkan untuk kampus negeri, biayanya sudah seperti di kampus swasta."
    "Wajah Reza tersenyum, namun Putri tahu bahwa Reza saat ini sedang tidak baik-baik saja. Ia tidak ingin melihat Reza jadi makin kesusahan karenanya."
    p smile "Reza, kamu nggak perlu khawatir. Hari ini aku yang traktir makan, ya. Aku ngerti kok kalau kamu lagi susah, biar aku bantu sedikit."
    r "Eh, ga usah Put. Kamu juga kan nggak bisa terus-terusan bantu aku."
    r "Aku ngerti kok kalau kondisi aku lagi nggak gampang, tapi aku juga nggak mau kamu ngerasa terbebani. Aku bisa kok bayar sendiri, biar aku yang tanggung jawab."

    menu:
        "Biarkan Reza membayar":
            jump choice_1d
        "Bayar makanannya":
            jump choice_2d

label choice_1d:
    p "Tapi, Reza, kamu kan lagi susah, dan aku bisa bantu. Aku nggak masalah kok."
    r "Putri, aku tau niat kamu baik, tapi aku juga nggak mau kamu terlalu khawatir. Kalau kita terus menerus saling bantu tanpa ada pengertian, malah jadi masalah."
    r "Aku janji, semuanya bisa diatasi. Aku nggak akan biarkan keadaan ini terus menghalangi kita."
    "Putri terdiam sejenak, merasa lega mendengar kata-kata Reza."
    p "Iya, Reza. Aku ngerti. Terima kasih ya, udah bikin aku lebih tenang. Kita memang harus saling support, tapi jangan sampai ada yang merasa terbebani."
    r "Betul banget, kita hadapi ini bareng-bareng. Nggak usah khawatir. Kita akan terus berjalan bersama, oke?"
    p "Oke, Reza."
    "Mereka berdua saling bertukar senyum, merasa lebih nyaman setelah berbicara terbuka dan mencari solusi bersama."
    jump kosan

label choice_2d:
    "Tanpa mendengarkan kata-kata Reza, Putri bergegas menuju kasir."
    "Reza telat menyadarinya dan ketika ia sampai di kasir, transaksinya sudah selesai."
    r "Aduh, kamu nggak perlu repot-repot, aku jadi ngerasa nggak enak."
    p "Gapapa Reza, aku seneng bisa bantu pacar aku."
    r "Terima kasih banyak ya, Put. Aku nggak tau harus bilang apa lagi, kamu baik banget."
    "Putri merasa senang karena bisa membantu Reza meskipun ia tahu ini melawan norma dan kultur sosial ketika biasanya laki-laki yang membayar saat kencan."
    p "(Yah memang ini bukan hal yang biasa, tapi rasanya senang bisa membantu.)"
    jump kosan


label kosan:
    scene bg kos reza gelap
    with Dissolve(1.0)
    play music "kosreza.mp3"
    "Mereka menghabiskan waktu di kos Reza untuk membahas lebih lanjut bahasan mereka tadi."
    "Reza lebih memilih tinggal di kos-kosan daripada harus bolak balik dari kampus ke rumahnya yang berjarak kurang lebih 30 km dari kampusnya, padahal saat SMP dia tinggal di daerah sekitar kampusnya sekarang."
    "Lokasi kos-kosan ini berdempetan dengan rumah warga, menjadikan lingkungan sekitarnya selalu ramai oleh aktivitas warga sekitar."
    "Selain itu, pemilik kosan putra ini cukup ketat dan galak dengan peraturan yang tidak mengizinkan adanya tamu perempuan kecuali keluarga yang bersangkutan."
    "Meskipun begitu, Reza tidak begitu mengindahkan dan tetap mengajak pacarnya ke kamar kos tanpa memberitahu Putri tentang kondisi kosnya tersebut."
    "Mereka berdua pun duduk di tempat tidur dan mengobrol tentang banyak hal lainnya selama hampir 2 jam."
    stop music

    play sound "ketukpintungegas.mp3"
    #nanti ada transisi yang duar gt
    "Tak lama kemudian, terdengar ketukan pintu yang cukup keras."
    "Reza mengintip dari jendela dan mendapati bapak pemilik kosan sedang mengetuk pintu kosnya dengan wajah serius."
    play sound ".mp3"
    "Dengan panik Reza menyuruh Putri untuk sembunyi di bawah kasur."
    "Putri langsung menurut tanpa begitu mengerti apa yang terjadi. Reza kemudian membuka setengah pintu."
    scene bg kos reza terang
    show bapakkos
    with Dissolve(1.0)
    k "Ini saya lihat daritadi ada sandal perempuan di depan kamar kamu. Anak di sebelah tadi juga lapor ke bapak kalo kamar kamu berisik dan dia dengar suara perempuan. Kamu bawa pacar ke kamar ya, hah?"
    "Suara bapak kos yang cukup lantang itu didengar oleh warga sekitar, memancing keingintahuan mereka."
    play sound "bisik.mp3"
    "Bapak kos langsung mendorong paksa Reza yang mencoba menghalangi pintu, tanpa menunggu konfirmasi dari Reza yang tegang membisu."
    play sound "dobrakpintu.mp3" 
    with vpunch
    play sound "jatuh.mp3"
    play music "Heavy_Thrill.mp3"
    "Suara Reza jatuh dan hentakan pintu yang cukup keras membuat warga sekitar yang penasaran langsung mendekat ke depan kamar kos Reza."
    "Sekilas terlihat tidak ada siapa-siapa di kamar itu selain Reza, tetapi bapak kos menyadari ada jari kaki terlihat di ujung bawah kasur. Pada akhirnya, beliau memergoki Putri."
    k "Keluar kamu! Kamu pikir bisa membodohi saya dengan bersembunyi disitu?"
    with hpunch
    "Dengan wajah ketakutan, Putri keluar dari persembunyiannya."
    show bapakkos at left
    with easeinleft
    show reza kaget at right
    with easeinright
    r "Maaf pak, tetapi ini bukan seperti yang bapak pikirkan."
    k "Diam kamu! Saya bisa lihat kasurmu yang berantakan itu. Lagipula kalo kalian ga ngapa-ngapain, kenapa pacar kamu itu harus bersembunyi di bawah kasur?!"
    with hpunch
    k "Ga tahu diri ya kamu, Reza! Sudah selalu bayar kos telat, sekarang kamu malah mengotori citra kosan saya!"
    hide reza kaget
    play sound "tampar.mp3" 
    with vpunch
    play sound "jatuh.mp3"
    #nanti layar goyang
    "Tak mampu membendung amarahnya, beliau lantas memukul Reza hingga terjatuh ke lantai."
    hide bapakkos
    with Dissolve(1.0)
    play sound "gaspbareng.mp3"
    "Beberapa warga yang semula hanya menyaksikan dari depan kamar, kini juga ikut main hakim sendiri dengan mencaci maki Reza dan Putri."
    play sound "bisik.mp3"
    show tetangganpc at left
    with easeinleft
    show tetangganpcdua at right
    with easeinright
    t "ni apa-apaan? Tidak malu kalian, melakukan perbuatan tidak senonoh di sini?!"
    "Kami tau, ini pasti bukan pertama kali kalian seperti ini! Jangan kira kami nggak tau!"
    "Putri terkejut dan tidak tahu harus berbuat apa. Reza bangkit dan mencoba menjelaskan dengan tenang."
    hide tetangganpcdua
    with Dissolve(1.0)
    show reza kaget at right
    with moveinright
    r "Maaf, Bu, Pak. Tidak ada yang seperti itu, kami hanya ngobrol biasa. Tolong jangan terlalu cepat menilai."
    hide reza kaget
    with Dissolve(1.0)
    show tetangganpctiga at right
    with easeinright
    show tetangganpc at left
    with easeinleft
    x "Ah apalagi yang dilakukan cowo cewe dalam kamar kos begitu. Kami sudah cukup muak dengan perbuatan kalian!"
    t "Kurang ajar memang anak muda sekarang! Kasihan bapak kos yang terkenal religius di daerah ini, kalian malah mengotori kos-kosannya. Apa nanti kata orang-orang?"
    hide tetangganpc
    with Dissolve(1.0)
    hide tetangganpctiga
    with Dissolve(1.0)
    play sound "punch2.mp3"
    with vpunch
    $ renpy.pause(.2)
    "Tanpa mendengarkan ucapan Reza, beberapa tetangga langsung mengeroyok Reza, memukulinya secara kasar, sementara Putri hanya bisa terdiam dan melihat dengan perasaan bingung dan takut."
    with vpunch
    p cry "Tolong! Jangan! Apa yang kalian lakukan?!"
    play sound "punch2.mp3"
    $ renpy.pause(.2)
    with vpunch
    play sound "punch2.mp3"
    with vpunch
    # disini layar goyang brp kali
    "Selang beberapa menit, ibu-ibu yang kebetulan lewat melerai mereka."
    show tetangganpcfour
    v "Sudah, berhenti! Kalian ini mau bikin rusuh apa? Apa yang kalian lakukan ini tidak benar!"
    hide tetangganpcfour
    with Dissolve(1.0)
    "Mereka akhirnya mundur dan pergi dengan ekspresi mencibir, sementara Reza tergeletak di lantai, lebam di seluruh wajahnya. Sedikit darah mengalir dari sudut bibirnya dan seketika tidak sadarkan diri."
    show reza babak belur at left
    with Dissolve(1.0)
    show tetangganpcfour at right
    with Dissolve(1.0)
    v "Pak! Apa yang sudah bapak lakukan? Bagaimanapun dia tetap penghuni kos bapak yang harus bapak jaga, bukan malah menyakitinya seperti ini! Cepat bawa dia ke rumah sakit!"
    v "Kamu, pacarnya, cepatlah langsung pulang!"
    hide reza babak belur
    with Dissolve(1.0)
    hide tetangganpcfour
    with Dissolve(1.0)
    "Putri hanya bisa berdiri terpaku, matanya berkaca-kaca, tetapi ia mengangguk dan cepat-cepat pulang."
    "Saat itu yang dipikirkannya hanya nama baiknya dan berharap orang tuanya tidak mendengar kabar ini, tanpa terpikir atau peduli bagaimana nasib Reza setelah ini."
    stop music

    scene bg kamar malam
    with Dissolve(.5)
    "Di rumah, Putri merasa marah, kecewa, dan bingung."
    "Ia memutuskan untuk menjauhi Reza dengan cara memutuskan kontak dengannya, berharap orang-orang segera melupakan kejadian tadi."
    p cry "(Kenapa ini bisa terjadi? Semua ini jadi berantakan gara-gara pertemuan itu! Seharusnya dia bilang dari awal kalau aku tidak boleh kesini!)"
    
    scene sky with dissolve
    with Pause(1)
    "Hari-hari berlalu, dan Putri semakin merasa tertekan."
    "Setiap kali ia keluar dari kamar, orang-orang memandangnya dengan pandangan penuh kecaman, dan orang tuanya pun selalu mengungkit kejadian itu, menyalahkannya."

    scene bg kamar malam with dissolve
    with Pause(1)
    play music "depresi.mp3"
    play sound "bukapintu.mp3"
    show ibu marah
    with Dissolve(1.0)
    i "Kenapa sih kamu bisa terlibat seperti ini, Putri? Kamu tidak berpikir dulu? Kamu tau kan warga di sekitar sini sangat cepat menyebarkan gosip hingga fitnah."
    i "Apa kamu tau Ibu dan Bapak dapat imbasnya juga?!"
    p "Aku cuma ngobrol biasa kok bu, tetangga kos Reza yang tidak berpikir terlebih dahulu dan main hakim sendiri."
    i "Iya tapi tidak baik laki-laki dan perempuan berduaan dalam satu kamar. Apalagi kalian belum menikah."
    hide ibu marah
    with Dissolve(1.0)
    play sound "bukapintu.mp3"
    "Putri merasa semakin terperangkap dalam rasa bersalah dan isolasi."
    "Hingga pada suatu waktu ia mendengar kabar angin bahwa Reza tidak sempat diselamatkan, hatinya semakin hancur."
    p cry "(Ini semua salahku... Kalau saja aku bisa melakukan sesuatu… Kalau saja aku sempat meminta maaf kepadanya sebelum dia pergi untuk selamanya…)"
    "Keadaan mental Putri semakin memburuk."
    "Ia merasa terperangkap dalam perasaan bersalah yang mendalam dan mulai berpikir bahwa mungkin lebih baik mengakhiri semuanya."
    p "(Aku nggak bisa hidup dengan rasa bersalah ini.)"
    p "(Reza... Aku harus meminta maaf padanya. Tapi sekarang sudah terlambat.)"
    p "(Mungkin aku bisa menyusul dia, supaya aku bisa mengatakan semua hal yang belum sempat aku katakan...)"

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

    init: ### just setting variables in advance so there are no undefined variable problems
        $ timer_range = 0
        $ timer_jump = 0
        $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.
        
label questiontime1:
    
    label menu1:
        $ time = 3                                     ### set variable time to 3
        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        show screen countdown                          ### call and start the timer

        menu:
            "Menyerah":
                hide screen countdown
                jump choice_1e
            "Bertahan":
                hide screen countdown
                jump choice_2e

    label menu1_slow:
            jump choice_1e

label choice_1e:
    "BAD ENDING: SUICIDE"

    label badending:
        scene black
        with Pause(1)

        play music "badending.mp3"
        show cg bad ending with dissolve
        with Pause(2)

        scene black with dissolve
        with Pause(1)

    #scene bad ending
    return

label choice_2e:
    "Putri memutuskan untuk berusaha kuat."
    "Malam itu, ia tidak bisa tidur padahal sudah hampir subuh. Pikirannya penuh sementara ia juga berusaha untuk tetap menghilangkan pikiran-pikiran negatif yang tidak mau lepas dari kepalanya."
    "Tiba-tiba cahaya yang terang muncul di depannya."
    show binar
    with Dissolve(2.0)
    "Putri segera menyipitkan matanya karena silau."
    "Beberapa saat setelahnya, Putri terkejut sebab mendapati Makhluk Cahaya yang berwujud samar berdiri di hadapannya."
    a "Putri, apakah kamu yakin tindakanmu itu benar? Apa yang kamu lakukan dengan diri sendiri, dengan perasaanmu, dan dengan kehidupanmu, sudah sesuai dengan jalan yang seharusnya?"
    p mikir "Kamu siapa? Bagaimana kau bisa tahu tentangku?"
    b "Sebut saja aku Binar. Hanya itu yang cukup kamu ketahui tentangku. Sekarang, jawab saja pertanyaanku tadi."
    p "Aku... aku nggak tau. Aku merasa bersalah, aku merasa itu semua salahku. Aku nggak tau harus gimana lagi..."
    b "Tapi, Putri... apapun yang telah terjadi, hidupmu tidak berakhir begitu saja. Ada jalan lain selain kesedihan dan rasa bersalah."
    b "Kamu bisa memilih untuk hidup, untuk mengatasi rasa sakit ini dan memaafkan dirimu sendiri."

    menu:
        "Tidak setuju":
            jump choice_1f
        "Setuju":
            jump choice_2f

label choice_1f:
    p shocked "Tapi kenapa semuanya harus berakhir begini? Kenapa Reza harus jadi korban dan aku terus disalahkan?"
    b "Putri, terkadang keputusan yang benar dalam hati kita tidak selalu diterima dengan baik oleh dunia luar."
    b "Namun, menerima kenyataan dan mempelajari hikmah dari setiap kejadian adalah bagian dari perjalananmu."
    p cry "Aku tidak butuh hikmah! Reza mati karena ketidakadilan ini! Dan semua orang hanya menyalahkanku! Kenapa aku harus menerima ini semua?!"
    p "Aku hanya ingin hidupku kembali seperti semula dan mereka semua harus minta maaf kepadaku!"
    b "Jika kamu tidak bisa berdamai dengan dirimu sendiri, maka luka itu akan terus tinggal. Perjalananmu untuk menemukan kedamaian harus dimulai dari hatimu sendiri."
    b "Kalau itu memang keputusanmu, selamat tinggal, Putri."
    hide binar
    with Dissolve(2.0)
    "Makhluk Cahaya berpendar sebelum benar-benar menghilang, meninggalkan Putri sendirian di dalam kamarnya."
    "Putri duduk diam dalam penyesalan, merasa kosong dan kehilangan arah. Dalam keheningan, air matanya terus mengalir, tapi tak ada jawaban yang datang untuk mengakhiri rasa sakitnya."
    "BAD ENDING: FAINT"
    jump badending
    #scene bad ending
    #with Dissolve(.5)
    return

label choice_2f:
    "Putri duduk termenung di tepi tempat tidurnya, setelah merenungi semua kejadian yang menimpa dirinya."
    p mikir "Aku sudah memikirkannya. Semua yang terjadi mungkin memang takdirku."
    p "Aku tahu aku telah membuat banyak kesalahan, tapi aku memilih untuk menerima semua itu."
    scene cg cahaya
    with Dissolve(1.0)
    p smile "Aku tak bisa terus-menerus menyalahkan diriku. Jika ini jalanku, aku ingin melanjutkannya tanpa penyesalan."
    b "Kamu itu lebih kuat dari yang kamu kira. Ingat, menerima bukan berarti melupakan, tapi memahami bahwa semuanya adalah bagian dari perjalananmu."
    b "Aku akan selalu menjadi bagian dari dirimu. Jika kamu merasa keputusan yang kamu pilih sudah sesuai dengan yang kamu rasa benar, maka itu lebih penting daripada semua opini orang tentang dirimu."
    "Binar kemudian perlahan seperti memeluk Putri, meninggalkan kehangatan yang tenang di dadanya."
    "Putri memejamkan mata, merasakan kedamaian yang belum pernah ia rasakan selama beberapa bulan yang sulit ini."
    jump timeskip

label timeskip:
    scene sky
    with Dissolve(1.0)
    play music "timeskip.mp3"
    "Dipertemukan dengan makhluk cahaya itu mengubah hidup Putri sedikit demi sedikit. Ia mulai belajar untuk menerima kenyataan dan berani membantah segala gosip dan cap buruk yang diutarakan kepadanya."
    "Beberapa tahun berlalu."
    "Putri kini menjalani hidupnya sebagai mahasiswa tingkat akhir di sebuah kampus yang cukup jauh dari tempat tinggalnya."
    scene bg jalan kecil
    with Dissolve(1.0)
    "Sore itu, sepulangnya dari kampus, Putri berjalan santai di trotoar menuju kosannya."
    "Ia tersenyum kecil, merasa bangga pada dirinya sendiri karena berhasil melalui banyak hal sulit dalam hidupnya beberapa tahun belakangan."
    "Dipikir-pikir lagi, meskipun prestasinya biasa saja, ia selalu bangga dengan dirinya sendiri yang mampu keluar dari masa-masa sulit dan menjadi dirinya yang sekarang serta dikelilingi oleh teman-teman yang mendukungnya."
    "Baginya, menjadi seseorang yang bisa menerima kesalahan, memaafkan, dan terus berkembang adalah hal yang sangat ia syukuri."
    "Di tengah lamunan, ia meraba saku celananya yang ternyata rata semua. Ia terhenti mendadak."
    play sound "ambil.mp3"
    with hpunch
    p shocked "Hah? Dompetku?! Kok nggak ada?!"
    "Ia segera berhenti dan memeriksa ulang seluruh kantongnya dengan panik, lalu membuka tasnya untuk memastikan, namun tetap nihil."
    "Raut wajahnya semakin tegang."
    p "Tadi aku pasti bawa kok, aku ingat jelas dompet itu aku taruh di saku... Aduh, gimana ini?!"

    menu:
        "Kembali":
            jump choice_1g
        "Cari dompet":
            jump choice_2g

label choice_1g:
    p shocked "Duh kok nggak ada, pasti ini ada yang nyuri! Siapa sih yang berani-beraninya ambil dompet aku? Dasar nggak punya moral!"
    with hpunch
    "Ia menghentakkan kaki dengan keras, tangannya mengepal sambil menggerutu."
    p neutral "Dasar maling nggak tau diri! Semoga semua harinya hari senin terus!"
    "Putri terus menyumpahi pencuri yang tidak ia kenal sampai ia menuju kosan. Ia memutuskan untuk beristirahat dari hari yang terasa panjang ini."
    "BAD ENDING: MISCHIEF"
    jump badending
    #scene bad ending
    #with Dissolve(.5)

label choice_2g:
    "Putri memutuskan untuk menenangkan diri dan berusaha mencari dompet yang hilang dengan cara menelusuri jalan yang tadi ia lalui."
    "Rasa kesal yang sempat menguasainya kini sedikit mereda, digantikan oleh usaha untuk tetap sabar dan teliti mencari."
    p neutral "Oke jangan panik. Coba tenang dan telusuri jalan ini pelan-pelan. Dompetnya pasti ada di sini, harus ada."
    play sound "nabrak.mp3"
    with Pause(.5)
    "Putri melangkah perlahan, terus memindai jalan di sekelilingnya dengan fokus."
    with hpunch
    "Tiba-tiba, ia tidak sengaja menabrak seseorang di depannya."
    p confused "Ah, maaf, maaf banget, saya nggak sengaja..."
    "Ia segera ingin melanjutkan langkahnya, tapi suara orang itu menghentikannya."
    c "Putri?"
    "Putri berhenti sejenak, merasa ada yang aneh dengan suara itu, terdengar tidak asing."
    "Ia menoleh dengan cepat dan melihat seseorang yang mengenakan masker dan topi sehingga hanya matanya saja yang terlihat."
    p "Eh? Siapa ya?"
    c "Putri, tunggu dulu, aku ingin mengembalikan sesuatu."
    stop music
    "Orang itu mendekat, dan dengan perlahan ia membuka masker wajahnya."
    #play sound "sreettt.mp3"
    "Wajah yang sangat familiar, wajah Reza, muncul di hadapan Putri. Matanya terbelalak, terkejut."
    play music "trueending.mp3"
    scene cg reuni
    with Dissolve(1.5)
    p "Reza?! Itu kamu?! Tapi... tapi... bukannya kamu... kamu kan sudah..."
    r "Iya, aku tau ini pasti bikin kamu kaget. Tapi, Putri... Aku nggak meninggal seperti rumor itu. Aku sempet dibawa ke UGD, kondisiku sangat kritis saat itu. Aku sempat koma beberapa hari dan beberapa tulang rusukku patah."
    "Reza menarik napas dalam-dalam, menceritakan apa yang terjadi setelahnya."
    r "Setelah orang tuaku datang, aku dipindahkan ke rumah sakit yang lebih memadai. Setelah beberapa bulan dan keadaanku membaik, orang tuaku juga memutuskan untuk pindah lagi ke tempat tinggal baru."
    r "Mereka nggak mau ada gosip atau fitnah yang lebih parah dan merusak harga diri mereka juga aku. Saat itu, aku nggak bisa menghubungimu lagi, karena kita sudah putus kontak sejak kejadian itu."
    "Putri terdiam, mulutnya terbuka sedikit, merasa sangat terkejut dan penuh penyesalan."
    p "Reza, aku... aku nggak tahu harus ngomong apa. Aku sangat menyesal. Aku... aku salah banget waktu itu. Aku nggak bisa menghubungimu lagi, dan aku nggak tahu apa yang harus aku lakukan."
    p "Aku... aku minta maaf."
    r "Sudah, nggak perlu disesali lagi. Yang penting kita bisa bertemu sekarang dan semuanya bisa jelas. Aku juga sebenarnya ingin menjelaskan semuanya. Aku nggak ingin kamu terus merasa bersalah."
    p "Terima kasih sudah memberi aku kesempatan untuk menjelaskan. Aku... aku nggak tahu kalau kamu sudah melalui semua itu."
    p "Aku berharap kita bisa mulai lagi, dengan cara yang lebih baik."
    r "Tenang, kita bisa mulai dari sini. Masa lalu biarlah menjadi masa lalu."
    "Putri tersenyum, walaupun dengan air mata yang masih membasahi pipinya."
    scene bg jalan kecil
    with Dissolve(1.0)
    "Reza memberikan dompet yang telah ia temukan di jalan kepada Putri, dan mereka saling bertukar pandang dengan penuh pengertian."
    "Meskipun jalan mereka mungkin tak selalu mulus, namun setidaknya sekarang mereka berdua bisa berjalan bersama, memulai kembali dari awal dengan lebih dewasa, tanpa ada lagi yang disembunyikan."
    "TRUE ENDING: NEW BEGINNING"

    stop music
    "Terima kasih sudah menyelesaikan perjalanan Putri ini hingga akhir."
    "Kami harap agar semua yang ada di game ini bisa dijadikan pelajaran dalam menaati berbagai norma yang ada di masyarakat."
    "Kami pamit dulu!"

    label trueending:
        scene black
        with Pause(1)

        play music "trueending.mp3"
        show cg true ending with dissolve
        with Pause(2)

        scene black with dissolve
        with Pause(1)

    #scene true ending
    #with Dissolve(.5)
    #AKHIRNYA KELAR ANJENG!!!!!!!!!!!!

return