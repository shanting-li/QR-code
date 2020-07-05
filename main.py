import rsa # RSA signature module from pip
import qrcode # qrcode generator  module from pip
import zxing # qrcode scanning modue from pip
import pickle # save class as file




def gen_qrcode(student):
	'''
	input: single dictionary containing academic information of a student, which has to own the key 'name'
	output: QR code image (png), pkl files containing a pair of public key and secret key
	QR code settings:version = 1, error_correction = L, box_size = 10,border = 4

	'''
	tmp =''
	message = ''.join([tmp + k + ':'+ str(student[k]) +' ' for k in student.keys()])

	#generate keys
	pubkey, prikey = rsa.newkeys(1024)
	with open (f"{student['name']}_pubkey.pkl",'wb') as f:
		pickle.dump(pubkey,f)
	with open (f"{student['name']}_prikey.pkl",'wb') as f:
		pickle.dump(prikey,f)

	#use private key to sign the message
	sign = rsa.sign(message.encode(), prikey, 'SHA-256')


	#pack message and signature
	lst_sign = []
	for s in sign:
		lst_sign.append(int(s))
	merge = []
	merge = [message, lst_sign]

	# produce qrcode
	qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_L,
		box_size = 10,
		border = 4,)
	qr.add_data(merge)
	qr.make(fit = True)
	img = qr.make_image()
	img.save(f"{student['name']}.png")


	
def batch_gen(dic):
	'''
	input:a list containing a series of dictionaries students, which all own the key 'name'
	output: several QR code images (png) corresponding to each student, and related pkl files
	QR code settings:version = 1, error_correction = L, box_size = 10,border = 4
	The file name of each QR code is the value of the key 'name'.

	'''
	for s in dic:
		gen_qrcode(s)
		

def veri(stu):
	'''
	input: a QR code, which needs to be placed in the same file with this veri.py
	output: string containing the result of verification
	
	'''

	# scan the qrcode
	reader = zxing.BarCodeReader()
	stu_name = stu['name']
	barcode = reader.decode(f'{stu_name}.png')
	msg_get = barcode.parsed
	n = 0
	count = 0
	while n < len(msg_get):
		if count == 2:
			break
		elif msg_get[n] == '[':
			count += 1
		n += 1
	msg_aca = msg_get[2:n-4] #remove''
	msg_sign = msg_get[n:-2] #remove[]
	try:
		msg_sign = (b''.join([bytes([int(i)]) for i in msg_sign.split(',')]))
	except ValueError:
		return 'The QR Code is unreadable'

	# verify the message
	print ('Applying for pulickey')

	with open(f'{stu_name}_pubkey.pkl','rb') as f:
		pubkey = pickle.load(f)

	print ('Verifying ...')
	try:
		veri = rsa.verify(msg_aca.encode(),msg_sign, pubkey)
		return 'The Certificate is genuine'
	except rsa.VerificationError:
		return 'The Certificate is forged'







