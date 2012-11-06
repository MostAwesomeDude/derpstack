#!/usr/bin/env python

from __future__ import with_statement

import logging
import os
import sys

from derpstack import app

interpreter = os.path.expanduser("~/local/bin/python")
if sys.executable != interpreter:
    os.execl(interpreter, interpreter, *sys.argv)

app.use_x_sendfile = False

handler = logging.FileHandler("error.log")
handler.setLevel(logging.WARNING)
app.logger.addHandler(handler)

application = app
