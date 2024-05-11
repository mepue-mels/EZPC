"""ezpc_classes.py"""
# This file contains the classes used for EzPC: PC Parts Picker

class User:
    pc_list = []

    def __init__(self, user_id = int, user_name = str, user_pw = str) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.user_pw = user_pw
    
    def new_pc(self):
        pc = Computer(self.user_id,None,None)
        self.add_pc(pc)
        return pc

    def add_pc(self, Computer):
        self.pc_list.append(Computer)
        Computer.user_id = self.user_id

    def remove_pc(self, comp_id):
        for pc in self.pc_list:
            if pc.comp_id == comp_id:
                self.pc_list.remove(pc)

    def pop_pc(self):
        self.pc_list.pop()
    
    def init_pc_list(self):
        self.pc_list = []
    
    def get_pc_list(self):
        return self.pc_list

class Computer:
    # part_list = [
    #             [None,None,0,None,None,None,None,None,None],         # case
    #             [None,None,0,None,None,None,None,None,None],         # cooler
    #             [None,None,0,None,None,None,None,None,None],         # cpu
    #             [None,None,0,None,None,None,None,None,None],         # gpu
    #             [None,None,0,None,None,None,None,None],              # mobo
    #             [None,None,0,None,None,None,None,None],              # psu
    #             [None,None,0,None,None,None,None,None,None,None],    # ram
    #             [None,None,0,None,None,None,None,None,None]          # storage
    #             ]
    
    # part_list = [None] * 8

    def __init__(self, user_id = int, comp_id = int, comp_name = str) -> None:
        self.user_id = user_id
        self.comp_id = comp_id
        self.comp_name = comp_name
        self.part_list = [
                        [None,None,0,None,None,None,None,None,None],         # case
                        [None,None,0,None,None,None,None,None,None],         # cooler
                        [None,None,0,None,None,None,None,None,None],         # cpu
                        [None,None,0,None,None,None,None,None,None],         # gpu
                        [None,None,0,None,None,None,None,None],              # mobo
                        [None,None,0,None,None,None,None,None],              # psu
                        [None,None,0,None,None,None,None,None,None,None],    # ram
                        [None,None,0,None,None,None,None,None,None]          # storage
                        ]
    
    def __repr__(self) -> str:
        return f"User ID = {self.user_id}\nComp ID = {self.comp_id}\nComp Name = {self.comp_name}\n"

    def add_part(self, Part):
        self.part_list.append(Part)

    def get_part_list(self):
        return self.part_list
    
    def remove_part(self, part_id):
        for part in self.part_list:
            if part.part_id == part_id:
                self.part_list.remove(part)


class Part:
    def __init__(self, comp_id = int, part_id = int, part_name = str, part_price = int) -> None:
        self.comp_id = comp_id
        self.part_id = part_id
        self.part_name = part_name
        self.part_price = part_price

class Case(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class Cooler(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class CPU(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class GPU(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class Motherboard(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class PSU(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class RAM(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)

class Storage(Part):
    def __init__(self, part_id, part_name, part_price) -> None:
        super().__init__(part_id, part_name, part_price)
 