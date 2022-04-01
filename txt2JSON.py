#!/usr/bin/python3
#Author: Brayden Karnes
#Date: 03/29/2022
#About: Python program for adding text to a JSON file.  Text must be seperated by newlines.  Key /n Value /n...

import json

def main():
   txtData = import_text_file()
   txtData_dict = text2dict(txtData)
   JSON_file = import_JSON()
   final_product = merge_files(JSON_file, txtData_dict)
   create_final_file(final_product)
   
def import_text_file():
    file_name = input("Enter path of .txt file to be added to JSON file: ")
    file = open(file_name,'r+')                                    
    data = file.read()
    file.close()

    return data

def text2dict(txtData):
    data_list = txtData.split("\n")                                                     #Converting imported data to list
    data_dict = {data_list[i]: data_list[i + 1] for i in range(0, len(data_list), 2)}   #Converting imported data from list to dictionary
    return data_dict

def import_JSON():
    json_filename = input("Enter path of JSON file to be modified: ")
    import_file = open(json_filename)        
    file_data = json.load(import_file)
    import_file.close()

    return file_data                                                                    #file_data is a LIST of dictionaries

def merge_files(json_file, txt_file):
    key = input("Enter key name for added dictionary element: ")
    json_key = input("Enter key in JSON file to correlate txt key values: ")
    for i in txt_file:
        for j in json_file:
            if (i == j[json_key]):
                j[key] = txt_file[i]

    return json_file

def create_final_file(final_product):
    final_product = str(final_product).replace("'", '"')
    filename = input("Enter name for final product file.  If overwritting original file, enter the original file path: ")
    file = open(filename, "w")
    file.write(str(final_product))
    file.close

main()