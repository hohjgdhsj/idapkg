# Some console-friendly functions

import threading
import urllib2

from pkg.package import InstallablePackage
from pkg.util import __work


def install(spec, repo):
    return __work(lambda: InstallablePackage.install_from_repo(repo, spec))


def remove(name):
    return __work(lambda: LocalPackage.by_name(name).remove())
