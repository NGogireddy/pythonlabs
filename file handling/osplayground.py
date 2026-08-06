import os

print(os.getcwd())
print(os.listdir())
os.mkdir('newdir1')
os.chdir('newdir1')
print(os.getcwd())
os.mkdir('newdir2')
print(os.listdir())