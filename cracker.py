import crypt,optparse,uuid
from threading import Thread

def cmpPass(cryptPass, word, salt):
   cryptWord = crypt.crypt(word,salt)
   if (cryptWord == cryptPass):
      print ("[+] Found Password " + word)
   return

def testPass(cryptPass, dname,salt):
   dicFile = open(dname,'r')
   for word in dicFile.readlines():
      word = word.strip('\n')
      t = Thread(target=cmpPass, args=(cryptPass, word, salt))
      t.start()
   return
   
def main():
   parser = optparse.OptionParser("usage%prog "+ "-f <file> -d <dictionary>")
   parser.add_option('-f', dest='fname', type='string', help='specify file to unlock')
   parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
   (options,args) = parser.parse_args()
   if (options.fname == None) | (options.dname == None):
      print (parser.usage)
      exit(0)
   else:
      fname = options.fname
      dname = options.dname

   passFile = open(fname)
   for line in passFile.readlines():
      salt = '311'
      t = Thread(target=testPass, args=(line,dname,salt))
      t.start()

if __name__=="__main__":
   main()