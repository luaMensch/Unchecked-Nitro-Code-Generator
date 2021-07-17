
import requests,random,string,datetime,multiprocessing

f = open('codes.txt', "a+")

def gencode():
    while True:
        code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        f.write(f'{code}\n')
        print(code)

if __name__ == "__main__":
    q=multiprocessing.Queue()
    processes=[multiprocessing.Process(target=gencode) for i in range(1,35)]
    for p in processes:
        p.start()
 
    for p in processes:
        p.join()
 
    result = [q.get() for p in processes]
    print(result)
