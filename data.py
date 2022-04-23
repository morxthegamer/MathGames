import json

class Data:
  def __init__(self, folder, file = ""):
    self.folder = folder
    self.file = file

  def getDataJson(self, file):
    with open(f"{self.folder}/{file}", "r") as f:
      return json.loads(f.read())

  def getData(self, file):
    with open(f"{self.folder}/{file}", "r") as g:
      return g.read()

  def setDataJson(self, file, data):
    with open(f"{self.folder}/{file}", "w") as j:
      j.write(json.dumps(data))

  def setData(self, file, data):
    with open(f"{self.folder}/{file}", "w") as j:
      j.write(data)

  def getFileData(self, file):
    with open(file, "r") as l:
      return l.read()

  def setFileData(self, file, data):
    with open(file, "w") as k:
      k.write(data)