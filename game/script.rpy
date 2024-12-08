define p = Character("Putri", color="#000000", image='putri')
define r = Character("Reza", color="#000000", image='reza')
define i = Character("Ibu", color="#000000", image='ibu')
define s = Character("Ibu-ibu Pasar", color="#000000", image='ibupasar')
define o = Character("Polisi", color="#000000", image='polisi')
define k = Character("Bapak Kos", color="#000000", image='bapakkos')
define a = Character("???", color="#000000", image='binar')
define b = Character("Binar", color="#000000", image='binar')

image side putri happy = im.Scale("images/side putri happy.png", 657, 855, xoffset=-180, yoffset=100)
image side putri mikir = im.Scale("images/side putri mikir.png", 657, 855, xoffset=-180, yoffset=100)
image side putri confused = im.Scale("images/side putri confused.png", 657, 855, xoffset=-180, yoffset=100)
image side putri cry = im.Scale("images/side putri cry.png", 657, 855, xoffset=-180, yoffset=100)
image side putri neutral = im.Scale("images/side putri neutral.png", 657, 855, xoffset=-180, yoffset=100)
image side putri smile = im.Scale("images/side putri smile.png", 657, 855, xoffset=-180, yoffset=100)

# NVL characters are used for the phone texting
define p_nvl = Character("Putri", kind=nvl, image="putri", callback=Phone_SendSound)
define r_nvl = Character("Reza", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

label start:

    scene dapur
    play sound "pagihari.mp3"
    "Embun pagi yang dingin tidak bisa mengganggu tidur nyenyak Putri yang sedang tergulung di dalam selimutnya, justru hawa dingin itu membuatnya semakin tenggelam dalam pulasnya tidur di hari Minggu."
    "Para embun sudah mulai beranjak, digantikan oleh sinar matahari pagi yang berusaha menembus tirai kamar Putri."
    
    show ibu
    i "Putri, bangun nak, ini udah siang lho!"
    hide ibu

    "Seketika Putri terbangun. Kepalanya sedikit pusing karena dibangunkan dengan tiba-tiba."
    "Faktanya, jam dinding di hadapan Putri menunjukkan pukul 6 lewat, masih pagi sekali untuk bangun di hari libur seperti ini."
    "Dengan malas, Putri melangkah untuk membukakan pintu."

    p neutral "Ada apa, Ibu?"
    show ibu 
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
    i "Iya, sama-sama. Hati-hati dijalan ya."
    p "Siap!"
    "Putri berpamitan dengan Ibunya dan ia pun mengendarai motornya menuju pasar."
    jump pasaran

label choice_2a:
    p "Ih, Bu. Kan masih pagi banget. Kenapa Ibu nggak beli sendiri aja atau minta Ayah? Aku masih ngantuk, tau..."
    i "Putri! Cara kamu ngomong ke Ibu itu nggak sopan. Kamu pikir Ibu ini siapa, nyuruh-nyuruh kamu tanpa alasan?"
    i "Ibu bangun pagi-pagi masak buat kalian semua, dan kamu malah membantah?!"
    p "Tapi, Bu..."
    i "Nggak ada tapi-tapian! Segera berangkat ke pasar. Ibu nggak mau denger alasan lagi!"
    p "Iya, iya. Aku berangkat."
    "Putri mengambil jaketnya dan berjalan keluar rumah dengan wajah kesal. Selagi melangkah, ia melirik helm yang sedang tergantung. Di benaknya terpikirkan apa ia harus mengenakannya atau tidak."

    scene teras
    menu:
        "Gunakan helm":
            jump choice_1b
        "Tidak menggunakan helm":
            jump choice_2b

label choice_1b:
    "Setelah memakai jaket, Putri mengambil helm dari gantungan dan mengenakannya sebelum ke menyalakan motornya."
    p "(Pakai helm itu penting. Nggak cuma soal aturan, tapi buat keselamatan.)"
    p "(Kalau terjadi apa-apa di jalan, setidaknya kepala terlindungi.)"
    "Ia mengecek kembali tali helm untuk memastikan terpasang dengan benar."
    p "(Kadang orang mikir dekat nggak perlu helm, tapi kecelakaan nggak lihat jarak. Lebih baik aman daripada menyesal.)"
    "Putri menyalakan motor dan melaju ke pasar dengan hati-hati, memastikan dirinya tetap patuh pada aturan lalu lintas."
    jump pasaran

label choice_2b:
    p "(Ah, cuma ke pasar, nggak jauh ini. Lagian nggak ada polisi juga, aman kok.)"
    
    
label pasaran:

    scene pasar
    menu:
        "Diam saja":
            jump choice_1c
        "Tegur Ibu-ibu tersebut":
            jump choice_2c

label choice_1c:
    p "huhu"

label choice_2c:



    scene pasar
    menu:
        "Biarkan Reza membayar":
            jump choice_1d
        "Bayar makanannya":
            jump choice_2d


label choice_1d:
    p "."



    #transform alpha_dissolve:
    #alpha 0.0
    #linear 0.5 alpha 1.0
    #on hide:
        #linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

#init: ### just setting variables in advance so there are no undefined variable problems
    #$ timer_range = 0
    #$ timer_jump = 0
    #$ time = 0

#screen countdown:
    #timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.
        
#label questiontime1:
    
    #label menu1:
        #$ time = 3                                     ### set variable time to 3
        #$ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        #$ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        #show screen countdown                          ### call and start the timer

        #menu:
            #"Menyerah":
                #hide screen countdown
                #jump choice_1e
            #"Bertahan":
                #hide screen countdown
                #jump choice_2e

    #label menu1_slow:
            #jump choice_1e


        #menu:
            #"Tidak setuju":
                #jump choice_1f
            #"Setuju":
                #jump choice_2f

#label choice_1f:

        #menu:
            #"Kembali":
                #jump choice_1g
            #"Cari dompet":
                #jump choice_2g


    

return