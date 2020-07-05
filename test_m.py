import rsa # RSA signature module from pip
import qrcode # qrcode generator  module from pip
import zxing # qrcode scanning modue from pip
import pickle # save class as file
import main



shanting_Li = {
	'name': 'Shanting_Li',
	'gpa': 3.6,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0815',
	'email':'lst104@gmail.com'
}
scarlett = {
	'name': 'Scarlett',
	'gpa': 3.3,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0805',
	'email':'scarlett14@gmail.com'
}

kenny = {
	'name': 'Kenny',
	'gpa': 3.1,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0892',
	'email':'kenny101@gmail.com'
}
levi = {
	'name': 'Levi',
	'gpa': 4.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0870',
	'email':'levi@gmail.com'
}
scarlett_fake = {
	'name': 'Scarlett_fake',
	'gpa': 4.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0870',
	'email':'sherry@gmail.com'
}
test = {
	'name': 'test',
	'gpa': 3.0,
	'major':'architecture',
	'degree': 'bachelor',
	'enroll_num': '0000',
	'email':'leon@gmail.com'
}

arch_department = [scarlett, levi]
main.batch_gen(arch_department)


print(main.veri(scarlett))
print(main.veri(levi))
print(main.veri(scarlett_fake))
print(main.veri(test))


