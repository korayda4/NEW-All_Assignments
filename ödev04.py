msg = "Bir şifre belirleyin\n-->"
while True:
    sifre = input(msg)
    if len(sifre) < 8:
        print("Şifreniz en az 8 karakter olmalıdır. Lütfen tekrar deneyin.")
        msg = "Bir şifre belirleyin(En az 8 karakter içermelidir)\n-->"
        continue
    if not any(kntrl.isdigit() and kntrl.isalpha() and kntrl.isupper() for kntrl in sifre):
        print("Şifreniz en az 1 rakam,harf ve büyük harf içermelidir. Lütfen tekrar deneyin.")
        msg = "Bir şifre belirleyin(Birtane rakam,harf ve büyük harf bulundurun)\n-->"
        continue
    else:
        print("Şifre Oluşturuldu!")
        
        break

    
    