# coding=utf-8
# Script to upload files to Dropbox

# Import correct libraries
import base64
import sys
from temboo.core.session import TembooSession
from temboo.Library.Dropbox.FilesAndMetadata import UploadFile

print str(sys.argv[1])

# Encode image
with open(str(sys.argv[1]), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Declare Temboo session and Choreo to upload files
session = TembooSession("ismarthome88", "myFirstApp", "42d33889ea9a45bd8c7bed97a2ccdf17")
uploadFileChoreo = UploadFile(session)

# Get an InputSet object for the choreo
uploadFileInputs = uploadFileChoreo.new_input_set()

# Set inputs
uploadFileInputs.set_AppKey("412wvvs18fz8626")
uploadFileInputs.set_AppSecret("426ckdalhh3tk3t")
uploadFileInputs.set_AccessToken("phgmf2fgdv8rge8u")
uploadFileInputs.set_AccessTokenSecret("q4qynhfgileze17")

uploadFileInputs.set_FileName(str(sys.argv[1]))
uploadFileInputs.set_FileContents(encoded_string)
uploadFileInputs.set_Root("sandbox")

# Execute choreo
uploadFileResults = uploadFileChoreo.execute_with_results(uploadFileInputs)
