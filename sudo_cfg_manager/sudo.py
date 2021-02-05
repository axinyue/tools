
import io

User_Alias="User_Alias"
Cmnd_Alias ="Cmnd_Alias"

CONTENT_SEP = ", "
Base_Template = "{define} {group_name} = {content}"

User_Common_Template="{user_group_name} ALL=(ALL) NOPASSWD: {common_groups}"
from setting import *

def sudoer_cfg_lines():
    
    lines = []
    for userGroup in USERS_GROUPS.keys():
        userLine = Base_Template.format(define=User_Alias,
                                        group_name=userGroup,
                                        content=CONTENT_SEP.join(USERS_GROUPS[userGroup]))
        lines.append(userLine)
    
    for commandGroup in COMMAND_GROUPS.keys():

        commandLine = Base_Template.format(define=Cmnd_Alias,
                                            group_name=commandGroup,
                                            content=CONTENT_SEP.join(COMMAND_GROUPS[commandGroup]))
        lines.append(commandLine)

    for userGroup in USERS_COMMON_GROUPS.keys():
        userGroupCommandLine = User_Common_Template.format(user_group_name=userGroup,
                                    common_groups = CONTENT_SEP.join(USERS_COMMON_GROUPS[userGroup])
                                    )

        lines.append(userGroupCommandLine)

    return lines

def write_to_file():
    ext_lines = sudoer_cfg_lines()


    with open("sudoers_defaults","r") as f:
        lines = f.readlines();

    with open("sudoers","w") as f:
        new_lines = ["".join(lines),]
        new_lines.extend(ext_lines)

        f.write("\n".join(new_lines))

write_to_file()