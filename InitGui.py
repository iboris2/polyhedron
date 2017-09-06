import FreeCAD,FreeCADGui

class PolyedreWorkbench ( Workbench ):
	"Polyedre workbench object"
	Icon = """
	/* XPM */
	static const char *test_icon[]={
	"16 16 2 1",
	"a c #000000",
	". c None",
	"................",
	"................",
	"................",
	"................",
	"................",
	"......####......",
	"......####......",
	"......####......",
	"......####......",
	"......####......",
	"......####......",
	"......####......",
	"......####......",
	"......####......",
	"................",
	"................"};
	"""
	MenuText = "Polyedre"
	ToolTip = "Polyedre workbench"

	def GetClassName(self):
		return "Gui::PythonWorkbench"

	def Initialize(self):
		import core
		self.appendToolbar("My Tools", ["IcosahedronTool","DodecahedronTool","TetrahedronTool"])
		self.appendMenu("My Tools", ["IcosahedronTool","DodecahedronTool","TetrahedronTool"])
		#self.appendToolbar("My Tools", ["DodecahedronTool"])
		#self.appendMenu("My Tools", ["DodecahedronTool"])



FreeCADGui.addWorkbench(PolyedreWorkbench)
