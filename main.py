# Test python env
def print_hello():
	animals = ['dog', 'cat','racoon', 'lion'] # in one line
	foods = [
		'Pizza',
		'Hamburger',
		'coke'
	] # w/o trailing comma
	names = [
		'John',
		'Dodo',
		'Tita',
		'dora',
	] # w/ trailing comma
	for f_name in names:
		print(f'hello, {f_name}')

if __name__ == '__main__':
	print_hello()
