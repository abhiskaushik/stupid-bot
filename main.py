import os
import sys
import re
import getpass
import signal
from datetime import datetime
from subprocess import call, Popen

from twisted.internet import reactor, protocol
from twisted.words.protocols import irc

from scan import scan_incoming_msg