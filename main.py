# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:23:10 2022

@author: xyyan
"""
from bank import Bank

def main():
    bank = Bank()
    bank.get_transaction_files("HW1")
    bank.process_transaction_files()
    bank.report()
    
if __name__ == '__main__':
    main()