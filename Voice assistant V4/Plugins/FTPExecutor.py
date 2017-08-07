import ftplib
import os
from ftplib import FTP

class FTPExecutor(object):
    def setServer(self, server, port=21):
        self.server = server
        self.port = port
        self.ftp = FTP(self.server, self.port)
        self.ftp.login()


    def execute(self, text):
        pass

    def procentCount(self, text):
        pass

    def nothingCanDo(self):
        pass

    def listEntire(self):
        self.ftp.login()
        data = self.ftp.retrlines("LIST")
        return data

    def changeDirectory(self, dir):
        self.ftp.login()
        self.ftp.cwd(dir)
        data = self.ftp.retrlines("LIST")
        return data

    def getFileFromServer(self, whereToDownload):
        filenames = self.ftp.nlst()
        for filename in filenames:
            host_file = os.path.join(whereToDownload, filename)

            try:
                with open(host_file, 'wb') as local_file:
                    self.ftp.retrbinary('RETR ' + filename, local_file.write)
            except ftplib.error_perm:
                pass

        return self.ftp.quit()

    def putFileToServer(self, path, ftype='TXT'):
        if ftype == 'TXT':
            with open(path) as fobj:
                return self.ftp.storlines('STOR ' + path, fobj)
        else:
            with open(path, 'rb') as fobj:
                return self.ftp.storbinary('STOR ' + path, fobj, 1024)