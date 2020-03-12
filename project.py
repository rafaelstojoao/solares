#! /home/rance/anaconda3/bin/python

# this script is intended to be run once a day, you could automate it with a software like cron

import os
from ftplib import FTP
# import psycopg2
# from psycopg2 import sql
from datetime import date, timedelta

# replaces North and South for + and minus to make it easy to calculate distance
def latitude_calculator(latitude):
    if latitude[0] == 'N':
        n_latitude = int(latitude[1:])
    else:
        n_latitude = -1 * int(latitude[1:])
    return n_latitude

# generic method that connects to ftp server and downloads data
def updateReport(path_in_server, local_path, file):
    ftp = FTP('ftp.swpc.noaa.gov')
    ftp.login()

    ftp.cwd(path_in_server)

    localfile = open(local_path + file, 'wb')
    ftp.retrbinary('RETR ' + file, localfile.write, 1024)
    localfile.close()
    ftp.quit()
    return


# downloads event report file, parse its contents and puts it in the database
def updateEventReport(file_prefix):
    path_in_server = 'pub/warehouse/2018/2018_events'
    file = file_prefix + "events.txt"
    local_path = 'Data/Reports/Event/'
    updateReport(path_in_server, local_path, file)
    #parseEventReport(local_path , file, file_prefix)
    return

# downloads region report (SRS) file, parse its contents
# and puts it in the database, linking to previous rotations
# of the same area
def updateRegionReport(file_prefix):
    path_in_server = '/pub/warehouse/2018/SRS'
    file = file_prefix + "SRS.txt"
    local_path =  'Data/Reports/ActiveRegion/'
    updateReport(path_in_server, local_path, file)
    #parseRegionReport(local_path, file)
    return

# put the data in the warehouse
# def sync(file_prefix):
#     cur.execute("INSERT INTO warehouse (date_, event, begin_, max, end_, obs, q, type, loc_frq, particular1, particular2, prev_nmbr, nmbr, location, lo, area, z, ll, nn, mag_type) SELECT e.date_, e.event, e.begin_, e.max, e.end_, e.obs, e.q, e.type, e.loc_frq, e.particular1, e.particular2, r.prev_nmbr, r.nmbr, r.location, r.lo, r.area, r.z, r.ll, r.nn, r.mag_type FROM event_report as e RIGHT OUTER JOIN region_report as r ON e.reg = r.nmbr;")
#     cur.execute("DELETE FROM public.event_report")
#     cur.execute("DELETE FROM public.region_report")
#     return

# we do this to get data from seven days before, having a secure margin as probably there is yet no data from the last few days
seven_days_before = date.today() - timedelta(days = 7)


# conn = psycopg2.connect(dbname="postgres", user="postgres", password="password", host='localhost', port='5432')
# cur = conn.cursor()

# the prefix of the files to be downloaded
file_prefix = seven_days_before.strftime("%Y%m%d")

updateEventReport(file_prefix)
updateRegionReport(file_prefix)
# sync(file_prefix)

# conn.commit()

# cur.close()
# conn.close()
