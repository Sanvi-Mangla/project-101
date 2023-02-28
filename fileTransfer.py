import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
        
def main():
    access_token = "sl.BZObBWepvUYu0WzQesN8uWX1HuwUVhp8Sg5WuOvwmMsjESut7Cu43D9xxmWZuwuuvilLxci6aY_QXezOU_Ew30cFGQaYfPcSroDxweJm6At9B3IMSydz6EudfpQOvVf3S28Kj2U"
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    transferData.upload_file(file_from, file_to)
    print("file has been transfered")

main()
