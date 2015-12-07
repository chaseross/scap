#This file goes to the new directory, and moves the .pdf file to output all all the
#       intermediate files to a garbage foler
# To reuse this, you shouldn't need to change anything assuming it is setup as
#       project folder  which has code, garbage, and output folders

import sys
import os.path
import os
import shutil
import glob

def cleanDirectory():

    path = os.getcwd()
    sourcePath = os.path.dirname(path)
    codePath = os.path.join(sourcePath, "code")
    garbagePath = os.path.join(sourcePath, "garbage")
    outputPath = os.path.join(sourcePath, "output")
    os.chdir(path)

    for pdffile in glob.iglob(os.path.join(codePath, "*.pdf")):
        shutil.copy(pdffile, outputPath)
        os.remove(pdffile)

    for pdffile in glob.iglob(os.path.join(codePath, "*.docx")):
        shutil.copy(pdffile, outputPath)
        os.remove(pdffile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.aux")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.pyc")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.toc")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.gz")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.bbl")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.blg")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.fdb_latexmk")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.fls")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.log")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

    for garbageFile in glob.iglob(os.path.join(codePath, "*.out")):
        shutil.copy(garbageFile, garbagePath)
        os.remove(garbageFile)

cleanDirectory()
