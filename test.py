nama = input("Masukkan namamu: ")

try: 
    umur = int(input("Berapa umurmu: "))
    if umur < 0:
        print("Tidak ada umur minus!")
    else:
        cita2 = input("Cita citamu apa: ")
        
        print(f"\nHalo, {nama}")
        if umur >= 20:
            print(f"Umurmu {umur} tahun ya 💪, kamu sudah dewasa!")
        elif umur >= 15:
            print(f"Umurmu {umur} tahun ya 🔥, kamu masih remaja labil!")
        else:
            print(f"Umurmu {umur} tahun ya 😅, kamu masih bocil!")
        print(f"Kamu mau jadi {cita2} ya, semangat ngejar cita-citamu ya!")
    
except ValueError:
    print("Umur harus angka bukan huruf!")