#!/usr/bin/env python3
import json
import os

import fedmsg

root = os.path.dirname(__file__)
path = os.path.join(root, "test.json")
with open(path, "r") as f:
    msg = json.load(f)

name = msg["test"]["namespace"].split(".")[0]
artifact_type = msg["artifact"]["type"]
topic = artifact_type + ".test.complete"

fedmsg.publish(topic=topic, name="relay_outbound", modname=name, msg=msg)
