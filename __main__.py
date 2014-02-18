import sys
import glob
from lxml import etree
from lxml.builder import E


def main(argv=None):
	""" File from directory and generage xml for gnome3  """
	if argv is None:
		argv = sys.argv
	if (len(argv)<2):
		print( "Need directory with jpg")
		exit(2)
	
	tb=glob.glob(argv[1]+"/*.jpg")
	if (len(tb)<1):
		print( "Need directory with jpg")
		exit(2)

	root=E.background(
		E.startime(
			E.year('2014'),E.month('02'),E.day('10'),
			E.hour('00'),E.minute('00'),E.second('00'))
		)
	for n,a in enumerate(tb):
		root.append(E.static(
			E.duration('1000.0'),E.file(tb[n])))
		fr=etree.Element('from')
		fr.text=tb[n]
		root.append(E.transition(
			E.duration('0.5'),fr,E.to(tb[(n+1)%len(tb)])))
		print("add %s"%(tb[n]))	
	open(argv[1]+'/dd.xml','w').write(etree.tostring(root,pretty_print=True).decode('utf-8'))
	cmd="gsettings set org.gnome.desktop.background picture-uri file://"+argv[1]+'/dd.xml'
	print(cmd)


if (__name__=="__main__"):
	main()

