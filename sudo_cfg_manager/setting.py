USERS_GROUPS = {
    "FS_DEV_OPS_GROUP":["user"]
}

PROCESSES_COMMONS = """
/bin/nice
/bin/kill
/usr/bin/kill
/usr/bin/killall
/usr/sbin/lsof
/usr/bin/netstat
"""

LOCAL_SHELL_COMMONS="""
/usr/bin/bash
/usr/bin/sh
/bin/chmod
/bin/chown
"""

def load(lines):
    commons = lines.split()
    commons = [common for common in commons if common.strip()!=""]
    return commons

COMMAND_GROUPS={
    "PROCESSES": load(PROCESSES_COMMONS),
    "LOCAL_SHELL":load(LOCAL_SHELL_COMMONS)
}

USERS_COMMON_GROUPS = {
    "FS_DEV_OPS_GROUP":COMMAND_GROUPS.keys()
}
