import qrcode


def generate_qr_code():
    # Getting input from the user
    title, univercity, location = input("Enter Your Data: ").split(' ')
    
    # Concatenating the input strings
    data = f"{title}{univercity}{location}"
    
    # Encoding the data using make() function
    qr_code_img = qrcode.make(data)
    
    # Saving the image file
    qr_code_img.save('QRCode.png')
    
    print("[+] Generated!")


generate_qr_code()