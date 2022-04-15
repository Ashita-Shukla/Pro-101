import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BFxFA6OKX2nHbl6kYPPNFJU6DZgTUCr75reoPOPAFoybGxCCu7tIZfp867Z81lIy1KBkbIVm72V1gXPdLPkHaNi0UYqXI2AsThd1ya4ztoRbFpQVbjlOmNnO3nx9snU1pxwIbV_P8kI2'
    transferData = TransferData(access_token)

    file_from = input('Enter File Path To Transfer:')
    file_to = input('Enter Full Path:') # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")
if __name__ == '__main__':
    main()
