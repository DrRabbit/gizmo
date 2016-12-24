import pickle

your_data = {'foo': 'bar'}

path = 'C:\\Users\\Alex\\Documents\\pickle\\test.pickle'

# Store data (serialize)
with open(path, 'wb') as handle:
    pickle.dump(your_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Load data (deserialize)
with open(path, 'rb') as handle:
    unserialized_data = pickle.load(handle)

print(your_data == unserialized_data)

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
z = x + y


if x != 5:
    pass



