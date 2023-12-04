# https://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

def plot_map(lat, lon, mapType):

    # m = Basemap(llcrnrlon=-100.,llcrnrlat=20.,urcrnrlon=20.,urcrnrlat=60., rsphere=(6378137.00,6356752.3142),\
    #              resolution='l',projection='merc', lat_0=40.,lon_0=-20.,lat_ts=20.)
    bottomLeftLon = int(lon) - 40.0
    if bottomLeftLon > 180.0:
        bottomLeftLon = 180.0
    elif bottomLeftLon < -180.0:
        bottomLeftLon = -180.0

    bottomLeftLat = int(lat) - 20.0
    if bottomLeftLat > 90.0:
        bottomLeftLat = 90.0
    elif bottomLeftLat < -90.0:
        bottomLeftLat = -90.0
    
    topRightLon = int(lon) + 40.0
    if topRightLon > 180.0:
        topRightLon = 180.0
    elif topRightLon < -180.0:
        topRightLon = -180.0

    topRightLat = int(lat) + 20.0
    if topRightLat > 90.0:
        topRightLat = 90.0
    elif topRightLat < -90.0:
        topRightLat = -90.0

    m = Basemap(llcrnrlon=bottomLeftLon,llcrnrlat=bottomLeftLat,urcrnrlon=topRightLon,urcrnrlat=topRightLat, rsphere=(6378137.00,6356752.3142),\
                 resolution='l',projection='merc')
    # m.plot(6.5E6,2.8E6, color='m', marker ='*', markersize=5 )
    

    # OPTIONAL MAPS 1-fillcontinents / 2-etopo / 3-bluemarble / 4-shadedrelief
    if mapType == 1:
        m.fillcontinents()
    elif mapType == 2:
        m.etopo()
    elif mapType == 3:
        m.bluemarble()
    elif mapType == 4:
        m.shadedrelief()
    else:
        m.bluemarble()
    # m.drawcoastlines()
    # m.drawrivers()
    # m.drawstates()
    # draw parallels
    m.drawparallels(np.arange(-90,90,10),labels=[1,1,0,1])
    # draw meridians
    m.drawmeridians(np.arange(-180,180,10),labels=[1,1,0,1])
    m.plot(lon,lat,latlon=True, color='r', marker ='*', markersize=6)
    # plt.show()
    
class TDClass:
    def __init__(self, temperatures, depths):
        self.temperatures = []
        self.depths = []

def plot_temperatures(ax2, temperatureList, depthList, binfile):
    # fig2, ax1 = plt.subplots()
    # profile = plt.figure(1)
    # ax1 = plt.subplots()
    ax2.plot(temperatureList, depthList, linewidth=1.0)
    ax2.set_title(binfile.split("/")[-1],fontsize=8)
    ax2.set_ylabel('Depth [m]')
    ax2.set_xlabel('Temperature [°C]')
    # ax2.grid(color = 'color', linestyle = 'linestyle', linewidth = number)
    ax2.grid(color = 'grey', linestyle = '--', linewidth = 0.1)
    # plt.show()


def plots(temperatureList, depthList, binfile, lat, lon, mapType ):
    
    # fig = plt.figure() # SAME PLOT
    # ax1 = plt.subplot(211) # SAME PLOT
    fig1, ax1 = plt.subplots() # INDIVIDUAL PLOTS
    plot_map(lat,lon,mapType) # INDIVIDUAL PLOTS
    # ax2 = plt.subplot(212) #SAME PLOT
    fig2, ax2 = plt.subplots()
    plot_temperatures(ax2, temperatureList, depthList, binfile)
    plt.show()
