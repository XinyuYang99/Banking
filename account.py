# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:14:27 2022

@author: xyyan
"""
class Account:
    
    def __init__(self, name, account_type):
        self._name = name
        self._account_type = account_type
        self._fee_charged = 0.0
        self._balance = 0.0
        
    def get_name(self):
        return self._name
    
    def get_account_type(self):
        return self._account_type
    
    def get_fees_charged(self):
        return self._fee_charged
    
    def get_balance(self):
        return self._balance
    
class RetailAccount(Account):
    
    def __init__(self, name, account_type):
        Account.__init__(self, name, account_type)
        
    def process_transaction(self, is_deposit, amount):
        if is_deposit:
            self._balance += amount
        elif self._balance - amount < 0.0 :
            fee = 30.0
            self._balance -= fee
            self._fee_charged += fee
        else:
            self._balance -= amount
            
class BusinessAccount(Account):
    def __init__(self, name, account_type):
        Account.__init__(self, name, account_type)
        
    def process_transaction(self, is_deposit, amount):
        if is_deposit:
            self._balance += amount
        elif self._balance - amount < 0.0 :
            fee = 0.01 * (amount - self._balance)
            self._balance -= fee
            self._fee_charged += fee
        else:
            self._balance -= amount