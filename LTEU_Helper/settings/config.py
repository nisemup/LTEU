import configparser
import os
import re

settings = 'settings/settings.ini'
practice = 'settings/practice.ini'
lectures = 'settings/lectures.ini'
sgs = configparser.ConfigParser()
sgs.read(settings)
pr = configparser.ConfigParser()
pr.read(practice)
lc = configparser.ConfigParser()
lc.read(lectures)


def c_create():
    if not os.path.exists('settings/settings.ini'):
        sgs.add_section('SETTINGS')

        sgs.set('SETTINGS', 'main_admin', '516654350')
        sgs.set('SETTINGS', 'admins', '516654350,516654350')
        sgs.set('SETTINGS', 'preset', 'lectures')

    if not os.path.exists('settings/practice.ini'):
        pr.add_section('FORM')

        pr.set('FORM', '1', '1️⃣| Перша пара: <b>{lesson} | 8:30 - 9:50 | {house}</b>')
        pr.set('FORM', '2', '2️⃣| Друга пара: <b>{lesson} | 10:10 - 11:30 | {house}</b>')
        pr.set('FORM', '3', '3️⃣| Третя пара: <b>{lesson} | 11:50 - 13:10 | {house}</b>')
        pr.set('FORM', '4', '4️⃣| Четверта пара: <b>{lesson} | 13:30 - 14:50 | {house}</b>')
        pr.set('FORM', '5', "5️⃣| П'ята пара: <b>{lesson} | 15:00 - 16:20 | {house}</b>")
        pr.set('FORM', '6', "6️⃣| Шоста пара: <b>{lesson} | 16:30 - 17:50 | {house}</b>")

        pr.set('FORM', 'n1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('FORM', 'n2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('FORM', 'n3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('FORM', 'n4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('FORM', 'n5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('FORM', 'n6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('PRE_mon')

        pr.set('PRE_mon', 'name_1', '')
        pr.set('PRE_mon', 'house_1', '')
        pr.set('PRE_mon', 'start_1', '')
        pr.set('PRE_mon', 'end_1', '')
        pr.set('PRE_mon', 'count_1', '')

        pr.set('PRE_mon', 'name_2', '')
        pr.set('PRE_mon', 'house_2', '')
        pr.set('PRE_mon', 'start_2', '')
        pr.set('PRE_mon', 'end_2', '')
        pr.set('PRE_mon', 'count_2', '')

        pr.set('PRE_mon', 'name_3', '')
        pr.set('PRE_mon', 'house_3', '')
        pr.set('PRE_mon', 'start_3', '')
        pr.set('PRE_mon', 'end_3', '')
        pr.set('PRE_mon', 'count_3', '')

        pr.add_section('PRE_tue')

        pr.set('PRE_tue', 'name_1', '')
        pr.set('PRE_tue', 'house_1', '')
        pr.set('PRE_tue', 'start_1', '')
        pr.set('PRE_tue', 'end_1', '')
        pr.set('PRE_tue', 'count_1', '')

        pr.set('PRE_tue', 'name_2', '')
        pr.set('PRE_tue', 'house_2', '')
        pr.set('PRE_tue', 'start_2', '')
        pr.set('PRE_tue', 'end_2', '')
        pr.set('PRE_tue', 'count_2', '')

        pr.set('PRE_tue', 'name_3', '')
        pr.set('PRE_tue', 'house_3', '')
        pr.set('PRE_tue', 'start_3', '')
        pr.set('PRE_tue', 'end_3', '')
        pr.set('PRE_tue', 'count_3', '')

        pr.add_section('PRE_wed')

        pr.set('PRE_wed', 'name_1', '')
        pr.set('PRE_wed', 'house_1', '')
        pr.set('PRE_wed', 'start_1', '')
        pr.set('PRE_wed', 'end_1', '')
        pr.set('PRE_wed', 'count_1', '')

        pr.set('PRE_wed', 'name_2', '')
        pr.set('PRE_wed', 'house_2', '')
        pr.set('PRE_wed', 'start_2', '')
        pr.set('PRE_wed', 'end_2', '')
        pr.set('PRE_wed', 'count_2', '')

        pr.set('PRE_wed', 'name_3', '')
        pr.set('PRE_wed', 'house_3', '')
        pr.set('PRE_wed', 'start_3', '')
        pr.set('PRE_wed', 'end_3', '')
        pr.set('PRE_wed', 'count_3', '')

        pr.add_section('PRE_thu')

        pr.set('PRE_thu', 'name_1', '')
        pr.set('PRE_thu', 'house_1', '')
        pr.set('PRE_thu', 'start_1', '')
        pr.set('PRE_thu', 'end_1', '')
        pr.set('PRE_thu', 'count_1', '')

        pr.set('PRE_thu', 'name_2', '')
        pr.set('PRE_thu', 'house_2', '')
        pr.set('PRE_thu', 'start_2', '')
        pr.set('PRE_thu', 'end_2', '')
        pr.set('PRE_thu', 'count_2', '')

        pr.set('PRE_thu', 'name_3', '')
        pr.set('PRE_thu', 'house_3', '')
        pr.set('PRE_thu', 'start_3', '')
        pr.set('PRE_thu', 'end_3', '')
        pr.set('PRE_thu', 'count_3', '')

        pr.add_section('PRE_fri')

        pr.set('PRE_fri', 'name_1', '')
        pr.set('PRE_fri', 'house_1', '')
        pr.set('PRE_fri', 'start_1', '')
        pr.set('PRE_fri', 'end_1', '')
        pr.set('PRE_fri', 'count_1', '')

        pr.set('PRE_fri', 'name_2', '')
        pr.set('PRE_fri', 'house_2', '')
        pr.set('PRE_fri', 'start_2', '')
        pr.set('PRE_fri', 'end_2', '')
        pr.set('PRE_fri', 'count_2', '')

        pr.set('PRE_fri', 'name_3', '')
        pr.set('PRE_fri', 'house_3', '')
        pr.set('PRE_fri', 'start_3', '')
        pr.set('PRE_fri', 'end_3', '')
        pr.set('PRE_fri', 'count_3', '')

        pr.add_section('G_1_mon')

        pr.set('G_1_mon', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_1_mon', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_1_mon', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_1_mon', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_1_mon', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_1_mon', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_1_tue')

        pr.set('G_1_tue', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_1_tue', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_1_tue', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_1_tue', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_1_tue', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_1_tue', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_1_wed')

        pr.set('G_1_wed', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_1_wed', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_1_wed', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_1_wed', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_1_wed', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_1_wed', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_1_thu')

        pr.set('G_1_thu', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_1_thu', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_1_thu', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_1_thu', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_1_thu', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_1_thu', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_1_fri')

        pr.set('G_1_fri', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_1_fri', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_1_fri', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_1_fri', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_1_fri', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_1_fri', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_2_mon')

        pr.set('G_2_mon', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_2_mon', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_2_mon', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_2_mon', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_2_mon', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_2_mon', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_2_tue')

        pr.set('G_2_tue', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_2_tue', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_2_tue', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_2_tue', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_2_tue', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_2_tue', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_2_wed')

        pr.set('G_2_wed', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_2_wed', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_2_wed', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_2_wed', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_2_wed', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_2_wed', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_2_thu')

        pr.set('G_2_thu', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_2_thu', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_2_thu', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_2_thu', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_2_thu', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_2_thu', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_2_fri')

        pr.set('G_2_fri', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_2_fri', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_2_fri', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_2_fri', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_2_fri', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_2_fri', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_3_mon')

        pr.set('G_3_mon', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_3_mon', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_3_mon', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_3_mon', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_3_mon', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_3_mon', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_3_tue')

        pr.set('G_3_tue', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_3_tue', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_3_tue', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_3_tue', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_3_tue', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_3_tue', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_3_wed')

        pr.set('G_3_wed', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_3_wed', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_3_wed', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_3_wed', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_3_wed', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_3_wed', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_3_thu')

        pr.set('G_3_thu', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_3_thu', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_3_thu', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_3_thu', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_3_thu', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_3_thu', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        pr.add_section('G_3_fri')

        pr.set('G_3_fri', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        pr.set('G_3_fri', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        pr.set('G_3_fri', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        pr.set('G_3_fri', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        pr.set('G_3_fri', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        pr.set('G_3_fri', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

    if not os.path.exists('settings/lectures.ini'):
        lc.add_section('FORM')

        lc.set('FORM', '1', '1️⃣| Перша пара: <b>{lesson} | 8:30 - 9:50 | {house}</b>')
        lc.set('FORM', '2', '2️⃣| Друга пара: <b>{lesson} | 10:10 - 11:30 | {house}</b>')
        lc.set('FORM', '3', '3️⃣| Третя пара: <b>{lesson} | 11:50 - 13:10 | {house}</b>')
        lc.set('FORM', '4', '4️⃣| Четверта пара: <b>{lesson} | 13:30 - 14:50 | {house}</b>')
        lc.set('FORM', '5', "5️⃣| П'ята пара: <b>{lesson} | 15:00 - 16:20 | {house}</b>")
        lc.set('FORM', '6', "6️⃣| Шоста пара: <b>{lesson} | 16:30 - 17:50 | {house}</b>")

        lc.set('FORM', 'n1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('FORM', 'n2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('FORM', 'n3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('FORM', 'n4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('FORM', 'n5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('FORM', 'n6', "6️⃣| Шоста пара: <b>пари немає</b>")
        lc.add_section('PRE_mon')

        lc.set('PRE_mon', 'name_1', '')
        lc.set('PRE_mon', 'house_1', '')
        lc.set('PRE_mon', 'start_1', '')
        lc.set('PRE_mon', 'end_1', '')
        lc.set('PRE_mon', 'count_1', '')

        lc.set('PRE_mon', 'name_2', '')
        lc.set('PRE_mon', 'house_2', '')
        lc.set('PRE_mon', 'start_2', '')
        lc.set('PRE_mon', 'end_2', '')
        lc.set('PRE_mon', 'count_2', '')

        lc.set('PRE_mon', 'name_3', '')
        lc.set('PRE_mon', 'house_3', '')
        lc.set('PRE_mon', 'start_3', '')
        lc.set('PRE_mon', 'end_3', '')
        lc.set('PRE_mon', 'count_3', '')

        lc.add_section('PRE_tue')

        lc.set('PRE_tue', 'name_1', '')
        lc.set('PRE_tue', 'house_1', '')
        lc.set('PRE_tue', 'start_1', '')
        lc.set('PRE_tue', 'end_1', '')
        lc.set('PRE_tue', 'count_1', '')

        lc.set('PRE_tue', 'name_2', '')
        lc.set('PRE_tue', 'house_2', '')
        lc.set('PRE_tue', 'start_2', '')
        lc.set('PRE_tue', 'end_2', '')
        lc.set('PRE_tue', 'count_2', '')

        lc.set('PRE_tue', 'name_3', '')
        lc.set('PRE_tue', 'house_3', '')
        lc.set('PRE_tue', 'start_3', '')
        lc.set('PRE_tue', 'end_3', '')
        lc.set('PRE_tue', 'count_3', '')

        lc.add_section('PRE_wed')

        lc.set('PRE_wed', 'name_1', '')
        lc.set('PRE_wed', 'house_1', '')
        lc.set('PRE_wed', 'start_1', '')
        lc.set('PRE_wed', 'end_1', '')
        lc.set('PRE_wed', 'count_1', '')

        lc.set('PRE_wed', 'name_2', '')
        lc.set('PRE_wed', 'house_2', '')
        lc.set('PRE_wed', 'start_2', '')
        lc.set('PRE_wed', 'end_2', '')
        lc.set('PRE_wed', 'count_2', '')

        lc.set('PRE_wed', 'name_3', '')
        lc.set('PRE_wed', 'house_3', '')
        lc.set('PRE_wed', 'start_3', '')
        lc.set('PRE_wed', 'end_3', '')
        lc.set('PRE_wed', 'count_3', '')

        lc.add_section('PRE_thu')

        lc.set('PRE_thu', 'name_1', '')
        lc.set('PRE_thu', 'house_1', '')
        lc.set('PRE_thu', 'start_1', '')
        lc.set('PRE_thu', 'end_1', '')
        lc.set('PRE_thu', 'count_1', '')

        lc.set('PRE_thu', 'name_2', '')
        lc.set('PRE_thu', 'house_2', '')
        lc.set('PRE_thu', 'start_2', '')
        lc.set('PRE_thu', 'end_2', '')
        lc.set('PRE_thu', 'count_2', '')

        lc.set('PRE_thu', 'name_3', '')
        lc.set('PRE_thu', 'house_3', '')
        lc.set('PRE_thu', 'start_3', '')
        lc.set('PRE_thu', 'end_3', '')
        lc.set('PRE_thu', 'count_3', '')

        lc.add_section('PRE_fri')

        lc.set('PRE_fri', 'name_1', '')
        lc.set('PRE_fri', 'house_1', '')
        lc.set('PRE_fri', 'start_1', '')
        lc.set('PRE_fri', 'end_1', '')
        lc.set('PRE_fri', 'count_1', '')

        lc.set('PRE_fri', 'name_2', '')
        lc.set('PRE_fri', 'house_2', '')
        lc.set('PRE_fri', 'start_2', '')
        lc.set('PRE_fri', 'end_2', '')
        lc.set('PRE_fri', 'count_2', '')

        lc.set('PRE_fri', 'name_3', '')
        lc.set('PRE_fri', 'house_3', '')
        lc.set('PRE_fri', 'start_3', '')
        lc.set('PRE_fri', 'end_3', '')
        lc.set('PRE_fri', 'count_3', '')

        lc.add_section('G_1_mon')

        lc.set('G_1_mon', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_1_mon', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_1_mon', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_1_mon', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_1_mon', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_1_mon', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_1_tue')

        lc.set('G_1_tue', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_1_tue', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_1_tue', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_1_tue', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_1_tue', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_1_tue', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_1_wed')

        lc.set('G_1_wed', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_1_wed', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_1_wed', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_1_wed', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_1_wed', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_1_wed', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_1_thu')

        lc.set('G_1_thu', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_1_thu', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_1_thu', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_1_thu', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_1_thu', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_1_thu', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_1_fri')

        lc.set('G_1_fri', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_1_fri', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_1_fri', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_1_fri', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_1_fri', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_1_fri', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_2_mon')

        lc.set('G_2_mon', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_2_mon', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_2_mon', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_2_mon', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_2_mon', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_2_mon', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_2_tue')

        lc.set('G_2_tue', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_2_tue', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_2_tue', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_2_tue', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_2_tue', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_2_tue', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_2_wed')

        lc.set('G_2_wed', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_2_wed', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_2_wed', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_2_wed', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_2_wed', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_2_wed', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_2_thu')

        lc.set('G_2_thu', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_2_thu', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_2_thu', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_2_thu', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_2_thu', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_2_thu', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_2_fri')

        lc.set('G_2_fri', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_2_fri', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_2_fri', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_2_fri', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_2_fri', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_2_fri', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_3_mon')

        lc.set('G_3_mon', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_3_mon', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_3_mon', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_3_mon', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_3_mon', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_3_mon', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_3_tue')

        lc.set('G_3_tue', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_3_tue', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_3_tue', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_3_tue', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_3_tue', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_3_tue', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_3_wed')

        lc.set('G_3_wed', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_3_wed', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_3_wed', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_3_wed', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_3_wed', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_3_wed', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_3_thu')

        lc.set('G_3_thu', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_3_thu', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_3_thu', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_3_thu', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_3_thu', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_3_thu', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

        lc.add_section('G_3_fri')

        lc.set('G_3_fri', '1', '1️⃣| Перша пара: <b>пари немає</b>')
        lc.set('G_3_fri', '2', '2️⃣| Друга пара: <b>пари немає</b>')
        lc.set('G_3_fri', '3', '3️⃣| Третя пара: <b>пари немає</b>')
        lc.set('G_3_fri', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
        lc.set('G_3_fri', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
        lc.set('G_3_fri', '6', "6️⃣| Шоста пара: <b>пари немає</b>")

    c_save()


def c_set(section, key, value, path='presets'):
    if path == 'settings':
        sgs.set(section, key, value)
    elif path == 'presets':
        if sgs.get('SETTINGS', 'preset') == 'lectures':
            cp = lc
        else:
            cp = pr
        cp.set(section, key, value)
    c_save()


def c_get(section):
    keys = []
    if sgs.get('SETTINGS', 'preset') == 'lectures':
        [keys.append(key) for key in lc[section].values()]
    else:
        [keys.append(key) for key in pr[section].values()]
    while len(keys):
        if re.findall('пари немає', keys[-1]):
            del keys[-1]
        else:
            break
    if not keys:
        result = 'Пар немає'
    else:
        result = '\n\n'.join(keys)
    return result


def admins():
    result = []
    admins = sgs.get('SETTINGS', 'admins')
    if re.findall(', | |,', admins):
        result = re.split(', | |,', admins)
        result = [int(x) if x.lstrip('-').isdecimal() else x for x in result]
    else:
        result.append(admins)
    return result


def c_get_key(section, key, path='presets'):
    if path == 'settings':
        result = sgs.get(section, key)
        return result
    elif path == 'presets':
        if sgs.get('SETTINGS', 'preset') == 'lectures':
            result = lc.get(section, key)
        else:
            result = pr.get(section, key)
        return result


def c_save(path='settings'):
    if path == 'settings':
        with open('settings/settings.ini', "w") as config_file:
            sgs.write(config_file)
        with open('settings/lectures.ini', "w") as config_file:
            lc.write(config_file)
        with open('settings/practice.ini', "w") as config_file:
            pr.write(config_file)
    elif path == 'presets':
        if sgs.get('SETTINGS', 'preset') == 'lectures':
            with open('settings/lectures.ini', "w") as config_file:
                lc.write(config_file)
        else:
            with open('settings/practice.ini', "w") as config_file:
                pr.write(config_file)


def c_gnrt_pre(group, day):
    if sgs.get('SETTINGS', 'preset') == 'lectures':
        cp = lc
    else:
        cp = pr
    i = 0
    keys = []
    [keys.append(key) for key in cp[f'G_{group}_{day}'].values()]
    while i <= len(keys)-1:
        if re.findall('пари немає', keys[i]):
            del keys[i]
        else:
            i += 1
    name = re.findall('([\u263a-\U0001f645]\|.*?).\|', keys[0])
    start = re.findall('\|.(\d+:\d+)', keys[0])
    end = re.findall('(\d+:\d+).\|', keys[-1])
    house = re.findall('\d.\|.(.*)\</b\>', keys[0])
    count = len(keys)
    cp.set(f'PRE_{day}', f'name_{group}', f'{name[0]}')
    cp.set(f'PRE_{day}', f'start_{group}', f'{start[0]}')
    cp.set(f'PRE_{day}', f'end_{group}', f'{end[0]}')
    cp.set(f'PRE_{day}', f'house_{group}', f'{house[0]}')
    cp.set(f'PRE_{day}', f'count_{group}', f'{count}')


def get_pre(group, day):
    if sgs.get('SETTINGS', 'preset') == 'lectures':
        cp = lc
    else:
        cp = pr
    name = cp.get(f'PRE_{day}', f'name_{group}')
    start = cp.get(f'PRE_{day}', f'start_{group}')
    end = cp.get(f'PRE_{day}', f'end_{group}')
    house = cp.get(f'PRE_{day}', f'house_{group}')
    count = cp.get(f'PRE_{day}', f'count_{group}')
    return name, start, end, house, count


def c_clear(group, day):
    if sgs.get('SETTINGS', 'preset') == 'lectures':
        cp = lc
    else:
        cp = pr
    cp.set(f'G_{group}_{day}', '1', '1️⃣| Перша пара: <b>пари немає</b>')
    cp.set(f'G_{group}_{day}', '2', '2️⃣| Друга пара: <b>пари немає</b>')
    cp.set(f'G_{group}_{day}', '3', '3️⃣| Третя пара: <b>пари немає</b>')
    cp.set(f'G_{group}_{day}', '4', '4️⃣| Четверта пара: <b>пари немає</b>')
    cp.set(f'G_{group}_{day}', '5', "5️⃣| П'ята пара: <b>пари немає</b>")
    cp.set(f'G_{group}_{day}', '6', "6️⃣| Шоста пара: <b>пари немає</b>")