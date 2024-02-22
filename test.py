import random
from time import sleep
from tqdm import tqdm

print("Йде завантаження файлів ...")
for i in tqdm(range(100), colour="green"):
    sleep(random.uniform(0.01, 0.1))

print("Файли успішно завантажені\n" + "files.xlsm")