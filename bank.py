# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:08:08 2022

@author: xyyan
"""
from prettytable import PrettyTable
from account import RetailAccount, BusinessAccount
from utilities import read_file, get_text_between_two_delimiters
import os

class Bank:
    
    def __init__(self):
        self.transaction_files = {}
        self.accounts = {}
        self.fees_charged = {}
    
    def get_transaction_files(self, directory):
        for file in os.listdir(directory):
            if file.startswith('transactions') and file.endswith('.csv'):
                num = get_text_between_two_delimiters(file, '_', '.')
                self.transaction_files[int(num)] = file
    
    def process_transaction_files(self):
        num = 1
        while True:
            if num not in self.transaction_files.keys():
                break
            self.process_transaction(self.transaction_files[num])
            num += 1
    
    def process_transaction(self, file):
        transactions = read_file(file, False)
        for transaction in transactions:
            account = None
            if transaction[1] == 'R':
                if transaction[0] not in self.accounts.keys():
                    account = RetailAccount(transaction[0], transaction[1])
                    self.accounts[account.get_name()] = account
                else:
                    account = self.accounts[transaction[0]]
            elif transaction[1] == 'B':
                if transaction[0] not in self.accounts.keys():
                    account = BusinessAccount(transaction[0], transaction[1])
                    self.accounts[account.get_name()] = account
                else:
                    account = self.accounts[transaction[0]]
            
            account.process_transaction(transaction[2] == 'D', float(transaction[3]))
        
    def report(self):
        overall_retail_accounts_balance, overall_business_accounts_balance = 0.0, 0.0
        overall_retail_fees_charged, overall_business_fees_charged = 0.0, 0.0
        retail_accounts, business_accounts = [], []
            
        for name, account in self.accounts.items():
            if account.get_account_type() == 'R':
                overall_retail_accounts_balance += account.get_balance()
                overall_retail_fees_charged += account.get_fees_charged()
                retail_accounts.append(account)
            elif account.get_account_type() == 'B':
                overall_business_accounts_balance += account.get_balance()
                overall_business_fees_charged += account.get_fees_charged()
                business_accounts.append(account)
                    
        sorted_by_retail_balances = sorted(retail_accounts, key = lambda x: x.get_balance(), reverse = True)
        sorted_by_business_balances = sorted(business_accounts, key = lambda x: x.get_balance(), reverse = True)

        print()
        x = PrettyTable()
        x.title = "Retail Accounts"
        x.field_names = ['Name', 'Balance', 'Fees Charged']
        for field_name in x.field_names:
            x.align[field_name] = 'c'
        for account in sorted_by_retail_balances:
            x.add_row([account.get_name(), round(account.get_balance(), 2), round(account.get_fees_charged(), 2)])
        x.add_row([' ',' ',' '])
        x.add_row(['TOTAL', round(overall_retail_accounts_balance, 2), round(overall_retail_fees_charged, 2)])
        print(x)
        # print(x.get_string(title="Retail Accounts"))

        
        print()
        y = PrettyTable()
        y.title = 'Business Accounts'
        y.field_names = ['Name', 'Balance', 'Fees Charged']
        for field_name in y.field_names:
            y.align[field_name] = 'c'
        for account in sorted_by_business_balances:
            y.add_row([account.get_name(), round(account.get_balance(), 2), round(account.get_fees_charged(), 2)])
        y.add_row([' ',' ',' '])
        y.add_row(['TOTAL', round(overall_business_accounts_balance, 2), round(overall_business_fees_charged, 2)])
        # print(x.get_string(title="Business Accounts"))
        print(y)

