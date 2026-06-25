
import requests
import json
import numpy as np

lons = [-72.5,-73.5]
lats = [42.5,41.5]

### set up a bounding box encompassing teh are for which you want to obtain GHCN station data (west longitudes are denoted by a negative sign)

bbox_set = str(np.min(lons))+','+str(np.min(lats))+','+str(np.max(lons))+','+str(np.max(lats))

### build an input dictionary specifying the tiem period of interest,the variable (pcpn for precipitation) and the desired reduction

## Returns MAXIMUM ANNUAL TOTAL PRECIPITATION at each station over the specified period.
#input_dict = {"bbox":bbox_set,"sdate":"1985-12-31","edate":"2014-12-31","meta":"ll,sids,elev,valid_daterange","elems":[{"name":"pcpn","interval":[1],"duration":1,"reduce":"sum","smry":"max"}]}  ##annual max precip

## Returns MAXIMUM ONE-DAY PRECIPITATION  at each station over the specified period.
#input_dict = {"bbox":bbox_set,"sdate":"1985","edate":"2014","meta":"ll,sids,elev,valid_daterange","elems":[{"name":"pcpn","interval":[1],"duration":1,"reduce":"max","smry":"max"}]}      ##max 1 day precip

# Returns AVERAGE ANNUAL 1-DAY PRECIPITATION at each station over the specified period.
input_dict = {"bbox":bbox_set,"sdate":"1985","edate":"2014","meta":"ll,sids,elev,valid_daterange","elems":[{"name":"pcpn","interval":[1],"duration":1,"reduce":"max","smry":"mean"}]}      ##average max 1 day precip

# Returns AVERAGE ANNUAL NUMBER OF DAYS WITH >10mm of precipitation at each station over the specified period (not used in paper).
#input_dict = {"bbox":bbox_set,"sdate":"1985","edate":"2014","meta":"ll,elev,sids,valid_daterange","elems":[{"name":"pcpn","interval":[1],"duration":1,"reduce":"cnt_gt_0.39","smry":"mean"}]}      ##annual mean days >10mm

# Returns AVERAGE ANNUAL TOTAL PRECIPITATION  at each station over the specified period.
#input_dict = {"bbox":bbox_set,"sdate":"1985-12-31","edate":"2014-12-31","meta":"ll,elev,valid_daterange,sids","elems":[{"name":"pcpn","interval":[1],"duration":1,"reduce":"sum","maxmissing":"30","smry":"mean"}]}  ##annual mean precip

## ALL input dictionaries also return metadata for each station

## Requests data from ACIS Server

req = requests.post('http://data.rcc-acis.org/MultiStnData', json = input_dict)
m_data = req.json()

### Addition documentation regarding ACIS web service calls is available at https://www.rcc-acis.org/docs_webservices