import imapclient
a=imapclient.IMAPClient('imap.gmail.com')
a.login("user mail","password")
a.list_folders()
a.search("string")
ALL
FROM
TO
SUBJECT
SINCE
BEFORE
ON
CC
ANSWERED
UNANSWERED
DRAFTED
DELETED
LARGE N
SMALL
NOT 
OR

uid=a.gmail_search("string")
b=a.fetch(UID,body[])

import pyzmail

a=pyzmail.pyzmessage.factory(uid,body[])
a.get_subject()
a.get_address(from,to,cc,bcc)
a.delete_message
a.logout()
