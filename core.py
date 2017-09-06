"""
Examples for a feature class and its view provider.
(c) 2009 Werner Mayer LGPL
"""

__author__ = "Werner Mayer <wmayer@users.sourceforge.net>"
import FreeCAD,FreeCADGui, Part


class IcosahedronTool():

	def GetResources(self):
		return {'Pixmap'  : 'My_Command_Icon', # the name of a svg file available in the resources
			'Accel' : "Shift+S", # a default shortcut (optional)
			'MenuText': "My New Command",
			'ToolTip' : "What my new command does"}

	def Activated(self):
		a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Icosahedron")
		Icosahedron(a)
		a.ViewObject.Proxy=0
		FreeCAD.ActiveDocument.recompute()
		return

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		return True

class Icosahedron:
	def __init__(self, obj):
		'''Add some custom properties to our box feature'''
		obj.addProperty("App::PropertyLength","Radius","Box","radius of the Icosahedron").Radius=10.0
		obj.Proxy = self

	def onChanged(self, fp, prop):
		'''Do something when a property has changed'''

	def execute(self, fp):
		scale = fp.Radius/1.90211303259
		phy = 1.61803398875
		f = list()
		for i in (-scale,scale):
			for j in (-scale,scale):
				k = scale
				f.append(Part.Face(Part.makePolygon([(-k,0,i*phy), (k,0,i*phy), (0,j*phy,i*1), (-k,0,i*phy)])))
				f.append(Part.Face(Part.makePolygon([(0,i*phy,-k), (0,i*phy,k), (j*phy,i*1,0), (0,i*phy,-k)])))
				f.append(Part.Face(Part.makePolygon([(i*phy,-k,0), (i*phy,k,0), (i*1,0,j*phy), (i*phy,-k,0)])))
				for k in (-scale,scale):
					f.append(Part.Face(Part.makePolygon([(i*1,0,k*phy), (0,j*phy,k*1), (i*phy,j*1,0), (i*1,0,k*phy)])))
		fp.Shape = Part.Solid(Part.Shell(f))

FreeCADGui.addCommand('IcosahedronTool',IcosahedronTool())

class DodecahedronTool():

	def GetResources(self):
		return {'Pixmap'  : 'My_Command_Icon', # the name of a svg file available in the resources
			'Accel' : "Shift+E", # a default shortcut (optional)
			'MenuText': "IcosahedronTool",
			'ToolTip' : "draw IcosahedronTool"}

	def Activated(self):
		a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Dodecahedron")
		Dodecahedron(a)
		a.ViewObject.Proxy=0
		FreeCAD.ActiveDocument.recompute()
		return

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		return True

class Dodecahedron:
	def __init__(self, obj):
		'''Add some custom properties to our box feature'''
		obj.addProperty("App::PropertyLength","Radius","Box","Length of the Dodecahedron").Radius=10.0
		obj.Proxy = self

	def onChanged(self, fp, prop):
		'''Do something when a property has changed'''

	def execute(self, fp):
		scale = fp.Radius/1.7320508075689
		phy = 1.61803398875
		f = list()
		k = scale
		for i in (-scale,scale):
			for j in (-scale,scale):
				f.append(Part.Face(Part.makePolygon([(i,j,-k), (i/phy,j*phy,0), (i,j,k), (i*phy,0,k/phy), (i*phy,0,-k/phy), (i,j,-k)])))
				f.append(Part.Face(Part.makePolygon([(j,-k,i), (j*phy,0,i/phy), (j,k,i), (0,k/phy,i*phy), (0,-k/phy,i*phy), (j,-k,i)])))
				f.append(Part.Face(Part.makePolygon([(-k,i,j), (0,i/phy,j*phy), (k,i,j), (k/phy,i*phy,0), (-k/phy,i*phy,0), (-k,i,j)])))
		fp.Shape = Part.Solid(Part.Shell(f))

FreeCADGui.addCommand('DodecahedronTool',DodecahedronTool())

class TetrahedronTool():

	def GetResources(self):
		return {'Pixmap'  : 'My_Command_Icon', # the name of a svg file available in the resources
			'Accel' : "Shift+S", # a default shortcut (optional)
			'MenuText': "My New Command",
			'ToolTip' : "What my new command does"}

	def Activated(self):
		a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Tetrahedron")
		Tetrahedron(a)
		a.ViewObject.Proxy=0
		FreeCAD.ActiveDocument.recompute()
		return

	def IsActive(self):
		"""Here you can define if the command must be active or not (greyed) if certain conditions
		are met or not. This function is optional."""
		return True

class Tetrahedron:
	def __init__(self, obj):
		'''Add some custom properties to our box feature'''
		obj.addProperty("App::PropertyLength","Radius","Box","radius of the Icosahedron").Radius=10.0
		obj.Proxy = self

	def onChanged(self, fp, prop):
		'''Do something when a property has changed'''

	def execute(self, fp):
		scale = fp.Radius/1.2247448 
		a = scale * 0.70710678118 #1/sqrt(2)
		f = list()
		for i in (-scale,scale):
			f.append(Part.Face(Part.makePolygon([(0,scale,a), (0,-scale,a), (i,0,-a),(0,scale,a)])))
			f.append(Part.Face(Part.makePolygon([(scale,0,-a), (-scale,0,-a), (0,i,a),(scale,0,-a)])))
		fp.Shape = Part.Solid(Part.Shell(f))

FreeCADGui.addCommand('TetrahedronTool',TetrahedronTool())


