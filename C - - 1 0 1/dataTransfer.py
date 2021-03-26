import dropbox
class TransferData:
    def __init__(self, acessToken):
        self.acessToken=acessToken
    def uploadFile(self, source, destination):
        dbx=dropbox.Dropbox(self.acessToken)
        f=open(source, 'rb')
        dbx.files_upload(f.read(), destination)

def main():
    acessToken='cKhvlm-3tHUAAAAAAAAAAcTlQq1NyInHsmaxdnielmL7efBncGGoSzvJHKO8PAVK'
    td=TransferData(acessToken)
    source=input("enter the file part to transfer: ")
    destination=input("enter dropbox part to upload: ")
    td.uploadFile(source, destination)
    print("file(s) have been moved")

main()