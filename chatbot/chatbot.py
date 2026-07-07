def chatbot(pesan):
    pesan = pesan.lower()

    if "halo" in pesan or "hi" in pesan or "hai" in pesan:
        return "Halo juga!"

    elif "apa kabar" in pesan:
        return "Aku baik."

    elif "bye" in pesan:
        return "Dah!"

    elif "siapa" in pesan and "developer" in pesan:
        return "Ah kepo deh!"

    elif "siapa" in pesan or "nama" in pesan or "kamu" in pesan:
        return "Aku Kana! Asisten kamu di sini, mau nanya apa? Aku siap bantu ;)"

    elif "apa" in pesan or "unspokenpoetries" in pesan:
        return "Simplenya, di sini tempat buat nampilin portofolio aja."

    elif "kontak" in pesan or "dihubungi" in pesan:
        return "developer@unspokenpoetries.my.id"

    elif "azriel" in pesan:
        return "<3"

    elif "kapan" in pesan or "dibuatnya" in pesan:
        return "Kapan yah... jujur lupa, pokoknya suatu hari saat UAS di bulan Juni 2026."

    elif "dijual" in pesan:
        return "Gak ada yang dijual ya, gilakkk"

    else:
        return "Duh, gak ngerti!"