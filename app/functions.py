import os


def get_uploaded_images():
    rootdir = os.getcwd()
    images = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            filename = os.path.join(subdir, file).split("\\")[-1]
            if ".png" in filename or ".jpg" in filename:
                images.append(filename)

    return images
