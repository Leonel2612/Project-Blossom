from linked_list import LinkedList,Node
from blossom_lib import flower_definitions

class HashMap():
    def __init__(self,array_size):
         self.array_size=array_size
         self.array=[LinkedList() for item in range(self.array_size)]

    def hash(self,key,colision=0):
        self.key_bytes=key.encode()
        hash_code=sum(self.key_bytes)
        return hash_code+colision

    def compressor(self,hash_code):
        return hash_code%self.array_size

    def assign(self,key,value):
        array_index=self.compressor(hash(key))
        payload = Node([key, value])
        self.list_at_array=self.array[array_index]
        for item_key in self.list_at_array:
            if key==item_key[0]:
                item_key[1]=value
                return

        self.list_at_array.insert(payload)

    def retrieve_everything(self):

        for index, linked_list in enumerate(self.array):
            current_node=linked_list.get_head_node()
            if current_node:
                print("LinkedList #{}".format(index))
                while current_node:
                    value=current_node.get_value()[1]
                    print("{}|  {}|{}".format(index,sum(value.encode()),value))
                    current_node=current_node.get_next_node()
            else:
                print("LinkedList #{}".format(index))
                print("This slot is free")
            print("\n")



    def retrieve(self,key):
        count=0
        array_index=self.compressor(hash(key))
        self.list_at_index=self.array[array_index]
        self.count=0

        for item_key in self.list_at_index:
            if key==item_key[0]:
                return item_key[1]

        return None




blossom=HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0],flower[1])


blossom.retrieve_everything()















