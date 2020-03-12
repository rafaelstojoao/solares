from sunpy.instr import goes
from sunpy.time import TimeRange


tran=TimeRange('1986-09-01 00:00','1996-10-31 12:00')
ciclo22=TimeRange('1986-09-01 00:00','1996-10-31 23:59')
ciclo23=TimeRange('1996-10-01 00:00','2008-09-21 23:59')
ciclo24=TimeRange('2008-09-22 00:00','2020-03-06 23:59')




#Ciclo solar 22
#O ciclo solar 22: 1986-09-01 to 1996-10-31

#ciclo solar 23:  1996-10-01  to 2008-09-21
#ciclo 23 – se encontra entre os três mais ativos, empatando com o terceiro ciclo e superando nos máximos os ciclos 19 e 21.

#ciclo solar 24:  2008-09-22   to
result=goes.get_goes_event_list(ciclo22,goes_class_filter='X')
print(' event_date | inicio_em | data_pico | fim_em | classe | regiao_atividade_NOAA')
print('CICLO 22:')
#goes_class_filter: (optional) string
#    a string specifying a minimum GOES class for inclusion in the list, e.g. 'M1', 'X2'.
for r in result:
    print(r['event_date'] + ' | ' + r['start_time'].value + ' | ' + r['peak_time'].value+ ' | ' + r['end_time'].value+ ' | ' + r['goes_class']+ ' | ' + str(r['noaa_active_region']))

print('CICLO 23:')
result=goes.get_goes_event_list(ciclo23,goes_class_filter='X')

for r in result:
    print(r['event_date'] + ' | ' + r['start_time'].value + ' | ' + r['peak_time'].value+ ' | ' + r['end_time'].value+ ' | ' + r['goes_class']+ ' | ' + str(r['noaa_active_region']))


print('CICLO 24: ')
result=goes.get_goes_event_list(ciclo24,goes_class_filter='X')
for r in result:
    print(r['event_date'] + ' | ' + r['start_time'].value + ' | ' + r['peak_time'].value+ ' | ' + r['end_time'].value+ ' | ' + r['goes_class']+ ' | ' + str(r['noaa_active_region']))
