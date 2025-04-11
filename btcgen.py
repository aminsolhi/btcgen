# -*- coding: utf-8 -*-

"""
Created on Thu Mar 14 17:50:54 2024

Bitcoin Puzzle Scanner for 2^66 ~ 2^67 range
Developer: Amin Solhi
Contacts:  email: amin.solhi@gmail.com, +9891111842779
"""

import threading
import bitcoin
import ecdsa
import secrets
from timeit import default_timer as timer   
import datetime
import sys
import argparse

lock = threading.Lock()

global target_address
global output_file
global rng
global private_key
global end_range
global ks
global start
global random_mode
global num_threads
global _loop_ks
rng=1




parser = argparse.ArgumentParser(description='Process boolean values.')
#parser.add_argument('-m', '--random_mode', type=int, help='Enter True or False', required=False)
parser.add_argument('-s', '--start_hex', type=str, help='Private Key Start Hexadecimal', required=False)
parser.add_argument('-e', '--end_hex', type=str, help='Private Key End Hexadecimal', required=False)
parser.add_argument('-o', '--output_file', type=str, help='OutPut File for save Result', required=False)
parser.add_argument('-a', '--target_address', type=str, help='Target Address for Search', required=False)
parser.add_argument('-t', '--Thread', type=int, help='Thread value', required=False)
parser.add_argument('-r', '--Random_per', type=int, help='Random enable and enter Kilo Key Space', required=False)
args = parser.parse_args()




if args.target_address :
    target_address = args.target_address
else :
    target_address = "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9"
if args.output_file :
    output_file = args.output_file
else:
    output_file = "data.txt"
if args.Random_per:
    rng=args.Random_per
    random_mod = True
else:
    random_mod = False
#private_key=args_p.text
if args.start_hex :
    private_key=args.start_hex
else:
    private_key="40000000000000000"
if args.end_hex :
    end_range=int(args.end_hex, 16)
else:
    end_range = int("80000000000000000", 16)
if args.Thread :
    num_threads = args.Thread
else:
    num_threads = 1

ks=0
start = timer()
start_range = int(private_key, 16)



print ("\nBTCGEN Bitcoin Puzzle Scanner \n")
print ("BTC Address : ",target_address)
print ("OutPut File : ",output_file)
print ("Randome Mod : ",f"{str(random_mod)}")
if (random_mod):
    print ("Random Key  : ",f'per {rng}K key')
print ("Device      :  CPU")
print ("Thread      : ",num_threads)
print ("Global Start: ",private_key)
print ("Global END  : ",(f'{end_range:x}'))

print('\n')

def remove_leading_zeros(input_string):
    result = ""
    zero_found = False
    for char in input_string:
        if char != "0":
            zero_found = True
        if zero_found:
            result += char
    return result

def normalize_hex_string(hex_str):
    if len(hex_str) < 64:
        hex_str = '0' + hex_str
        if len(hex_str) < 64:
            hex_str = normalize_hex_string(hex_str)
    return hex_str

def generate_random_priv():  
    global start_range, end_range  
       
    if end_range is None or end_range <= start_range:  
        print(f"Start Range: {start_range}, End Range: {end_range}")  # برای عیب‌یابی چاپ می‌شود  
        raise ValueError("Invalid range for generating random private key. Ensure that end_range is greater than start_range.")  
    
    random_priv_key = secrets.randbelow(end_range - start_range) + start_range  
    return normalize_hex_string(hex(random_priv_key)[2:])  # تبدیل به هگزادسیمال و بازگرداندن  


def generate_private_key(num_hex):  
    global private_key  
    num_decimal = int(num_hex, 16)  
    num_decimal += 1  
    
    # بررسی اینکه آیا عدد بزرگتر از end_range است  
    if num_decimal >= end_range:   
        sys.exit("Stopping the program.")  
    
    num_hex = normalize_hex_string(f'{num_decimal:x}')  
    return num_hex  



def private_key_to_public_key(private_key):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    compressed_public_key = vk.to_string("compressed").hex()
    return compressed_public_key


def address_compare(_i:int):
        global private_key
        global rng
        global ks
        global start
        global target_address
        global i
        global _loop
        global _loop_ks
        print(f"\r[{str(datetime.timedelta(seconds=int(timer()-start)))}] [T:"+"{:.2f}".format(ks/1000000)+f"Mk] [R:{i}] [PK:{(remove_leading_zeros(private_key))}] ",end=" ")
        public_key = private_key_to_public_key(private_key)
        bitcoin_address = bitcoin.pubtoaddr(public_key)
        if bitcoin_address == target_address:
            with open(output_file, "a") as f:
                f.write('\nprivate key int: ' + private_key + '\nBitcoin address: ' + bitcoin_address + '\n_________\n')
            print("\nFound matching Bitcoin address for private key:", private_key)
            input("")   
        private_key = generate_private_key(private_key)
        with lock:
            ks += 1
            _loop_ks +=1
            

def scan_for_address():
    global rng
    global _loop
    global num_threads 
    global _loop_ks
    _loop_ks = 0
    _rng = (int(rng*1000)//num_threads)
    for _loop in range(_rng):
        mainboard()
      
        

def scan_for_address_random():
    global private_key
    global rng
    private_key = generate_random_priv()
    scan_for_address()
   

def main():
    global i
    global private_key
    i=0
    private_key=normalize_hex_string(private_key)
    if random_mod:
        while True:
            i+=1
            scan_for_address_random()
    else:
        while True:
            scan_for_address()


def mainboard():  
    global num_threads  
    thread_list = []  
    
    for _i in range(num_threads):  
        thread = threading.Thread(target=address_compare, args=(_i,))
        thread_list.append(thread)  
        thread.start()  

    for thread in thread_list:
        thread.join()  

if __name__ == "__main__":
    main()