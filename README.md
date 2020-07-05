# QR-code
The function is to use QR code, containing digital signature and academic information, to authenticate college degree 

This repository contains 3 python files which can realize the function of producing and verifying digital signatures encoded in QR Code. 

1.main.py 

To use it you also need to install the following 4 modules: rsa, qrcode, zxing, pickle

It contains the codes to produce QR code according to student's academic information.

There are 3 functions, gen_qrcode, batch_gen and veri. 


2.test_m.py 

It contains several dictionaries to help you test the two programs mentioned above. 

To help test all possibilities, you also need to download the two png files and pkls. 
Please place all the files mentioned above in one file.
