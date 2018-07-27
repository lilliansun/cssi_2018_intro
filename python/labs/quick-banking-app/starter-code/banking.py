#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code
import time

class BankAccount(object):
    def __init__(self, label, balance, transact):
        self.label = label
        self.balance = balance
        self.transact = transact

    def __str__(self):
        return "The amount of money in {name}'s bank account is {bal}".format(name = self.label, bal = self.balance)

    def withdraw(self, amount):
        if ((self.balance - amount)<0):
            print ("Error: you must have {diff} more dollars".format(
                diff = amount - self.balance))
        elif (amount <0):
            print("Error: You cannot withdraw a negative amount")
        else:
            self.balance = self.balance - amount
            new_transact = Transaction(time.ctime(), "withdraw", amount, self)
            self.transactions.append(new_transact)


    def deposit(self, amount):
        if (amount<0):
            print("Error: You cannot deposit a negative amount")
        else:
            self.balance = self.balance + amount
            new_transact = Transaction(time.ctime(), "deposit", amount, self)
            self.transactions.append(new_transact)

    def rename(self, label):
        if(label == ""):
            print("Error: Choose a label that is not blank")
        else:
            self.label = label

    def transfer(self, dest_account, amount):
        if(self.balance -amount<0):
            print ("Error: must have {d} more dollars".format(
                d = amount - self.balance))
        elif (amount < 0):
            print ("Error: must transfer a positive amount")
        else:
            dest_account.deposit(amount)
            self.withdraw(amount)
            new_transact = Transaction(time.ctime(), "transfer", amount, dest_account)
            self.transactions.append(new_transact)


class Transaction(object):
    def __init__(self, time, type, amount, dest_account):
        self.time = time
        self.type = type
        self.amount = amount
        self.dest_account = dest_account

    def __str__(self, time, type, amount, dest_account):
        return "{ti}: {ty} ${a} to/from {des}".format(
            ti = time, ty = type, a = amount, des = dest_account.label)
