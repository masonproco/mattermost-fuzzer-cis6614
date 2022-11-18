import atheris

with atheris.instrument_imports():
    import qrcode
    import sys

def TestQRCodeGenerate(word):

    try:
        word = word.decode("utf-8")
    except:
        return

    img = qrcode.make(word)
    img.save("./qrcodes/" + word + ".png")

atheris.Setup(sys.argv, TestQRCodeGenerate)
atheris.Fuzz()


