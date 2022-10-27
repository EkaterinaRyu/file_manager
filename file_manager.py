# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:11:44 2022

@author: Екатерина
"""

import os
import shutil

def settings_change(login): 
#    os.mkdir('E:/Финашка/Алгоритмы/файловый менеджер', mode=0o777)    
    print('Хотите указать путь для сооздания новой директории? [да/нет]')
    yn = input()
    if yn == 'да':
        settings = open(r'settings.txt', 'w')
        print('Укажите абсолютный путь для сооздания новой директории или введите [назад].\n(Папка будет создана автоматически и считаться корневой.)')
        dr = str(input())
        settings.write(dr)
        settings.close()
        with open('settings.txt', 'r') as settings:
            drr = os.path.normpath(settings.readline()+'/'+login)
        try:
            os.mkdir(drr, mode=0o777)
        except FileExistsError:
            print('Такая директория уже есть.')
        print('Для {} создана корневая папка.'.format(login))
    
        with open('settings.txt', 'w') as settings:
            settings.write(os.path.normpath(os.getcwd()+'/'+login))
        os.chdir(drr)
    else:
        print('Ладно.')
    
def info():
    print('Доступны следующие команды в формате:\n[команда] [название файла/папки]:')
    с = ['выход', 'создать', 'переименовать', 'удалить', 'назад', 'вперед', 
         'настройки', 'справка', 'где', 'показать', 'редактировать', 'читать', 'копировать', 'переместить']
    print(с)

def input_check(act):
    pass

def dontunderstand():
    print('Я не понял. Хотите вызвать справку? [да/нет]')
    yn = input()
    if yn == 'да':
        info()
    else:
        print('Ладно.')

def creating(drr, name, a):
    try:
        if a == True:
            print('Создаю файл...')
            file = open(name, 'w+')
            file.close()
        elif a == False:
            print('Создаю папку...')
            os.mkdir(os.path.normpath(os.getcwd()+'/'+name), mode=0o777)
        else: dontunderstand()
    except FileExistsError:
        print('Файл/папка уже существует. Попробуйте изменить название.')

def deleting(name, a):
    if a == False:
        if(os.path.isdir(name)):
            if len(os.listdir()) == 0:
                os.rmdir(name)
                print('Папка удалена.')
            else:
                print('Кажется в папке что-то есть. Посмотрите сами:')
                print(os.listdir(os.getcwd()+'/'+name))
                print('Удалить папку вместе с содержимым? [да/нет]')
                yn = input()
                if yn == 'да':
                    shutil.rmtree(os.path.normpath(os.getcwd()+'/'+name), ignore_errors=False, onerror=None)
                    print('Папка удалена вместе с содержимым.')
                else:
                    print('Ладно.')
        else:
            print('Кажется такой папки не существует.')    
    elif a == True:
        if(os.path.isfile(name)):
            os.remove(name)
            print("Файл удален.")
        else:
            print("Кажется такого файла не существует.")
    else: dontunderstand()
    
def renaming(oldname):
    print('Введите новое имя:')
    newname = str(input())
    os.rename(oldname, newname)
    print('Переименовано.')

def read(name, a):
    if a == True:
        file = open(name, 'r')
        print('Вывожу содержимое файла {}'.format(name))
        print(file.readlines())
        file.close()
    else: print('Кажется это папка, а не файл.')

def change(name, a):
    if a == True:
        file = open(name, 'w+')
        print('Введите желамое:')
        i = str(input())
        file.write(i)
        file.close()
    else: print('Кажется это папка, а не файл.')
     
def up(name, a):
    if a == True:
        print('Кажется это файл, а не папка.')
    elif a == False:
        print('Перехожу в папку {}...'.format(name))
        os.chdir(os.getcwd()+'/'+name)

def copying(name, drr):
    print(drr)
    print('Укажите абсолютный путь до папки, куда создать копию:')
    i = str(input())
    try:
        fp = os.path.normpath(os.getcwd()+'/'+name)
        ds = os.path.normpath(drr + '/' + i)
        shutil.copyfile(fp, ds)
    except FileNotFoundError and PermissionError:
       print('Для создания копии необходимо находится в папке оригинала.\nИ копировать можно только файлы.')
    
def moving(name, drr):
    print('Укажите куда переместить:')
    i = str(input())
    try:
        fp = os.path.normpath(os.getcwd()+'/'+name)
        print(fp)
        ds = os.path.normpath(drr + '/' + i)
        shutil.move(fp, ds)
    except (FileNotFoundError):
       print('Для перемещения необходимо находится в папке оригинала.')

def down(drr, login):
    a = os.path.split(os.getcwd())
    if a[1] == login:
        print('Вы находитесь в корневой папке.\nДальше лежат туманные земли, где никто никогда не бывал...')
    else:
        print('Перехожу в родительскую папку...')
        os.chdir('..')
   
def main():
    
    with open('settings.txt', 'r') as settings:
        drr = os.path.normpath(settings.readline())
        print(drr)
        settings.close()
    
    print('Добро пожаловать в файловый менеджер!\nВведите логин:')
    login = str(input())
    
    m = False
    for i in os.listdir():
        if i == login:
            print('О, я Вас знаю!')
            os.chdir(login)
            m = True
    if m == False:
        print('Кажется я Вас не узнаю. Пожалуйста, воспользуйтель командой [настройки].')
    
    while True:
        print('\nВведите команду:')
        act = input().split(' ')
        input_check(act)
        
        if len(act) > 1:
            if '.' in act[1]:
                a = True
            else: a = False
        
        if act[0] == 'выход':
            print('До свидания!')
            break
        
        elif act[0] == 'справка': info()
        
        elif act[0] == 'настройки': settings_change(login)
        
        elif act[0] == 'создать': creating(drr, str(act[1]), a)
                   
        elif act[0] == 'удалить': deleting(str(act[1]), a)
                
        elif act[0] == 'переименовать': renaming(str(act[1]))
        
        elif act[0] == 'где': print(os.getcwd())
        
        elif act[0] == 'показать': print(os.listdir())
            
        elif act[0] == 'вперед': up(act[1], a)
        
        elif act[0] == 'назад': down(drr, login)
        
        elif act[0] == 'редактировать': change(str(act[1]), a)
        
        elif act[0] == 'читать': read(str(act[1]), a)
        
        elif act[0] == 'копировать': copying(str(act[1]), drr)
        
        elif act[0] == 'переместить': moving(str(act[1]), drr)
        
        else: dontunderstand()
            
main()