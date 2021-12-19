
from tkinter import *
import tkinter.font

root = Tk()
root.geometry("400x640")
changefont = tkinter.font.Font(size = 10)
judul = Label(root,text="SISTEM PAKAR DETEKSI PENYAKIT",font=changefont)
judul.place(x=90,y=10)

labelfr = LabelFrame(root,text ="Hasil",padx=20,pady=20)
labelfr.place(x=10,y=360)

penyakit = ["Covid", "Flu", "TBC", "Tipes", "Bronchitis", "Asma", "Pneumonia"]
gejala = ["Demam", "Batuk", "Sakit Tenggorokan", "Kehilangan Rasa dan Bau", "Diare", \
          "Sesak Napas", "Nyeri Dada"]
pengetahuan = [
    ["Covid", "Demam", 0.6, 0.2],
    ["Covid", "Batuk", 0.4, 0.4],
    ["Covid", "Sakit Tenggorokan", 0.2, 0.6],
    ["Covid", "Kehilangan Rasa dan Bau", 0.8, 0.2],
    ["Covid", "Diare", 0.2, 0.4],
    ["Covid", "Sesak Napas", 0.4, 0.4],
    ["Covid", "Nyeri Dada", 0.6, 0.2],
    ["Flu", "Demam", 0.6, 0.4],
    ["Flu", "Batuk", 0.2, 0.6],
    ["Flu", "Kehilangan Rasa dan Bau", 0.8, 0.2],
    ["TBC", "Demam", 0.2, 0.6],
    ["TBC", "Batuk", 0.4, 0.4],
    ["TBC", "Kehilangan Rasa dan Bau", 0.4, 0.2],
    ["TBC", "Sesak Napas", 0.8, 0.2],
    ["TBC", "Nyeri Dada", 0.6, 0.2],
    ["Tipes", "Demam", 0.8, 0.2],
    ["Tipes", "Batuk", 0.2, 0.6],
    ["Tipes", "Sakit Tenggorokan", 0.4, 0.2],
    ["Tipes", "Diare", 0.4, 0.2],
    ["Bronchitis", "Batuk", 0.8, 0.2],
    ["Bronchitis", "Kehilangan Rasa dan Bau", 0.4, 0.4],
    ["Bronchitis", "Sesak Napas", 0.4, 0.2],
    ["Bronchitis", "Nyeri Dada", 0.4, 0.2],
    ["Asma", "Batuk", 0.2, 0.6],
    ["Asma", "Sesak Napas", 0.8, 0.2],
    ["Asma", "Nyeri Dada", 0.4, 0.2],
    ["Pneumonia", "Demam", 0.4, 0.4],
    ["Pneumonia", "Sakit Tenggorokan", 0.8, 0.2],
    ["Pneumonia", "Sesak Napas", 0.6, 0.2],
    ["Pneumonia", "Nyeri Dada", 0.6, 0.02]
    
]

demam = Label(root,text = "Apakah Anda Mengalami Demam?")
batuk = Label(root,text = "Apakah Anda Mengalami Batuk?")
sakittenggorokan = Label(root,text = "Apakah Anda Sakit Tenggorokan?")
kehilanganrasa = Label(root,text = "Apakah Anda Kehilangan Rasa dan Bau?")
diare = Label(root,text = "Apakah Anda Mengalami Diare?")
sesaknapas = Label(root,text = "Apakah Anda Mengalami Sesak Napas?")
nyeridada = Label(root,text = "Apakah Anda Mengalami Nyeri Dada?")

demam.place(x = 20, y = 40)
batuk.place(x = 20, y = 80)
sakittenggorokan.place(x = 20, y = 120)
kehilanganrasa.place(x = 20, y = 160)
diare.place(x = 20, y = 200)
sesaknapas.place(x = 20, y = 240)
nyeridada.place(x = 20, y = 280)

dm = StringVar()
dm.set("none")
rbdm1 = Radiobutton(root, text ="Ya",variable=dm,value="ya").place(x=20, y=60)
rbdm1 = Radiobutton(root, text ="Tidak",variable=dm,value="tidak").place(x=80, y=60)

bt = StringVar()
bt.set("none")
rbbt1 = Radiobutton(root, text ="Ya",variable=bt,value="ya").place(x=20, y=100)
rbbt1 = Radiobutton(root, text ="Tidak",variable=bt,value="tidak").place(x=80, y=100)

st = StringVar()
st.set("none")
rbst1 = Radiobutton(root, text ="Ya",variable=st,value="ya").place(x=20, y=140)
rbst1 = Radiobutton(root, text ="Tidak",variable=st,value="tidak").place(x=80, y=140)

kr = StringVar()
kr.set("none")
rbkr1 = Radiobutton(root, text ="Ya",variable=kr,value="ya").place(x=20, y=180)
rbkr1 = Radiobutton(root, text ="Tidak",variable=kr,value="tidak").place(x=80, y=180)

dr = StringVar()
dr.set("none")
rbdr1 = Radiobutton(root, text ="Ya",variable=dr,value="ya").place(x=20, y=220)
rbdr1 = Radiobutton(root, text ="Tidak",variable=dr,value="tidak").place(x=80, y=220)

sn = StringVar()
sn.set("none")
rbsn1 = Radiobutton(root, text ="Ya",variable=sn,value="ya").place(x=20, y=260)
rbsn1 = Radiobutton(root, text ="Tidak",variable=sn,value="tidak").place(x=80, y=260)

nd = StringVar()
nd.set("none")
rbnd1 = Radiobutton(root, text ="Ya",variable=nd,value="ya").place(x=20, y=300)
rbnd1 = Radiobutton(root, text ="Tidak",variable=nd,value="tidak").place(x=80, y=300)
        
def hitung():
            gejala_dipilih = []
            if dm.get() == "ya":
                gejala_dipilih.append(gejala[0])
            if bt.get() == "ya":
                gejala_dipilih.append(gejala[1])
            if st.get() == "ya":
                gejala_dipilih.append(gejala[2])
            if kr.get() == "ya":
                gejala_dipilih.append(gejala[3])
            if dr.get() == "ya":
                gejala_dipilih.append(gejala[4])
            if sn.get() == "ya":
                gejala_dipilih.append(gejala[5])
            if nd.get() == "ya":
                gejala_dipilih.append(gejala[6])

            penyakit_terpilih = []
            for i in range(len(pengetahuan)):
                for j in range(len(gejala_dipilih)):
                    if (pengetahuan[i][1] == gejala_dipilih[j]):
                        if pengetahuan[i][0] not in penyakit_terpilih:
                            penyakit_terpilih.append(pengetahuan[i][0])
            print("penyakit terpilih", penyakit_terpilih)

            list_cf = []
            for i in range(len(penyakit_terpilih)):
                print("===="+penyakit_terpilih[i]+"====")
                jmlpengetahuan = 0
                pengetahuanke = 0
                for j in range(len(pengetahuan)):
                            if(pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
                                jmlpengetahuan = jmlpengetahuan + 1
                mblama = 0
                mdlama = 0
                for j in range(len(pengetahuan)):
                    if(pengetahuan[j][0] == penyakit_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
                        pengetahuanke = pengetahuanke + 1
                        if (jmlpengetahuan == 1):
                            mb = pengetahuan[j][2]
                            md = pengetahuan[j][3]
                            cf = mb - md
                            print("mb = ", mb)
                            print("md = ", md)
                            print("cf = mb - md = ", mb, " - ", md, " = ", cf);
                            list_cf.append(cf)
                        elif (jmlpengetahuan > 1):
                            if (pengetahuanke == 1):
                                mblama = pengetahuan [j][2]
                                mdlama = pengetahuan [j][3]
                                print ("mblama = ", mblama)
                                print ("mdlama = ", mdlama)
                            elif (pengetahuanke == 2):
                                mbbaru = pengetahuan[j][2]
                                mdbaru = pengetahuan[j][3]
                                mbsementara = (mblama + mbbaru) * (1 - mblama)
                                mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                                print("mbsementara = (mblama + mbbaru) * (1 - mblama) = (",\
                                    mblama, " + ", mbbaru, ") * (1 - ", mblama, ") = ", mbsementara)
                                print("mdsementara = (mdlama + mdbaru) * (1 - mdlama) = (",\
                                    mdlama, " + ", mdbaru, ") * (1 - ", mdlama, ") = ", mdsementara)
                                if (jmlpengetahuan == 2):
                                    mb = mbsementara
                                    md = mdsementara
                                    cf = mb - md
                                    print ("mb = mbsementara = ", mb)
                                    print ("md = mdsementara = ", md)
                                    print ("cf = mb - md = ", mb, " - ", md, " = ", cf)
                                    list_cf.append(cf)
                            elif(pengetahuanke >= 3):
                                mblama = mbsementara
                                mdlama = mdsementara
                                print("mblama = mbsementara = ", mblama)
                                print("mdlama = mdsementara = ", mdlama)
                                mbbaru = pengetahuan[j][2]
                                mdbaru = pengetahuan[j][3]
                                print("mbbaru = ", mbbaru)
                                print("mdbaru = ", mdbaru)
                                mbsementara = (mblama + mbbaru) * (1 - mblama)
                                mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                                print("mbsementara = (mblama + mbbaru) * (1 - mblama) = (", \
                                    mblama, " + ", mbbaru, ") * (1- ", mblama, ") = ",mbsementara)
                                print("mdsementara = (mdlama + mdbaru) * (1 - mdlama) = (", \
                                    mdlama, " + ", mdbaru, ") * (1- ", mdlama, ") = ",mdsementara)
                                if(jmlpengetahuan == pengetahuanke):
                                    mb = mbsementara
                                    md = mdsementara
                                    cf = mb - md
                                    print("mb = mbsementara = ", mb)
                                    print("md = mdsementara = ", md)
                                    print("cf = mb - md = ",mb, " - ", md, " = ", cf)
                                    list_cf.append(cf)
            print("Peyakit Terpilih", penyakit_terpilih)
            print(list_cf)
            penyakitrangking = []
            cfrangking = []
            for i in range(len(penyakit_terpilih)):
                penyakitrangking.append(penyakit_terpilih[i])
                cfrangking.append(list_cf[i])
            for i in range(len(penyakit_terpilih)):
                for j in range (len(penyakit_terpilih)):
                    if j > i:
                        if cfrangking[j] > cfrangking[i]:
                            tmpcf = cfrangking[i]
                            tmppenyakit = penyakitrangking[i]
                            cfrangking[i] = cfrangking[j]
                            penyakitrangking[i] = penyakitrangking[j]
                            cfrangking[j] = tmpcf
                            penyakitrangking[j] = tmppenyakit
            print("rangking penyakit", penyakitrangking)
            print("rangking CF:", cfrangking)
            garis = Label(text="---------------------------HASIL PERHITUNGAN---------------------------").place(x=5,y=360)
            txtpenyakit = Label(text="Diagnosis penyakit anda adalah : ").place(x=20, y=380)
            lblpenyakitrangking = Label(text=penyakitrangking[0], fg = "blue").place(x=20, y=400)
            txtpenyakit2 = Label(text="Kemungkinan penyakit lain adalah : ").place(x=20, y=420)
            lblpenyakitrangking2 = Label(text=penyakitrangking[1], fg = "blue").place(x=20, y=440)
            txtpenyakit2 = Label(text="Hasil perhitungan nilai CF dari penyakit anda adalah : ").place(x=20, y=460)
            lblcfrangking = Label(text=cfrangking[0], fg = "blue").place(x=20,y=480)

            if penyakitrangking[0] == "Covid":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Tetap Di Rumah dan Hubungi Dokter").place(x=20,y=520)
                sol3 = Label(text="2. Istirahat yang cukup dan sering minum air putih hangat").place(x=20,y=540)
                garis1 = Label(text="------------------------------------------------------------------").place(x=5,y=560)
            elif penyakitrangking[0] == "Flu":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Istirahat yang cukup dan sering minum air putih hangat").place(x=20,y=520)
                sol3 = Label(text="2. Gunakan humidifier").place(x=20,y=540)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=560)
            elif penyakitrangking[0] == "TBC":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Tetap tenang dan tidak panik").place(x=20,y=520)
                sol3 = Label(text="2. Hubungi dokter spesialis pernafasan ").place(x=20,y=540)
                sol4 = Label(text="3. Istirahat yang cukup dan mengkonsumsi makanan yang kaya akan serat").place(x=20,y=560)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif penyakitrangking[0] == "Tipes":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Istirahat yang cukup").place(x=20,y=520)
                sol3 = Label(text="2. Kurangi aktifitas outdoor").place(x=20,y=540)
                sol4 = Label(text="3. Banyak minum air putih").place(x=20,y=560)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif penyakitrangking[0] == "Brochitis":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Segera hubungi dokter THT").place(x=20,y=520)
                sol3 = Label(text="2. Hindari polusi udara dan debu").place(x=20,y=540)
                sol4 = Label(text="3. Melakukan terapi herbal").place(x=20,y=560)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif penyakitrangking[0] == "Asma":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Kurangi aktifitas fisik yang berlebihan").place(x=20,y=520)
                sol3 = Label(text="2. Melakukan Latihan pernapasan di pagi hari secara berkala").place(x=20,y=540)
                sol4 = Label(text="3. Hindari polusi udara dan debu").place(x=20,y=560)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif penyakitrangking[0] == "Pneumonia":
                sol = Label(text="Solusi dari penyakit anda: ").place(x=20,y=500)
                sol2 = Label(text="1. Meminum antibiotic pereda nyeri pada pernapasan").place(x=20,y=520)
                sol3 = Label(text="2. Jaga kualitas udara di rumah").place(x=20,y=540)
                sol4 = Label(text="3. Melakukan terapi oksigen").place(x=20,y=560)
                sol5 = Label(text="4. Istirahat yang cukup").place(x=20,y=580)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=600)


btn = Button(root,text="Hitung",command=hitung).place(x=20, y=330)
root.mainloop()