import os
from os.path import splitext, exists, join
from shutil import move

"""
Do not forget to create each directory for each respective file type!
"""

SourceDir = "Your Downloads directory"
DestDirAudio = "Your Audios directory"
DestDirVideo = "Your Videos directory"
DestDirImage = "Your Images directory"
DestDirDocuments = "Your Documents directory"
DestDirZip = "Your Zip directory"
DestDirExe = "Your Exe directory"

ImageExtensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
                    ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt",
                    ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

VideoExtensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv",
                    ".mov", ".qt", ".flv", ".swf", ".avchd"]

AudioExtensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

DocumentExtensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def OrganizeFiles():
    with os.scandir(SourceDir) as entries:
        for entry in entries:
            name = entry.name
            CheckAudioFiles(entry, name)
            CheckVideoFiles(entry, name)
            CheckImageFiles(entry, name)
            CheckDocumentFiles(entry, name)
            CheckZipFiles(entry, name)


def MakeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
        return name


def MoveFile(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = MakeUnique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        os.rename(oldName, newName)
    move(entry, dest)


def CheckAudioFiles(entry, name):
    for Extension in AudioExtensions:
        if name.endswith(Extension) or name.endswith(Extension.upper()):
            MoveFile(DestDirAudio, entry, name)
            print(f"Moved audio file: {name}")


def CheckVideoFiles(entry, name):
    for Extension in VideoExtensions:
        if name.endswith(Extension) or name.endswith(Extension.upper()):
            MoveFile(DestDirVideo, entry, name)
            print(f"Moved video file: {name}")


def CheckImageFiles(entry, name):
    for Extension in ImageExtensions:
        if name.endswith(Extension) or name.endswith(Extension.upper()):
            MoveFile(DestDirImage, entry, name)
            print(f"Moved image file: {name}")


def CheckDocumentFiles(entry, name):
    for Extension in DocumentExtensions:
        if name.endswith(Extension) or name.endswith(Extension.upper()):
            MoveFile(DestDirDocuments, entry, name)
            print(f"Moved document file: {name}")


def CheckZipFiles(entry, name):
    if name.endswith(".zip") or name.endswith(".ZIP"):
        MoveFile(DestDirZip, entry, name)
        print(f"Moved Zip file: {name}")


def CheckExeFiles(entry, name):
    if name.endswith(".exe") or name.endswith(".EXE"):
        MoveFile(DestDirExe, entry, name)
        print(f"Moved Exe file: {name}")


OrganizeFiles()
