import sys

for package in ('requests'):
    locals()[package] = __import__(package)
    for mod in list(sys.modules):
        if mod == package or mod.startswith(package + '.'):
            sys.modules['dms.v2.packages.' + mod] = sys.modules[mod]
