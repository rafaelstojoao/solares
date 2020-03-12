#The Heliophysics Event Knowledgebase (HEK) is a repository of feature and event information about the Sun. Entries are generated both by automated algorithms and human observers. SunPy accesses this information through the hek module, which was developed through support from the European Space Agency Summer of Code in Space (ESA-SOCIS) 2011

#To search the HEK, you need a start time, an end time, and an event type. Times are specified as strings or Python datetime objects. Event types are specified as upper case, two letter strings, and are identical to the two letter abbreviations found at the HEK website, http://www.lmsal.com/hek/VOEvent_Spec.html.
#vale a pena conferir  http://www.lmsal.com/hek/VOEvent_Spec.html
#https://buildmedia.readthedocs.org/media/pdf/sunpy/documentation_sprint/sunpy.pdf

#The classification system for solar flares uses the letters A, B, C, M or X, according to the peak flux in watts per square metre (W/m2) of X-rays with wavelengths 100 to 800 picometres (1 to 8 ångströms), as measured at the Earth by the GOES spacecraft.


from sunpy.net import hek
client = hek.HEKClient()

tstart = '2011/08/09 07:23:56'
tend = '2011/08/09 12:40:29'
event_type = 'FL'
# result = client.search(hek.attrs.Time(tstart,tend),hek.attrs.EventType(event_type),FL_GOESCls='M')
result = client.search(hek.attrs.Time(tstart,tend),hek.attrs.EventType(event_type),hek.attrs.FL.PeakFlux > 4000.0)
print(result['fl_goescls'])

#Peak flux range at 100–800 picometre (watts/square metre)
#A 	< 10−7
#B 	10−7 – 10−6
#C 	10−6 – 10−5
#M 	10−5 – 10−4
#X 	> 10−4

print(len(result))

print(result.keys())