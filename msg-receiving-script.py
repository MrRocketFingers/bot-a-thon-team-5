import extract_msg

msg_file = "ALCAMPO - Consumable Orders - 06abril2020" + ".msg"

f = r"msg_file"  # Replace with yours
msg = extract_msg.Message(f)
msg_sender = msg.sender
msg_date = msg.date
msg_subj = msg.subject
msg_message = msg.body