# pwintools-samples

[![buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/tabdiukov)

Quick scripts to facilitate "pwintools", a pwnTools port for Windows.

## Serial
Simple test program for "pwintools"

Guide:
1. download & install "com0com",
2. configure it to emulate one serial ports pair (such as `COM1<-->COM2`)
3. download & install "COM Port Data Emulator", set it up to
    * Use one of two ports *not in use* (such as COM2)
    * (by default) Generate: random text
4. Start "COM Port Data Emulator" (bottom right corner)
5. Run this text script
