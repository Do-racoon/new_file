# Test python env
def print_hello():
	animals = ['dog', 'cat','racoon'] # in one line
	foods = [
		'Pizza',
		'Hambuger'
	] # w/o trailing comma
	names = [
		'John',
		'Dodo',
		'Tita',
	] # w/ trailing comma
	for f_name in names:
		print(f'hello, {f_name}')

if __name__ == '__main__':
	print_hello()
