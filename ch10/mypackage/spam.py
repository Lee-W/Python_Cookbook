import pkgutil

data = pkgutil.get_data(__package__, 'somedata.dat')

print('Data from ', data)