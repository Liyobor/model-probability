from ModelTester import ModelTester
from SimpleFileExplorer import SimpleFileExplorer
from alive_progress import alive_bar
tester = ModelTester("220916model.tflite","002.xlsx")
path = input("輸入路徑\n")
explorer = SimpleFileExplorer(path)
files = explorer.getFiles()
with alive_bar(len(files)) as bar:
    for file in files:
        # print(path+'\\'+file)
        if file[-3:]=="wav":
            # print(file)
            tester.loadWavFile(file)
            tester.NormalizedMaxDBFS(-7)
            tester.doLibrosa(stepLength=16000,repeatTimes=5)
        bar()
    tester.exportDeatils()
    tester.exportResult()
    tester.clearResult()
    