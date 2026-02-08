import qrcode
myqr = qrcode.make("https://www.linkedin.com/in/sravanthi-kalavakunta?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")

myqr.save("myqr.png")