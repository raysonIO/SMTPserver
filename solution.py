from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):


   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

   GSERVER = "smtp.nyu.edu"
   PORT = 1025
   LOOPB = "127.0.0.1"
   #Dont use startTLS port. 465 is for SSL

   # Create socket
   clientSocket = socket(AF_INET, SOCK_STREAM) #(socket's address family, designation:TCP Socket)

   clientSocket.connect((LOOPB,PORT))  #Connection object SOLICITATION SEND


   recv = clientSocket.recv(1024).decode() # RECIEVE



   # Send HELO command and print server response.
   heloCommand = 'EHLO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   #RESPONSE
   recv1 = clientSocket.recv(1024).decode()


   # Send MAIL FROM command and print server response.

   mailFrom = "MAIL FROM:<testacc66966@gmail.com>\r\n"
   clientSocket.send(mailFrom.encode())
   #response
   recv2 = clientSocket.recv(1024)
   recv2 = recv2.decode()



   # Send RCPT TO command and print server response.
   # Fill in start

   rcptTo = "RCPT TO:<bcr7974@nyu.edu>\r\n"
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024)
   recv3 = recv3.decode()

   # Fill in end

   # Send DATA command and print server response.
   # Fill in start

   dataCom = "DATA\r\n"
   clientSocket.send(dataCom.encode())
   recv4 = clientSocket.recv(1024)
   recv4 = recv4.decode()


   msg = """ \r\n Roses are red Violets are blue
         python is awesome
         and so are you
         ."""
   endmsg = "\r\n.\r\n"


   # Send message data.
   # Fill in start
   someSubject = "Subject: Paging chuck testa2 \r\n\r\n"
   clientSocket.send(someSubject.encode())
   clientSocket.send(msg.encode())
   clientSocket.send(endmsg.encode())
   recv5 = clientSocket.recv(1024)
   recv5 = recv5.decode()

   # Fill in end

   # Message ends with a single period.
   # Fill in start


   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quitCom = "QUIT\r\n"
   clientSocket.send(quitCom.encode())
   recv10 = clientSocket.recv(1024)
   recv10 = recv10.decode()
   clientSocket.close()

   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
