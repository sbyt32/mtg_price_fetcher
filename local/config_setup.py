import configparser
import os


config = configparser.ConfigParser()
config.read('config.ini')

if os.path.exists('config.ini'):
    config_create = input("config.ini already exists, replace? y/n ")
    if not config_create == "y" and not config_create == "n":
        print("Invalid Input")

if not os.path.exists('config.ini') or config_create == "y":
    config['DEFAULT']           = {}
    config['CONNECT']           = {}
    config['DEFAULT']['path']   = ""
    config['DEFAULT']['config'] = "config.ini"
    config['CONNECT']["host"]   = input("Host Address: (Default: localhost) ") or "localhost"
    config['CONNECT']["user"]   = input("Username: ")
    config['CONNECT']["pass"]   = input(f"Password for {config['CONNECT']['user']}: ")
    config['CONNECT']["dbname"] = input("Database: (Default: price_tracker) ") or "price_tracker"
    with open('config.ini', 'w') as config_update:
        config.write(config_update)