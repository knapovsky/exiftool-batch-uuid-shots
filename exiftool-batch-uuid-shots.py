import uuid
import os
# import exiftool
import subprocess

exiftool = "/opt/homebrew/bin/exiftool"
path = "./images"
files = os.listdir(path)

for i in range(len(files)):

    # Generate UUID for an Image
    unique_filename = str(uuid.uuid4().hex)

    print("-------------")

    print("Changing file: "+files[i]+", to UUID: "+unique_filename)

    # Save UUID to ImageUniqueID EXIF tag
    try:
        subprocess.call(["/opt/homebrew/bin/exiftool", "-overwrite_original", "-Exif:ImageUniqueID="+unique_filename+"", ""+path+"/"+files[i]])
        print("EXIF changed on file: "+files[i])
    except:
        print("EXIF cannot be changed on file: "+files[i])
        exit

    # Save UUID to RAW Filename EXIF tag
    try:
        subprocess.call(["/opt/homebrew/bin/exiftool", "-overwrite_original", "-XMP:RawFileName="+files[i]+"", ""+path+"/"+files[i]])
        print("EXIF changed on file: "+files[i])
    except:
        print("EXIF cannot be changed on file: "+files[i])
        exit

    # Change filename
    try:
        os.rename(path+"/"+files[i], path+"/"+unique_filename+".jpg")
        print("Filename changed on file: "+files[i]+", now: "+unique_filename+".jpg")
    except:
        print("Filename cannot be changed on file: "+files[i])
        exit

    print("-------------")

#print(f"After Renaming: {os.listdir(path)}")
print("-------------")
print("All Files renamed")