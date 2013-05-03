"""do just walls in eplusinterface"""

from idfreader import idfreader


iddfile = "../iddfiles/Energy+V7_2_0.idd"
fname = "../idffiles/V_7_2/box_tiltrot.idf"
 
bunchdt, data, commdct = idfreader(fname, iddfile)
surfaces = bunchdt['BUILDINGSURFACE:DETAILED'.upper()]
# surfaces = bunchdt['FenestrationSurface:Detailed'.upper()]

wall = surfaces[0]
# n_vertices = 'Number_of_Vertices'
# n_vertices_i = wall.objls.index(n_vertices)


for surface in surfaces:
    name = surface.Name
    area = surface.area
    # height = surface.height
    # width = surface.width
    azimuth = surface.azimuth
    tilt = surface.tilt
    # coords = surface.coords
    # print name, area, height, width, azimuth, tilt
    # print name, azimuth
    print name, area, azimuth, tilt

