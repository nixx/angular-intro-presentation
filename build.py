#!/usr/bin/python

# TODO: Implement watching.. Boring to recreate
import sys,shutil,os

from subprocess import call

def build():
	exit_code = call(["hovercraft", "-c", "presentation.css", "javascript_course.rst", "build"])
	if exit_code == 0:
		print "Success!"
		sys.exit(0)
	else:
		print "Failed"
		sys.exit(-1)


if len(sys.argv) < 2:
	build();
elif sys.argv[1] == "build":
	build();
elif sys.argv[1] == "clean" and os.path.exists("build"):
	shutil.rmtree("build")
	sys.exit(0)
